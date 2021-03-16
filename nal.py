import launcher
from game import Game
from util import fail
import logging
import datasource
from time import sleep
import ui
import glob
import os
import atexit


def exit_handler():
    # TODO consentire configurazione
    print('La console si chiuderà tra 10 secondi. Per evitare in futuro che la console si chiuda, lanciare nal.py da un terminale esterno.')
    sleep(10)


atexit.register(exit_handler)


logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info("Starting...")

for f in glob.glob('tmp/*'):
    os.remove(f)

gamesList = datasource.getGames()

ui.createUI(gamesList)
ui.runUI()

'''
if not game:
    fail("The game is not on the list")
game = launcher.launch_game(game)
if not game:
    fail()
else:
    datasource.saveGame(game)
print("This window will close in 10 seconds")
sleep(10)
'''
