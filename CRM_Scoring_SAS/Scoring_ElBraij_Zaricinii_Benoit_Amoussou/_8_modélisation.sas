
/******************Modélisation********************/

/*Echantillonnage train_test*/

data score.ech_train score.ech_test;
set score.scoring_final;
if ranuni(10)>0.3 then output score.ech_train;
else output score.ech_test;
run;

/***vérification du taux de cible dans les deux echantillon***/
proc freq data=score.ech_train;table don_annee_N;run;
proc freq data=score.ech_test;table don_annee_N;run;

*liste des variables retenues pour la modélisation;
%let listvar=Civilite_Mademoiselle Civilite_Monsieur Civilite_Soci_te Montant_Don_N_moins_01 Montant_Don_N_moins_02 
Montant_Don_N_moins_03 Montant_Don_N_moins_04 Montant_Don_N_moins_05 Montant_Don_N_moins_06 Montant_Don_N_moins_07 Montant_Don_N_moins_08 Montant_Don_N_moins_09  
Montant_Don_N_moins_10 NB_don_par_Autre_Canal NB_don_par__INTERNET NB_paiement_AUTRE NB_paiement_CHEQUE abonnement_Nl_g abonnement_Nl_s age_18_25_ans age_25_35_ans 
age_35_45_ans age_45_55_ans age_55_65_ans age_65_75_ans age_Plus_75_ans max_mnt mean_mnt  nb_don_annee_N_moins_01 nb_don_annee_N_moins_02 nb_don_annee_N_moins_03   
nb_don_annee_N_moins_04 nb_don_annee_N_moins_05 nb_don_annee_N_moins_06 nb_don_annee_N_moins_07 nb_don_annee_N_moins_08 nb_don_annee_N_moins_09 nb_don_annee_N_moins_10  
origine_Autre origine_BDD origine_Web_actif pct_annee_avec_don  top_adresse_email_FAI top_membre top_portable_renseigne top_telephone_renseigne;

*Modèle de régression logistique;
proc logistic data=score.ech_train outest = coef_cible descending ;
model don_annee_N =&listvar
/ selection=stepwise;
output out=result_train xbeta=xb predicted=prev ;
run;

*Transposer la table coef_cible;
proc transpose data=coef_cible
out=table_coef_cible (keep=_NAME_ don_annee_N where=(coef ne .)
rename=(_NAME_=variable don_annee_N=coef));
run;

*Exporet en excel;
PROC EXPORT DATA=table_coef_cible
OUTFILE= "table_coef_cible.xlsx"             
            DBMS=XLSX REPLACE;
RUN;

*Appliquer le modèle sur l'échantillon test;
proc score data=score.ech_test(rename=(don_annee_N=cible_avant))                                                                                                                                                                                                               
    score=coef_cible 	out=result_test	type='PARMS';                                                                                                                                                                                                                                               
	var &listvar;                                                                                                                                                                                                                                                   
run; 

/*Cibler notre echantillon en 10 deciles par la note.*/
proc rank data=result_train(keep=xb prev don_annee_N) out=rang groups=10;
ranks rang;
var xb;
run;
/*proc sort sur les données par le rang et par la variable xb*/
proc sort data=rang;
by rang xb;
run;
/*Construire une table d'analyse sur l'échantillon train pour évaluer le modèle*/
data analyse_model;
set rang;
by rang;
retain eff_target eff seuil_min seuil_max 0;/*eff_target est l'éffectif de la variable cible par tranche*/
/*eff est l'effectif total par tranche; seuil_min est le minimum par tranche de xb; 
seuil_max est le maximum par tranche de xb*/
if first.rang then seuil_min=xb;
eff=eff+1;
if don_annee_N=1 then eff_target+1;
if last.rang then do;
	seuil_max=xb;
	taux_target=(eff_target*100)/eff;
	output;
	eff_target=0;
	eff=0; 
	seuil_min=0;
	seuil_max=0;
	keep rang eff eff_target seuil_min seuil_max taux_target;
end;
run;
/*Ajout des nouvelles variables*/
data analyse_model2;
set analyse_model;
/*Calcul des variables probabilité minimale te probabilité maximale*/
proba_min=exp(seuil_min)/(1+exp(seuil_min));
proba_max=exp(seuil_max)/(1+exp(seuil_max));
run;

proc rank data=result_test(keep=cible_avant don_annee_N) out=rang2 groups=10;
ranks rang2;
var don_annee_N;
run;
/*proc sort sur les données par le rang2 et par la variable don_annee_N*/
proc sort data=rang2;
by rang2 don_annee_N;
run;
/*Construire une table d'analyse sur l'échantillon train pour évaluer le modèle*/
data analyse_model_test;
set rang2;
by rang2;
retain eff_target_test eff_test 0;/*eff_target est l'éffectif de la variable cible par tranche*/
/*eff est l'effectif total par tranche;*/
eff_test=eff_test+1;
if cible_avant=1 then eff_target_test+1;
if last.rang2 then do;
	taux_target_test=(eff_target_test*100)/eff_test;
	output;
	eff_target_test=0;
	eff_test=0; 
	keep rang2 eff_test eff_target_test  taux_target_test;
end;
run;
/*Jointure des tables d'analyse*/
proc sql;
create table analyse as select t1.rang,t1.eff,t2.eff_test, t1.eff_target,t2.eff_target_test, t1.seuil_min, t1.seuil_max,t1.proba_min, t1.proba_max, t1.taux_target,  t2.taux_target_test
from  analyse_model2  t1 full join analyse_model_test  t2 on t1.rang=t2.rang2;
quit;

/**Export de la table vers excel**/
/*
PROC EXPORT DATA=analyse
OUTFILE= "analyse.xlsx"             
            DBMS=XLSX REPLACE;
RUN;
*/
