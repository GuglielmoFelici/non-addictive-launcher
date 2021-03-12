import subprocess
import time
from game import Game


def launch_game(game: Game):
    # TODO clone
    if game.current_weekly_seconds > game.max_weekly_seconds:
        print('You had too much ¯\\_(ツ)_/¯')
        return
    print(f'{game.path} {game.arguments}')
    game.total_seconds += 1
    return game


'''
    p = subprocess.Popen([game.path] + game.arguments)
    start = time.time()
    p.wait()
    elapsed = int(time.time() - start)
    game.total_seconds += elapsed
    game.current_weekly_seconds += elapsed
    secondsLeft = max(0,
                      game.max_weekly_seconds -
                      game.current_weekly_seconds)
    print(f'You\'ve played for {elapsed} seconds ({int(elapsed/60)} minutes)')
    print(
        f'You have {secondsLeft} seconds ({int(secondsLeft/60)} minutes) left)')
    game
    '''
