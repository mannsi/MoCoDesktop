__author__ = 'mannsi'


import os
import glob
from moCo.command import Command


def _get_dropbox_folder_path():
    """
    Returns the default dropbox folder of the system. If there exists a better way of
    finding the dropbox path I am all for it
    """
    try:
        return os.path.join(os.path.expanduser('~'), 'Dropbox', 'MoCo')
    except:
        raise FileNotFoundError("Dropbox folder not found")


def get_commands():
    """
    Returns commands for all files in the predefined dropbox folder
    """
    dropbox_folder = _get_dropbox_folder_path()
    dropbox_files = glob.glob(os.path.join(dropbox_folder, '*'))
    commands = []
    for file in dropbox_files:
        commands.append(Command(file))
    return commands
