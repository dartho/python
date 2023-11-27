class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_desc="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_desc = item_desc

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${round(self.item_price, 2)} = ${round(self.item_quantity * self.item_price, 2)}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_desc}, {self.item_quantity} oz.")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, cart_item: ItemToPurchase):
        self.cart_items.append(cart_item)

    def remove_item(self, item_name):
        item_found = False
        item: ItemToPurchase
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, cart_item: ItemToPurchase):
        item_found = False
        item: ItemToPurchase
        for idx in range(len(self.cart_items)):
            item = self.cart_items[idx]
            if item.item_name == cart_item.item_name:
                modified_item = ItemToPurchase(item.item_name, item.item_price, cart_item.item_quantity, item.item_desc)
                self.cart_items[idx] = modified_item
                item_found = True
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        count = 0
        item: ItemToPurchase
        for item in self.cart_items:
            count += item.item_quantity
        return count

    def get_cost_of_cart(self):
        total = 0
        item: ItemToPurchase
        for item in self.cart_items:
            total += item.item_quantity * item.item_price
        return total

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        item: ItemToPurchase
        for item in self.cart_items:
            item.print_item_cost()
        print()
        print(f"Total: ${round(self.get_cost_of_cart(), 2)}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        item: ItemToPurchase
        for item in self.cart_items:
            item.print_item_description()


def print_menu():
    print("""MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:""")


def execute_menu(option, cart: ShoppingCart):
    if option == "a":
        print("ADD ITEM TO CART")
        print("Enter the item name:")
        name = input()
        print("Enter the item description:")
        desc = input()
        print("Enter the item price:")
        price = input()
        print("Enter the item quantity:")
        quantity = input()
        cart.add_item(ItemToPurchase(name, float(price), int(quantity), desc))
    elif option == "r":
        print("REMOVE ITEM FROM CART")
        print("Enter name of item to remove:")
        remove_name = input()
        cart.remove_item(remove_name)
    elif option == "c":
        print("CHANGE ITEM QUANTITY")
        print("Enter the item name:")
        change_name = input()
        print("Enter the new quantity:")
        change_quantity = input()
        cart.modify_item(ItemToPurchase(change_name, 0, int(change_quantity)))
    elif option == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions()
    elif option == "o":
        print("OUTPUT SHOPPING CART")
        cart.print_total()
    print()


print("Enter customer's name:")
cust_name = input()
print("Enter today's date:")
curr_date = input()
print(f"Customer name: {cust_name}")
print(f"Today's date: {curr_date}")
shopping_cart = ShoppingCart(cust_name, curr_date)

menu_opt = ""
while menu_opt != "q":
    print_menu()
    menu_opt = input()
    if menu_opt != "q":
        execute_menu(menu_opt, shopping_cart)
