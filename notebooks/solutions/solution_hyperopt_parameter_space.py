
space4xgb = {
    'n_estimators': pyll.scope.int(hp.quniform('n_estimators', 1 , 1000,1)),
    'eta': hp.loguniform('eta' , np.log(10**-4) , np.log(10**2) ),
    'max_depth': pyll.scope.int(hp.quniform('max_depth', 1, 16, 1)),
    'subsample': hp.uniform('subsample', 0.3, 1)
}
