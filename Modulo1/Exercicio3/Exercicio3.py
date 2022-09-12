"""
Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:

a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados.
"""

print('Questionário Policial')
resp = input('Mora perto da vítima? S/N ')
cont = 0
if resp.upper() == 'S':
    cont += 1
resp = input('Já trabalhou com a vítima? S/N ')
if resp.upper() == 'S':
    cont += 1
resp = input('Telefonou para a vítima? S/N ')
if resp.upper() == 'S':
    cont += 1
resp = input('Esteve no local do crime? S/N ')
if resp.upper() == 'S':
    cont += 1
resp = input('Devia para a vítima? S/N ')
if resp.upper() == 'S':
    cont += 1

if cont == 5:
    print('Assassino')
elif (cont >= 3) and (cont < 5):
    print('Cúmplices')
elif cont == 2:
    print('Suspeito')
else:
    print('Inocente')

