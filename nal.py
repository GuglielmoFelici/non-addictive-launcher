import json
import sys
import launcher
from game import Game
import shutil
from util import fail
import logging

DATASOURCE_NAME = 'games.json'


shutil.copy(DATASOURCE_NAME, f'{DATASOURCE_NAME}.bak')
logging.basicConfig(level=logging.DEBUG)

with open(DATASOURCE_NAME) as dataSource:
    games = json.load(dataSource)

errorMsg = f'Specify a game from this list: \n{" ".join([game for game in games])}'
if len(sys.argv) != 2:
    fail(errorMsg)

gameName = sys.argv[1]
if gameName not in games:
    fail(errorMsg)
game = Game(games[gameName])
game = launcher.launch_game(game)
if not game:
    fail()
games[gameName].update(game.toDict())
with open(DATASOURCE_NAME, 'w') as dataSource:
    json.dump(games, dataSource, indent=4)
