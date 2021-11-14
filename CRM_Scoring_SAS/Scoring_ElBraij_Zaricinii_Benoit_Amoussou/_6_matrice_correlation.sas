

/***corrélation entre variables retenues et avec la variable cible***/
proc corr data = score.Donnees_scoring out = correlation_mat;
var 
don_annee_N
age_18_25_ans 
age_25_35_ans 
age_35_45_ans
age_45_55_ans
age_55_65_ans 
age_65_75_ans
age_Moins_de_18_ans
age_Plus_75_ans  
nb_don_annee_N_moins_10
nb_don_annee_N_moins_09
nb_don_annee_N_moins_08
nb_don_annee_N_moins_07
nb_don_annee_N_moins_06
nb_don_annee_N_moins_05
nb_don_annee_N_moins_04
nb_don_annee_N_moins_03
nb_don_annee_N_moins_02
nb_don_annee_N_moins_01
nb_don_total 
NB_don_par_Telephone
NB_don_par__INTERNET
NB_don_par_Autre_Canal
NB_paiement_CB
NB_paiement_CHEQUE
NB_paiement_AUTRE
origine_Autre
origine_BDD 
origine_B_n_vole
origine_Web
origine_Web_actif
abonnement_Nl_g  
abonnement_Nl_s
pas_dabonnement
top_telephone_renseigne
top_portable_renseigne
top_membre
top_adresse_email_FAI
top_email_avec_nom
top_email_avec_prenom
Civilite_Madame
Civilite_Mademoiselle
Civilite_Monsieur
Civilite_Soci_te 
pct_annee_avec_don  
recence
Montant_Don_N_moins_10
Montant_Don_N_moins_09
Montant_Don_N_moins_08
Montant_Don_N_moins_07
Montant_Don_N_moins_06
Montant_Don_N_moins_05
Montant_Don_N_moins_04
Montant_Don_N_moins_03
Montant_Don_N_moins_02
Montant_Don_N_moins_01
max_mnt   
mean_mnt     
montant_don_total;
run;

PROC EXPORT DATA=correlation_mat
OUTFILE= "correlation_mat.xlsx"             
            DBMS=XLSX REPLACE;
RUN;
