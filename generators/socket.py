import pymsgbox
from generators.effects.effectGenerator import effect_generator as genEffects
from generators.effects.effectGenerator import effect_json_gen as effectBuilder


def UserIn(text):
    return pymsgbox.prompt(text, 'SOCKET DETAILS')

def user_input_array():
    debug = UserIn('Debug Mode? [y/n]')
    hasEffects = UserIn('Should the Socket have effects? [y/n]')
    numEffects = [0, 'null:null', 0]
    if hasEffects == 'y':
        numEffects = genEffects()
    if debug == 'y':
        modID = UserIn('Socket Material mod ID')
        print(modID)
        matID = UserIn('Socket Material name')
        print(matID)
        duraCost = UserIn('Durability Gained/Lost? use a [-] to indicate lost')
        print(duraCost)
        integCost = UserIn('Integrity Gained/Lost? use a [-] to indicate lost')
        print(integCost)
        xpCost = UserIn('XP Cost in Levels')
        print(xpCost)
        tintHEX = UserIn('Part Color as a HEX value (HEX = xxxxxx)')
        print(tintHEX)
    else:
        modID = UserIn('Socket Material mod ID')
        matID = UserIn('Socket Material name')
        duraCost = UserIn('Durability Gained/Lost? use a [-] to indicate lost')
        integCost = UserIn('Integrity Gained/Lost? use a [-] to indicate lost')
        xpCost = UserIn('XP Cost in Levels')
        tintHEX = UserIn('Part Color as a HEX value (HEX = xxxxxx)')
    build_json(modID, matID, duraCost, integCost, xpCost, tintHEX, numEffects)

def build_json(modID, matID, duraCost, integCost, xpCost, tintHEX, numEffects):
    numberOfEffects = numEffects
    with open("generators/outputs/single_socket.json", 'w+') as f:
        f.close()
    with open("generators/outputs/single_socket.json", 'a') as f:
        f.write("{\n\t\"key\": \"" + modID + ':' + matID + '\",\n')
        f.write("\"category\": \"misc\",\n")
        f.write("\"durability\": " + duraCost + ",")
        f.write("\"integrity\": " + integCost)
        if int(numberOfEffects[2]) > 0:
            f.write(",\n \"effects\": {\n")
            effectBuilder(numberOfEffects[0], numberOfEffects[1], f)
        f.write("\n\t\"glyph\": {")
        f.write("\n\t\t\"tint\": \"" + tintHEX + "\",\n\t\t\"textureX\": 80,\n\t\t\"textureY\": 16\n\t},")
        f.write("\n\t\"models\": [\n\t\t{\n\t\t\t\"location\": \"tetra:items/module/single/binding/socket/default\",")
        f.write("\n\t\t\t\"tint\": \"" + tintHEX + "\"\n\t\t}\n\t]\n}")

    with open("generators/outputs/double_socket.json", 'w+') as f:
        f.close()
    with open("generators/outputs/double_socket.json", 'a') as f:
        f.write("{\n\t\"key\": \"" + modID + ':' + matID + '\",\n')
        f.write("\"category\": \"misc\",\n")
        f.write("\"durability\": " + duraCost + ",")
        f.write("\"integrity\": " + integCost)
        if int(numberOfEffects[2]) > 0:
            f.write(",\n \"effects\": {\n")
            effectBuilder(numberOfEffects[0], numberOfEffects[1], f)
        f.write("\n\t\"glyph\": {")
        f.write("\n\t\t\"tint\": \"" + tintHEX + "\",\n\t\t\"textureX\": 80,\n\t\t\"textureY\": 16\n\t},")
        f.write("\n\t\"models\": [\n\t\t{\n\t\t\t\"location\": \"tetra:items/module/double/binding/socket/default\",")
        f.write("\n\t\t\t\"tint\": \"" + tintHEX + "\"\n\t\t}\n\t]\n}")

    with open("generators/outputs/sword_socket.json", 'w+') as f:
        f.close()
    with open("generators/outputs/sword_socket.json", 'a') as f:
        f.write("{\n\t\"key\": \"" + modID + ':' + matID + '\",\n')
        f.write("\"category\": \"misc\",\n")
        f.write("\"durability\": " + duraCost + ",")
        f.write("\"integrity\": " + integCost)
        if int(numberOfEffects[2]) > 0:
            f.write(",\n \"effects\": {\n")
            effectBuilder(numberOfEffects[0], numberOfEffects[1], f)
        f.write("\n\t\"glyph\": {")
        f.write("\n\t\t\"tint\": \"" + tintHEX + "\",\n\t\t\"textureX\": 80,\n\t\t\"textureY\": 16\n\t},")
        f.write("\n\t\"models\": [\n\t\t{\n\t\t\t\"location\": \"tetra:items/module/sword/binding/socket/default\",")
        f.write("\n\t\t\t\"tint\": \"" + tintHEX + "\"\n\t\t}\n\t]\n}")
