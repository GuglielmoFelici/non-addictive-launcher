import tkinter as tk
from tkinter import ttk
import game
from typing import List, Union
from PIL import Image, ImageTk
import util
import launcher
import threading
import datasource


WIDTH = 500
HEIGHT = 400

root = tk.Tk()

# Assets
playButtonGreen = ImageTk.PhotoImage(Image.open(
    'icons/__play_green.png').resize((20, 20)))
playButtonBlack = ImageTk.PhotoImage(Image.open(
    'icons/__play_black.png').resize((20, 20)))


class GameViewManager:

    ''' Un gameViewManager contiene un dizionario di widget presenti nella entry di un gioco. Utilizzando questo oggetto, la UI viene aggiornata ogni volta che si modifica il dizionario. '''

    def __init__(self, game):
        self.__view = {
            'isPlaying': False
        }
        self.game = game

    def setWidget(self, key):
        return key in self.__view

    def getWidgetValue(self, key):
        return self.__view[key]

    def editWidget(self, key: 'str', val: str):
        self.__view[key] = val
        self.updateWidgets()

    def updateWidgets(self):
        # TODO cache image
        if self.setWidget('playButton'):
            if self.game.hasTimeLeft() and not self.__view['isPlaying']:
                icon = playButtonGreen
                self.__view['playButton']['cursor'] = "hand2"
                self.__view['playButton']['state'] = tk.NORMAL
            else:
                icon = playButtonBlack
                self.__view['playButton']['state'] = tk.DISABLED
            self.__view['playButton']['image'] = icon
            self.__view['playButton'].image = icon

        if self.setWidget('progressBar'):
            self.__view['progressBar']['value'] = (self.game.secondsLeft() /
                                                   self.game.max_weekly_seconds) * 100

        if self.setWidget('timeLeft'):
            self.__view['timeLeft']['text'] = f'Left: {util.prettyTime(self.game.secondsLeft())}'


gameViewManagers = {}


def launchGame(game):
    gameViewManager = gameViewManagers[game.name]
    gameViewManager.editWidget('isPlaying', True)
    gamePlayingThread = threading.Thread(
        target=launcher.launchGameWithPolling,
        args=[
            game,
            5,
            gameViewManager.updateWidgets
        ])

    def whenGameEnds():
        gameViewManager.editWidget('isPlaying', False)
        datasource.saveGame(game)

    joinerThread = threading.Thread(
        target=util.joinerThread,
        args=[
            gamePlayingThread,
            whenGameEnds
        ])
    gamePlayingThread.start()
    joinerThread.start()


def createGamesViews(games: List[game.Game], startColumn=0):
    row = 0
    for game in games:
        gameViewManager = GameViewManager(game)
        gameViewManagers[game.name] = gameViewManager
        img = ImageTk.PhotoImage(
            game.getIcon() or Image.new('RGB', (30, 30), (0, 0, 0)))
        # Game icon
        imgLabel = tk.Label(
            root,
            image=img
        )
        imgLabel.image = img  # Impedisce al garbage collector di distruggere l'immagine
        imgLabel.grid(
            row=row,
            column=startColumn,
            pady=15,
            padx=5
        )
        gameTitle = tk.Label(
            root,
            text=game.name.capitalize(),
        )
        gameTitle.grid(
            row=row,
            column=startColumn+1
        )

        root.grid_columnconfigure(startColumn+2, weight=1)  # spacing
        playButton = tk.Button(
            root,
            command=lambda: launchGame(game),
            borderwidth=0
        )
        playButton.grid(
            row=row,
            column=startColumn+3,
            padx=10
        )
        progressBar = ttk.Progressbar(
            root,
            orient=tk.HORIZONTAL,
            length=WIDTH,
            mode='determinate'
        )
        progressBar.grid(
            row=row + 1,
            column=0,
            columnspan=3,
            padx=5
        )
        timeLeft = ttk.Label(
            root,
        )
        timeLeft.grid(
            row=row+1,
            column=3,
            padx=10
        )
        gameViewManager.editWidget('title', gameTitle)
        gameViewManager.editWidget('playButton', playButton)
        gameViewManager.editWidget('progressBar', progressBar)
        gameViewManager.editWidget('icon', imgLabel)
        gameViewManager.editWidget('timeLeft', timeLeft)
        row = row + 2


def createUI(games: List[game.Game]):
    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.resizable(False, False)
    root.title('Non Addictive Launcher')
    createGamesViews(games)


def runUI():
    root.mainloop()
