# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
print('=' * 40)
print('{: ^40}' .format('BANCO CEV'))
print('=' * 40)
valor = int(input('Que valor você quer sacar? '))

cinq = valor // 50
if cinq != 0:
    print(f'Total de {cinq} notas de R$50.')
    valor -= (cinq * 50)
vinte = valor // 20
if vinte != 0:
    print(f'Total de {vinte} notas de R$20.')
    valor -= (vinte * 20)
dez = valor // 10
if dez != 0:
    print(f'Total de {dez} notas de R$10.')
    valor -= (dez * 10)
um = valor // 1
if um != 0:
    print(f'Total de {um} notas de R$1.')
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
