
# Normalize some features to be between 0 and 1

def featureScaling(arr):
	maxi = max(data)
	mini = min(data)
	normalized = []
	for point in data:
		normalpoint = float(point - mini) / float(maxi -mini)
		normalized.append(normalpoint)
	return normalized


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)



# Rescale with sklearn - good for SVM with RBF and for KMeans
# weights is a numpy array and needs to be float
# type in python interpreter ctrl D to esc
import numpy
from sklearn.preprocessing import MinMaxScaler
weights = ([[115.], [140.], [175.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
rescaled_weight

# output:
array([[ 0.        ],
       [ 0.41666667],
       [ 1.        ]])
