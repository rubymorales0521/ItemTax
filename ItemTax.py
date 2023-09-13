def Store():
    items = {
        "purse": 120.00,
        "perfume": 90.00,
        "lipGloss": 15.00
    }
    totalCost = 0.0

# items.items is what brings the item name along with price on same line
    for item, price in items.items():
        cart = input("Would you like to buy " + item + "? (yes/no) ")
        if cart.lower() == "yes":
            quantity = int(input("How many " + item + " would you like? "))
            totalCost += price * quantity # += basically x =x+y

    tax = 0.08
    salesTax = totalCost * tax
    totalCost += salesTax

    print ("\nSubtotal: $" + str(totalCost - salesTax))
    print ("Sales Tax (8%): $" + format(salesTax, ".2f")) #used format and .2f to round tax
    print("Total: $" + str(totalCost))
# call store function to run
Store()