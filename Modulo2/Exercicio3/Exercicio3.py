"""
Faça uma função que recebe duas listas e retorna a soma item a item dessas
listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
retornar [1+3, 4+5, 3+1] = [4, 9, 4].
"""


def soma(l1, l2):
    d = []
    for x, y in enumerate(l1):
        d.append(y + l2[x])
    return d


l1 = [1, 4, 3]
l2 = [3, 5, 1]
print(soma(l1, l2))
