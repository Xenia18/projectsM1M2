
/*creation des indicateurs*/
data etape1;
set score.Donnees_score;
montant_don_total= sum(of Montant_Don_N_moins_11--Montant_Don_N_moins_01);
nb_don_total= sum(of nb_don_annee_N_moins_11--nb_don_annee_N_moins_01);
*création de la variable recence;
if nb_don_annee_N_moins_11>0 then recence = 11;
if nb_don_annee_N_moins_10>0 then recence = 10;
if nb_don_annee_N_moins_09>0 then recence = 9;
if nb_don_annee_N_moins_08>0 then recence = 8;
if nb_don_annee_N_moins_07>0 then recence = 7;
if nb_don_annee_N_moins_06>0 then recence = 6;
if nb_don_annee_N_moins_05>0 then recence = 5;
if nb_don_annee_N_moins_04>0 then recence = 4;
if nb_don_annee_N_moins_03>0 then recence = 3;
if nb_don_annee_N_moins_02>0 then recence = 2;
if nb_don_annee_N_moins_01>0 then recence = 1;
run;


%let liste_var=Montant_Don_N_moins_01, Montant_Don_N_moins_02,Montant_Don_N_moins_03, Montant_Don_N_moins_04,
Montant_Don_N_moins_05, Montant_Don_N_moins_06,Montant_Don_N_moins_07, Montant_Don_N_moins_08,
Montant_Don_N_moins_09, Montant_Don_N_moins_10,Montant_Don_N_moins_11;

proc sql;
create table etape2 as select
*,

max(&liste_var) as max_mnt,
min(&liste_var) as min_mnt,
montant_don_total/11 as mean_mnt,
sum(Montant_Don_N_moins_01>0,Montant_Don_N_moins_02>0,Montant_Don_N_moins_03>0, Montant_Don_N_moins_04>0,
Montant_Don_N_moins_05>0, Montant_Don_N_moins_06>0,Montant_Don_N_moins_07>0, Montant_Don_N_moins_08>0,
Montant_Don_N_moins_09>0, Montant_Don_N_moins_10>0,Montant_Don_N_moins_11>0)/11*100 as pct_annee_avec_don

from etape1;
quit;
