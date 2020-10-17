from random import shuffle
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def gather_info():
    return render_template('form.html')

@app.route('/', methods=['POST'])  
def display_assignments():
    # request.form = ImmutableMultiDict
    # ex: {"faction1":"Faction","faction2":"Faction","link1":"on","link2":"on","player1":"Player name","player2":"Player name"}
    assignables = request.form
    players = build_player_list(assignables)
    factions = build_faction_list(assignables)
    assignments = assign_factions(players, factions)
    return render_template('index.html', assignments=assignments)

def build_player_list(players):
    player_list = []
    for key, value in players.items():
        if 'player' in key:
            player_list.append(value)
    return player_list

def build_faction_list(factions):
    faction_list = []
    for key, value in factions.items():
        if 'faction' in key:
            faction_list.append(value)
    return faction_list

def assign_factions(players, factions):        
    shuffle(factions)
    if len(factions) != len(players):
        raise Exception('The number of players and factions must match.')
    else:
        assignments = list(zip(players, factions))
    return assignments