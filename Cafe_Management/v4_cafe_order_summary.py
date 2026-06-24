# Cafe Order Management - Full System

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

total = 0
ordered_items = []

while True:
    order = input("\nEnter Your Item: ").lower()

    if order in menu:
        qty = int(input("How much Quantity do you required: "))
        ordered_items.append({"item": order, "qty": qty, "price": menu[order] * qty})
        total += menu[order] * qty
    else:
        print("Sorry, Item Not Available!")

    choice = input("Do You Want anything else (Yes/No): ").lower()
    if choice != "yes":
        break

print("\n--- Order Summary ---")
print("Items Ordered:")
for entry in ordered_items:
    print(f"  - {entry['item'].title()} x{entry['qty']}  ₹{entry['price']}")

print(f"\nTotal: ₹{total}")
print("Thank You, Visit Again 😍")