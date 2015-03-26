__author__ = 'mannsi'

import os
import subprocess
import moCo.logger as logger


class Command():
    """
    Encapsulates a MoCo command
    """

    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as f:
            self.text_commands = f.readlines()

    def execute(self):
        for text_command in self.text_commands:
            self._run_command(text_command)
            self._delete_file()

    def _run_command(self, text_command):
        logger.get_logger().debug("Executing command '" + text_command + "'")
        try:
            subprocess.call(text_command.split(), shell=True)
        except:
            logger.get_logger().error("Unable to run command '" + text_command + "'", exc_info=True)

    def _delete_file(self):
        try:
            os.remove(self.file_path)
        except:
            logger.get_logger().error("Unable to delete file '" + self.file_path + "'", exc_info=True)