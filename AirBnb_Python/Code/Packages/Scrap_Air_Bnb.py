# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:24:38 2020

@author: Yanis
"""

import pandas as pd
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException


def Scrap_Air_Bnb (chrome_path, lien, Nb_vingtaine_pages):
        
    app_urls=[]
    
    Base_final=pd.DataFrame()
    
    Compteur=0
    
    while Compteur<Nb_vingtaine_pages:
    
    
        driver=webdriver.Chrome(chrome_path)
        driver.get(lien)
        time.sleep(4)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div[4]/div[2]/div/button'))).click()
        driver.maximize_window()
        
        
    
        
        publication_urls = driver.find_elements_by_class_name('_8ssblpx')
        
        
        for i in publication_urls:
            
            url_loc=i.find_element_by_xpath(".//div/div/div/div/a").get_attribute("href")
            app_urls.append(url_loc)
            
    
    
        
        for urls in app_urls:
            driver.get(urls)  
            time.sleep(3)
            
            
            Nom_list=[]
            Description_type_list=[]
            
            Prix_Originel_list=[]
            Prix_Reduc_list=[]
            
            Voyageurs_list=[]
            Chambres_list=[]
            Lits_list=[]
            Salles_de_Bain_list=[]
            
            
            Note_list=[]
            Nb_com_list=[]
            
            Logement_Entier_list=[]
            
            Arrivée_irréprochable_list=[]
            Excellente_communication_list=[]
            Accueil_unique_list=[]
            Hôte_expérimenté_list=[]
            Parfaitement_propre_list=[]
            Propre_et_rangé_list=[]
            Idéalement_situé_list=[]
            Annulation_gratuite_pendant_48_heures_list=[]
            Annulation_gratuite_longue_list=[]
            Arrivée_autonome1_list=[]
            Superhost_list=[]
            Description_list=[]
                
            ########Standard
            Wifi_list=[]
            WiFi_portable_list=[]
            Lave_linge_list=[]
            Espace_travail_ordi_list=[]
            Equipement_base_list=[]
            Chauffage_list=[]
            Fer_à_Repasser_list=[]
            Télévision_list=[]
            Eau_chaude_list=[]
            Cheminée_list=[]
            Climatisation_list=[]
            Sèche_linge_list=[]
            Connexion_Ethernet_list=[]
            
            #######Équipements pour les familles
            Table_à_langer_list=[]
            Chaise_haute_list=[]
            Lit_pour_bébé_list=[]
            Livres_et_jouets_pour_enfants_list=[]
            
            ######Installations
            
            Parking_payant_list=[]
            Parking_gratuit_list=[]
            Chargeur_EV_list=[]
            Salle_de_sport_list=[]
            Jacuzzi_list=[]
            Ascenseur_list=[]
            Piscine_list=[]
            
            
            
            ###############Restauration
            Cuisine_list=[]
            Réfrigérateur_list=[]
            Vaisselle_et_couverts_list=[]
            Four_à_micro_ondes_list=[]
            Petit_déjeuner_list=[]
            four_list=[]
            Lave_vaisselle_list=[]
            Cafetière_list=[]
            Cuisinière_list=[]
            Ustensiles_de_cuisine_de_base_list=[]
            
            
            
            ############Accès des voyageurs
            
            
            Personnel_list=[]
            Entrée_privée_list=[]
            Salon_privé_list=[]
            Boîte_à_clé_sécurisée_list=[]
            Clés_remises_par_hôte_list=[]
            
            
            ############### Extérieur
            
            Jardin_list=[]
            
            
            ##########Salle de bain et chambre
            Sèche_cheveux_list=[]
            Cintres_list=[]
            Shampooing_list=[]
            Gel_douche_list=[]
            Oreillers_et_couvertures_supplémentaires_list=[]
            Draps_list=[]
            Porte_de_la_chambre_avec_verrou_list=[]
            
            
            
            ####Logistique
            Dépôt_de_bagages_autorisé_list=[]
            Séjours_longue_durée_autorisé_list=[]
            
            
            ###############Securité
            Détecteur_de_fumée_list=[]
            Détecteur_de_monoxyde_de_carbone_list=[]
            Extincteur_list=[]
            Kit_de_premiers_secours_list=[]
            
            Nb_équipement_list=[]
            
            Fête_list=[] 
            Fumeur_list=[]
            Animaux_list=[]
            Bébés_list=[]
        
            lien_list=[]
        
        
            try:
                try:
                    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/div[1]/div/div/header/div/div[1]/a[@class="_1bbjafr"]')
                    continue
                    
                except:
                    
                    try:
                        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/div[1]/div/div/header/div/div[1]/a[@class="_mn0k6xr"]')
                        continue
                    
                    except:
                        
                        
                        try: 
                            driver.find_element_by_xpath('//*[@id="summary"]/div/div/div[1]/div/div/div[1]/div[1]/div/span/h1/span')
                        
                        
                            Nom=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="summary"]/div/div/div[1]/div/div/div[1]/div[1]/div/span/h1/span'))).text
                            Nom_list.append(Nom)        
                            
                            Prix_originel=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="room"]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]//span[contains(text(), "€")]'))).text
                            Prix_Originel_list.append(Prix_originel) 
                            
                            Prix_Reduc=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="room"]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]//span[contains(text(), "nuit")]/parent::span/preceding-sibling::span/span'))).text
                            Prix_Reduc_list.append(Prix_Reduc) 
                            
                            try:
                                Note=driver.find_element_by_xpath('//*[@id="room"]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/button/div/div[1]/div[2]/div/div').text
                                Note_list.append(Note)
                            except:
                                Note_list.append("nan")
                    
                            try:
                                Nb_com=driver.find_element_by_xpath('//*[@id="room"]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/button/div/span').text
                                Nb_com_list.append(Nb_com)
                            except:
                                Nb_com_list.append("nan")
                                
                            
                            
                            try: 
                                
                                carac=driver.find_element_by_xpath('//*[@id="room"]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div[1]')
                            
                                try:
                                    Voyageurs=carac.find_element_by_xpath('.//div[contains(text(), "voyageur")]').text
                                    Voyageurs_list.append(Voyageurs)
                                except:
                                    Voyageurs_list.append("nan")
                                    
                                try:
                                    try:
                                        Chambres=carac.find_element_by_xpath('.//div[contains(text(), "chambre")]').text
                                        Chambres_list.append(Chambres)
                                    except:
                                        Chambres=carac.find_element_by_xpath('.//div[contains(text(), "Studio")]').text
                                        Chambres_list.append(Chambres)
                                except:
                                    Chambres_list.append("nan")
                                    
                                try:
                                    Lits=carac.find_element_by_xpath('.//div[contains(text(), "lit")]').text
                                    Lits_list.append(Lits)
                                except:
                                    Lits_list.append("nan")
                                try:
                                    Salles_de_Bain=carac.find_element_by_xpath('.//div[contains(text(), "bain")]').text
                                    Salles_de_Bain_list.append(Salles_de_Bain)
                                except:
                                    Salles_de_Bain_list.append("nan")
                                   
                            except:
                                
                                 carac=driver.find_element_by_xpath('//*[@id="room"]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]//div[contains(text(), "privée")]/following::div')
                                 
                                 try:
                                     Voyageurs=carac.find_element_by_xpath('.//div[contains(text(), "voyageur")]').text
                                     Voyageurs_list.append(Voyageurs)
                                 except:
                                     Voyageurs_list.append("nan")
                                    
                                 try:
                                     try:
                                         Chambres=carac.find_element_by_xpath('.//div[contains(text(), "chambre")]').text
                                         Chambres_list.append(Chambres)
                                     except:
                                        Chambres=carac.find_element_by_xpath('.//div[contains(text(), "Studio")]').text
                                        Chambres_list.append(Chambres)
                                 except:
                                    Chambres_list.append("nan")
                                    
                                 try:
                                     Lits=carac.find_element_by_xpath('.//div[contains(text(), "lit")]').text
                                     Lits_list.append(Lits)
                                 except:
                                     Lits_list.append("nan")
                                     
                                    
                                
                                 try:
                                     Salles_de_Bain=carac.find_element_by_xpath('.//div[contains(text(), "bain")]').text
                                     Salles_de_Bain_list.append(Salles_de_Bain)
                                 except:
                                     Salles_de_Bain_list.append("nan")
                                     
                                 
                    
                            
                            try:
                                Highlights=driver.find_element_by_xpath('//*[@id="room"]/div[2]/div/div[2]/div[1]/div/div[3]/div')
                                
                                try:
                                    Description_type=Highlights.find_element_by_xpath('.//span[contains(text(), "Logement entier")]/following::div').text
                                    Description_type_list.append(Description_type)
                                except:
                                     Description_type=Highlights.find_element_by_xpath('.//div[contains(text(), "priv")]').text
                                     Description_type_list.append(Description_type)
                                
                                
                                
                                try:
                                    Logement_Entier=Highlights.find_element_by_xpath('.//span[contains(text(), "Logement entier")]')
                                    Logement_Entier_list.append(1)
                                except:
                                        Logement_Entier_list.append(0)
                                                               
                                    
                                try:
                                    Arrivée_irréprochable=Highlights.find_element_by_xpath('.//span[contains(text(), "arrivée irréprochable")]')
                                    Arrivée_irréprochable_list.append(1)
                                except:
                                    Arrivée_irréprochable_list.append(0)
                                
                    
                                try:
                                    Excellente_communication=Highlights.find_element_by_xpath('.//span[contains(text(), "Excellente communication")]')
                                    Excellente_communication_list.append(1)
                                except:
                                    Excellente_communication_list.append(0)
                     
                                try:
                                    Hôte_expérimenté=Highlights.find_element_by_xpath('.//span[contains(text(), "hôte expérimenté")]')
                                    Hôte_expérimenté_list.append(1)
                                except:
                                    Hôte_expérimenté_list.append(0)                
                    
                                try:
                                    Accueil_unique=Highlights.find_element_by_xpath('.//span[contains(text(), "Accueil unique")]')
                                    Accueil_unique_list.append(1)
                                except:
                                    Accueil_unique_list.append(0)
                                
                                
                                try:
                                    Parfaitement_propre=Highlights.find_element_by_xpath('.//span[contains(text(), "Parfaitement propre")]')
                                    Parfaitement_propre_list.append(1)
                                except:
                                    Parfaitement_propre_list.append(0)            
            
                                try:
                                    Propre_et_rangé=Highlights.find_element_by_xpath('.//span[contains(text(), "Propre et rangé")]')
                                    Propre_et_rangé_list.append(1)
                                except:
                                    Propre_et_rangé_list.append(0)   
                                
                                try:
                                    Idéalement_situé=Highlights.find_element_by_xpath('.//span[contains(text(), "Idéalement situé")]')
                                    Idéalement_situé_list.append(1)
                                except:
                                    Idéalement_situé_list.append(0)              
                    
                                try:
                                    Annulation_gratuite_pendant_48_heures=Highlights.find_element_by_xpath('.//div[contains(text(), "Annulation gratuite pendant")]')
                                    Annulation_gratuite_pendant_48_heures_list.append(1)
                                except:
                                    Annulation_gratuite_pendant_48_heures_list.append(0)    
                                
                                
                                try:
                                    Annulation_gratuite_longue=Highlights.find_element_by_xpath('.//span[contains(text(), "Annulation gratuite jusqu")]')
                                    Annulation_gratuite_longue_list.append(1)
                                except:
                                    Annulation_gratuite_longue_list.append(0)            
                    
                    
                                try:
                                    Arrivée_autonome1=Highlights.find_element_by_xpath('.//span[contains(text(), "Arrivée autonome")]')
                                    Arrivée_autonome1_list.append(1)
                                except:
                                    Arrivée_autonome1_list.append(0)  
                    
                                try:
                                    Superhost=Highlights.find_element_by_xpath('.//span[contains(text(), "Superhost")]')
                                    Superhost_list.append(1)
                                except:
                                    Superhost_list.append(0)                  
                                
                            except:
                                pass  
                            
                            try:
                                try:
                                    driver.find_element_by_xpath('//*[@id="details"]//div[contains(text(), "En savoir plus sur le logement")]')
                                
                                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="details"]//div[contains(text(), "En savoir plus sur le logement")]'))).click()
                
                                
                                    Description=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="details"]'))).text
                                    Description_list.append(Description)
                                    
                                except:
                                    Description=driver.find_element_by_xpath('//*[@id="details"]').text
                                    Description_list.append(Description)
                            except:
                                Description_list.append("nan")
                            
                            lien_list.append(driver.current_url)
                            
                            
                                
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                        
                                    
                        
                        except:
                            
                            try:
                                Nom=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="site-content"]/div/div[1]/div/div/div/section/div[1]/div[1]/h1'))).text
                                Nom_list.append(Nom)
                            except:
                                Nom_list.append("nan")
                                
                            try:
                                Prix_originel=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="site-content"]/div/div[4]/div/div/div[3]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/span/span'))).text
                                Prix_Originel_list.append(Prix_originel) 
                            except:
                                Prix_Originel_list.append("nan")
                                
                            try: 
                                Prix_Reduc=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="site-content"]/div/div[4]/div/div/div[3]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div//span[contains(text(), "nuit")]/preceding-sibling::span'))).text
                                Prix_Reduc_list.append(Prix_Reduc)
                            except:
                                Prix_Reduc_list.append("nan")
                            
                            
                            try:
                                Note=driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div/div/div/section/div[1]/div[2]/span[1]/span[2]/button').text[0:4]
                                Note_list.append(Note)
                            except:
                                Note_list.append("nan")
                    
                            try:
                                Nb_com=driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div/div/div/section/div[1]/div[2]/span[1]/span[2]/button').text[4:]
                                Nb_com_list.append(Nb_com)
                            except:
                                Nb_com_list.append("nan")
                                
                            try:
                                try:
                                    driver.find_element_by_xpath('//*[@id="site-content"]/div/div[4]/div/div/div[1]/div[2]/div//div[contains(text(), "Logement entier")]')
                                    
                                    Description_type=driver.find_element_by_xpath('//*[@id="site-content"]/div/div[4]/div/div/div[1]/div[2]/div//div[contains(text(), "Logement entier")]/following::div').text
                                    Description_type_list.append(Description_type)  
                                    
                                except:
                                    Description_type=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="site-content"]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/section/div/div/div/div[1]/div[1]'))).text
                                    Description_type_list.append(Description_type)
                            except:
                                Description_type_list.append("nan")
                                
                                
                            try:
                                carac=driver.find_element_by_xpath('//*[@id="site-content"]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/section/div/div/div/div[1]')
                            except:
                                pass
                            
                            try:
                                Voyageurs=carac.find_element_by_xpath('.//div/span[contains(text(), "voyageur")]').text
                                Voyageurs_list.append(Voyageurs)
                            except:
                                Voyageurs_list.append("nan")
                                
                            
                            try:
                                try:
                                    Chambres=carac.find_element_by_xpath('.//div/span[contains(text(), "chambre")]').text
                                    Chambres_list.append(Chambres)
                                except:
                                    Chambres=carac.find_element_by_xpath('.//div/span[contains(text(), "Studio")]').text
                                    Chambres_list.append(Chambres)
                            except:
                                Chambres_list.append("nan")
                                
                            
                            try:
                                Lits=carac.find_element_by_xpath('.//div/span[contains(text(), "lit")]').text
                                Lits_list.append(Lits)
                            except:
                                Lits_list.append("nan")
                                
                            
                            try:
                                Salles_de_Bain=carac.find_element_by_xpath('.//div/span[contains(text(), "bain")]').text
                                Salles_de_Bain_list.append(Salles_de_Bain)
                            except:
                                Salles_de_Bain_list.append("nan")
                                
                                
                                
                                
                            try:
                                Highlights=driver.find_element_by_xpath('//*[@id="site-content"]/div/div[4]/div/div/div[1]/div[2]/div')
                            except:
                                pass
                    
                            try:
                                Logement_Entier=Highlights.find_element_by_xpath('.//div[contains(text(), "Logement entier")]')
                                Logement_Entier_list.append(1)
                            except:
                                    Logement_Entier_list.append(0)
                                
                                
                            try:
                                Arrivée_irréprochable=Highlights.find_element_by_xpath('.//div[contains(text(), "arrivée irréprochable")]')
                                Arrivée_irréprochable_list.append(1)
                            except:
                                Arrivée_irréprochable_list.append(0)
                
                            try:
                                Excellente_communication=Highlights.find_element_by_xpath('.//div[contains(text(), "Excellente communication")]')
                                Excellente_communication_list.append(1)
                            except:
                                Excellente_communication_list.append(0)
                                
                
                            try:
                                Accueil_unique=Highlights.find_element_by_xpath('.//div[contains(text(), "Accueil unique")]')
                                Accueil_unique_list.append(1)
                            except:
                                Accueil_unique_list.append(0)
                            
                            
                            try:
                                Parfaitement_propre=Highlights.find_element_by_xpath('.//div[contains(text(), "Parfaitement propre")]')
                                Parfaitement_propre_list.append(1)
                            except:
                                Parfaitement_propre_list.append(0)   
        
                            try:
                                Propre_et_rangé=Highlights.find_element_by_xpath('.//div[contains(text(), "Propre et rangé")]')
                                Propre_et_rangé_list.append(1)
                            except:
                                Propre_et_rangé_list.append(0)   
                                
                
                                
                            try:
                                Hôte_expérimenté=Highlights.find_element_by_xpath('.//div[contains(text(), "hôte expérimenté")]')
                                Hôte_expérimenté_list.append(1)
                            except:
                                Hôte_expérimenté_list.append(0)    
                            
                            try:
                                Idéalement_situé=Highlights.find_element_by_xpath('.//div[contains(text(), "Idéalement situé")]')
                                Idéalement_situé_list.append(1)
                            except:
                                Idéalement_situé_list.append(0)              
                
                            try:
                                Annulation_gratuite_pendant_48_heures=Highlights.find_element_by_xpath('.//div[contains(text(), "Annulation gratuite pendant")]')
                                Annulation_gratuite_pendant_48_heures_list.append(1)
                            except:
                                Annulation_gratuite_pendant_48_heures_list.append(0)    
                            
                            
                            try:
                                Annulation_gratuite_longue=Highlights.find_element_by_xpath('.//div[contains(text(), "Annulation gratuite jusqu")]')
                                Annulation_gratuite_longue_list.append(1)
                            except:
                                Annulation_gratuite_longue_list.append(0)            
                
                
                            try:
                                Arrivée_autonome1=Highlights.find_element_by_xpath('.//div[contains(text(), "Arrivée autonome")]')
                                Arrivée_autonome1_list.append(1)
                            except:
                                Arrivée_autonome1_list.append(0)  
                
                            try:
                                Superhost=Highlights.find_element_by_xpath('.//div[contains(text(), "Superhost")]')
                                Superhost_list.append(1)
                            except:
                                Superhost_list.append(0)                  
                            
                           
                            
                            
                            try:
                                if driver.find_element_by_xpath('//*[@data-plugin-in-point-id="DESCRIPTION_DEFAULT"]//*[@class="_siy8gh"]').text[-5:]=="suite":
                                
        
                                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@data-plugin-in-point-id="DESCRIPTION_DEFAULT"]//*[@class="_siy8gh"]//button'))).click()
                
                                
                                    Description=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@data-plugin-in-point-id="DESCRIPTION_DEFAULT"]//*[@class="_siy8gh"]'))).text
                                    Description_list.append(Description)
                                    
                                else:
                                    Description=driver.find_element_by_xpath('//*[@data-plugin-in-point-id="DESCRIPTION_DEFAULT"]//*[@class="_siy8gh"]').text
                                    Description_list.append(Description)
                            except:
                                Description_list.append("nan")
                                
                                
                                
                            try:
                                driver.find_element_by_xpath('//*[@class="_h0dm2e"][contains(text(), "Règlement intérieur")]/following::div/span[contains(text(), "pas ")][contains(text(), "bébés")]')
                                Bébés_list.append(0)
                            except:
                                Bébés_list.append(1)
                                
                                
                            try:
                                driver.find_element_by_xpath('//*[@class="_h0dm2e"][contains(text(), "Règlement intérieur")]/following::div/span[contains(text(), "Pas ")][contains(text(), "animaux")]')
                                Animaux_list.append(0)
                            except:
                                Animaux_list.append(1)
                                
                            try:
                                driver.find_element_by_xpath('//*[@class="_h0dm2e"][contains(text(), "Règlement intérieur")]/following::div/span[contains(text(), "Non")][contains(text(), "fumeur")]')
                                Fumeur_list.append(0)
                            except:
                                Fumeur_list.append(1)
                                
                                
                            try:
                                driver.find_element_by_xpath('//*[@class="_h0dm2e"][contains(text(), "Règlement intérieur")]/following::div/span[contains(text(), "Pas")][contains(text(), "fête")]')
                                Fête_list.append(0)
                            except:
                                Fête_list.append(1)    
                                
                                
                            try:
                                Nb_equipement=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@formfactor="DESKTOP"][contains(text(), "Afficher ")][contains(text(), "équipement")]'))).text
                                Nb_équipement_list.append(Nb_equipement)
                            except:
                                Nb_équipement_list.append("nan")
                                
                                
                        
                            try:
                                elem=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@formfactor="DESKTOP"][contains(text(), "Afficher ")][contains(text(), "équipement")]')))
                                elem.click()
                            except:
                                pass
                            
                            try:
                                wait.until(EC.presence_of_element_located((By.XPATH,'//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]')))
                            
                                
                            except:
                                pass
    
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Wi-Fi")]')
                                 
                            except InvalidSelectorException:
                                Wifi_list.append(1)    
                            except NoSuchElementException :
                                Wifi_list.append(0)
                                
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Wi-Fi portable")]')
                                 
                            except InvalidSelectorException:
                                WiFi_portable_list.append(1)    
                            except NoSuchElementException :
                                WiFi_portable_list.append(0)
                                    
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Lave-linge")]')
                             
                            except InvalidSelectorException:
                                Lave_linge_list.append(1)    
                            except NoSuchElementException :
                                Lave_linge_list.append(0)                            
                                
                                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Espace de travail pour ordinateur")]')
                             
                            except InvalidSelectorException:
                                Espace_travail_ordi_list.append(1)    
                            except NoSuchElementException :
                                Espace_travail_ordi_list.append(0)    
                                                    
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Équipements de base")]')
                             
                            except InvalidSelectorException:
                                Equipement_base_list.append(1)    
                            except NoSuchElementException :
                                Equipement_base_list.append(0)    
                                                    
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Chauffage")]')
                             
                            except InvalidSelectorException:
                                Chauffage_list.append(1)    
                            except NoSuchElementException :
                                Chauffage_list.append(0)           
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Fer à repasser")]')
                             
                            except InvalidSelectorException:
                                Fer_à_Repasser_list.append(1)    
                            except NoSuchElementException :
                                Fer_à_Repasser_list.append(0)      
                            
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Télévision")]')
                             
                            except InvalidSelectorException:
                                Télévision_list.append(1)    
                            except NoSuchElementException :
                                Télévision_list.append(0)   
                                
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Eau chaude")]')
                                 
                            except InvalidSelectorException:
                                Eau_chaude_list.append(1)    
                            except NoSuchElementException :
                                Eau_chaude_list.append(0)    
                                
                                
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Cheminée")]')
                                 
                            except InvalidSelectorException:
                                Cheminée_list.append(1)    
                            except NoSuchElementException :
                                Cheminée_list.append(0)    
                                
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Climatisation")]')
                                 
                            except InvalidSelectorException:
                                Climatisation_list.append(1)    
                            except NoSuchElementException :
                                Climatisation_list.append(0)
                                
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Sèche-linge")]')
                                 
                            except InvalidSelectorException:
                                Sèche_linge_list.append(1)    
                            except NoSuchElementException :
                                Sèche_linge_list.append(0)    
                                
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Standard")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Connexion Ethernet")]')
                                 
                            except InvalidSelectorException:
                                Connexion_Ethernet_list.append(1)    
                            except NoSuchElementException :
                                Connexion_Ethernet_list.append(0)    
                                
                                
                            
                            #######Équipements pour les familles
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Équipements pour les familles")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Connexion Ethernet")]')
                                 
                            except InvalidSelectorException:
                                Table_à_langer_list.append(1)    
                            except NoSuchElementException :
                                Table_à_langer_list.append(0)    
                                
                                
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Équipements pour les familles")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Chaise haute")]')
                                 
                            except InvalidSelectorException:
                                Chaise_haute_list.append(1)    
                            except NoSuchElementException :
                                Chaise_haute_list.append(0)    
                                    
                                
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Équipements pour les familles")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Lit pour bébé")]')
                                 
                            except InvalidSelectorException:
                                Lit_pour_bébé_list.append(1)    
                            except NoSuchElementException :
                                Lit_pour_bébé_list.append(0)    
                                    
                                
                                
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Équipements pour les familles")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Livres et jouets pour enfants")]')
                                 
                            except InvalidSelectorException:
                                Livres_et_jouets_pour_enfants_list.append(1)    
                            except NoSuchElementException :
                                Livres_et_jouets_pour_enfants_list.append(0)    
                                    
                                
                            ######Installations
                            
                            
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Installations")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Parking payant")]')
                                 
                            except InvalidSelectorException:
                                Parking_payant_list.append(1)    
                            except NoSuchElementException :
                                Parking_payant_list.append(0)    
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Installations")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Parking gratuit")]')
                                 
                            except InvalidSelectorException:
                                Parking_gratuit_list.append(1)    
                            except NoSuchElementException :
                                Parking_gratuit_list.append(0)    
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Installations")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Chargeur EV")]')
                                 
                            except InvalidSelectorException:
                                Chargeur_EV_list.append(1)    
                            except NoSuchElementException :
                                Chargeur_EV_list.append(0)    
                            
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Installations")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Salle de sport")]')
                                 
                            except InvalidSelectorException:
                                Salle_de_sport_list.append(1)    
                            except NoSuchElementException :
                                Salle_de_sport_list.append(0)    
                            
                            
                                    
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Installations")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Jacuzzi")]')
                                 
                            except InvalidSelectorException:
                                Jacuzzi_list.append(1)    
                            except NoSuchElementException :
                                Jacuzzi_list.append(0)    
                                    
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Installations")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Ascenseur")]')
                                 
                            except InvalidSelectorException:
                                Ascenseur_list.append(1)    
                            except NoSuchElementException :
                                Ascenseur_list.append(0)    
                                    
                            
                            
                            try:
                                
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Installations")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Piscine_list")]')
                                 
                            except InvalidSelectorException:
                                Piscine_list.append(1)    
                            except NoSuchElementException :
                                Piscine_list.append(0)    
                                
                                    
                            
                            
                            ######### Restauration    
                            
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Cuisine")]')
                             
                            except InvalidSelectorException:
                                Cuisine_list.append(1)    
                            except NoSuchElementException :
                                Cuisine_list.append(0)      
                                
                                
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Réfrigérateur")]')
                             
                            except InvalidSelectorException:
                                Réfrigérateur_list.append(1)    
                            except NoSuchElementException:
                                Réfrigérateur_list.append(0)      
                                    
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Vaisselle et couverts")]')
                             
                            except InvalidSelectorException:
                                Vaisselle_et_couverts_list.append(1)    
                            except NoSuchElementException:
                                Vaisselle_et_couverts_list.append(0)  
                            
                             
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Four à micro-ondes")]')
                             
                            except InvalidSelectorException:
                                Four_à_micro_ondes_list.append(1)    
                            except NoSuchElementException:
                                Four_à_micro_ondes_list.append(0)  
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Petit déjeuner")]')
                             
                            except InvalidSelectorException:
                                Petit_déjeuner_list.append(1)    
                            except NoSuchElementException:
                                Petit_déjeuner_list.append(0)       
                                    
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Four")]')
                             
                            except InvalidSelectorException:
                                four_list.append(1)    
                            except NoSuchElementException:
                                four_list.append(0)  
                                
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Lave-vaisselle")]')
                             
                            except InvalidSelectorException:
                                Lave_vaisselle_list.append(1)    
                            except NoSuchElementException:
                                Lave_vaisselle_list.append(0)  
                                
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Cafetière")]')
                             
                            except InvalidSelectorException:
                                Cafetière_list.append(1)    
                            except NoSuchElementException:
                                Cafetière_list.append(0)  
                                
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Cuisinière")]')
                             
                            except InvalidSelectorException:
                                Cuisinière_list.append(1)    
                            except NoSuchElementException:
                                Cuisinière_list.append(0)
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Ustensiles de cuisine de base")]')
                             
                            except InvalidSelectorException:
                                Ustensiles_de_cuisine_de_base_list.append(1)    
                            except NoSuchElementException:
                                Ustensiles_de_cuisine_de_base_list.append(0)
                                
                            
                            ############Accès des voyageurs
                            
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Accès des voyageurs")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Personnel")]')
                             
                            except InvalidSelectorException:
                                Personnel_list.append(1)    
                            except NoSuchElementException:
                                Personnel_list.append(0)
                                    
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Accès des voyageurs")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Entrée privée")]')
                             
                            except InvalidSelectorException:
                                Entrée_privée_list.append(1)    
                            except NoSuchElementException:
                                Entrée_privée_list.append(0)
                                
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Accès des voyageurs")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Salon privé")]')
                             
                            except InvalidSelectorException:
                                Salon_privé_list.append(1)    
                            except NoSuchElementException:
                                Salon_privé_list.append(0)
                                
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Accès des voyageurs")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Boîte à clé sécurisée")]')
                             
                            except InvalidSelectorException:
                                Boîte_à_clé_sécurisée_list.append(1)    
                            except NoSuchElementException:
                                Boîte_à_clé_sécurisée_list.append(0)
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Accès des voyageurs")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Clés remises par hôte")]')
                             
                            except InvalidSelectorException:
                                Clés_remises_par_hôte_list.append(1)    
                            except NoSuchElementException:
                                Clés_remises_par_hôte_list.append(0)
                                                
                                
                            ###################### Extérieur    
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Restauration")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Jardin")]')
                             
                            except InvalidSelectorException:
                                Jardin_list.append(1)    
                            except NoSuchElementException:
                                Jardin_list.append(0)  
                                
                                
                            ########################## Chambre et salle de bain
          
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Chambre et salle de bain")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Sèche-cheveux")]')
                             
                            except InvalidSelectorException:
                                Sèche_cheveux_list.append(1)    
                            except NoSuchElementException:
                                Sèche_cheveux_list.append(0)
                                
                                
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Chambre et salle de bain")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Cintres")]')
                             
                            except InvalidSelectorException:
                                Cintres_list.append(1)    
                            except NoSuchElementException:
                                Cintres_list.append(0)
                              
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Chambre et salle de bain")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Shampooing")]')
                             
                            except InvalidSelectorException:
                                Shampooing_list.append(1)    
                            except NoSuchElementException:
                                Shampooing_list.append(0)
                                    
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Chambre et salle de bain")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Gel douche")]')
                             
                            except InvalidSelectorException:
                                Gel_douche_list.append(1)    
                            except NoSuchElementException:
                                Gel_douche_list.append(0)
                                    
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Chambre et salle de bain")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Oreillers et couvertures supplémentaires")]')
                             
                            except InvalidSelectorException:
                                Oreillers_et_couvertures_supplémentaires_list.append(1)    
                            except NoSuchElementException:
                                Oreillers_et_couvertures_supplémentaires_list.append(0)
                                
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Chambre et salle de bain")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Draps")]')
                             
                            except InvalidSelectorException:
                                Draps_list.append(1)    
                            except NoSuchElementException:
                                Draps_list.append(0)
                                
                                
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Chambre et salle de bain")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Porte de la chambre avec verrou")]')
                             
                            except InvalidSelectorException:
                                Porte_de_la_chambre_avec_verrou_list.append(1)    
                            except NoSuchElementException:
                                Porte_de_la_chambre_avec_verrou_list.append(0)  
                                
                            
                            ################## Logistique  
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Logistique")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Dépôt de bagages autorisé")]')
                             
                            except InvalidSelectorException:
                                Dépôt_de_bagages_autorisé_list.append(1)    
                            except NoSuchElementException:
                                Dépôt_de_bagages_autorisé_list.append(0)
                                
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Logistique")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Séjours longue durée autorisé")]')
                             
                            except InvalidSelectorException:
                                Séjours_longue_durée_autorisé_list.append(1)    
                            except NoSuchElementException:
                                Séjours_longue_durée_autorisé_list.append(0)
                                    
                              
                                
                            ################### Dispositif de sécurité 
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Dispositif de sécurité")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Détecteur de fumée")]')
                             
                            except InvalidSelectorException:
                                Détecteur_de_fumée_list.append(1)    
                            except NoSuchElementException:
                                Détecteur_de_fumée_list.append(0)
                                
                                
                                
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Dispositif de sécurité")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Détecteur de monoxyde de carbone")]')
                             
                            except InvalidSelectorException:
                                Détecteur_de_monoxyde_de_carbone_list.append(1)    
                            except NoSuchElementException:
                                Détecteur_de_monoxyde_de_carbone_list.append(0)
                                
                            
                            
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Dispositif de sécurité")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Extincteur")]')
                             
                            except InvalidSelectorException:
                                Extincteur_list.append(1)    
                            except NoSuchElementException:
                                Extincteur_list.append(0)
                                
                            
                                
                            try:
                                driver.find_element_by_xpath('//*[@role="dialog"][@aria-label="Équipements"]/div/div/div/section/section/div[@class="_aujnou"]/div/h3[contains(text(), "Dispositif de sécurité")]/following::div[@class="_1dotkqq"]/div[@class="_vzrbjl"]/text()[contains(.,"Kit de premiers secours")]')
                             
                            except InvalidSelectorException:
                                Kit_de_premiers_secours_list.append(1)    
                            except NoSuchElementException:
                                Kit_de_premiers_secours_list.append(0)
                                        
                                
                                
                         
                            lien_list.append(driver.current_url)
                                
               
                try:
                    Base=pd.DataFrame({"Nom": Nom_list,"Description_type": Description_type_list,"Prix_Originel":Prix_Originel_list,"Prix_Reduc":Prix_Reduc_list,
                           "Voyageurs": Voyageurs_list ,"Chambres":Chambres_list,"Lits": Lits_list, "Salles_de_Bain":Salles_de_Bain_list,
                           "Note":Note_list, "Nb_com":Nb_com_list, "Logement_Entier":Logement_Entier_list,"Arrivée_irréprochable":Arrivée_irréprochable_list,
                           "Hôte_expérimenté":Hôte_expérimenté_list,"Excellente_communication":Excellente_communication_list, "Accueil_unique":Accueil_unique_list,
                           "Parfaitement_propre":Parfaitement_propre_list,"Propre et rangé":Propre_et_rangé_list, "Idéalement_situé":Idéalement_situé_list,
                           "Annulation_gratuite_pendant_48_heures":Annulation_gratuite_pendant_48_heures_list,"Annulation_gratuite_longue": Annulation_gratuite_longue_list ,
                           "Arrivée_autonome":Arrivée_autonome1_list,"Superhost_list": Superhost_list, "Wi-Fi":Wifi_list,"WiFi_portable":WiFi_portable_list,
                           "lave_linge":Lave_linge_list," Espace_travail_ordi":Espace_travail_ordi_list, "Equipement_base":Equipement_base_list,
                           "Chauffage":Chauffage_list, "Fer_à_Repasser":Fer_à_Repasser_list, "Télévision":Télévision_list, "Eau_chaude":Eau_chaude_list,
                           "Table_à_langer":Table_à_langer_list, "Chaise_haute":Chaise_haute_list, "Lit_pour_bébé":Lit_pour_bébé_list, 
                           "Livres_et_jouets_pour_enfants":Livres_et_jouets_pour_enfants_list, "Parking_payant":Parking_payant_list, "Parking_gratuit":Parking_gratuit_list,
                           "Chargeur_EV":Chargeur_EV_list, "Salle_de_sport":Salle_de_sport_list, "Jacuzzi":Jacuzzi_list, "Ascenseur":Ascenseur_list, "Piscine":Piscine_list,
                           "Cuisine":Cuisine_list, "Réfrigérateur":Réfrigérateur_list, "Vaisselle_et_couverts":Vaisselle_et_couverts_list, "Four_à_micro_ondes":Four_à_micro_ondes_list,
                           "Petit_déjeuner":Petit_déjeuner_list, "four":four_list, "Lave_vaisselle":Lave_vaisselle_list, "Cafetière":Cafetière_list, "Cuisinière":Cuisinière_list,
                           "Ustensiles_de_cuisine_de_base":Ustensiles_de_cuisine_de_base_list, "Acceuil_Personnel":Personnel_list,
                           "Entrée_privée":Entrée_privée_list, "Salon_privé":Salon_privé_list, "Boîte_à_clé_sécurisée":Boîte_à_clé_sécurisée_list, 
                           "Clés_remises_par_hôte":Clés_remises_par_hôte_list, "Jardin":Jardin_list, "Sèche_cheveux":Sèche_cheveux_list, "Cintres":Cintres_list, 
                           "Shampooing":Shampooing_list, "Gel_douche":Gel_douche_list, "Oreillers_et_couvertures":Oreillers_et_couvertures_supplémentaires_list,
                           "Draps":Draps_list, "Porte_de_la_chambre_avec_verrou":Porte_de_la_chambre_avec_verrou_list, "Dépôt_de_bagages_autorisé":Dépôt_de_bagages_autorisé_list, 
                           "Séjours_longue_durée_autorisé":Séjours_longue_durée_autorisé_list, "Détecteur_de_fumée":Détecteur_de_fumée_list, 
                           "Détecteur_de_monoxyde_de_carbone":Détecteur_de_monoxyde_de_carbone_list, "Extincteur":Extincteur_list, "Kit_de_premiers_secours":Kit_de_premiers_secours_list,
                           "Fête":Fête_list, "Fumeur":Fumeur_list, "Animaux":Animaux_list,"Bébés":Bébés_list,
                           "Nb_équipement":Nb_équipement_list,"Description":Description_list, "Lien":lien_list})   
                    try:
                        Base_final=Base_final.append(Base)
                    except:
                        pass
                    
                except:
                     pass
            
            except:
                try:
                    continue
                except:
                    return Base_final
            
        driver.get(lien)
            
        try:
            element=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@aria-label="Suivant"]')))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            element.click()
            lien=driver.current_url
        except:
            pass
                
                
        Compteur+=1
        app_urls=[]
        driver.close()
                
    
    
        
    return Base_final

