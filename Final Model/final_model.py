import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

from nltk.corpus import stopwords

import pickle

def model():
    # Stopwords
    sws = stopwords.words('english')
    sws.extend(['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november','december'])
    sws.extend(['2009', '2010', '2011', '2012', '2013', '2014', '2015''2016', '2017', '2018','26', '27', '81','00', '000'])
    sws.extend(['cbs', 'npr', 'wsj', 'nbc', 'getty', 'com', 'toggle', 'images','article', 'cbsn', 'sign'])

    # Load Data
    print "Loading Data..."
    df = pd.read_csv('joint.csv')
    # Drop NaN
    df.dropna(inplace=True)
    df = df.reset_index(drop=True)

    # Test-Train split
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['type'].values, test_size=0.3)

    # Pipeline
    pl = make_pipeline(TfidfVectorizer(stop_words=sws, ngram_range=(1, 1), max_features=10000), LogisticRegression(C=9, max_iter=1000., solver='liblinear', class_weight='balanced'))
    
    # Fit
    print "Fitting..."
    pl.fit(X_train, y_train)

    # Scorer
    print "Scoring..."
    y_pred = pl.predict(X_test)
    print confusion_matrix(y_test, y_pred)
    print accuracy_score(y_test, y_pred)
    print classification_report(y_test, y_pred)
    pickle.dump(pl, open('final_model.p', 'wb'))

if __name__=='__main__':
    model()
