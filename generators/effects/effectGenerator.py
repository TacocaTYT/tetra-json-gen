import pymsgbox


def UserIn(text):
    return pymsgbox.prompt(text, 'Effect Details')

def effect_generator():
    numEffects = UserIn('number of effects as an int')
    i = int(numEffects)
    effectList = []
    effectLevelList = []
    while i > 0:
        effectName = UserIn('name of effect')
        effectList.append(effectName + '|')
        effectLevel = UserIn('What level is the applied effect')
        if effectLevel == '':
            effectLevel = '1'
        effectLevelList.append(int(effectLevel))
        i -= 1
    return effectList, effectLevelList, numEffects

def effect_json_gen(effectList, effectLevelList, f):
    for i in effectLevelList:
        f.write("\t\"" + effectList[0] + "\":" + effectLevelList[0] + "\n")
        effectLevelList.pop(0)
        effectList.pop(0)
