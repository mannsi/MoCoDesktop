__author__ = 'mannsi'

import ntpath
import os
import subprocess
import moCo.logger as logger


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
        for command in self.commands:
            logger.get_logger().debug("Executing command '" + command + "'")
            try:
                subprocess.call(command.split(), shell=True)
            except:
                logger.get_logger().error("Unable to run command '" + command + "'", exc_info=True)
        try:
            self._delete_file()
        except:
            logger.get_logger().error("Unable to delete file '" + self.absolute_file_path + "'", exc_info=True)

    def _delete_file(self):
        os.remove(self.absolute_file_path)