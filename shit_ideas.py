from random import choice, randint

spirits = ['rye whiskey', 'scotch whiskey', 'bourbon', 'vodka', 'gin', 'jenever', 'rum', 'mezcal', 'port', 'tequila']
#List of ideas go in
adjective = ['energetic', 'sketchy', 'suspicious', 'ridiculous']
#for storytelling
verb = ['walk', 'drive', 'run', 'swim', 'cycle']
#more storytelling
spices = ['cinnamon', 'cloves', 'juniper berries', 'coffee beans']
#more story telling

method = ['shake', 'stir']
missionstyle = ['serve over ice', 'serve neat', 'serve over crushed ice']
location = ['old fashioned glass', 'collins glass', 'julep tin', 'tiki mug', 'flute', 'coup', 'martini glass']
additional = ['top with soda', 'top with tonic', 'top with prosecco', ' ']

recipe = []

def randomMeasure():
    return str(randint(1, 10) * 5) + 'minutes'
# time constraints

def getSpiritForRecipe(recipe):
    return randomMeasure() + ' ' + choice([spirit for spirit in spirits if spirit not in recipe])

# Add a random number of spirits to the recipe, minimum of 2, maximum of all available spirits
#numberOfSpirits = randint((2,4) len(spirits))
numberOfSpirits = randint(2, len(spirits))
#python generating random numbers

for i in range(numberOfSpirits):
    recipe.append(getSpiritForRecipe(recipe))

recipe.append(choice(method))
recipe.append(choice(missionstyle))
recipe.append(choice(location))
recipe.append(choice(additional))
recipe.append(choice(adjective) + ' ' + choice(verb))
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
