import pandas as pd
import os

source_path = './data/'

def pre_processing():

    list = []

    with os.scandir(source_path) as source:
        for s in source:
            if s.name.endswith('.cif') and s.is_file():
                for f in source:
                    file = open(f,'r')
                    for f in file:
                        if 'ATOM' in f:
                            list.append(f)

    for l in list:
        if "'ALL ATOMS'" or "X-RAY" or "isotropic" in l:
            list.remove(l)

    df = pd.DataFrame(list)
    df = df.rename(columns={0: 'name'})
    df = df.name.str.split(expand=True)

    df.columns = ['group_PDB',
          'id',
          'symbol',
          'atom_id',
          'alt_id',
          'comp_id',
          'asym_id',
          'entity_id',
          'seq_id',
          'pdbx_PDB_ins_code',
          'Cartn_x',
          'Cartn_y',
          'Cartn_z',
          'occupancy',
          'B_iso_or_equiv',
          'formal_charge',
          'auth_seq_id',
          'auth_comp_id',
          'auth_asym_id',
          'auth_atom_id',
          'pdbx_PDB_model_num']

    dataset = df.to_csv('./data/pdb_dataset.csv', index=False)

    return dataset