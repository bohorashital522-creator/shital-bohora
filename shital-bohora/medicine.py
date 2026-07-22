import datetime
import os

class Medicine:
    """Represents a medicine item in the wholesale system."""
    def __init__(self, name, brand, stock, rate_tab, rate_strip, tabs_per_strip):
        self.name = name
        self.brand = brand
        self.stock = int(stock)
        self.rate_tab = float(rate_tab)
        self.rate_strip = float(rate_strip)
        self.tabs_per_strip = int(tabs_per_strip)

    def __str__(self):
        return f"{self.name} ({self.brand}) | Stock: {self.stock} | Tab: Rs.{self.rate_tab} | Strip: Rs.{self.rate_strip}"

class InventoryManager:
    """Handles data storage and file updates[cite: 66, 83]."""
    def __init__(self, filename):
        self.filename = filename
        self.medicines = []
        self.load_inventory()

    def load_inventory(self):
        """Reads inventory from the text file[cite: 68]."""
        self.medicines = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 6:
                        self.medicines.append(Medicine(*[d.strip() for d in data]))

    def save_inventory(self):
        """Updates the text file immediately after transactions[cite: 70, 83]."""
        with open(self.filename, 'w') as file:
            for med in self.medicines:
                file.write(f"{med.name}, {med.brand}, {med.stock}, {med.rate_tab}, {med.rate_strip}, {med.tabs_per_strip}\n")

class Transaction:
    """Generates unique invoices for sales and restocks[cite: 69, 79, 81, 84]."""
    @staticmethod
    def create_invoice(person, items, trans_type):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{trans_type}_{person}_{timestamp}.txt"
        
        total_amount = 0
        invoice_content = f"--- MedStore Wholesale {trans_type.upper()} ---\n"
        invoice_content += f"Name: {person}\nDate: {datetime.datetime.now()}\n"
        invoice_content += "-" * 40 + "\n"
        
        for item in items:
            invoice_content += f"{item['name']} ({item['brand']})\n"
            invoice_content += f"Qty: {item['qty']} {item['unit']} | Subtotal: Rs.{item['subtotal']}\n"
            total_amount += item['subtotal']
            
        invoice_content += "-" * 40 + f"\nTOTAL BILL: Rs.{total_amount}"
        
        with open(filename, 'w') as f:
            f.write(invoice_content)
        print(f"\nInvoice successfully generated: {filename}")

def main():
    # Setup inventory [cite: 71, 78]
    manager = InventoryManager("inventory.txt")
    
    while True: # Main program loop [cite: 93, 94]
        print("\n--- MedStore Management System ---")
        print("1. View Stock")
        print("2. Process Sale (Customer)")
        print("3. Process Restock (Supplier)")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        try:
            if choice == '1':
                print("\nAvailable Medicines:")
                for i, med in enumerate(manager.medicines):
                    print(f"{i+1}. {med}")
            
            elif choice == '2': # Sales transaction [cite: 63, 64]
                idx = int(input("Select medicine number: ")) - 1
                med = manager.medicines[idx]
                
                customer = input("Customer Name: ")
                unit = input("Sale unit (tablet/strip): ").lower()
                qty = int(input(f"Quantity of {unit}s: "))
                
                # Logic for stock update and discount [cite: 64, 70]
                if unit == "strip":
                    total_tabs = qty * med.tabs_per_strip
                    price = qty * med.rate_strip
                    discount = 0.05 * price if qty >= 2 else 0
                else:
                    total_tabs = qty
                    price = qty * med.rate_tab
                    discount = 0

                if med.stock >= total_tabs:
                    med.stock -= total_tabs
                    item = {"name": med.name, "brand": med.brand, "qty": qty, "unit": unit, "subtotal": price - discount}
                    Transaction.create_invoice(customer, [item], "sale")
                    manager.save_inventory()
                else:
                    print("Error: Not enough stock.")

            elif choice == '3': # Restock transaction [cite: 81, 83]
                idx = int(input("Select medicine number: ")) - 1
                med = manager.medicines[idx]
                
                supplier = input("Supplier/Vendor Name: ")
                qty_tabs = int(input("Tablets received: "))
                
                med.stock += qty_tabs
                item = {"name": med.name, "brand": med.brand, "qty": qty_tabs, "unit": "tablets", "subtotal": qty_tabs * med.rate_tab}
                Transaction.create_invoice(supplier, [item], "restock")
                manager.save_inventory()

            elif choice == '4':
                print("Closing system...")
                break
                
        except (ValueError, IndexError): # Error handling 
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()