
def add(inventory):
    Add = 'yes'
    while Add == 'yes':
        # Request the data
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        # Create the dictionary and save it in the list
        product = {"name": name, "price": price, "quantity": quantity}
        inventory.append(product)

        print(f"{name} added successfully!")

        # Ask if they want to continue adding in this same session
        Add = input("Do you want to add another product? (yes/no): ").lower()
