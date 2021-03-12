
import sys
import launcher
from game import Game
from util import fail
import logging
import datasource

logging.basicConfig(level=logging.DEBUG)

errorMsg = f'Specify a game from this list: \n{" ".join([game for game in datasource.getGames()])}'
if len(sys.argv) != 2:
    fail(errorMsg)

game = datasource.getGame(sys.argv[1])
if not game:
    fail(errorMsg)
game = launcher.launch_game(game)
if not game:
    fail()
else:
    datasource.saveGame(game)
