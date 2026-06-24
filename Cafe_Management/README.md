# ☕ Cafe Ordering System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-orange)

A beginner-friendly Python project that simulates a real-world cafe ordering system. Built step-by-step across multiple versions, each introducing new concepts and features.

---

## 📌 Features

- 📋 Display cafe menu with prices
- 🛒 Take single or multiple customer orders
- 🔢 Quantity-based ordering
- 🧾 Track all ordered items
- 💰 Calculate total bill automatically
- ✅ Generate a detailed order summary

---

## 📂 Project Structure

```
cafe-ordering-system/
├── basic_cafe_order.py         # Version 1 — Single item order
├── multi_order_cafe.py         # Version 2 — Multiple item orders
├── quantity_enabled_cafe.py    # Version 3 — Quantity support
├── cafe_order_management.py    # Version 4 — Full order management
└── README.md
```

---

## 🗂️ Version History

| Version | File | Key Features |
|---------|------|--------------|
| v1 | `basic_cafe_order.py` | Display menu, order single item, calculate bill |
| v2 | `multi_order_cafe.py` | Order multiple items, loop-based ordering, total bill |
| v3 | `quantity_enabled_cafe.py` | Quantity support, price × quantity calculation |
| v4 | `cafe_order_management.py` | Full order tracking, order summary, final bill |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/cafe-ordering-system.git

# Navigate into the project folder
cd cafe-ordering-system
```

### Running the Project

Start with the latest full-featured version:

```bash
python cafe_order_management.py
```

Or explore earlier versions to see how the project evolved:

```bash
python basic_cafe_order.py
python multi_order_cafe.py
python quantity_enabled_cafe.py
```

---

## 📸 Sample Output

```
Welcome To Our Cafe

Pizza      : ₹49
Salad      : ₹35
Burger     : ₹100
Pop Corn   : ₹150
Sandwich   : ₹60

Enter Your Item: pizza
How much Quantity do you require: 2

Do You Want anything else? (Yes/No): yes

Enter Your Item: burger
How much Quantity do you require: 1

----------------------------------------
           ORDER SUMMARY
----------------------------------------
Items Ordered:
  - pizza  x2   ₹98
  - burger x1   ₹100

Total Bill: ₹198
----------------------------------------

Thank You, Visit Again! 😍
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.x | Core language |
| Dictionaries | Menu storage |
| Lists | Order tracking |
| Loops & Conditionals | Order flow control |
| f-strings / String Methods | Output formatting |

---

## 🎯 Learning Outcomes

This project helps you practice and understand:

- **Python Dictionaries** — storing menu items and prices
- **Lists** — tracking ordered items dynamically
- **Loops** — handling continuous order input
- **Conditional Statements** — validating user choices
- **String Methods** — case-insensitive input handling
- **Basic Billing Logic** — price × quantity calculations
- **User Input Handling** — collecting and processing CLI input

---

## 🔮 Future Improvements

- [ ] Add a discount or coupon code system
- [ ] Export order summary to a `.txt` or `.pdf` file
- [ ] Add a GUI using `tkinter`
- [ ] Connect to a database to store order history
- [ ] Build a web version using Flask or Django

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Made with ❤️ for Python beginners learning through hands-on projects.