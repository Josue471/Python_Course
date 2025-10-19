# Crear una variable tipo string
a = "123"

# Conversión a entero
i = int(a)
print("Entero:", i)

# Conversión a flotante
f = float(a)
print("Flotante:", f)

# Conversión a booleano
b = bool(a)  # En Python, cualquier string no vacío es True
print("Booleano:", b)

# Conversión a lista
l = list(a)  # Convierte cada carácter del string en un elemento de la lista
print("Lista:", l)

# Conversión a tupla
t = tuple(a)  # Igual que list(), pero crea una tupla en lugar de lista
print("Tupla:", t)
