import hashlib
from importlib.resources import path
import os
from pickle import FALSE


class DeleteDuplicateFiles:
  def __init__(self):
    self.home_dir = os.getcwd()
    self.File_hashes = []
    self.block_size = 65536
    self.count_cleaned = 0

  # create a hash of the file
  def create_hash(self, filename:str)->str:
    filehash = hashlib.sha256()
    try:
      with open(filename, 'rb') as file:
        fileblock = file.read(self.block_size)
        while len(fileblock)>0:
          filehash.update(fileblock)
          fileblock = file.read(self.block_size)
        filehash = filehash.hexdigest()
      return filehash
    except:
      return False

  # remove the file from my computer
  def deleteFiles(self)->None:
    all_dir = [path[0] for path in os.walk(".")]
    for path in all_dir:
      os.chdir(path)
      all_files = [file for file in os.listdir() if os.path.isfile(file)]
      for file in all_files:
        filehash = self.create_hash(file)
        if not filehash in self.File_hashes:
          if filehash:
            self.File_hashes.append(filehash)
        else:
          byte_saved = os.path.getsize(file)
          self.count_cleaned+=1
          os.remove(file); filename = file.split('/')[-1]
          print(filename, '.. cleaned ')
      os.chdir(self.home_dir)
def main():
  duplicateDeletor = DeleteDuplicateFiles()
  duplicateDeletor.deleteFiles()
main() 