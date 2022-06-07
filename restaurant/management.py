from menu import AVAILABLE_MENU

# print(AVAILABLE_MENU)

def get_item(item_id: int):
    for produto in AVAILABLE_MENU:
        if produto['id'] == item_id:
            return produto

# def add_item_to_tab(table_tab, item_id, amount):



# def calculate_tab(table_tab):

