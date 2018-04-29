from random import choice, randint

spirits = ['rye whiskey', 'scotch whiskey', 'bourbon', 'vodka', 'gin', 'jenever', 'rum', 'mezcal', 'port', 'tequila']
fruit = ['orange', 'lemon', 'lime', 'grapefruit']
fruitstyle = ['peel', 'wedge', 'slice', 'twist', 'zest']
spices = ['cinnamon', 'cloves', 'juniper berries', 'coffee beans']

method = ['shake', 'stir']
icestyle = ['serve over ice', 'serve neat', 'serve over crushed ice']
glass = ['old fashioned glass', 'collins glass', 'julep tin', 'tiki mug', 'flute', 'coup', 'martini glass']
additional = ['top with soda', 'top with tonic', 'top with prosecco', ' ']

recipe = []

def randomMeasure():
    return str(randint(1, 10) * 5) + 'ml'
# additional part in here which specifies a maximum measure amount? 120/150ml
def getSpiritForRecipe(recipe):
    return randomMeasure() + ' ' + choice([spirit for spirit in spirits if spirit not in recipe])

# Add a random number of spirits to the recipe, minimum of 2, maximum of all available spirits
#numberOfSpirits = randint((2,4) len(spirits))
numberOfSpirits = randint(2, len(spirits))
#python generating random numbers

for i in range(numberOfSpirits):
    recipe.append(getSpiritForRecipe(recipe))

recipe.append(choice(method))
recipe.append(choice(icestyle))
recipe.append(choice(glass))
recipe.append(choice(additional))
recipe.append(choice(fruit) + ' ' + choice(fruitstyle))
recipe.append(choice(spices))

for item in recipe:
    print " - %s" % item

	# add method
    # add curveball 
    # add barspoon of something
    # serve in glass
    # serve in curveball glass
    # add ridiculous backstory
    # add origin story 
    # alternative curveball origin - on request for more information
    # separate lists built as text files to be brought in and read  
