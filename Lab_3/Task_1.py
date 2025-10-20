# Definir las dos matrices 4x4
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

# Crear una matriz vacía 4x4 para el resultado (inicializada en ceros)
C = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Multiplicación de matrices (regla del producto punto)
for i in range(4):          # Recorre las filas de A
    for j in range(4):      # Recorre las columnas de B
        for k in range(4):  # Recorre los elementos de la fila/columna
            C[i][j] += A[i][k] * B[k][j]

# Mostrar el resultado
print("Resultado de la multiplicación A x B:")
for fila in C:
    print(fila)
