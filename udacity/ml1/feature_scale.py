
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

