class AromatParser:
    def __init__(self, protein_info, aminoacid_name):
        self.protein_name = protein_info
        self.pdb = protein_info + '.pdb'
        self.Line = []
        self.aminoacids = []
        self.aminoacid_name = aminoacid_name
        self.coordinates = {}

    def read_file(self, file_address):
        self.aminoacid_name = str(self.aminoacid_name).upper()
        address = file_address + '/' + self.pdb
        valid_atoms = ["CG", "CD1", "CD2", "CE1", "CE2", "CZ", "NE1", "CE3", "CZ2", "CZ3", "CH2", "OH", "ND1", "NE2"]
        with open(address) as pdb_file:
            for line in pdb_file:
                atom = str(line[13:16]).replace(' ', '')
                if "ATOM" in line[0:4] and self.aminoacid_name in line[17:20] and atom in valid_atoms:
                    res_number = str(line[22:26]).replace(' ', '')
                    res_number = int(res_number)
                    if "H" in line[13:14] or res_number < 0 or res_number == 0:
                        continue
                    else:
                        self.Line.append(line)
                elif "TER" in line[0:3]:
                    break

    def isoform_check(self):
        temp_line = self.Line
        self.Line = []
        for check in range(len(temp_line)):
            if temp_line[check][16:17] == 'A' or temp_line[check][16:17] == ' ':
                self.Line.append(temp_line[check])

    def get_aminoacids(self):
        try:
            first_aminoacid = self.Line[0][17:20] + '_' + str(self.Line[0][22:26]).replace(' ', '')
            self.aminoacids.append(first_aminoacid)
            for number in range(len(self.Line)):
                info = self.Line[number][17:20] + '_' + str(self.Line[number][22:26]).replace(' ', '')
                if info != self.aminoacids[-1]:
                    self.aminoacids.append(info)
            return self.aminoacids
        except IndexError:
            return None

    def get_atoms_coordinates(self):
        n = 0
        for aminoacid in range(len(self.aminoacids)):
            temp_dic = {}
            for atom in range(n, len(self.Line)):
                info = str(self.Line[atom][17:20]) + '_' + str(self.Line[atom][22:26]).replace(' ', '')
                if info == self.aminoacids[aminoacid]:
                    atom_info = str(self.Line[atom][13:16]).replace(' ', '')
                    x = float(str(self.Line[atom][30:38]))
                    y = float(str(self.Line[atom][38:46]))
                    z = float(str(self.Line[atom][46:54]))
                    dic = {atom_info: [x, y, z]}
                    temp_dic.update(dic)
                else:
                    n = atom
                    break
            temp_coordinates = {self.aminoacids[aminoacid]: temp_dic}
            self.coordinates.update(temp_coordinates)
        return self.coordinates

    def get_centers(self):
        center = []
        for i in range(len(self.aminoacids)):
            atoms_dic = self.coordinates[self.aminoacids[i]]
            x_sum = y_sum = z_sum = 0
            atoms_keys_list = list(atoms_dic)
            for atoms in range(len(atoms_dic)):
                x_sum += atoms_dic[atoms_keys_list[atoms]][0]
                y_sum += atoms_dic[atoms_keys_list[atoms]][1]
                z_sum += atoms_dic[atoms_keys_list[atoms]][2]
            temp_center = [self.aminoacids[i], round(x_sum / len(atoms_dic), 3), round(y_sum / len(atoms_dic), 3),
                           round(z_sum / len(atoms_dic), 3)]
            center.append(temp_center)
        return center

    def get_particular_aminoacid_atoms(self, aminoacid_name, residue_number):
        aminoacid_name = str(aminoacid_name).upper()
        particular_coordinates = {}
        aminoacid_info = aminoacid_name + '_' + str(residue_number)
        coordinates_keys = list(self.coordinates.keys())
        for i in range(len(coordinates_keys)):
            if aminoacid_info == coordinates_keys[i]:
                particular_coordinates.update({coordinates_keys[i]: self.coordinates[coordinates_keys[i]]})
        return particular_coordinates

    def write_particular_aminoacid_atoms(self, aminoacid_name, residue_number):
        aminoacid_name = aminoacid_name.upper()
        string = ''
        for i in range(len(self.Line)):
            if str(self.Line[i][17:20]).replace(' ', '') == aminoacid_name \
                    and str(self.Line[i][22:26]).replace(' ', '') == str(residue_number):
                string += self.Line[i]
        if string[-1] != '\n':
            string += '\n'
        return string


