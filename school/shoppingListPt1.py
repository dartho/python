class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${round(self.item_price, 2)} = ${round(self.item_quantity * self.item_price, 2)}")


items = []
num_items = 2
for i in range(num_items):
    print("Item " + str(i + 1))
    print("Enter the item name:")
    name = input()
    print("Enter the item price:")
    price = input()
    print("Enter the item quantity:")
    quantity = input()
    print()
    items.append(ItemToPurchase(name, float(price), int(quantity)))

print("TOTAL COST")
total_cost = 0
for i in items:
    i.print_item_cost()
    total_cost += i.item_price * i.item_quantity
print(f"\nTotal: ${round(total_cost, 2)}")
