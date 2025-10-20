# Lista de animales
animals = [
    "Ferret", "boar", "jaguar", "giraffe", "lizard", "locust", "lion", "wolf",
    "parrot", "raccoon", "butterfly", "jellyfish", "fly", "gnat", "bat", "otter",
    "bear", "polar bear", "oyster", "sheep", "bee", "eagle", "antelope", "spider",
    "squirrel", "tuna", "ostrich", "wasp", "whale", "bison", "buffalo", "owl",
    "donkey", "horse", "goat", "squid", "chameleon", "camel", "crab", "kangaroo",
    "cat", "dog"
]

# Crear diccionarios filtrados según la letra
dict_a = {animal: animal for animal in animals if "a" in animal.lower()}
dict_b = {animal: animal for animal in animals if "b" in animal.lower()}
dict_y = {animal: animal for animal in animals if "y" in animal.lower()}

# Mostrar resultados
print("Palabras con 'a':")
print(dict_a)
print("\nPalabras con 'b':")
print(dict_b)
print("\nPalabras con 'y':")
print(dict_y)
