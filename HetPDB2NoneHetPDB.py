from Bio.PDB import PDBParser, PDBIO, Select
import os


class NonHetSelect(Select):
    def accept_residue(self, residue):
        return 1 if residue.id[0] == " " else 0


if not os.path.exists('./NonHetPDBs'):
    os.mkdir('./NonHetPDBs')

dir_list = os.listdir('./PDBs/')
for i in dir_list:
    HetPDBs_dir = './PDBs/' + i
    pdb = PDBParser().get_structure(i, HetPDBs_dir)
    io = PDBIO()
    io.set_structure(pdb)
    NonHetPDBs_dir = './NonHetPDBs/' + i
    io.save(NonHetPDBs_dir, NonHetSelect())