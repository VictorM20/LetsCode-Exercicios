"""
Finalmente chegamos ao último exercício dessa sequência relacionada à
manipulação de arquivos.

Neste exercício você deve criar um novo arquivo chamado
"alunos_media.csv". Esse novo arquivo é uma cópia de "alunos.csv" porém
com uma coluna a mais chamada "Média" que vai abrigar os valores das
médias das provas de cada aluno da lista.

Se você utilizou a biblioteca CSV para realizar os dois primeiros exercícios,
muito será reaproveitado aqui. A biblioteca CSV permite a interpretação de
cada linha como listas, que são fáceis de manipular.
"""

import pandas as pd

table = pd.read_csv('/home/victor/Documentos/GitHub/LetsCode-Exercicios/Modulo3/Exercicio1/alunos.csv')
table['Média'] = (table['Prova_1'] + table['Prova_2'] + table['Prova_3'] + table['Prova_4']) / 4
pd.options.display.float_format = '{:.2f}'.format
print(table)
alunos_media = table.to_csv('alunos_media.csv', index=False)

