libname score "";

/*exclure identifiant_personne avant de  faire les statistiques descriptives*/
data Donnees_score;
set score.Donnees_score(drop=identifiant_personne);
run;
/* les statistiques descriptives sur les variables numeriques*/
proc means data=Donnees_score N  MIN Q1 mean MEDIAN Q3 MAX STD SKEWNESS KURTOSIS;
run;
/* Calcul de la frequence sur les variables catégorielles*/
proc freq data=Donnees_score;
tables Civilite age origine abonnement;
run;
/*voir les observation de NB_paiement_AUTRE et de top_membre differents de 0 pour voir si les variables
avec peu d'observation ont l'interêt de garder dans l'analyse et qu'ils influencent sur la cible*/
proc sql;
create table try as select *
from Donnees_score
where NB_paiement_AUTRE not = 0;
quit; 
proc sql;
create table try2 as select *
from Donnees_score
where top_membre not = 0;
quit; 
/*Statistiques descriptives de la variables cible ou ces 2 variables retenus précedémént sont differents  de 0*/
proc means data=try N  MIN Q1 mean MEDIAN Q3 MAX STD SKEWNESS KURTOSIS;
var nb_don_annee_N;
run;
proc means data=try2 N  MIN Q1 mean MEDIAN Q3 MAX STD SKEWNESS KURTOSIS;
var nb_don_annee_N;
run;
proc freq data=try;
tables nb_don_annee_N ;
run;

proc freq data=try2;
tables nb_don_annee_N ;
run;
/*observer la variable tranche d'age 65 75 pour voir si les valeurs de tranche >1 sont des sociétés*/
proc sql;
create table tr_age as select * from Donnees_score where TR_age_65_75_ans not = 0;
quit;
proc freq data=tr_age;
tables civilite;
run;
