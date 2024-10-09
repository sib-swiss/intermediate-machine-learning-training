## tentative correction

best_scores = []
num_rounds = []
eta = 0.1
subsamples = np.arange(0.1,1.01,0.05)
for subsample in subsamples:
    xgb_model = xgb.XGBClassifier(
        n_jobs=multiprocessing.cpu_count()-2,
        early_stopping_rounds=10 ,
        eta = eta, 
        subsample = subsample,
        eval_metric= 'auc' )

    xgb_model.fit(X_train , y_train  , 
                  eval_set=[(X_train, y_train),(X_valid, y_valid)],
                  verbose=False )

    best_scores.append( xgb_model.best_score )
    num_rounds.append( xgb_model.best_iteration )

fig,ax=plt.subplots(1,2,figsize = (10,5))
ax[0].plot( subsamples , best_scores )
ax[0].set_xlabel('subsample')
ax[0].set_ylabel('score')
ax[0].grid()

ax[1].plot( subsamples , num_rounds )
ax[1].set_xlabel('subsample')
ax[1].set_ylabel('number of rounds')
ax[1].grid()
