__author__ = 'mannsi'

import ntpath
import os
import subprocess
import logging
from threading import Thread


class Command():
    """
    Encapsulates a MoCo command
    """

    def __init__(self, file_path):
        self.absolute_file_path = file_path
        self.basename = ntpath.basename(file_path)
        with open(file_path) as f:
            self.commands = f.readlines()

    def execute(self):
        try:
            t = Thread(target=self._thread_execute)
            t.start()
        except:
            logging.getLogger("moco").error("Unable to run command(s) '" + str(self.commands) + "'", exc_info=True)
        try:
            self._delete_file()
        except:
            logging.getLogger("moco").error("Unable to delete file '" + self.absolute_file_path + "'", exc_info=True)

    def _thread_execute(self):
        try:
            for command in self.commands:
                subprocess.call(command.split(), shell=True)
        except:
            logging.getLogger("moco").error("Unable to run command(s) '" + str(self.commands) + "'", exc_info=True)

    def _delete_file(self):
        os.remove(self.absolute_file_path)