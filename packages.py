#import unicodedata
#import re #regex
#import os
#import unidecode
#from PIL import Image

import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        print("\nInstalling package {}...".format(package))
        pip.main(['install', package])

def run():
  for package in ['unidecode','regex','pillow','opencv-python']:
    import_or_install(package)