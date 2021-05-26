def str_length_checker(string):
    after_point_str = string.split('.')[1]
    if len(after_point_str) < 3:
        zero = 3 - len(after_point_str)
        string += '0' * zero
    return string


def fix_atom_number(pdbformat_string):
    counter = 1
    new_string = ''
    split_string = pdbformat_string.split('\n')
    for i in range(len(split_string)):
        split_string[i] = split_string[i].strip()
        if split_string[i] != '':
            atom_number = str(counter)
            space = 7 - len(atom_number)
            atom_number = space * ' ' + atom_number
            prefix = split_string[i][0: 4] + atom_number + split_string[i][11:] + '\n'
            counter += 1
            new_string += prefix
    return new_string


def dic2pdb(aminoacid_name, aminoacid_number, chain, **kwargs):
    line = ''
    '''aminoacid_name = aminoacid_name.replace('H', 'HIS')
    aminoacid_name = aminoacid_name.replace('F', 'PHE')
    aminoacid_name = aminoacid_name.replace('Y', 'TYR')
    aminoacid_name = aminoacid_name.replace('W', 'TRP')'''
    res_number_space = 4 - len(str(aminoacid_number))
    aminoacid_number = ' ' * res_number_space + aminoacid_number
    if 'HIS' == aminoacid_name or 'H' == aminoacid_name:
        keys_list = list(kwargs)
        for i in range(len(keys_list)):
            x_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][0])))
            y_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][1])))
            z_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][2])))
            new_x = x_space * ' ' + str(kwargs[keys_list[i]][0])
            new_y = y_space * ' ' + str(kwargs[keys_list[i]][1])
            new_z = z_space * ' ' + str(kwargs[keys_list[i]][2])
            kwargs[keys_list[i]] = [str_length_checker(new_x), str_length_checker(new_y), str_length_checker(new_z)]
        atoms_list = ['CG', 'ND1', 'CD2', 'CE1', 'NE2']
        atom_type = ['C', 'N', 'C', 'C', 'N']
        for j in range(len(atoms_list)):
            if j == 0:
                line += 'ATOM         ' + atoms_list[j] + '  ' + 'HIS' + ' ' + chain + aminoacid_number + \
                        '    ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] + \
                        '                       ' + atom_type[j] + '\n'
            else:
                line += 'ATOM         ' + atoms_list[j] + ' ' + 'HIS' + ' ' + chain + aminoacid_number +  \
                        '    ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] +\
                        '                       ' + atom_type[j] + '\n'

    elif 'TRP' == aminoacid_name or 'W' == aminoacid_name:
        keys_list = list(kwargs)
        for i in range(len(keys_list)):
            x_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][0])))
            y_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][1])))
            z_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][2])))
            new_x = x_space * ' ' + str(kwargs[keys_list[i]][0])
            new_y = y_space * ' ' + str(kwargs[keys_list[i]][1])
            new_z = z_space * ' ' + str(kwargs[keys_list[i]][2])
            kwargs[keys_list[i]] = [str_length_checker(new_x), str_length_checker(new_y), str_length_checker(new_z)]
        atoms_list = ['CG', 'CD1', 'CD2', 'NE1', 'CE2', 'CE3', 'CZ2', 'CZ3', 'CH2']
        atom_type = ['C', 'C', 'C', 'N', 'C', 'C', 'C', 'C', 'C']
        for j in range(len(atoms_list)):
            if j == 0:
                line += 'ATOM         ' + atoms_list[j] + '  ' + 'TRP' + ' ' + chain + ' ' + aminoacid_number + \
                        '   ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] + \
                        '                       ' + atom_type[j] + '\n'
            else:
                line += 'ATOM         ' + atoms_list[j] + ' ' + 'TRP' + ' ' + chain + ' ' + aminoacid_number +  \
                        '   ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] +\
                        '                       ' + atom_type[j] + '\n'
    elif 'TYR' == aminoacid_name:
        keys_list = list(kwargs)
        for i in range(len(keys_list)):
            x_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][0])))
            y_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][1])))
            z_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][2])))
            new_x = x_space * ' ' + str(kwargs[keys_list[i]][0])
            new_y = y_space * ' ' + str(kwargs[keys_list[i]][1])
            new_z = z_space * ' ' + str(kwargs[keys_list[i]][2])
            kwargs[keys_list[i]] = [str_length_checker(new_x), str_length_checker(new_y), str_length_checker(new_z)]
        atoms_list = ['CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH']
        atom_type = ['C', 'C', 'C', 'C', 'C', 'C', 'O']
        for j in range(len(atoms_list)):
            if j == 0:
                line += 'ATOM         ' + atoms_list[j] + '  ' + 'TY0' + ' ' + chain + ' ' + aminoacid_number + \
                        '   ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] + \
                        '                       ' + atom_type[j] + '\n'
            elif j == 5 or j == 6:
                line += 'ATOM         ' + atoms_list[j] + '  ' + 'TY0' + ' ' + chain + ' ' + aminoacid_number + \
                        '   ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] + \
                        '                       ' + atom_type[j] + '\n'
            else:
                line += 'ATOM         ' + atoms_list[j] + ' ' + 'TY0' + ' ' + chain + ' ' + aminoacid_number +  \
                        '   ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] +\
                        '                       ' + atom_type[j] + '\n'
    elif 'PHE' == aminoacid_name or 'F' == aminoacid_name:
        keys_list = list(kwargs)
        for i in range(len(keys_list)):
            x_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][0])))
            y_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][1])))
            z_space = 8 - len(str_length_checker(str(kwargs[keys_list[i]][2])))
            new_x = x_space * ' ' + str(kwargs[keys_list[i]][0])
            new_y = y_space * ' ' + str(kwargs[keys_list[i]][1])
            new_z = z_space * ' ' + str(kwargs[keys_list[i]][2])
            kwargs[keys_list[i]] = [str_length_checker(new_x), str_length_checker(new_y), str_length_checker(new_z)]
        atoms_list = ['CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ']
        atom_type = ['C', 'C', 'C', 'C', 'C', 'C']
        for j in range(len(atoms_list)):
            if j == 0 or j == 5:
                line += 'ATOM         ' + atoms_list[j] + '  ' + 'PHE' + ' ' + chain + ' ' + aminoacid_number + \
                        '   ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] + \
                        '                       ' + atom_type[j] + '\n'
            else:
                line += 'ATOM         ' + atoms_list[j] + ' ' + 'PHE' + ' ' + chain + ' ' + aminoacid_number + \
                        '   ' + kwargs[atoms_list[j]][0] + kwargs[atoms_list[j]][1] + kwargs[atoms_list[j]][2] + \
                        '                       ' + atom_type[j] + '\n'
    else:
        line = 0
    return line


def sort_list(*args):
    sorted_list = []
    for i in range(len(args)):
        first_aa_info = args[i][0].split(':')[1]
        second_aa_info = args[i][1].split(':')[1]
        if int(first_aa_info.split('_')[1]) > int(second_aa_info.split('_')[1]):
            sorted_list.append([args[i][1], args[i][0]])
    return sorted_list