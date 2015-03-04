
import moCo.dropbox
import moCo.logger
import time
import logging


def run(computer_id, dropbox_folder=None):
    moCo.logger.initialize_logging(logging.DEBUG)
    while True:
        _execute_commands(computer_id, dropbox_folder)
        time.sleep(5)


def _execute_commands(computer_id, dropbox_folder=None):
    commands = moCo.dropbox.get_commands(computer_id, dropbox_folder)
    for command in commands:
        command.execute()

