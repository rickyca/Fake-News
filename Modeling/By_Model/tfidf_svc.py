import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron

from sklearn.model_selection import GridSearchCV

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

def score_it_df(gs, X_test, y_test):
    # Init Series
    results = pd.Series()

    # Get best estimator
    pl = gs.best_estimator_

    # Calculate baseline
    unique, counts = np.unique(y_test, return_counts=True)
    results['baseline'] = float(max(counts))/sum(counts)

    y_pred = gs.predict(X_test)
    # Score
    results['score'] = accuracy_score(y_test, y_pred)

    # Steps
    results['steps'] = ' -> '.join(pl.named_steps.keys())

    # Details
    detailed_steps = ''
    for i,k in pl.named_steps.items():
        step = ' '.join("{0}={1}".format(key, val) for key, val in k.get_params().items())
        step = i + ' -> ' + step
        detailed_steps = detailed_steps + step + '\n'

    results['details'] = detailed_steps

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    results['predicted_fake__fake'] = cm[0,0]
    results['predicted_real__fake'] = cm[0,1]
    results['predicted_fake__real'] = cm[1,0]
    results['predicted_real__real'] = cm[1,1]
    return results

# Load Data
print "Loading Data..."
df = pd.read_csv('joint.csv')
# Drop NaN
df.dropna(inplace=True)
df = df.reset_index(drop=True)

# Test-Train split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['type'].values, test_size=0.3)

# Encoder
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)

# Pipeline
pl = make_pipeline(TfidfVectorizer(), SVC())
print "Fitting..."

# Gridsearch params
params = {
    'svc__C': range(1,30),
    'svc__kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
    'svc__class_weight': [None, 'balanced'],
    'tfidfvectorizer__stop_words' : [None, 'english'],
    'tfidfvectorizer__ngram_range': [(i,j) for j in range(1,4) for i in range(j,3)],
    'tfidfvectorizer__max_features': range(10000,100000,2)
}
gs = GridSearchCV(pl, param_grid=params)
gs.fit(X_train, y_train)
#pl.fit(X_train, y_train_encoded)

# Scorer
print "Scoring..."
result = score_it_df(gs, X_test, y_test)
#result = score_it_df(pl, X_test, y_test_encoded)

# Save results
results = pd.read_csv('log.csv')
results = results.append(result, ignore_index=True)
results.to_csv('log.csv', index=False)
