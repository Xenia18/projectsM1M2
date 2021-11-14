/*Calcul de la variable cible et suppression des variables non nécessaires*/
data score.Donnees_scoring (rename=(abonnement_Newsletter_g_n_rale=abonnement_Nl_g abonnement_Newsletter_sp_cifique=abonnement_Nl_s abonnement_Pas_d_abonnement=pas_dabonnement));
set score.DonneesDumifiees(drop=age_Non_renseign_ Civilite_Non_renseign_ abonnement civilite age origine
identifiant_personne nb_don_annee_N_moins_11 TR_age_65_75_ans Montant_Don_N Montant_Don_N_moins_11 nb_don_annee_N min_mtt);
if nb_don_annee_N >= 1 then don_annee_N=1;
else don_annee_N=0;
run;
/*observer la répartition de la variable cible*/
proc freq data=Donnees_scoring;
tables don_annee_N;
run;
