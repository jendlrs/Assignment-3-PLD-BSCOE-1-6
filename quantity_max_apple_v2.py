def getMoney():
    moneyA= float(input("\nEnter the amount of money you have: \n> "))
    return moneyA

def getCostForApple ():
    cost_per_appleA= float(input("\nPrice per apple: \n> "))
    return cost_per_appleA

def computeForMaxQuantity ():
    max_quantityA= int(money/cost_per_apple)
    return max_quantityA

def computeForChange():
    changeA= money % cost_per_apple
    return changeA

def display(max_quantityA, changeA):
    print(f"\nYou can buy {max_quantityA:,} apples and your change is {changeA:,.2f} pesos. \n")

money= getMoney()
cost_per_apple= getCostForApple ()
max_quantity= computeForMaxQuantity ()
change= computeForChange ()

display(max_quantity,change)