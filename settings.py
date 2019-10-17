from os import path
from glob import glob

ROOT_DIR = path.dirname(path.abspath(__file__))
IMG_DIR = glob(ROOT_DIR + "\\**\\img")[0]
