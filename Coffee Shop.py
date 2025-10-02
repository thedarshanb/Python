# Coffee Shop Mini Project using Python

menu = {
    "1": {"name": "Espresso", "price": 2.00},
    "2": {"name": "Cappuccino", "price": 3.00},
    "3": {"name": "Latte", "price": 3.50},
    "4": {"name": "Mocha", "price": 4.00},
    "5": {"name": "Flat White", "price": 4.50}
}

print("Welcome to the Coffee Shop!")
for key, item in menu.items():
    print(f"{key}. {item['name']} - ${item['price']:.2f}")

while True:
    choice = input("Please enter the number of your choice: ")

    if choice in menu:
        print(f"You have chosen {menu[choice]['name']}.")
        print(f"Total: ${menu[choice]['price']:.2f}")
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for your order!")