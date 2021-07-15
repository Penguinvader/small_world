import itertools
from itertools import combinations, permutations
import requests

card_data = requests.get(
    "https://db.ygoprodeck.com/api/v7/cardinfo.php").json()

handtraps = [
    'Ash Blossom & Joyous Spring',
    'Ghost Sister & Spooky Dogwood',
    'Ghost Ogre & Snow Rabbit',
    'Ghost Belle & Haunted Mansion',
    'Ghost Reaper & Winter Cherries',
    'Skull Meister',
    'D.D. Crow',
    'Effect Veiler',
    'Wattkinetic Puppeteer',
    'PSY-Framegear Gamma',
    'Dimension Shifter',
    'Fantastical Dragon Phantazmay',
    'Ghost Mourner & Moonlit Chill',
    'Nibiru, the Primal Being',
    'Droll & Lock Bird',
    'Artifact Lancea',
    'Ally of Justice Cycle Reader',
    'Gnomaterial',
    'Retaliating "C"',
    'Contact "C"',
    'Sauravis, the Ancient and Ascended'
]


def is_monster(x): return 'Monster' in x['type']


def find(card_name):
    for card in card_data['data']:
        if card['name'].lower() == card_name.lower() and is_monster(card):
            return card
    print(card_name, 'not found!')
    return None


def is_connected(card1, card2, card3):
    return (sum(card1[x] == card2[x] for x in ['attribute', 'race', 'level', 'atk', 'def']) == 1) and (sum(card2[x] == card3[x] for x in ['attribute', 'race', 'level', 'atk', 'def']) == 1)


def searchcards():
    cname = input('Card in hand:\n')
    while not (first_card := find(cname)):
        cname = input('Enter name again:\n')
    cname = input('\nCard to search:\n')
    while not (end_card := find(cname)):
        cname = input('Enter name again:\n')

    print('\nApplicable handtraps:')
    for handtrap in [find(x) for x in handtraps]:
        if is_connected(first_card, handtrap, end_card):
            print(handtrap['name'])


def unique_main_monsters(ydk_path):
    ydk_path = ydk_path if ydk_path[-4:] == ".ydk" else ydk_path + ".ydk"
    with open(ydk_path, "r") as deck_list:
        deck = deck_list.read().split("\n")
    main_deck = []
    for j in deck:
        if j in ["#extra", "!side"]:
            break
        elif j.isnumeric():
            for i in card_data["data"]:
                if i.get("id") == int(j) and is_monster(i) and i not in main_deck:
                    main_deck.append(i)
    return main_deck


def find_trios_in_deck(deck):
    trios = []
    for trio in itertools.permutations(deck, 3):
        if(is_connected(*trio)):
            trios.append(tuple(card['name'] for card in trio))
    return trios


if __name__ == '__main__':
    if input('Handtrap search mode? y/n\n').lower() == 'y':
        searchcards()
    else:
        deck = unique_main_monsters(input('Deck name:\n'))
        trios = list(set(find_trios_in_deck(deck)))
        monsterdict = {}
        for monster in deck:
            name = monster['name']
            for trio in trios:
                if name == trio[0]:
                    if name not in monsterdict:
                        monsterdict[name] = {}
                    if trio[2] not in monsterdict[name]:
                        monsterdict[name][trio[2]] = []
                    monsterdict[name][trio[2]].append(trio[1])

        for key in monsterdict:
            print('\n' + key)
            for key2 in monsterdict[key]:
                print('    ' + key2)
                for item in monsterdict[key][key2]:
                    print('        ' + item)
