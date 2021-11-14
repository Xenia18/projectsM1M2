# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 02:39:25 2020

@author: Yanis
"""

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm




def cleaning (DataFrame):
    
    df=DataFrame.copy()
    df[['Prix_sans_reduc','Autre1']]=df['Prix_Originel'].str.split('€',n=1,expand=True)
    df[['Prix_reduc','Autre2']]=df['Prix_Reduc'].str.split('€',n=1,expand=True)
    df = df.astype({"Prix_sans_reduc": float, "Prix_reduc": float})
    
    df[['Autre3','Nb_comments']]=df['Nb_com'].str.split('(',n=1,expand=True)
    df[['Nb_comments','Autre3']]=df['Nb_comments'].str.split(')',n=1,expand=True)
    df = df.astype({ "Nb_comments": float})
    df[['Nb_Voyageurs','Autre3']]=df['Voyageurs'].str.split(' ',n=1,expand=True)
    #df[['Nb_Chambres','Autre3']]=df['Chambres'].str.split(' ',n=1,expand=True)
    df[['Nb_Lits','Autre3']]=df['Lits'].str.split(' ',n=1,expand=True)
    df[['Nb_Salles_de_Bain','Autre3']]=df['Salles_de_Bain'].str.split(' ',n=1,expand=True)
    df=df.drop(columns=['Autre3','Autre1','Prix_Originel','Prix_Reduc','Autre2','Nb_com','Salles_de_Bain','Lits','Voyageurs'])
    try:
        df=df.drop(columns=['Unnamed: 0'])
    except:
        pass
    
    #df1 = pd.read_csv(r'D:\downmoads_D\python\S2\Appartement\Mini_Base (1).csv', decimal=",",delimiter=";")
    df['Note']=df['Note'].str.replace(',','.')
    
    df[['Note','atr']]=df['Note'].str.split('(',n=1,expand=True)
    df[['Note']]=df[['Note']].apply(pd.to_numeric)
    df=df.drop(columns=['atr'])
    df['Nb_Salles_de_Bain']=df['Nb_Salles_de_Bain'].str.replace(',','.')
    df['Nb_Salles_de_Bain']=df['Nb_Salles_de_Bain'].str.replace('Demi-salle','0.5')
    df['Nb_Salles_de_Bain']=df['Nb_Salles_de_Bain'].str.replace('Demie','0.5')
    #df.to_csv('min-base-airbnb.csv')
    df = df.astype({ "Nb_Lits": float, 'Nb_Salles_de_Bain':float, 'Nb_Voyageurs':float})
    
    ## Traitement de valeurs manquantes ##
    df['Nb_comments'].fillna(0,inplace=True)
    
    mean = df["Note"].mean()
    df["Note"].fillna(mean, inplace=True)
    df['Description_type'].value_counts()

    #Remplacer par obs qui ressemble le plus
    
    mean1 = df["Nb_Salles_de_Bain"].mean()
    df["Nb_Salles_de_Bain"].fillna(mean1, inplace=True)
    
    mean2 = df["Nb_Lits"].mean()
    df["Nb_Lits"].fillna(mean2, inplace=True)
    
    try:
        df=df.drop(columns=['index'])
    except:
        pass
    
    df.dropna(subset=['Nom', 'Chambres','Description'],inplace=True)
    
    try:
        df=df.drop(columns=['Unnamed: 0.1',])
    except:
        pass
    
    df = df.reset_index()
    ## Création de variables##
    
    culte=['Montparnasse','Eiffel','Elysées','Triomphe','Louvre','Dame','Sacré','Montmartre','Michel','Panthéon','Luxembourg','Orsay','Honoré','Germain','Madeleine','Concorde','Odéon']
    
    for y in range (len(df['Description'].tolist())):
        if type(df['Description'][y]) is str :
            counter=0
            for x in culte:
                if x in df['Description'][y] or x in df['Nom'][y]:
                    counter+=1	
            if counter==0:      
                df.at[y, 'coté'] = 0
            else:
                df.at[y, 'coté'] = 1
        else:
            df.at[y, 'coté'] = 0
            
    
            
    
    df['parking']= df['Parking_payant']+df['Parking_gratuit']
    df['parking']=df['parking'].replace(2,1)
    df['parking'].value_counts()
    
    
    df['propre,rangé']=df['Parfaitement_propre']+df['Propre et rangé']
    
    
    df['Nb_équipement']=df['Nb_équipement'].str.replace(' ','')
    df[['qtr','Nb_équipement_total']]=df['Nb_équipement'].str.split('s',n=1,expand=True)
    df[['Nb_équipement_total','qtr']]=df['Nb_équipement_total'].str.split('é',n=1,expand=True)
    df['Nb_équipement_total'].value_counts()
    
    df['Nb_équipement_total']=df['Nb_équipement_total'].replace('lesd', np.nan)
    df = df.astype({ "Nb_équipement_total": float})
    mean = df["Nb_équipement_total"].mean()
    df["Nb_équipement_total"].fillna(mean, inplace=True)
    df['Nb_équipement']=df["Nb_équipement_total"]
    df = df.drop(columns=['qtr','Nb_équipement_total'])
    
    
    ## Isolation des variables numériques ##
    data_num = df
    object_col = [ "Nom", "Description_type", "Chambres", "index", "Description", "Lien"]
    data = data_num.drop(object_col,1)

    
    try:
        df=df.drop(columns=['index'])
    except:
        pass
    
    
    df["Studio"]=((df['Chambres'] == 'Studio')).astype(int)
    df=df.drop(columns=['Nom','Description_type','Chambres','Description','Lien'])
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.reset_index(inplace=True)
    
    try:
        df=df.drop(columns=['index'])
    except:
        pass
    
    q = df["Prix_sans_reduc"].quantile(0.95)
    
    df_sans_extrem=df[df["Prix_sans_reduc"] < q]


    return df_sans_extrem