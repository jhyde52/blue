'''
 Thomas Bayes first provided a simple theorem and an equation that allows new evidence 
 to update belief. Basically we can be more x is an apple if we know that x is red.

In machine learning, naive Bayes classifiers are a family of simple probabilistic 
classifiers based on applying Bayes' theorem with strong (naive) independence assumptions 
between the features.

Naive just means we make some assumptions that might be wrong like that the absence or 
presence of a specific feature in independent of the other features. Like red, fruit,
round, size all independently contribute to something being an apple.

When dealing with continuous data, a typical assumption is that the continuous values 
associated with each class are distributed according to a Gaussian distribution.

The Normal Distribution has:
mean (avg) = median (number in the middle of sorted list) = mode (most frequent number)
symmetry about the center
50 percent of values less than the mean and 50 percent greater than the mean
'''

http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB.partial_fit
>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]) # data features
>>> Y = np.array([1, 1, 1, 2, 2, 2]) # data labels
>>> from sklearn.naive_bayes import GaussianNB
>>> clf = GaussianNB()
>>> clf.fit(X, Y) # fit means train-this actually trains the model here on features, labels
GaussianNB(priors=None) # Prior probabilities of the classes/classification if any.
>>> print(clf.predict([[-0.8, -1]])) # what is the class/label for this new data point?
[1] # pretty good prediction!

>>> clf_pf = GaussianNB() 
>>> clf_pf.partial_fit(X, Y, np.unique(Y)) # partial fit - Just runs on different batches/chunks of the data set - his is especially useful when the whole dataset is too big to fit in memory at once.
GaussianNB(priors=None)
>>> print(clf_pf.predict([[-0.8, -1]])) # another good prediction!

