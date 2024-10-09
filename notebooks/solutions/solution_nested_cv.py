#proposed solution
def nestedCV( X ,y ):
    
    skf_external = StratifiedKFold( n_splits=5 , shuffle=True )
    
    test_scores = []
    for t,v in skf_external.split(X,y):
        model , cv_score = simpleCV( X[ t,: ] ,y[t] )
        test_scores.append( roc_auc_score( y[v] , model.predict_proba( X[v,:] ) , multi_class='ovr' ) )

    model, cv_score = simpleCV( X ,y )
    
    return model, np.mean( test_scores )
