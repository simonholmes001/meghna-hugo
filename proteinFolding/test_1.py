from os.path import splitext
from pdbx.reader.PdbxReader import PdbxReader
from pdbx.reader.PdbxContainers import *
from sys import argv, exit

cif = open("/Volumes/LaCie/proteinFolding/structures/00/100d.cif")

pRd = PdbxReader(cif)

data = []

pRd.read(data)

cif.close()
