from menu import AVAILABLE_MENU

# print(AVAILABLE_MENU)

def get_item(item_id: int):
    for produto in AVAILABLE_MENU:
        if produto['id'] == item_id:
            return produto

def add_item_to_tab(table_tab, item_id, amount):
    produto = get_item(item_id)
    if produto == None:
        return False
    else:
        produto['amount'] = amount
        table_tab.append(produto)
        print(table_tab)
        return True

add_item_to_tab([ {"id": 34, "name": "FRENCH TOAST", "price": 5.0}], 1, 2)

def calculate_tab(table_tab):
    valor_total = 0
    for produto in table_tab:
        valor_total+= produto['price']*produto['amount']
    return valor_total
    
calculate_tab([{'id': 1, 'name': 'ADICIONAL FRANGO 50G', 'price': 4.0, 'amount': 3},
 {"id": 34, "name": "FRENCH TOAST", "price": 5.0, 'amount': 2},
  {"id": 32, "name": "COOKIE", "price": 5.0, 'amount': 1}
])