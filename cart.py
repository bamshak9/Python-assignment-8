"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""
class ShoppingCart:
    def __init__(self,prices):
        self.prices=prices
        self.items={}
    def add_item(self,item,quantity):
        if item in self.items.keys():
            self.items[item]+=quantity
        else:
            self.items[item]=quantity
    def remove_item(self, item, quantity):
        if item in self.items.keys():
            if quantity>=self.items[item]:
                self.items.pop(item)
            else:
                self.items[item]-=quantity
        else:
            print("Item not in cart")
    def clear_cart(self):
        self.items.clear()
    def calculate_total(self):
        cost=0
        for item in self.items:
            cost+=(self.items[item]*self.prices[item])
        return cost
    


prices = {"Shirt": 5000, "Shoes": 12000}
cart = ShoppingCart(prices)
cart.add_item("Shirt", 2)
print(cart.calculate_total())
cart.remove_item("Shirt", 1)
print(cart.calculate_total())