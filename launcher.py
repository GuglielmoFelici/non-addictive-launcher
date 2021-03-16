import subprocess
import time
from game import Game
import util
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def startGameProcess(game: Game) -> subprocess.Popen:
    # TODO clone
    if (game.needsReset()):
        game.reset()
    if not game.hasTimeLeft():
        logger.info('You had too much ¯\\_(ツ)_/¯')
        return None
    try:
        logger.info(game.path + " " + str(game.arguments))
        p = subprocess.Popen([game.path] + game.arguments)
    except FileNotFoundError as e:
        logger.error(
            f"Impossibile trovare l'eseguibile per \"{game.name}\". Verificare il database.")
        return None
    return p


def launchGameBlocking(game: Game) -> Game:
    p = startGameProcess(game)
    start = time.time()
    logger.info(
        f'Started {game.name}, you have {util.prettyTime(game.secondsLeft())} left')
    p.wait()
    elapsed = int(time.time() - start)
    game.total_seconds += elapsed
    game.current_weekly_seconds += elapsed
    logger.info(f'Played {game.name} for: {util.prettyTime(elapsed)}')
    logger.info(f'Time left: {util.prettyTime(game.secondsLeft())}')
    return game


def launchGameWithPolling(game: Game, pollRate=5, pollCallback=None) -> Game:
    p = startGameProcess(game)
    terminated = False
    while not terminated:
        try:
            start = time.time()
            p.wait(timeout=pollRate)
            terminated = True
            raise subprocess.TimeoutExpired(p.args, int(time.time() - start))
        except subprocess.TimeoutExpired as e:
            elapsed = int(time.time() - start)
            game.total_seconds += elapsed
            game.current_weekly_seconds += elapsed
            if pollCallback:
                pollCallback()
    return game
