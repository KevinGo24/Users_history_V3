def uptade(inventory):
    if not inventory:
        print('The inventory is empty!')
    else:
        print('Current inventory:')
        for index, product in enumerate(inventory):
            print
            (f"{index + 1}. {product['name']} - Quantity: {product['quantity']} - Price: ${product['price']}")
        
        try:
            product_index = int(input('Enter the number of the product you want to update: ')) - 1
            if 0 <= product_index < len(inventory):
                new_quantity = int(input('Enter the new quantity: '))
                new_price = float(input('Enter the new price: '))
                inventory[product_index]['quantity'] = new_quantity
                inventory[product_index]['price'] = new_price
                print('Product updated successfully!')
            else:
                print('Invalid product number.')
        except ValueError:
            print('Please enter valid numbers for product selection, quantity, and price.')