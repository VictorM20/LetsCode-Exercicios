"""
Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
programa deve imprimir a mensagem “O novo valor é [valor]”.
"""

valor = float(input('Digite um valor R$ '))

new_valor = valor - (valor * 15) / 100
print('O novo valor é R$',new_valor)