# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 03:56:26 2020

@author: Yanis
"""

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

import sklearn
import numpy
from sklearn.decomposition import PCA
from sklearn.preprocessing import  StandardScaler
from sklearn import model_selection

from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVR
from sklearn.svm import SVR

from itertools import compress



def corr_select(CleanDataFrame, Var="Prix_sans_reduc", corr=0.2 ):
    
    cor = CleanDataFrame.corr()
    cor_target = abs(cor[Var])
    relevant_features = cor_target[cor_target>corr]
    relevant_features
    list_nrf = list(relevant_features.index)
    list_nrf.remove('Prix_reduc')
    Selected_corr = CleanDataFrame[list_nrf]
    
    return Selected_corr, list_nrf




def pvalue_select(CleanDataFrame, X,  Y="Prix_sans_reduc" ):
    
    y=CleanDataFrame[Y]
    x=CleanDataFrame[X]
    x=sm.add_constant(x)
    model=sm.OLS(y,x)
    results = model.fit()
    
    return results.pvalues



def ACP_select(CleanDataFrame):
    
    df1=CleanDataFrame.copy()

    col_to_drop = ["Prix_reduc"]
    cpY=df1.drop(col_to_drop,1)
    
    cpX=df1[['Porte_de_la_chambre_avec_verrou','Détecteur_de_monoxyde_de_carbone','Détecteur_de_fumée','Extincteur','Kit_de_premiers_secours','Boîte_à_clé_sécurisée']]
    
    
    sc=StandardScaler()
    
    Z = sc.fit_transform(cpX)
    x = pd.DataFrame(Z)
    y = cpY.loc[:,['Prix_sans_reduc']].values
    
    pca = PCA(n_components=1)
    Secu_pca = pca.fit_transform(x)
    Secu_pca = pd.DataFrame(Secu_pca)
    
    
    Secu_pca.columns = ['Secu1']
    
    
    
    
    df2=CleanDataFrame.copy()

    col_to_drop = ["Prix_reduc"]
    cpY=df2.drop(col_to_drop,1)
    
    cpX=df2[['Cuisine','Réfrigérateur','Vaisselle_et_couverts','Four_à_micro_ondes','four','Lave_vaisselle','Cafetière','Cuisinière','Ustensiles_de_cuisine_de_base']]
    
    
    sc=StandardScaler()
    
    Z = sc.fit_transform(cpX)
    x = pd.DataFrame(Z)
    y = cpY.loc[:,['Prix_sans_reduc']].values
    
    pca = PCA(n_components=1)
    
    Cuisine_pca = pca.fit_transform(x)
    Cuisine_pca = pd.DataFrame(Cuisine_pca)

    
    Cuisine_pca.columns = ['Cuisine1']
    
    
        
    
    df3=CleanDataFrame.copy()

    col_to_drop = ["Prix_reduc"]
    cpY=df3.drop(col_to_drop,1)
    
    cpX=df3[['Note','Arrivée_irréprochable','Hôte_expérimenté','Excellente_communication','Accueil_unique']]
    
    
    sc=StandardScaler()
    
    Z = sc.fit_transform(cpX)
    x = pd.DataFrame(Z)
    y = cpY.loc[:,['Prix_sans_reduc']].values
    
    pca = PCA(n_components=1)
    
    Host_pca = pca.fit_transform(x)
    Host_pca = pd.DataFrame(Host_pca)
    
    
    Host_pca.columns = ['Host1']
    
    
    
    
    df4=CleanDataFrame.copy()

    col_to_drop = ["Prix_reduc"]
    cpY=df4.drop(col_to_drop,1)
    
    cpX=df4[['Bébés','Livres_et_jouets_pour_enfants','Lit_pour_bébé','Chaise_haute','Table_à_langer']]
    
    
    sc=StandardScaler()
    
    Z = sc.fit_transform(cpX)
    x = pd.DataFrame(Z)
    y = cpY.loc[:,['Prix_sans_reduc']].values
    
    pca = PCA(n_components=1)
    
    Bébé_pca = pca.fit_transform(x)
    Bébé_pca = pd.DataFrame(Bébé_pca)
    
    
    Bébé_pca.columns = ['Bébé1']
    
    
    
    df5=CleanDataFrame.copy()

    col_to_drop = ["Prix_reduc"]
    cpY=df5.drop(col_to_drop,1)
    
    cpX=df5[['Piscine','Jacuzzi','Salon_privé','Salle_de_sport']]
    

    sc=StandardScaler()
    
    Z = sc.fit_transform(cpX)
    x = pd.DataFrame(Z)
    y = cpY.loc[:,['Prix_sans_reduc']].values
    
    pca = PCA(n_components=1)
    
    Luxe_pca = pca.fit_transform(x)
    Luxe_pca = pd.DataFrame(Luxe_pca)
    
    Luxe_pca.columns = ['Luxe1']
    
    
        
    df6=CleanDataFrame.copy()

    col_to_drop = ["Prix_reduc"]
    
    cpY=df6.drop(col_to_drop,1)
    
    
    cpX=df6[['Nb_Salles_de_Bain','Nb_Lits','Nb_Voyageurs']]
    

    sc=StandardScaler()
    
    Z = sc.fit_transform(cpX)
    x = pd.DataFrame(Z)
    y = cpY.loc[:,['Prix_sans_reduc']].values
    
    pca = PCA(n_components=1)
    
    List_nb_pca = pca.fit_transform(x)
    List_nb_pca = pd.DataFrame(List_nb_pca)
    
    List_nb_pca.columns = ['List_nb']
    
    
    ACP_Base = pd.concat([Cuisine_pca,Secu_pca,Host_pca,Bébé_pca,Luxe_pca,List_nb_pca], axis=1)
    
    
    
    return ACP_Base


def rfe_select (Base, nb_var, model):
    
    if model =="LinearRegression":
        model=LinearRegression()
        
    elif model=="DecisionTreeRegressor":
        model=DecisionTreeRegressor()
    
    elif model=="RandomForestRegressor":
        model=RandomForestRegressor()
        
    elif model=="LinearSVR":
        model=LinearSVR()
        
    Test=Base.copy()  


    Test1=Test.drop(['Prix_sans_reduc','Prix_reduc'],axis=1)
  
    
    rfe = RFE(model, nb_var)
    
    rfe = rfe.fit(Test1, Test[["Prix_sans_reduc"]])
    
    List_var=list(compress(Test.columns, rfe.support_))
    
    if "Prix_sans_reduc" not in List_var:
        List_var.append('Prix_sans_reduc')
    else:
        pass
    
    try:
        List_var.remove("Prix_reduc")
    except:
        pass
    
    return Test[List_var]






