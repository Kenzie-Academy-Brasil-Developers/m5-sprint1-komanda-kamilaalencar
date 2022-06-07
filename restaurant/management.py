from restaurant.menu import AVAILABLE_MENU

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
        return True

def calculate_tab(table_tab):
    valor_total = 0
    for produto in table_tab:
        valor_total+= produto['price']*produto['amount']
    return valor_total
