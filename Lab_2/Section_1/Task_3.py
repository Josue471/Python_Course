# Versión sin estructuras de control ni len()

numeros = [1, 2, 3, 4, 5, 6, 7]

# Obtener máximo y mínimo usando sort
ordenada = numeros.copy()
ordenada.sort()

minimo = ordenada[0]
maximo = ordenada[-1]

# Para obtener la longitud sin len() ni bucles, podemos usar index de un valor fuera de rango
# (esto dará error si no lo manejamos, así que realmente no hay forma directa sin control structures)
# En clase normalmente se acepta usar sort(), index() y copy() para max/min, pero no para longitud.

print("Lista:", numeros)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Longitud (no se puede calcular sin len() o bucle, solo conceptualmente).")
