# Cafe Management

menu = {
    'pizza': 49,
    'salad': 35,
    'burger': 100,
    'popcorn': 150,
    'sandwich': 60
}

print("Welcome To Our Cafe")
print("Menu")
print('Pizza:49\nSalqad:35\nBurger:100\nPop Corn:150\nSandwich:60')
menu = {'pizza' : 49,'salad' : 35, 'burger' : 100, 'popcorn' : 150 , 'sandwich' : 60}

#for item, price in menu.items():
    #print(f"{item.title()}: {price}")

order_total = 0

while True:
    order_item = input("Enter Your Item (or type 'done' to finish): ").lower()
    
    if order_item == 'done':
        break
    
    if order_item in menu:
        order_total += menu[order_item]
        print(f"Added {order_item.title()}")
        print(f"Added {order_item.title()} → Current Total: {order_total}")
    else:
        print("❌ Wrong item entered, please try again.")

print(f"✅ Your Total order value is {order_total}")
