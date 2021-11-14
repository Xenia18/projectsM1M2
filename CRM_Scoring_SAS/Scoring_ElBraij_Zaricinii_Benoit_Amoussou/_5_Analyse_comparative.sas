
/*****Analyse comparative
Tableaux croisés avec la variable cible*****/

%let liste_var = 
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
;

%put &liste_var;

%macro croisement_cible(table_in =,table_out = , liste = , nb_var =);
%do i = 1 %to &nb_var ;
%let var = %scan(&liste,&i);

proc freq data = &table_in noprint ;
tables don_annee_N*&var / missing out = freq_&var ;
run ;


proc freq data = &table_in noprint ;
tables &var / missing out = freqt_&var;
run ;

data freq_&var (drop = &var percent) ;
set freq_&var (where = (don_annee_N = 1));
length modalite $50 variable $50. ;
variable = "&var" ;
modalite = &var ;
run ;

data freqt_&var (rename = (count = count_tot ) drop = percent &var);
set freqt_&var ;
length modalite $50 ;
modalite = &var ;
run ;

proc sort data = freq_&var ;by modalite ;run;

proc sort data = freqt_&var ;by modalite ;run;

data fusion_&var ;
merge freq_&var  freqt_&var ;
by modalite ;
run ;

%end ;


data &table_out (drop = don_annee_N);
set 
%do i = 1 %to &nb_var ;
%let var = %scan(&liste,&i);
fusion_&var
%end ;
;
tx_cible = count/count_tot ;
run ;

%mend;

%croisement_cible(table_in=score.Donnees_scoring, table_out=resultat_croisement_cible,liste=&liste_var,nb_var=36);

/**Export de la table vers excel**/
PROC EXPORT DATA=resultat_croisement_cible
OUTFILE= "croisement_cible.xlsx"             
            DBMS=XLSX REPLACE;
RUN;
