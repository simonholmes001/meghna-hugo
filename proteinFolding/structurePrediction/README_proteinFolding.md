# Intro & Set-Up

### Command line tools for downloading the protein data base (PDB) dataset

See:
- http://www.wwpdb.org/ftp/pdb-ftp-sites

To download coordinate files in PDB Exchange Format using the macromolecular Crystallographic Information File (mmCIF) run the following commands:


```bash

rsync -rlpt -v -z --delete --port=33444 \
rsync.rcsb.org::ftp_data/structures/divided/mmCIF/ ./mmCIF
```
Downloading the entire PDB data base will take approx 2 1/2 days & will require 43.94 GB of disk space.

### Data Items Describing Atomic Positions

See:
- http://mmcif.wwpdb.org/docs/tutorials/content/atomic-description.html

### Data Items Describing Molecular Entities

See:
- http://mmcif.wwpdb.org/docs/tutorials/content/molecular-entities.html

### Introduction to PDB Format

See:
- https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

