import math

entropy = -(0.6667) * math.log(0.6667, 2) - 0.333*math.log(0.333, 2) # log base 2
print entropy

# -pslow * log2 of pslow - pfast * log2 of pfast
# 1.0

# info gain = entropy(parent) - weighted avg * entropy(children)
# 0.688 weighted avg (3/4) * the entropy of children
# info gain is .3112

# gini index is similar to entropy calculation but a little different
# in sklearn you can use criterion entropy but you have to calculate import

# a biased classifier can't learn
# a high variance algorithm learns too much from training
# need something in the middle that can generalize a bit