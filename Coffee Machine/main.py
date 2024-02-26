from Coffee_Data import MENU, resources

profit = 0

def is_resourses_suff(order_ingred):
    for item in order_ingred:
        if order_ingred[item] > resources[item]:
            print(f"Sorry insufficient {item}.")
            return False
    return True


def process_Coin():
    print("Please insert coins...")
    total += int(input("How mony Rs.1 coins ?")) * 1
    total += int(input("How mony Rs.2 coins ?")) * 2
    total += int(input("How mony Rs.5 oins ?")) * 5
    total += int(input("How mony Rs.10 coins ?")) * 10
    return total


def is_transac_Suc(moneyRec, drinkCost):
    if moneyRec >= drinkCost:
        change = moneyRec - drinkCost
        print(f"Here is Rs{change} in change.")
        global profit
        profit += drinkCost
        return True
    else:
        print(f"Not Enough money. Money refunded.")
        return False
    

is_on = True
while is_on:
    choice = input("What would like to order(espresso / latte / cappiccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
    else:
        drink = MENU[choice]
        if is_resourses_suff(drink["ingredient"]):
            payment = process_Coin()
            is_resourses_suff(payment, drink["cast"])
