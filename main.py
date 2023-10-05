import numpy as np

# reading bidimensional array from txt
matrix = np.genfromtxt("matrix.txt", delimiter=',')
print(f"Matriz original:\n{matrix}\n")

# statistical measures from matrix
print(f"Menor elemento de cada linha: {matrix.min(axis=1)}")
print(f"Média dos elementos das mesmas colunas: {matrix.mean(axis=0)}")
print(f"Soma de todos os elementos: {matrix.sum()}\n")

# transposed matrix
transposed_matrix = matrix.T
print(f"Matriz transposta:\n{transposed_matrix}\n")
transposed_and_five = transposed_matrix + 5
print(f"Matriz transposta + 5:\n{transposed_and_five}\n")

# product between matrix and its transposed + 5
print(f"Matriz x (Matriz transposta + 5):\n{matrix @ transposed_and_five}\n")

# filter matrix
filter = (matrix > 0) & (matrix < 20)
print(f"Os elementos positivos da matriz menores que 20 são: {matrix[filter]}\n")

# arithmetic operation on matrix
# identity + (2 * matrix * transposed_matrix)
res = 2 * matrix
res = res @ transposed_matrix
res = np.identity(res.shape[0]) + res
print(f"I + ((2 * Matriz) * Matriz transposta) =\n{res}")
