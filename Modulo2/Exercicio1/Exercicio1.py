"""
Faça um programa que olhe todos os itens de uma lista e diga quantos deles
são pares.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = []

for i in lista:
    if i % 2 == 0:
        lista2.append(i)
print(lista2)
