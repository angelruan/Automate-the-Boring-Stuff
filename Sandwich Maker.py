from sys import _clear_type_cache
import pyinputplus as pyip 
import time 
# This game help you to customize your own sub. Enjoy!
# Ask user to input their choices of bread 
bread_prices = {"wheat":1, "white":1, "sourdough":1.5}
menu_input = pyip.inputMenu(
    prompt= "Please select your bread type:\n", 
    # List comprehension
    choices = [ bread.ljust(20) + "$"+str(bread_prices[bread]) for bread in bread_prices.keys()],
    allowRegexes=bread_prices.keys()
)
time.sleep(0.5)
print("You chose "+menu_input+" bread as your bread\n")
total_price = bread_prices[menu_input]

# Ask user to input their choices of protein
protein_prices = {"chicken":2, "turkey":2,"ham":3,"tofu":1}
protein_input = pyip.inputMenu(
    prompt= "Please set your protein: chicken($2), turkey($2), ham($3), or tofu($1)\n", 
    choices=[protein.ljust(20)+"$"+str(protein_prices[protein]) for protein in protein_prices],
    allowRegexes=protein_prices.keys()
    )
time.sleep(0.5)
print("You chose "+protein_input+" as your protein")
total_price = total_price+protein_prices[protein_input]

# Ask user if they want cheese
cheese_price = {"cheddar":2,"swiss":3,"mozzarella":2}
cheese_yesorno = pyip.inputYesNo(
    prompt="Do you want cheese?\n",
    caseSensitive=False,
    yesVal='yes',
    noVal='no'
)
if cheese_yesorno == 'yes':
    cheese_input= pyip.inputMenu(
        prompt="What kind of cheese would you like: cheddar, swiss, or mozzarella.\n",
        choices=[cheese.ljust(20)+'$'+str(cheese_price[cheese]) for cheese in cheese_price.keys()],
        allowRegexes=cheese_price.keys()
    )
    total_price = total_price + cheese_price[cheese_input]
else:
    total_price 
print("Your total price is "+ "$"+str(total_price))
