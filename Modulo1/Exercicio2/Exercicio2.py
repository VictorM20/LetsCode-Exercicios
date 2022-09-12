"""
Faça um programa que leia a validade das informações:

a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação
inválida.
"""

while True:
    idade = int(input('Digite sua idade: '))
    if (idade >= 0) and (idade <= 150):
        print(f'Sua idade é {idade} anos.')
        break
    else:
        print('Digite sua idade entre 0 e 150')

while True:
    salario = float(input('Digite seu Salário: '))
    if salario > 0:
        print('Seu salário é de R$', salario)
        break
    else:
        print('Seu salário deve ser acima de 0')
while True:
    sexo = input('Digite seu sexo: M, F ou O: ')
    sexo = sexo.upper()
    if sexo == 'M':
        print('Seu sexo é Masculino')
        break
    elif sexo == 'F':
        print('Seu sexo é Feminino')
        break
    elif sexo == 'O':
        print('Seu sexo é Outros')
        break
    else:
        print('Sexo inválido!')

