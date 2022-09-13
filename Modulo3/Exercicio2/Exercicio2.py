"""
Para o segundo exercício, você deve criar um programa que realize uma
cópia do arquivo "alunos.csv". Essa cópia deve ser um arquivo chamado
"alunos_copia.csv".

Novamente, aqui você também não precisa utilizar a biblioteca CSV mas se
usar, seu código pode ser reutilizado na próxima questão sem muitas
modificações.
"""
with open('/home/victor/Documentos/GitHub/LetsCode-Exercicios/Modulo3/Exercicio1/alunos.csv', 'r') as arquivo:
    with open('alunos_copia.csv', 'w') as arquivo_copia:
        for linha in arquivo:
            arquivo_copia.write(linha)