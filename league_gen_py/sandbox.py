__author__ = 'ryan'
import copy
import riot_api_wrapper.RiotAPI as API
import key as KEY


"""class dummy:
    def __init__(self):
        self.test = 1
        self.test1 = 2

    def setTest(self, int):
        self.test = int

    def getTest1(self):
        return self.test"""

def main ():
    api = API.RiotAPI(KEY.KEY)
    a = api.get_champion_list('spells')
    # a = api.get_champion_list()
    # print type(a['data']['MonkeyKing'])
    # print a['data']['Leblanc']
    x = 0
    keys = []
    for key in a['data'].iteritems(): # Get the list of keys from the API list of spells. Keys are essentially champ names.
        keys.append(key)
        x = x+1
    for each in keys:
        print each[0]
    # print(api.get_champion_list('spells'))
    """print "Number of keys: ", len(keys)
    print type(keys) # list
    print type(a['data']) # a['data'] is a dictionary
    print type(a['data']['MonkeyKing']) #dictionary
    print type(a['data']['MonkeyKing']['spells']) #list
    print len(a['data']['MonkeyKing']['spells']) #list with 4 things. all related to wukong.
    print type(a['data']['MonkeyKing']['spells'][0]) # a dictionary """
    for each in a['data']['FiddleSticks']['spells'][0]:
        print each
        print a['data']['FiddleSticks']['spells'][3][each]

    """print a['data']['MonkeyKing']['spells'][0]['sanitizedDescription']
    print a['data']['MonkeyKing']['spells'][0]['sanitizedTooltip']
    print a['data']['MonkeyKing']['spells'][0]['effect']"""

    """print type(a['data']['MonkeyKing']['spells'][3]['vars'])
    print len(a['data']['MonkeyKing']['spells'][0]['vars'])
    print a['data']['MonkeyKing']['spells'][0]['vars'][0] """
    #print a['data']['MonkeyKing']['spells'][3]['effect']
    #print a['data']['MonkeyKing']['spells'][3]['effect'][0]
    #print a['data']['MonkeyKing']['spells'][3]['effect'][1]
    #print a['data']['MonkeyKing']['spells'][3]['effect'][2]
    # https://developer.riotgames.com/docs/static-data
    # IMPORTANT KEYS
    # 'name'        - Name of the spell
    # 'cooldown'    - a list of the cooldowns
    # 'resource'    - type of resource needed
    # 'effect'      - not entirely certain, it's a list. index 1 appears to be scaling for base effect.
    # 'vars'        - a list of "variables" for the spell. each index is a dictionary that has the keys:
    #                 'coeff' : [coeff], 'link' : scaling type, and 'key' : someKey
    # 'cost'        - the resource cost to cast the spell.
    #
    # Not necessarily important, but e1 seems to be base damage. guessing e is short for effect. the values for it seem
    # to be stored in the 'effect' key



    # cooldownBurn - cdr in seconds. returns in X/Y/Z
    # cooldown - cdr in seconds, returns as [x, y, z]
    # vars - returns a dict with keys 'coeff', scaling type, and 'key' (not sure what this is)
    # leveltip - I thiiink this is tool tip.
    # costType - what resource this consumes
    # description - description (shocker)
    #
    # Dict looks like it goes JSONDICT['data'][keyForChampionName]['spells'][intForSpellQWER][keyForSpellAspect]
    # keyForChampionName - This should be decided by getting a list of keys from iterating through JSONDICT['data'].iteritems()
    # intForSpellQWER - This should be any value 0-3, maps to q, w, e, r
    # keyForSpellAspect - probably just going to hardcode this or something. but can be attained by for each'ing in JSONDICT['data'][keyForChampionName][intForSpellQWER]


    y = 0
    """for key, value in keys:
        print key
        print value
        print value['spells'][3]['key']
        y+=1"""

    # Give

    """a = dummy()
    b = copy.deepcopy(a)
    print ("a: ", a.getTest1())
    print ("b: ", b.getTest1())
    print "changing b's value."
    b.setTest(5)
    print("a: ", a.getTest1())"""

main()