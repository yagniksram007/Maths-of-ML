import numpy as np

# Generate a sample user-item matrix (replace this with your actual data)
user_item_matrix = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 0, 4],
    [0, 1, 5, 4],
])

# Perform SVD
U, sigma, Vt = np.linalg.svd(user_item_matrix, full_matrices=False)

# Set the desired number of latent factors (adjust as needed)
k = 2

# Reduce dimensionality by retaining the top-k singular values and corresponding vectors
U_k = U[:, :k]
sigma_k = np.diag(sigma[:k])
Vt_k = Vt[:k, :]

# Reconstruct the user-item matrix using the reduced matrices
user_item_matrix_reconstructed = np.dot(np.dot(U_k, sigma_k), Vt_k)

# Print the original and reconstructed matrices
print("Original User-Item Matrix:")
print(user_item_matrix)
print("\nReconstructed User-Item Matrix:")
print(user_item_matrix_reconstructed)

