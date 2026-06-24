"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    lista = {}
    for item in items:
        if item in lista:
            lista[item] +=1
        else:
            lista[item] = 1
    return lista

print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    for item in items:
        if item in inventory:
            inventory[item] +=1
        else:
            inventory[item] = 1
    return inventory
            
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    for item_remover in items:
        if item_remover in inventory and inventory[item_remover] > 0:
            inventory[item_remover] -=1
    return inventory

print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))
print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))
    

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory
    
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    lista = []

    for item, quantidade in inventory.items():
        if quantidade > 0:
            tupla = (item, quantidade)
            lista.append(tupla)
    return lista
            
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))