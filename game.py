class Game:

    path: str
    arguments: []
    max_weekly_seconds: int
    current_weekly_seconds: int
    total_seconds: int

    def __init__(self, inputDict):
        self.__dict__.update(inputDict)

    def toDict(self):
        return {
            "path": self.path,
            "arguments": self.arguments,
            "max_weekly_seconds": self.max_weekly_seconds,
            "current_weekly_seconds": self.current_weekly_seconds,
            "total_seconds": self.total_seconds
        }
