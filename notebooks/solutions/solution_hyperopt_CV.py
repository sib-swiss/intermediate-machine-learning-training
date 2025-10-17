## tentative solution
def hyperopt_xgb_train_CV5( params ):
    
    skf = StratifiedKFold(n_splits=5 , shuffle=True , random_state = 2024 )
    
    losses = -1 * cross_val_score( xgb.XGBClassifier(n_jobs=multiprocessing.cpu_count()-2 , **params) , 
                eye_features, labels, scoring = 'roc_auc_ovr' , cv = skf )
        
    return_dict = {'loss': np.mean(losses),
                   'loss_variance' : np.var(losses),
                   'status': STATUS_OK
                   }
    return return_dict
