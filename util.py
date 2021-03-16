import datetime
import logging
import threading

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def fail(message: str = ""):
    if message:
        logger.error(message)
    exit(1)


def getLastMonday():
    today = datetime.date.today()
    return today - datetime.timedelta(days=today.weekday())


def prettyTime(seconds):
    return str(datetime.timedelta(seconds=seconds))


def joinerThread(targetThread: threading.Thread, callback=None):
    targetThread.join()
    if callback:
        callback()
