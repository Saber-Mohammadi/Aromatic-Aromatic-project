from Aromatic_Parser import AromatParser
import Pair_Compare
import orientation_analysis


#TRP is reference and PHE is partner
#features of PHE after transportation will be write in a file named 'TRP_PHE_features.txt'

write_file = open('./PHE_PHE_features.txt', 'w')
write_file.write('PROTEIN' + '_' + 'AMINOACID' + ','
                 + 'CG_x' + ',' + 'CG_y' + ',' + 'CG_z' + ','
                 + 'CD1_x' + ',' + 'CD1_y' + ',' + 'CD1_z' + ','
                 + 'CD2_x' + ',' + 'CD2_y' + ',' + 'CD2_z' + ','
                 + 'CE1_x' + ',' + 'CE1_y' + ',' + 'CE1_z' + ','
                 + 'CE2_x' + ',' + 'CE2_y' + ',' + 'CE2_z' + ','
                 + 'CZ_x' + ',' + 'CZ_y' + ',' + 'CZ_z' + ',' + '\n')

Pairs_address = '../Pairs.txt'
pdb_file_addres = '/home/saber/refined_dataset'

data_type = 1
pairs = []
with open(Pairs_address)as pairs_file:
    for row in pairs_file:
        split_row = row.split('\t')
        protein_name = split_row[0]
        Partner = split_row[2]
        Reference = split_row[1]
        pairs.append(protein_name + ':' + Partner)
        pairs.append(protein_name + ':' + Reference)
pairs_file.close()
pairs_set = list(set(pairs))


TOTAL_COORDINATES = {}

for i in range(len(pairs_set)):
    pro_name = pairs_set[i].split(':')[0]
    aa_name = pairs_set[i].split(':')[1].split('_')[0].replace('F', 'PHE')
    aa_number = pairs_set[i].split(':')[1].split('_')[1]
    pdb = AromatParser(pro_name, aa_name)
    pdb.read_file(pdb_file_addres)
    pdb.isoform_check()
    pdb.get_aminoacids()
    pdb.get_atoms_coordinates()
    coordinates = pdb.get_particular_aminoacid_atoms(aa_name, aa_number)
    temp_coordinates = {pro_name + ':' + aa_name + '_' + aa_number: coordinates[aa_name + '_' + aa_number]}
    TOTAL_COORDINATES.update(temp_coordinates)

with open(Pairs_address)as pairs_file:
    for row in pairs_file:
        split_row = row.split('\t')
        protein_name = split_row[0]
        ref = split_row[1].replace('F', 'PHE')
        par = split_row[2].replace('F', 'PHE')
        ref_coord = TOTAL_COORDINATES[protein_name + ':' + ref]
        par_coord = TOTAL_COORDINATES[protein_name + ':' + par]
        ref_analysis = Pair_Compare.reference(ref.replace('TRP', 'F'), **ref_coord)
        temp_1st_par_coord = Pair_Compare.partner(par_coord, ref_analysis)
        ref_part_coord_after_y_check = orientation_analysis.y_orientation_check(ref.replace('PHE', 'F'),
                                                                                ref_analysis['reference_coordinates'],
                                                                                temp_1st_par_coord)

        final_coord = orientation_analysis.x_orientation_check(ref.replace('PHE', 'F'),
                                                                                ref_part_coord_after_y_check[0],
                                                                                ref_part_coord_after_y_check[1])

        write_file.write(protein_name + '_'+ ref + ',' + protein_name + '_' + par + ',' +
                         str(final_coord[data_type]['CG'][0]) + ',' + str(final_coord[data_type]['CG'][1]) + ',' + str(final_coord[data_type]['CG'][2]) +
                         ',' +
                         str(final_coord[data_type]['CD1'][0]) + ',' + str(final_coord[data_type]['CD1'][1]) + ',' + str(final_coord[data_type]['CD1'][2]) +
                         ',' +
                         str(final_coord[data_type]['CD2'][0]) + ',' + str(final_coord[data_type]['CD2'][1]) + ',' + str(final_coord[data_type]['CD2'][2]) +
                         ',' +
                         str(final_coord[data_type]['CE1'][0]) + ',' + str(final_coord[data_type]['CE1'][1]) + ',' + str(final_coord[data_type]['CE1'][2]) +
                         ',' +
                         str(final_coord[data_type]['CE2'][0]) + ',' + str(final_coord[data_type]['CE2'][1]) + ',' + str(final_coord[data_type]['CE2'][2]) +
                         ',' +
                         str(final_coord[data_type]['CZ'][0]) + ',' + str(final_coord[data_type]['CZ'][1]) + ',' + str(final_coord[data_type]['CZ'][2])  + '\n')

