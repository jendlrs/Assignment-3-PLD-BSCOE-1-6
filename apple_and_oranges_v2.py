def getApple():
    quantity_appleA= int(input("\nHow many apples do you want to buy?\n> "))
    return quantity_appleA

def getOrange ():
    quantity_orangeA= int(input("\n How many oranges do you want to buy? \n> "))
    return quantity_orangeA

def compute_for_total_cost():
    cost_per_apple= 20
    cost_per_orange= 25
    totalA= cost_per_apple*quantity_apples + cost_per_orange*quantity_oranges
    return totalA

def display(totalA):
    print (f"\nThe total amount is {totalA}\n")

quantity_apples= getApple()
quantity_oranges= getOrange()
total=compute_for_total_cost()

display(total)


