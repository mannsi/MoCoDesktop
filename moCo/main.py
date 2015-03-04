
import moCo.dropbox
import time


def run(computer_id, dropbox_folder=None):
    while True:
        _execute_commands(computer_id, dropbox_folder)
        time.sleep(5)


def _execute_commands(computer_id, dropbox_folder=None):
    commands = moCo.dropbox.get_commands(computer_id, dropbox_folder)
    for command in commands:
        command.execute()


if __name__ == "__main__":
    run("Home_Windows", "E:\Dropbox")
