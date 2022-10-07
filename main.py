#method is function inside pyth class
class Item:     #class
    pay_rate = 0.8
    def __init__(self, name: str, price, quantity): #some of the magic methods
        assert price >= 0  #assert validates the input specially for negative case
        assert quantity >= 0 ,f"quantity {quantity} cant be lesser or equal to zero"
        #constructor which will run automatically when a new obj is made
        self.name = name
        self.price = price
        self.quantity = quantity

        print(f"I am created for: {name}")
    def calculate_total_price(self, x, y):  #method
        return x*y  #return computed value

    def calc_total_price(self):  #method this time doesn't need to get args sepaarately because obj is itself passed thorugh self
        return self.price * self.quantity
item1 = Item("Phone",100,5)     #object
#item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity)) #method call
print(item1.calc_total_price())

#print(type(item1))
#print(type(item1.name))
#print(type(item1.price))
#print(type(item1.quantity))

item2 = Item("Laptop",1000,3)
#item2.name = "Phone"
#item2.price = 1000
#item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))   #method call


# if __name__ == '__main__':
# print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
 #WHEN CREATING A METHOD we use self instead of class name because using self allow us to go on instance level thus allowing to acces the changed values