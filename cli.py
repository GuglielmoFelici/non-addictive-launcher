import sys
import launcher
from game import Game
from util import fail
import logging
import datasource
from time import sleep

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info("Starting...")

errorMsg = f'Specify a game from this list: \n{", ".join([game for game in datasource.getGamesJson()])}\n'
gameName = sys.argv[1] if len(sys.argv) == 2 else input(errorMsg)
game = datasource.getGame(gameName)

if not game:
    fail("The game is not on the list")
game = launcher.launchGame(game)
if not game:
    fail()
else:
    datasource.saveGame(game)
print("This window will close in 10 seconds")
sleep(10)
