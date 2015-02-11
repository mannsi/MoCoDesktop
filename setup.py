__author__ = 'mannsi'

from ez_setup import use_setuptools

use_setuptools()
from setuptools import setup
from setuptools.command.install import install
from subprocess import call
from platform import system
import getpass


_system = system()


class CustomInstallCommand(install):
    """Customized setuptools install command - makes auto run auto start and owned by root."""

    def run(self):
        install.run(self)
        if _system in ('Windows', 'cli'):
            pass
        elif _system == 'Linux':
            call(["sudo", "chmod", "+x", "/etc/init.d/mo_co_autostart_linux"])
            call(["sudo", "update-rc.d", "mo_co_autostart_linux", "defaults"])
        else:
            raise RuntimeError('Unsupported system: ' + _system)


startup_folder_path = ''
startup_scripts = []

if _system == 'Windows':
    current_user = getpass.getuser()
    startup_folder_path = "C:\\Users\\" + current_user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    startup_scripts = ['moCo/mo_co_autostart_windows.bat']
elif _system == 'Linux':
    startup_folder_path = "/etc/init.d"
    startup_scripts = ['moCo/mo_co_autostart_linux']

setup(name='MoCo'
      , version='0.1.2'
      , description='Control your computer via mobile device'
      , author='mannsi'
      , author_email=''
      , url=''
      , packages=['moCo']
      , data_files=[(startup_folder_path, startup_scripts)]
      , scripts=["moCoMain.py"]
      , entry_points={"console_scripts": ["mo_co = moCoMain:run"]}
      , cmdclass={'install': CustomInstallCommand}

)