import numpy as np

test_array = np.asarray([[1, 2], [3, 4]])
print(test_array)
print(test_array.shape)
# test_array.tofile('tmp.dat')
np.save('tmp.npy', test_array)

new_data = np.load('tmp.npy')
print(new_data)
print(new_data.shape)
