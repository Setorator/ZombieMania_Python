import os
from glob import glob

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = glob(ROOT_DIR + "\\**\\img")
