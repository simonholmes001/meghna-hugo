from Bio.PDB import *

#parser = MMCIFParser()

#structure = parser.get_structure('testOne', '/Users/simonholmes/mathisi/alkoho-platform/proteinFolding/2bvs.cif')

#print(type(structure))
#print(structure)

mmcif_dict = MMCIF2Dict('/Users/simonholmes/mathisi/alkoho-platform/proteinFolding/2bvs.cif')
