import os
from datetime import datetime

inventory = {
    1: {"name": "Rice", "net_qty": "5 kg", "stock": 150, "price": 550.00},
    2: {"name": "Wheat Flour (Atta)", "net_qty": "5 kg", "stock": 120, "price": 400.00},
    3: {"name": "Cooking Oil", "net_qty": "1 litre", "stock": 100, "price": 280.00},
    4: {"name": "Sugar", "net_qty": "1 kg", "stock": 130, "price": 110.00},
    5: {"name": "Salt", "net_qty": "1 kg", "stock": 140, "price": 25.00},
    6: {"name": "Milk", "net_qty": "1 litre", "stock": 80, "price": 90.00},
    7: {"name": "Eggs", "net_qty": "12 pcs (tray)", "stock": 90, "price": 180.00},
    8: {"name": "Tea Leaves", "net_qty": "250 gm", "stock": 70, "price": 150.00},
    9: {"name": "Lentils (Dal)", "net_qty": "1 kg", "stock": 100, "price": 200.00},
    10: {"name": "Onion", "net_qty": "1 kg", "stock": 110, "price": 60.00},
}

bill_no = 0


def show_inventory():
    print(f"\n{'ID':<4}{'Name':<22}{'Net Qty':<15}{'Stock':<8}{'Price':<8}")
    for mid, item in inventory.items():
        print(f"{mid:<4}{item['name']:<22}{item['net_qty']:<15}{item['stock']:<8}{item['price']:<8.2f}")


def take_order():
    cart = []
    while True:
        show_inventory()
        mid = int(input("\nMedicine ID (0 to finish): "))
        if mid == 0:
            break
        if mid not in inventory:
            print("Invalid ID.")
            continue

        item = inventory[mid]
        qty = int(input(f"Quantity of {item['name']} (Available: {item['stock']}): "))
        if qty <= 0 or qty > item["stock"]:
            print("Invalid quantity.")
            continue

        item["stock"] -= qty
        cart.append({"name": item["name"], "qty": qty, "price": item["price"], "total": qty * item["price"]})

    return cart


def generate_invoice(cart, name, phone):
    global bill_no
    if not cart:
        print("No items purchased.")
        return

    bill_no += 1
    subtotal = sum(i["total"] for i in cart)
    tax = subtotal * 0.05
    grand_total = subtotal + tax

    print("\n" + "=" * 45)
    print("             SITAL STORE")
    print("=" * 45)
    print(f"Invoice No: {bill_no}   Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Customer: {name}   Phone: {phone}")
    print("-" * 45)
    for i in cart:
        print(f"{i['name']:<20}{i['qty']:<5}{i['price']:<8.2f}{i['total']:<8.2f}")
    print("-" * 45)
    print(f"Subtotal: Rs {subtotal:.2f}")
    print(f"Tax (5%): Rs {tax:.2f}")
    print(f"Total:    Rs {grand_total:.2f}")
    print("=" * 45)

    os.makedirs("invoices", exist_ok=True)
    with open(f"invoices/invoice_{bill_no}.txt", "w") as f:
        f.write(f"SITAL STORE\nInvoice No: {bill_no}\nCustomer: {name} ({phone})\n\n")
        for i in cart:
            f.write(f"{i['name']} x{i['qty']} = Rs {i['total']:.2f}\n")
        f.write(f"\nSubtotal: Rs {subtotal:.2f}\nTax: Rs {tax:.2f}\nTotal: Rs {grand_total:.2f}\n")


def main():
    while True:
        print("\n1. View Inventory\n2. New Purchase\n3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            show_inventory()
        elif choice == "2":
            name = input("Customer name: ")
            phone = input("Phone: ")
            cart = take_order()
            generate_invoice(cart, name, phone)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()