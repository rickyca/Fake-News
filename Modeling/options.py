from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.decomposition import TruncatedSVD

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier

import numpy as np

def get_option_pipeline(n_preprocessing,n_method, n_dim_reduct=-1, n_ensemble=-1):
    '''
    Returns a list to pass to make_pipeline function.
    Example:
        opt = get_option_pipeline(0,0)
        make_pipeline(*opt)
    '''
    preprocessing = [CountVectorizer(), TfidfVectorizer()]
    dim_reduct = [TruncatedSVD()]
    method = [LogisticRegression(), KNeighborsClassifier(), DecisionTreeClassifier(), SVC(), MLPClassifier()]
    ensemble = [AdaBoostClassifier(), BaggingClassifier()]

    steps = []
    steps.append(preprocessing[n_preprocessing])
    if n_dim_reduct >= 0:
        steps.append(dim_reduct[n_dim_reduct])

    if n_ensemble >= 0:
        steps.append(ensemble[n_ensemble])
    else:
        steps.append(method[n_method])
    return steps

def get_option_params(n_preprocessing,n_method, n_dim_reduct=-1, n_ensemble=-1):
    '''
    Returns a list of params to pass to GridSearchCV.
    Example:
        params = get_option_params(0,0)
        gs = GridSearchCV(pl, param_grid=params)
    '''
    preprocessing = [{
        'countvectorizer__stop_words' : ['english'],
        'countvectorizer__ngram_range': [(1,1),(2,2)]#[(j,i) for j in range(1,4) for i in range(j,3)]
        }, {
        'tfidfvectorizer__stop_words' : ['english'],
        'tfidfvectorizer__ngram_range': [(1,1),(2,2)]#[(j,i) for j in range(1,4) for i in range(j,3)]
        }]

    dim_reduct = [{
        'truncatedsvd__n_components': range(60,100,30)
    }]

    method = [{
        'logisticregression__penalty': ['l2', 'l1'],
        'logisticregression__C': np.arange(1,20,4),
        'logisticregression__class_weight': [None, 'balanced'] ,
        'logisticregression__solver': ['liblinear'],
        'logisticregression__max_iter': [1000]
        }, {
        'kneighborsclassifier__n_neighbors': range(3,40,3),
        'kneighborsclassifier__weights': ['uniform', 'distance']
        }, {
        'decisiontreeclassifier__max_features': np.arange(0.3,0.8,0.1),
        'decisiontreeclassifier__min_samples_split': range(2,10),
        'decisiontreeclassifier__class_weight': [None, 'balanced']
        }, {
        'svc__C': range(1,30,5),
        'svc__kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'svc__class_weight': [None, 'balanced']
        }, {
        'mlpclassifier__hidden_layer_sizes': [(i,) for i in range(105,300,50)],
        'mlpclassifier__activation': ['logistic', 'tanh', 'relu'],
        #'mlpclassifier__alpha': np.arange(0.0001, 0.01, 0.0009),
        'mlpclassifier__learning_rate': ['adaptive']#['constant', 'invscaling', 'adaptive']
        }]

    ensemble = [{
        'adaboostclassifier__base_estimator': [DecisionTreeClassifier(min_samples_leaf=1 ,min_samples_split=8, max_features=0.4)],#, LogisticRegression(), KNeighborsClassifier(), SVC(), MLPClassifier()],
        'adaboostclassifier__n_estimators': range(5,100,30),
        'adaboostclassifier__learning_rate': np.arange(0.6,1.0,0.2)
        }, {
        'baggingclassifier__base_estimator': [DecisionTreeClassifier(min_samples_leaf=1 ,min_samples_split=8, max_features=0.4)],#, LogisticRegression(), KNeighborsClassifier(), SVC(), MLPClassifier()],
        'baggingclassifier__n_estimators': range(3,34,10),
        'baggingclassifier__max_features': np.arange(0.6,1.0,0.2)
        }]

    params = {}
    params.update(preprocessing[n_preprocessing])

    if n_dim_reduct >= 0:
        params.update(dim_reduct[n_dim_reduct])

    if n_ensemble >= 0:
        params.update(ensemble[n_ensemble])
    else:
        params.update(method[n_method])
    return params
