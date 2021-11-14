# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 02:29:24 2020

@author: ville
"""

import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVR
from sklearn.svm import SVR
## Packages fo scaling ##
from sklearn.preprocessing import  StandardScaler
from sklearn import model_selection


def modelisation (Clean_Base):
    
    df=Clean_Base.copy()
    
    y_train =df['Prix_sans_reduc']
    X_train =df.drop('Prix_sans_reduc',axis=1)
    
    #Train et Test
    seed = 69
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_train, y_train, test_size=0.2, random_state=seed)
    
    
    #Feature scaling
    sc = StandardScaler()
    X_train_scaled = sc.fit_transform(X_train)
    X_train_scaled = pd.DataFrame(X_train_scaled)
    
    
    scoring="neg_mean_squared_error"
    
    models = []
    models.append(('LiR', LinearRegression()))
    models.append(('DTR', DecisionTreeRegressor()))
    models.append(('RDF', RandomForestRegressor(n_estimators=10)))
    models.append(('SVM', LinearSVR(epsilon=1.5)))
    models.append(('SVR', SVR(kernel="poly", degree=2, C=100, epsilon =0.1)))
    
    results=[]
    names=[]


    def prediction(N,M):
    #for name,model in models:
        from warnings import simplefilter
        simplefilter(action='ignore', category=FutureWarning)
    
        cv_results=model_selection.cross_val_score(M,X_train_scaled,y_train,cv=10,scoring=scoring)
        results.append(cv_results)
        names.append(N)
        model_scores_rmse = np.sqrt(-cv_results)
        
        msg = "%s: %f (%f)" % (N, model_scores_rmse.mean(), model_scores_rmse.std())
        print(msg)        
        
        return


    Lir_scores_precision = prediction(models[0][0],models[0][1])
    DTR_scores_precision = prediction(models[1][0],models[1][1])
    RDF_scores_precision = prediction(models[2][0],models[2][1])
    SVM_scores_precision = prediction(models[3][0],models[3][1])
    SVR_scores_precision = prediction(models[4][0],models[4][1])
    
    return 









