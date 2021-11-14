
/*one hot encoding des variables cat�gorielles*/
/*data df01; set scoring;*/
/*Madame=0;if Civilite="Madame" then Madame=1;*/
/*Monsieur=0;if Civilite="Monsieur" then Monsieur=1;*/
/*run;*/

/* D�finir une macro pour cr�er les variables 'dummifi�es" */
%macro DummyVars(DSIn,    /* le dataframe en input */
                 VarList, /* le nom des variables � dummifier */
                 DSOut);  /* le dataframe en output */
   
   data AddFakeY / view=AddFakeY;
      set &DSIn;
      _Y = 0;      
   run;
   proc glmselect data=AddFakeY NOPRINT outdesign(addinputvars)=&DSOut(drop=_Y);
      class      &VarList;   
      model _Y = &VarList /  noint selection=none;
   run;
%mend;

%DummyVars(scoring, age Civilite origine abonnement , score.DonneesDumifiees);
