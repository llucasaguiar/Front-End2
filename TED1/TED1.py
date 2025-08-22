# input gênero e altura de 15 pessoas
# informar a maior e menor altura no grupo
# a média da altura do gênero masculino
# o número do gênero feminino

import time

bd_pessoas = []

def cadastrar_pessoas(bd, genero, altura):
    pessoas = [genero, altura]
    bd.append(pessoas)
    return bd

def lista_pessoas(bd):
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

while True:
    print('1 - Cadastrar pessoa')
    print('2 - Listar pessoas')
    print('3 - Informar a menor e maior altura da pessoas')
    print('4 - Informar a média da altura do gênero masculino')
    print('5 - Informar o número de pessoas do gênero feminino')
    op = int(input('Digite sua opção: '))

    if op == 1:
        genero = input('Digite o gênero da pessoa (masculino ou feminino): ')
        altura = int(input('Digite a altura da pessoa em centímetros (cm): '))
        bd_pessoas = cadastrar_pessoas(
            bd=bd_pessoas,
            genero=genero,
            altura=altura
        )
        print('Pessoa cadastrada!')

    elif op == 2:
        lista_pessoas(bd_pessoas)
        print('Pessoas listadas!')

    elif op == 3:
        menor_alt = min(bd_pessoas)
        maior_alt = max(bd_pessoas)
        print(f'A menor e maior alturas são de {menor_alt} e {maior_alt} cm, respectivamente.')

    elif op == 4:
        
        

    else:
        print(f'Opção {op} invalida!')



    time.sleep(2)