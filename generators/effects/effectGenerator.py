import pymsgbox


def UserIn(text):
    return pymsgbox.prompt(text, 'Effect Details')

def effect_generator():
    numEffects = UserIn('number of effects as an int')
    i = int(numEffects)
    effectList = []
    effectLevelList = []
    while i > 0:
        effectName = UserIn('What Effect? MUST be in the style of [tetra:workable]')
        effectList.append(effectName)
        effectLevel = UserIn('What level is the applied effect? NUMBERS ONLY OR PROGRAM BREAKS')
        if effectLevel == '' or effectLevel != int:
            effectLevel = '1'
        effectLevelList.append(int(effectLevel))
        i -= 1
    return effectList, effectLevelList, numEffects

def effect_json_gen(effectList, effectLevelList, f):
    print(effectList)
    print(effectLevelList)
    #effectLevelListDummy = effectLevelList
    #effectListDummy = effectList
    for i in range(len(effectLevelList)):
        f.write("\t\"" + effectList[i] + "\":" + str(effectLevelList[i]) + "\n")
        # effectLevelListDummy.pop(0)
        # effectListDummy.pop(0)
    f.write("\t},")
    print(effectList)
    print(effectLevelList)
