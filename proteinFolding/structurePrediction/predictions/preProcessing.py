import pandas as pd
import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "dataSet")

print(CUR_DIR)
print(DATA_DIR)

def pre_processing():

    list = []

    with os.scandir(DATA_DIR) as source:
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

    for i in range(21, 57):
        df.drop(i, axis=1, inplace=True)

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

    indexNames = df2[df2['comp_id'] == 'DG'].index
    df2.drop(indexNames, inplace=True)

    indexNames = df2[df2['comp_id'] == 'DA'].index
    df2.drop(indexNames, inplace=True)

    indexNames = df2[df2['comp_id'] == 'DT'].index
    df2.drop(indexNames, inplace=True)

    indexNames = df2[df2['comp_id'] == 'DC'].index
    df2.drop(indexNames, inplace=True)

    indexNames = df2[df2['comp_id'] == 'G'].index
    df2.drop(indexNames, inplace=True)

    indexNames = df2[df2['comp_id'] == 'A'].index
    df2.drop(indexNames, inplace=True)

    indexNames = df2[df2['comp_id'] == 'T'].index
    df2.drop(indexNames, inplace=True)

    indexNames = df2[df2['comp_id'] == 'C'].index
    df2.drop(indexNames, inplace=True)

    dataset = df.to_csv(DATA_DIR + '/pdb_dataset.csv', index=False)

    return dataset



pre_processing()