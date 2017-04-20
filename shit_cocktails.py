import random
import subprocess 
#this imports random to the script

measures = [' 5ml', ' 10ml', ' 15ml', ' 20ml', ' 25ml', ' 30ml', ' 35ml', ' 40ml', ' 45ml', ' 50ml' ]
spirits = [' rye whiskey', ' scotch whiskey', ' bourbon', ' vodka', ' gin', ' jenever', ' rum', ' mezcal', ' port', ' tequila']

partone = random.choice(measures) + random.choice(spirits)
parttwo = random.choice(measures) + random.choice(spirits)

fruit = [' orange', ' lemon', ' lime', ' grapefruit']
fruitstyle = [' peel', ' wedge', ' slice', ' twist', ' zest']
spices = [' and cinnamon', ' and cloves', ' and juniper berries', ' and coffee beans']
garnishlist = fruit + fruitstyle + spices

garnish = random.choice(fruit) + random.choice(fruitstyle) + random.choice(spices)



recipe = partone + parttwo + garnish 
print recipe








