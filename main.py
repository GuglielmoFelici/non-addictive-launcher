import json
import sys
import launcher
from game import Game

DATASOURCE_NAME = 'games.json'


def fail(message: str):
    print(message)
    print(
        f'Specify a game from this list: {[game for game in games]}')
    dataSource.close()
    exit(1)


dataSource = open(DATASOURCE_NAME, 'r')
games = json.load(dataSource)
dataSource.close()
dataSource = open(DATASOURCE_NAME, 'w')

errorMsg = f'Specify a game from this list: {[game for game in games]}'
if len(sys.argv) != 2:
    fail(errorMsg)

gameName = sys.argv[1]
if gameName not in games:
    fail(errorMsg)
game = Game(games[gameName])
game = launcher.launch_game(game)
if not game:
    fail('You had too much ¯\\_(ツ)_/¯')
games[gameName].update(game.toDict())
with open('games.json', 'w') as data:
    print(games[gameName], '\n', game.toDict())
    json.dump(games, data, indent=4)
data.close()
