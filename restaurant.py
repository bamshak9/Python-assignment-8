"""
TASK: Create a RestaurantOrder class.

Requirements:
1. Store orders in a dictionary (item → quantity).
2. Provide a method to add items to the order.
3. Provide a method to remove items from the order.
4. Provide a method to calculate the total bill (use a price list dictionary).
5. Provide a method to show the current order.

Example Usage:
    prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
    order = RestaurantOrder(prices)
    order.add_item("Pizza", 2)
    order.add_item("Drink", 3)
    print(order.calculate_total())  # 5500
"""
class RestaurantOrder:
    def __init__(self, prices):
        self.prices= prices
        self.orders={}
    def add_item(self,item, quantity):
        self.orders[item]=quantity
    def remove_item(self,item):
        if item in self.orders.keys():
            self.orders.pop(item)
        else:
            print("Item not ordered")
    def calculate_total(self):
        total=0
        for item in self.orders:
            total+=(self.orders[item]*self.prices[item])
        return total
    def show_current_order(self):
        print(self.orders)
    
    


my_prices={"Pizza": 2000, "Burger": 1500, "Drink": 500}
order = RestaurantOrder(my_prices)
order.show_current_order()
order.add_item("Pizza",2)
order.add_item("Drink", 3)
order.show_current_order()
print(order.calculate_total())