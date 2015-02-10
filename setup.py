__author__ = 'mannsi'

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup
from setuptools.command.install import install
from subprocess import call


class CustomInstallCommand(install):
    """Customized setuptools install command - makes auto run auto start and owned by root."""
    def run(self):
        install.run(self)
        call(["sudo", "chmod", "+x", "/etc/init.d/mo_co_autostart"])
        call(["sudo", "update-rc.d", "mo_co_autostart", "defaults"])

setup(name='MoCo'
      , version='0.1.2'
      , description='Control your computer via mobile device'
      , author='mannsi'
      , author_email=''
      , url=''
      , packages=['moCo']
      , data_files=[('/etc/init.d', ['moCo/mo_co_autostart'])]
      , scripts=["moCoMain.py"]
      , entry_points={"console_scripts": ["mo_co = moCoMain:run"]}
      , cmdclass={'install': CustomInstallCommand}

)