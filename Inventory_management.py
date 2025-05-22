inventory = {
    "1":{"item": "rice","quantity":50,"price":5000},
    "2":{"item": "sugar","quantity":30,"price":3800},
    "3":{"item": "milk","quantity":20,"price":1500},
    "4":{"item": "salt","quantity":15,"price":1000},
    "5":{"item": "beans","quantity":60,"price":3000}
}
def display_inventory():
    print("\nCurrent Inventory:")
    for key,value in inventory.items():
        print(f"ID: {key}, item {value['item']}, Quantity: {value['quantity']}, Price: UGX {value['price']}")

def update_inventory():
    item_id = input("Enter the ID of the item to update:  ")
    if item_id in inventory:
        print("1.Update Quantity")
        print("2.Update Price")
        choice = input("Enter your item choice: ")
        if choice == "1":
            quantity = int(input("Enter the new quantity: "))
            inventory[item_id]["quantity"] = quantity
            print(f"Quantity of {inventory[item_id]['item']} updated to  {quantity} kg")
        elif choice == "2":
            price = int(input("Enter the new price: "))
            inventory[item_id]["price"] = price
            print(f"Price of {inventory[item_id]['item']} updated to UGX {price}")
            
        else:
            print("Invalid item choice")
     
     
    else:
         print("item not found in inventory")
         
def add_item():
    item_id = input("Enter the ID of the new item: ")
    item_name = input("Enter the name of the new item: ")
    quantity = int(input("Enter the quantity of the new item: "))
    price =int(input("Enter the price of the new item: "))
    inventory[item_id]= {"item":item_name ,"quantity": quantity ,"price": price}
    print(f"Item {item_name} added to inventory")
    
             

def remove_item():
    item_id = input("Enter the ID of the item to remove: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Item with ID {item_id} has been removed from inventory")
    else:
        print("Item not found in inventory")
        
while True:
    print("\nInventory Management System ")
    print("1. Display Inventory")
    print("2. Update Inventory")
    print("3. Add Item")
    print("4. Remove Item")
    print("5. Exit")
    
    choice = input("Select option: ")
    
    if choice == "1":
        display_inventory()
    elif choice == "2":
        display_inventory()
        update_inventory()
    elif choice == "3":
        add_item()
    elif choice == "4":
        display_inventory()
        remove_item()
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again!")
        
         
        
            