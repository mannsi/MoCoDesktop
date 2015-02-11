
import moCo.dropbox
import time


def run(dropbox_folder=None):
    while True:
        _execute_commands(dropbox_folder)
        time.sleep(5)


def _execute_commands(dropbox_folder=None):
    commands = moCo.dropbox.get_commands(dropbox_folder)
    for command in commands:
        command.execute()


if __name__ == "__main__":
    run("E:\Dropbox")