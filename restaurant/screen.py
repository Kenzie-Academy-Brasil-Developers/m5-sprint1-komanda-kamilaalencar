import os
from restaurant.management import add_item_to_tab, calculate_tab

TABLE_TAB = []

def initial_screen():
    while True:
        print('1. Adicionar item a comanda')
        print('2. Fechar comanda')
        resposta = input('Digite o que deseja fazer: ')
        os.system('clear')
        if resposta == '1':
            add_item_screen()
        elif resposta == '2':
            check_out_screen()
        else:
            print('Digite uma opção válida (1 ou 2)\n')
        break



def add_item_screen():
    while True:
        id_do_item = int(input('Digite o id do item:'))
        quantidade_do_item = int(input('Digite a quantidade desejada:'))
        adicionar_produtos = add_item_to_tab(TABLE_TAB, id_do_item, quantidade_do_item)
        os.system('clear')
        if adicionar_produtos == False:
            print(f'{id_do_item} não é um id de item válido\n')
        else:
            for item in TABLE_TAB:
                nome_do_item = item['name']
            print(f'{quantidade_do_item} {nome_do_item} adicionado(s) a comanda!\n')
            break
    initial_screen()


def check_out_screen():
    while True:
        os.system('clear')
        for indice, produto in enumerate(TABLE_TAB):
            numero_do_item = indice + 1
            quantidade = produto['amount']
            nome = produto['name']
            sub_total = produto['price'] * quantidade
            print(f'Item {numero_do_item} : {quantidade} {nome} - R${sub_total}')
        print('-' * 100)
        print(f'Total: R${calculate_tab(TABLE_TAB)}\n')
        print('Digite F para finalizar o sistema')
        fechamento = input()
        if fechamento.upper() == 'F':
            break



