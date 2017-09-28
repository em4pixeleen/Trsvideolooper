from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'Trs_Video_Looper',
      version           = '1.1.0',
      author            = 'Daniel Verde',
      author_email      = 'danielsv@trisonworld.com',
      description       = 'Application to turn a RPi into a dedicated looping video playback device for information displays and digital signage.',
      license           = 'GNU GPLv2',
      url               = 'https://github.com/em4pixeleen/trsvideolooper',
      install_requires  = ['pyudev'],
      packages          = find_packages())
