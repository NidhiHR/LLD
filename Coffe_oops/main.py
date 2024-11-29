from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# print("What would you like to have (espresso/latte/cuppocino)")
# user_inp=input()

money_machine=MoneyMachine()
coffe_maker=CoffeeMaker()
menu=Menu()

is_on=True

while is_on:
    print(f"what would you like to order {menu.get_items()}")
    userip=input()
    if userip=="off":
        is_on=False
    elif userip=="report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(userip)
        if coffe_maker.is_resource_sufficient(drink):
            print(f"\nTHE AMOUNT NEED TO BE PAID IS {drink.cost}\n")
            money_machine.make_payment(drink.cost)
            coffe_maker.make_coffee(drink)




# print(f"what would you like to order {menu.get_items()}")
# userip=input()

# drink=menu.find_drink(userip)
# if drink:
#     print('It is available')

#     if coffe_maker.is_resource_sufficient(drink):
#         print(f'The cost of coffee is {drink.cost}')

#         if money_machine.make_payment(drink.cost):
#             print(money_machine.report())
#             print(coffe_maker.report())








