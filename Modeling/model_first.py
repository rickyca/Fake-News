import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier


from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

def score_it(pl, X_test, y_test):
    orig_stdout = sys.stdout
    f = open('log_file.txt', 'a')
    sys.stdout = f

    print "=================================================================\n"
    print "Pipeline\n"
    for i,k in pl.named_steps.items():
        print i,':'
        print k
    y_pred = pl.predict(X_test)
    print "\nScore: ", accuracy_score(y_test, y_pred)
    unique, counts = np.unique(y_test, return_counts=True)
    print "Baseline: ", float(max(counts))/sum(counts), dict(zip(unique, counts)), '\n'

    print pd.DataFrame(confusion_matrix(y_test, y_pred), \
                       columns=['Predicted BS', 'Predicted Real'], index=['BS', 'Real'])
    print
    print classification_report(y_test, y_pred)
    print "=================================================================\n"

    sys.stdout = orig_stdout
    f.close()
    return

# Load Data
print "Loading Data..."
df = pd.read_csv('joint.csv')
# Drop NaN
df.dropna(inplace=True)
df = df.reset_index(drop=True)

# Test-Train split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['type'].values, test_size=0.3)

# Pipeline
pl = make_pipeline(CountVectorizer(), DecisionTreeClassifier())
print "Fitting..."
pl.fit(X_train, y_train)

# Scorer
print "Scoring..."
score_it(pl, X_test, y_test)
