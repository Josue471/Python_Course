#Numeros
nums = [5, 2, 9, 1, 5, 6]
resultado = nums.sort()
print(nums)       # list modificada: [1, 2, 5, 5, 6, 9]
print(resultado)  # None

#------------------------------------------------------------------------------------------
#Orden inverso
nums = [5, 2, 9, 1]
nums.sort(reverse=True)
print(nums)  # [9, 5, 2, 1]

#------------------------------------------------------------------------------------------

#Strings (alfabético — cuidado con mayúsculas/minúsculas)
words = ["banana", "Apple", "cherry"]
words.sort()
print(words)  # Por defecto: ['Apple', 'banana', 'cherry']  (mayúsculas antes que minúsculas)

#------------------------------------------------------------------------------------------

#Ordenar por longitud
words = ["a", "abcd", "abc", "ab"]
words.sort(key=len)
print(words)  # ['a', 'ab', 'abc', 'abcd']

#------------------------------------------------------------------------------------------

#Listas de tuplas: ordenar por el segundo elemento
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
pairs.sort(key=lambda x: x[1])  # ordenar por x[1]
print(pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]

#------------------------------------------------------------------------------------------

#Lista de diccionarios: ordenar por una clave del dict
students = [
    {"name": "Ana", "grade": 88},
    {"name": "Luis", "grade": 95},
    {"name": "Juan", "grade": 78},
]
students.sort(key=lambda s: s["grade"])  # por calificación ascendente
print(students)
# [{'name': 'Juan', 'grade': 78}, {'name': 'Ana', 'grade': 88}, {'name': 'Luis', 'grade': 95}]

#------------------------------------------------------------------------------------------

#Orden estable: ejemplo práctico

data = [
    ("A", 2),
    ("B", 1),
    ("A", 1),
    ("B", 2),
]
# Primero ordenamos por la segunda clave (asc)
data.sort(key=lambda x: x[1])
# Luego ordenamos por la primera clave (asc)
data.sort(key=lambda x: x[0])
print(data)
# Resultado: [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
# La estabilidad asegura que para la misma primera clave, el orden por la segunda se mantuvo.

#------------------------------------------------------------------------------------------

#Cuando necesitas un comparador estilo cmp (Python 3 no tiene cmp directo)

from functools import cmp_to_key

def comparador(a, b):
    # ejemplo: ordenar por resto al dividir entre 10, y si igual, por valor numérico
    ra, rb = a % 10, b % 10
    if ra < rb: return -1
    if ra > rb: return 1
    return a - b

nums = [21, 32, 43, 14, 25]
nums.sort(key=cmp_to_key(comparador))
print(nums)  # ordenado por a%10, luego por valor si hay empate