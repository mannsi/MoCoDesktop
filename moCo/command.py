__author__ = 'mannsi'

import ntpath
import os
import subprocess
from threading import Thread


class Command():
    """
    Encapsulates a MoCo command
    """

    def __init__(self, file_path):
        self.absolute_file_path = file_path
        self.basename = ntpath.basename(file_path)
        with open(file_path) as f:
            self.command = f.readline()

    def execute(self):
        try:
            t = Thread(target=self._thread_execute)
            t.start()
        except Exception as ex:
            raise Exception("Unable to run command '" + self.command + "'")
        try:
            self._delete_file()
        except:
            raise Exception("Unable to delete file '" + self.absolute_file_path + "'")

    def _thread_execute(self):
        subprocess.call(self.command.split())

    def _delete_file(self):
        os.remove(self.absolute_file_path)