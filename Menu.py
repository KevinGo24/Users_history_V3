Inventory = []
system = 'Yes'
#-------- Imports
from Add_product import add
from Show_Inventory import show
from search_inventory import search
from Uptade_inventory import uptade
from Archive import *
from inventory_statistics import buscarmaximo
from Delete_inventory import delete
#-------- 
def menu():
    global system
    while system == 'Yes':
        print('='*72)
        print('='*10, "Welcome to our FantasyGo user system", '='*10)
        print('='*72)
        print("1. Add Product")
        print("2. Show Inventory")
        print("3. Look for Inventory")
        print("4. Update Invenotry")
        print("5. Delete Inventory")
        print("6. inventory statistics")
        print("7. save cssv")
        print("8. upload csv")
        print("9. Exit")
        print('='*72)
        Users = int(input('Which option do you want to choose: '))
        if Users == 1:
            # Aquí llamas a tu función de agregar
            add(Inventory)
        elif Users == 2:
            show(Inventory)
        elif Users == 3:
            search(Inventory)
        elif Users == 4:
            uptade(Inventory)
        elif Users == 5:
            delete(Inventory)
        elif Users == 6:
            buscarmaximo(Inventory)
        elif Users == 7:
            save_csv(Inventory)
        elif Users == 8:
            load_csv()
        # Esto rompe el ciclo while
        elif Users == 9:
            print("Exit system...")
            system = 'no' 
        else:
            print("Invalid option, please try again.")
    if Users < 1 or Users > 9:
        print("Invalid operation. Please select an option from 1 to 4.")