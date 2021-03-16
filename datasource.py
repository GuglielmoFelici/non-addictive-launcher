import json
from game import Game
import shutil

DATASOURCE_NAME = 'sviluppo.json'

shutil.copy(DATASOURCE_NAME, f'{DATASOURCE_NAME}.bak')
with open(DATASOURCE_NAME) as dataSource:
    games = json.load(dataSource)


def getGame(gameName: str):
    if gameName not in games:
        return None
    return Game(games[gameName])


def saveGame(game: Game):
    games[game.name].update(game.toDict())
    with open(DATASOURCE_NAME, 'w') as dataSource:
        json.dump(games, dataSource, indent=4)


def getGames():
    return [Game(games[name]) for name in games]


def getGamesJson():
    return games
