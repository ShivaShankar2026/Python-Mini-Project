# Basic Cafe Order - Single Item

menu = {
    "pizza": 49,
    "salad": 35,
    "burger": 100,
    "pop corn": 150,
    "sandwich": 60
}

print("Welcome To Our Cafe\n")
for item, price in menu.items():
    print(f"{item.title()} : {price}")

order = input("\nEnter Your Item: ").lower()

if order in menu:
    print(f"\nYour Bill Amount: {menu[order]}")
    print("\nThank You, Visit Again 😍")
else:
    print("Sorry, Item Not Available!")