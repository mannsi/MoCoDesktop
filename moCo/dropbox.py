__author__ = 'mannsi'


import os
import glob
from moCo.command import Command


def _get_dropbox_folder_path():
    """
    Returns the default dropbox folder of the system.
    """

    try:
        return os.path.join(os.path.expanduser('~'), 'Dropbox')
    except Exception as e:
        raise FileNotFoundError("Dropbox folder not found" + str(e))


def get_commands(dropbox_folder=None):
    """
    Returns commands for all files in the predefined dropbox folder
    """
    if not dropbox_folder:
        dropbox_folder = _get_dropbox_folder_path()

    dropbox_files_path = os.path.join(dropbox_folder, 'Apps', 'MoCoDBox', 'CommandsToRun')
    if not os.path.exists(dropbox_files_path):
        return []

    dropbox_files = glob.glob(os.path.join(dropbox_files_path, '*'))
    commands = []
    for file in dropbox_files:
        commands.append(Command(file))
    return commands
