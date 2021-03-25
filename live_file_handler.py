import time
import subprocess
from datetime import datetime, timedelta

from watchdog.events import FileSystemEventHandler
from env import SOCKET

class LiveFileHandler(FileSystemEventHandler):
    """
    Watch a file change a emit an websocket event
    """
    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()
        f = subprocess.check_output(['tail', '-1', event.src_path])
        print(f)
        SOCKET.emit(f)



