import subprocess
import time
from game import Game
import util


def launch_game(game: Game):
    # TODO clone
    if (game.needsReset()):
        game.reset()
    if game.current_weekly_seconds > game.max_weekly_seconds:
        print('You had too much ¯\\_(ツ)_/¯')
        return

    p = subprocess.Popen([game.path] + game.arguments)
    start = time.time()
    print(
        f'Started {game.name}, you have {util.prettyTime(game.secondsLeft())} left')
    p.wait()
    elapsed = int(time.time() - start)
    game.total_seconds += elapsed
    game.current_weekly_seconds += elapsed
    print(f'Played {game.name} for: {util.prettyTime(elapsed)}')
    print(f'Time left: {util.prettyTime(game.secondsLeft())}')
    return game
