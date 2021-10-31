def getMoney():
    moneyA= float(input("\n Enter the amount of money you have: \n> "))
    return moneyA
def getCostForApple ():
    cost_per_appleA= float(input("\n Price per apple: \n> "))
    return cost_per_appleA
def computeForMaxQuantity ():
    max_quantityA= int(money/cost_per_apple)
    return max_quantityA
def computeForChange():
    changeA= money % cost_per_apple
    return changeA

money=getMoney()
cost_per_apple= getCostForApple ()
max_quantity= computeForMaxQuantity ()
change= computeForChange ()