from Add_product import add

expensive_items = 0
max_price = 0
highest_position = 0  # Show the user the highest-priced product


def buscarmaximo(inventory):
    max_price = inventory[0]
    highest_position = inventory[0]
    for inv in inventory:
        if inv['price'] > max_price['price']:
            max_price = inv
        if inv['quantity'] > highest_position['quantity']:
            highest_position = inv

    print(f" El producto mayor es:{max_price['name']} y su cantidad es: {highest_position['quantity']} y su precio es : {max_price['price']}")
