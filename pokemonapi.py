import requests as r 
import pprint
pp = pprint.PrettyPrinter(depth=4)
Pokemons = ['cranidos', 'dartrix', 'shellder', 'lurantis', 'tentacool', 'cleffa', 'swampert', 'greedent', 'quilava', 'vigoroth', 
        'vibrava', 'rattata', 'corsola', 'palpitoad', 'loudred', 'togedemaru', 'kricketot', 'impidimp', 'phantump', 'snover', ]

Pokemon_dict = {
    
}
for name in Pokemons:
    pokedata = r.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if pokedata.status_code == 200:
        pokedata = pokedata.json()
    gamedata2 = pokedata['height']
    gamedata1 = pokedata['weight']
    gamedata3 = pokedata['types'][0]['type']['name']
    gamedata4 = [v['ability']['name'] for v in pokedata['abilities']]

    if gamedata3 not in Pokemon_dict:
        Pokemon_dict[gamedata3] = {}
        Pokemon_dict[gamedata3][name] = {}
        Pokemon_dict[gamedata3][name]['height'] = gamedata2
        Pokemon_dict[gamedata3][name]['weight'] = gamedata1
        Pokemon_dict[gamedata3][name]['abilities'] = {}
        Pokemon_dict[gamedata3][name]['abilities'] = gamedata4
    else:
        Pokemon_dict[gamedata3][name] = {}
        Pokemon_dict[gamedata3][name]['height'] = gamedata2
        Pokemon_dict[gamedata3][name]['weight'] = gamedata1
        Pokemon_dict[gamedata3][name]['abilities'] = {}
        Pokemon_dict[gamedata3][name]['abilities'] = gamedata4
        
pp.pprint(Pokemon_dict)

