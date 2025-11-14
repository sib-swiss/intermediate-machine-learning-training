## tentative correction ## ~30s to run on my computer

best_scores = []
num_rounds = []
sub_list = []
eta = 0.1
subsamples = np.arange(0.1,1.01,0.05)

for subsample in subsamples:
    for r in range(10):
        xgb_model = xgb.XGBClassifier(
            n_jobs=multiprocessing.cpu_count()-2,
            early_stopping_rounds=10 ,
            eta = eta, 
            subsample = subsample,
            eval_metric= 'auc',
            random_state = np.random.randint(1,100_000)) ## necessary to have randomness between reps

        xgb_model.fit(X_train , y_train  , 
                      eval_set=[(X_train, y_train),(X_valid, y_valid)],
                      verbose=False )

        best_scores.append( xgb_model.best_score )
        num_rounds.append( xgb_model.best_iteration )
        sub_list.append( subsample )


fig,ax=plt.subplots(1,2,figsize = (10,5))
ax[0].scatter( sub_list , best_scores , s = 3)
sns.lineplot( x=sub_list , y = best_scores , ax=ax[0])
ax[0].set_xlabel('subsample')
ax[0].set_ylabel('score')
ax[0].grid()

ax[1].scatter( sub_list , num_rounds , s = 3 )
sns.lineplot( x=sub_list , y = num_rounds , ax=ax[1])
ax[1].set_xlabel('subsample')
ax[1].set_ylabel('number of rounds')
ax[1].grid()