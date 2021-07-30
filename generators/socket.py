import pymsgbox
from generators.effects.effectGenerator import effect_generator as genEffects
from generators.effects.effectGenerator import effect_json_gen as effectBuilder

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
    numEffects = [0, 'null:null', 0]
    if hasEffects == 'y':
        genEffects()
        numEffects = genEffects
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
    build_json(modID, matID, duraCost, integCost, xpCost, tintHEX, numEffects)

def build_json(modID, matID, duraCost, integCost, xpCost, tintHEX, numEffects):
    with open("generators/outputs/single_socket.json", 'w+') as f:
        f.close()
    # with open("generators/outputs/single_socket.json", 'r+') as f:
    #     f.truncate(0)
    #     f.seek(0)
    with open("generators/outputs/single_socket.json", 'a') as f:
        f.write("{\n\"" + modID + ':' + matID + ',\n')
        f.write("\"category\": \"misc\",\n")
        f.write("\"durability\": " + duraCost + ",")
        f.write("\"integrity\": " + integCost)
        if numEffects[3] > 0:
            f.write(",\n \"effects\": {\n")
            effectBuilder(numEffects[0], numEffects[1], f)

    with open("generators/outputs/double_socket.json", 'w+') as f:
        f.close()
    # with open("generators/outputs/double_socket.json", 'r+') as f:
    #     f.truncate(0)
    #     f.seek(0)
    with open("generators/outputs/double_socket.json", 'a') as f:
        f.write("{\n\"" + modID + ':' + matID + ',\n')

    with open("generators/outputs/sword_socket.json", 'w+') as f:
        f.close()
    # with open("generators/outputs/sword_socket.json", 'r+') as f:
    #     f.truncate(0)
    #     f.seek(0)
    with open("generators/outputs/sword_socket.json", 'a') as f:
        f.write("{\n\"" + modID + ':' + matID + ',\n')
