
/*centrer réduire les variables*/
/* supression des variables fortement corrélées dans la matrice de corrélation**/
/**suppression des variables dichotomisées encore présentes parmi les variables retenues pour éviter les coréélations avec la constante***/

proc standard data= score.Donnees_scoring(drop=montant_don_total civilite_madame 
origine_B_n_vole origine_Web NB_don_par_Telephone NB_paiement_CB nb_don_total 
age_Moins_de_18_ans pas_dabonnement top_email_avec_nom top_email_avec_prenom)
out=score.scoring_final
mean=0 std=1 print;
var 
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
mean_mnt;  
run;
