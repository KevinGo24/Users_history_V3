from Show_Inventory import show_inventory

def search(inventory):
    if not inventory:
        print('The inventory is empty!')
        return

    search_name = input("Enter the name of the product to search: ").strip().lower()
    found_products = [product for product in inventory if product['name'].lower() == search_name]

    if found_products:
        print(f"\nFound {len(found_products)} product(s) matching '{search_name}':")
        for product in found_products:
            print(f"Product: {product['name']}")
            print(f"Price: ${product['price']}")
            print(f"Quantity: {product['quantity']}")
            print("=" * 30)
    else:
        print(f"No products found with the name '{search_name}'.")