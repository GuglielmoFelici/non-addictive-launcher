import util
import datetime
import logging


class Game:

    name: str
    path: str
    arguments: []
    max_weekly_seconds: int
    current_weekly_seconds: int
    total_seconds: int
    last_reset: str  # iso-formatted date

    def __init__(self, inputDict):
        self.__dict__.update(inputDict)

    def toDict(self):
        return {
            "name": self.name,
            "path": self.path,
            "arguments": self.arguments,
            "max_weekly_seconds": self.max_weekly_seconds,
            "current_weekly_seconds": self.current_weekly_seconds,
            "total_seconds": self.total_seconds,
            "last_reset": self.last_reset
        }

    def secondsLeft(self, inMinutes=False):
        ret = max(0,
                  self.max_weekly_seconds -
                  self.current_weekly_seconds)
        return int(ret/60) if inMinutes else ret

    def reset(self):
        self.current_weekly_seconds = 0
        self.last_reset = datetime.date.today().isoformat()
        logging.info(
            f'{self.name} last_reset updated to {self.last_reset}')

    def needsReset(self):
        return datetime.date.fromisoformat(self.last_reset) < util.getLastMonday()
