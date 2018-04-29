from random import choice, randint

spirits = ['dog walk', 'read a book', 'watch a film', 'stare blankly into the void', 'pondering', 'youtube spiral', 'recipe hunting', 'making new playlists', 'nest building', 'documentary watching']
#List of ideas go in
adjective = ['walk', 'drive', 'run', 'swim', 'cycle']
#for storytelling
verb = ['like a creep', 'with reckless abandon', 'suspiciously', 'ridiculously']
#more storytelling
spices = ['cinnamon', 'cloves', 'juniper berries', 'coffee beans']
#more story telling?

method = ['Adapt and Overcome', 'Panic']
missionstyle = ['Give a motivational speech', 'Initiate a regime change','Summon some demons', 'Call upon your ancestors for protection']
location = ['somewhere you have never been before', 'at work', 'on public transport', 'in your kitchen', 'in the middle of the road', 'screaming from the rooftops', 'whilst planning a quick exit']
additional = ['take a bow', 'congratulate yourself on a job well done', 'brush it off and carry on as if it never happened']

recipe = []

def randomMeasure():
    return str(randint(1, 10) * 5) + ' minutes'
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
