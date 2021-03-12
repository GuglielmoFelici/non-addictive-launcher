import datetime
import logging


def fail(message: str = ""):
    if message:
        logging.error(message)
    exit(1)


def getLastMonday():
    today = datetime.date.today()
    return today - datetime.timedelta(days=today.weekday())


def prettyTime(seconds):
    return str(datetime.timedelta(seconds=seconds))
