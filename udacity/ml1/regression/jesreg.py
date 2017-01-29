def studentReg(ages_train, net_worths_train):
   from sklearn import linear_model
   reg = linear_model.LinearRegression()
   reg.fit (ages_train, net_worths_train)

   print "my networth prediction", reg.predict([29])  # $173K
   print "slope:", reg.coef_ # 6.47
   print "intercept:", reg.intercept_ # -14.35
   return reg




