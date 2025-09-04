"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""
class Inventory:
    def __init__(self):
        self.items={}
    def add_item(self,item,quantity):
        if item.upper() not in self.items.keys():
            self.items[item.upper()]=quantity
        else:
            print(f'{item} already exists is inventory, use update to add')
    def remove_item(self, item, quantity):
        if item.upper() in self.items.keys():
            if quantity<=self.items[item.upper()]:
                self.items[item.upper()]-=quantity
                if self.items[item.upper()]==0:
                    self.items.pop(item.upper())
                    print(f"We are now out of{item.upper()}")
                else:
                    pass
            else:
                print(f"Sorry the amount of {item} in stock is not sufficient")
        else:
            print(f"{item} does not exist in inventory ")
    def update_stock(self, item,quantity):
        if item.upper() in self.items.keys():
            self.items[item.upper()]+=quantity
        else:
            print(f"{Item} not in inventory use add instead")
    def show_inventory(self):
        return self.items


treasure_store = Inventory()
favour_store = Inventory()           
treasure_store.add_item("Apples", 50)
treasure_store.add_item("Bananas", 30)
treasure_store.remove_item("Apples", 10)
print(treasure_store.show_inventory())

favour_store.add_item("Milk", 50)
favour_store.add_item("Garri", 30)
favour_store.remove_item("Milk", 40)
print(favour_store.show_inventory())