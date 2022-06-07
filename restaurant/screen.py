import os
from restaurant.management import add_item_to_tab

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
            print('Digite uma opção válida (1 ou 2)')



def add_item_screen():
    while True:
        id_do_item = int(input('Digite o id do item:'))
        quantidade_do_item = int(input('Digite a quantidade desejada:'))
        adicionar_produtos = add_item_to_tab(TABLE_TAB, id_do_item, quantidade_do_item)
        os.system('clear')
        if adicionar_produtos == False:
            print(f'{id_do_item} não é um id de item válido')
        else:
            for item in TABLE_TAB:
                nome_do_item = item['name']
            print(f'{quantidade_do_item} {nome_do_item} adicionado(s) a comanda!')
            print('\n')

            break
        initial_screen()


def check_out_screen():