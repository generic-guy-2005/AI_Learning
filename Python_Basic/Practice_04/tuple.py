# Creating tuple
drink = ("Soda", "Milk", "Coffee", "Tea")

# Accessing tuple
print(drink[3])

# Converting tuple
drinkable = list(drink)
drinkable[0] = "Mojito"

# Converting list
drink = tuple(drinkable)
print(drink)