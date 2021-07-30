import pymsgbox
from generators.effects.effectGenerator import effect_generator as genEffects

#-------------------------------
'''
modID = ""
matID = ""
duraCost = ""
integCost = ""
xpCost = ""
tintHEX = ""
'''
#-------------------------------

def UserIn(text):
    return pymsgbox.prompt(text, 'SOCKET DETAILS')

def user_input_array():
    debug = UserIn('Debug Mode? [y/n]')
    hasEffects = UserIn('Should the Socket have effects? [y/n]')
    if hasEffects == 'y':
        genEffects()
    if debug == 'y':
        modID = UserIn('mod ID')
        print(modID)
        matID = UserIn('Material name')
        print(matID)
        duraCost = UserIn('Durability Gained/Lost')
        print(duraCost)
        integCost = UserIn('Integrity Gained/Lost')
        print(integCost)
        xpCost = UserIn('XP Cost in Levels')
        print(xpCost)
        tintHEX = UserIn('Part Color as a HEX value (HEX = xxxxxx)')
        print(tintHEX)
    else:
        modID = UserIn('mod ID')
        matID = UserIn('Material name')
        duraCost = UserIn('Durability Gained/Lost')
        integCost = UserIn('Integrity Gained/Lost')
        xpCost = UserIn('XP Cost in Levels')
        tintHEX = UserIn('Part Color as a HEX value (HEX = xxxxxx)')
    #return modID, matID, duraCost, integCost, xpCost, tintHEX
    build_json(modID, matID, duraCost, integCost, xpCost, tintHEX)

def build_json(modID, matID, duraCost, integCost, xpCost, tintHEX):
    with open("generators/outputs/single_socket.json", 'r+') as f:
        f.truncate(0)
        f.seek(0)
        f.write("{\n\"" + modID + ':' + matID + ',\n')

    with open("generators/outputs/double_socket.json", 'r+') as f:
        f.truncate(0)
        f.seek(0)

    with open("generators/outputs/sword_socket.json", 'r+') as f:
        f.truncate(0)
        f.seek(0)



