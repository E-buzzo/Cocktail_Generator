#food="milk eggs cheese butter cream"
#just a string 
#inthefridge= list(food.split(" "))
#creates list from string, that is split into separate words - define where to split it
import random
#this imports random to the script


measures = [' 5ml', ' 10ml', ' 15ml', ' 20ml', ' 25ml', ' 30ml', ' 35ml', ' 40ml', ' 45ml', ' 50ml' ]
spirits = [' rye whiskey', ' scotch whiskey', ' bourbon', ' vodka', ' gin', ' jenever', ' rum', ' mezcal', ' port', ' tequila']
# added more items in a second list

partone = random.choice(measures) + random.choice(spirits)
parttwo = random.choice(measures) + random.choice(spirits)



fruit = [' orange', ' lemon', ' lime', ' grapefruit']
fruitstyle = [' peel', ' wedge', ' slice', ' twist', ' zest']
spices = [' and cinnamon', ' and cloves', ' and juniper berries', ' and coffee beans']
garnishlist = fruit + fruitstyle + spices
#assign name to the two variables combined

garnish = random.choice(fruit) + random.choice(fruitstyle) + random.choice(spices)



recipe = partone + parttwo + garnish 
print recipe

#inthefridge [inthefridge.index('butter')] = 'ham'
#searches for item .index replaces the indexed space ('') with new item ''
#inthefridge [inthefridge.index('ham')] = 'salmon'
#searches for item .index replaces the indexed space ('') with new item ''
#inthefridge.append('chutney')
#add item to the list


#+ random_food // this just prints same food twice
#print ingredients

#if I want a list to go from 0-10, can use range and say range will have 11 elements
#l = range(11)
#print l
#l = range (10,21)
#print l
#for f in ingredients:
	#new = f+ " lekker!"
	#print new 








