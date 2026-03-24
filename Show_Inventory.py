from Add_product import add
def show(inventory):

    if not inventory:
        print('The inventory is empty!')
    else:
        print("\n" + "="*30)
        print("CURRENT INVENTORY")
        print("="*30)

# Iterate through the list of products

    for product in inventory:
        print(f"Product: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"quantity: {product['quantity']}")
        print("=" * 30)