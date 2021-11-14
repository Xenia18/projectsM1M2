# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:08:45 2020

@author: Yanis
"""



import pandas as pd
import numpy as np
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



def Search(chrome_path, Ville, Adultes, Enfants, Bébés, Arrivée_Mois, Arrivée_Jour, Départ_Mois, Départ_Jour):
    
    
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://www.airbnb.fr/")
    time.sleep(4)
    Cookies=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button')
    Cookies.click()
    wait = WebDriverWait(driver, 20)
    
    
    time.sleep(2)
    
    
    ville= driver.find_element_by_xpath('//*[@id="bigsearch-query-attached-query"]')
    ville.clear()
    ville.send_keys(Ville)
    
    
    
    time.sleep(2)   
    
    
        
    Dates= driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/button')
    Dates.click()
    
    time.sleep(2)

    date = datetime.datetime.now()
    Mois=date.month
    
    
    if Arrivée_Mois == Mois:
        
        time.sleep(2)
        end="(@aria-label, ' "+str(Arrivée_Jour) +""" ')]"""
        Choix_date_Arrivée = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[contains"+end )
        Choix_date_Arrivée.click()
       

    else:
        
        time.sleep(2)
        count_1=Arrivée_Mois-Mois
        i=0
        
        while count_1>i:
            
            time.sleep(2)
            Mois_suivant=driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/button')
            Mois_suivant.click()
            i+=1
        
        driver.implicitly_wait(5)
        time.sleep(2)
        end_1="(@aria-label, ' "+str(Arrivée_Jour) +""" ')]"""
        Choix_date_Arrivée = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[contains"+end_1 )
        Choix_date_Arrivée.click()
       

    if Départ_Mois == Mois:
        
        driver.implicitly_wait(5)
        time.sleep(2)
        end_2="(@aria-label, ' "+str(Départ_Jour) +""" ')]"""
        Choix_date_Départ = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[contains"+end_2 )
        Choix_date_Départ.click()
        
    else:
        
        if Départ_Mois == Arrivée_Mois :
            
            driver.implicitly_wait(5)
            time.sleep(1)
            end_2="(@aria-label, ' "+str(Départ_Jour) +""" ')]"""
            Choix_date_Départ = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[contains"+end_2 )
            Choix_date_Départ.click()
            
        else:
            driver.implicitly_wait(5)
            time.sleep(2)
            count_2=Départ_Mois-Arrivée_Mois
            
            j=0
            
            while count_2>j:
                
                time.sleep(2)
                Mois_suivant=driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/button')
                Mois_suivant.click()
                j+=1
                
            driver.implicitly_wait(5)
            time.sleep(2)
            end_2="(@aria-label, ' "+str(Départ_Jour) +""" ')]"""
            Choix_date_Départ = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[contains"+end_2 )
            Choix_date_Départ.click()
            
            
            
    
    time.sleep(2)
    
    
    Voyageurs=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="_twinlf"][contains(text(), "Ajoutez des voyageurs")]')))
    Voyageurs.click()
    time.sleep(2)
    
    A=0
    E=0
    B=0
    
    while Adultes>A:
        
        driver.implicitly_wait(5)
        time.sleep(2)
        
        adultes=driver.find_element_by_xpath('//*[@id="stepper-adults"]/button[2]')
        adultes.click()
    
        A+=1
        
    while Enfants>E:
        
        driver.implicitly_wait(5)
        time.sleep(2)
    
        enfants=driver.find_element_by_xpath('//*[@id="stepper-children"]/button[2]')
        enfants.click()
        
        
        E+=1
        
    while Bébés>B:
        
        driver.implicitly_wait(5)
        time.sleep(2)
        
        bébés=driver.find_element_by_xpath('//*[@id="stepper-infants"]/button[2]')
        bébés.click()
        B+=1
        
    
    
    
            
    Lancer_Recherche=driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[2]/button')
    Lancer_Recherche.click()
    
    
    link=driver.current_url
    driver.close()
    

    return link


    