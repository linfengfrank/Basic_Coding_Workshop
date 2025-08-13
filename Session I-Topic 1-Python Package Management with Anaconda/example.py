import numpy as np

data = np.array([1, 2, 2, 3, 3, 3])
values, counts = np.unique_counts(data)
print(values)   # → array([1, 2, 3])
print(counts)   # → array([1, 2, 3])
