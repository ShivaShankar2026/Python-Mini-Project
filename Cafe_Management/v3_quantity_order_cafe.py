menu = {
    "pizza": 49,
    "salad": 35,
    "burger": 100,
    "pop corn": 150,
    "sandwich": 60
}

print("Welcome To Our Cafe\n")

for item, price in menu.items():
    print(f"{item.title()} : ₹{price}")

total = 0

while True:
    order = input("\nEnter Your Item: ").lower()

    if order in menu:
        qty = int(input("Enter Quantity: "))

        item_total = menu[order] * qty
        total += item_total

        print(f"Added {qty} {order.title()}(s)")
        print(f"Item Total: ₹{item_total}")
        print(f"Current Bill: ₹{total}")

    else:
        print("Sorry, Item Not Available!")

    another = input("\nDo you want to order another item? (yes/no): ").lower()

    if another != "yes":
        break

print("\n===== BILL =====")
print(f"Total Bill: ₹{total}")
print("Thank You, Visit Again 😍")