from os import listdir, rename
from os.path import isfile, join

thisfolder = "/home/luke/Documents/eskool/tnsi/docs/annales/epreuves_pratiques/2022/"
filenames = [f for f in listdir(thisfolder) if isfile(join(thisfolder, f))]

def renomme(filename:str):
  s = filename.replace("-", "_")
  return s

def appliqueRenommage(filenames):
  for old_filename in filenames:
    rename(old_filename, renomme(old_filename))

appliqueRenommage(filenames)