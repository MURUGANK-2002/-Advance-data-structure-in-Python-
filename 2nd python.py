import numpy as np

# 2D Array
print("=== 2D Array Operations ===")
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(array2d)
print("Size of 2D Array:", array2d.size)
print("\nSum of all elements in 2D Array:", np.sum(array2d))
print("Maximum value in 2D Array:", np.max(array2d))
print("Mean of 2D Array:", np.mean(array2d))

scaled_array2d = array2d * 2
print("\n2D Array after multiplying by 2: ")
print(scaled_array2d)

# 3D Array
print("\n=== 3D Array Operations ===")
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("3D Array:")
print(array3d)
print("Size of 3D Array:", array3d.size)
print("\nSum of all elements in 3D Array:", np.sum(array3d))
print("Maximum value in 3D Array:", np.max(array3d))
print("Mean of 3D Array:", np.mean(array3d))
