import tkinter as tk
from tkinter import messagebox

# ===== Original Classes =====
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def show(self):
        return f"{self.name} - PHP {self.price}"

class FilipinoItem(MenuItem):
    pass

class VegItem(MenuItem):
    pass

class InternationalItem(MenuItem):
    def get_price(self):
        return self.price + 12  # tax in peso

class Order:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def get_bill(self):
        total = 0
        lines = []
        for item in self.items:
            price = item.get_price()
            lines.append(f"{item.name} - PHP {price}")
            total += price
        lines.append(f"\nTotal: PHP {total}")
        return "\n".join(lines)

class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, item):
        self.order.add_items(item)

    def show_summary(self):
        return f"Customer: {self.name}\n\n" + self.order.get_bill()


# ===== Menu Data =====
menu = [
    FilipinoItem("Menudo", 69),
    FilipinoItem("Adobo", 79),
    FilipinoItem("Pork Sinigang", 99),
    FilipinoItem("Kare-Kare", 109),
    FilipinoItem("Lechon Kawali", 129),
    VegItem("Laing", 59),
    VegItem("Pinakbet", 79),
    InternationalItem("Shawarma Wrap", 49),
    InternationalItem("Shawarma Rice", 59),
    InternationalItem("Fried Chicken", 89),
    InternationalItem("Beef Kebab w/ Rice", 119)
]


# ===== GUI Application =====
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("BAHAY NI EYS - Order Menu")
        self.customer = None

        self.label = tk.Label(root, text = "Enter your name:")
        self.label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.start_button = tk.Button(root, text = "Start Order", command = self.start_order)
        self.start_button.pack(pady = 5)

        self.menu_listbox = tk.Listbox(root, selectmode = tk.MULTIPLE, width = 40)
        for item in menu:
            self.menu_listbox.insert(tk.END, item.show())
        self.menu_listbox.config(state=tk.DISABLED)
        self.menu_listbox.pack()

        self.order_button = tk.Button(root, text = "Place Order", command = self.place_order)
        self.order_button.config(state = tk.DISABLED)
        self.order_button.pack(pady=5)

        self.result = tk.Text(root, height = 15, width = 50, state = tk.DISABLED)
        self.result.pack(pady = 10)

    def start_order(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Required", "Please enter your name.")
            return

        self.customer = Customer(name)
        self.menu_listbox.config(state = tk.NORMAL)
        self.order_button.config(state = tk.NORMAL)
        self.name_entry.config(state = tk.DISABLED)
        self.start_button.config(state = tk.DISABLED)

    def place_order(self):
        selections = self.menu_listbox.curselection()
        if not selections:
            messagebox.showinfo("No Selection", "Please select at least one item.")
            return

        for num in selections:
            self.customer.place_order(menu[num])

        summary = self.customer.show_summary()
        self.result.config(state = tk.NORMAL)
        self.result.delete("1.0", tk.END)
        self.result.insert(tk.END, summary)
        self.result.config(state = tk.DISABLED)


# ===== Run the App =====
root = tk.Tk()
app = App(root)
root.mainloop()