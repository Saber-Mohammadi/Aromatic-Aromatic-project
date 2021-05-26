import math


class Reference_Parameters:
    def __init__(self, aminoacid_info, **kwargs):
        self.aminoacid_name = str(aminoacid_info).split('_')
        self.aminoacid_name = self.aminoacid_name[0]
        self.coordinates = kwargs
        
    def transition(self):
        try:
            cg_coordinates = {'x': self.coordinates['CG'][0], 'y': self.coordinates['CG'][1],
                              'z': self.coordinates['CG'][2]}
            x_transition = -cg_coordinates['x']
            y_transition = -cg_coordinates['y']
            z_transition = -cg_coordinates['z']
            return {'x_transition': x_transition, 'y_transition': y_transition, 'z_transition': z_transition}
        except KeyError:
            print 'Gama carbon could not be found'

    def x_rotation_angle(self):
        rotation_angle = None
        if 'F' == self.aminoacid_name or 'Y' == self.aminoacid_name or 'H' == self.aminoacid_name:
            try:
                rotation_angle = math.degrees(math.atan(self.coordinates['CE1'][2] / self.coordinates['CE1'][1]))
            except ZeroDivisionError:
                rotation_angle = 90
        elif 'H' == self.aminoacid_name:
            try:
                rotation_angle = math.degrees(math.atan(self.coordinates["CE1"][2] / self.coordinates["CE1"][1]))
            except ZeroDivisionError:
                rotation_angle = 90
        elif 'W' == self.aminoacid_name:
            try:
                rotation_angle = math.degrees(math.atan(self.coordinates['CE2'][2] / self.coordinates['CE2'][1]))
            except ZeroDivisionError:
                rotation_angle = 90
        if rotation_angle >= 0:
            return -rotation_angle
        elif rotation_angle <= 0:
            return abs(rotation_angle)

    def y_rotation_angle(self):
        rotation_angle = None
        if 'F' == self.aminoacid_name or 'Y' == self.aminoacid_name:
            try:
                rotation_angle = math.degrees(math.atan(self.coordinates['CZ'][2] / self.coordinates['CZ'][0]))
            except ZeroDivisionError:
                rotation_angle = 90
        elif 'H' == self.aminoacid_name:
            ne2_ce1_bond_x = (self.coordinates['NE2'][0] + self.coordinates['CE1'][0]) / 2
            ne2_ce1_bond_z = (self.coordinates['NE2'][2] + self.coordinates['CE1'][2]) / 2
            try:
                rotation_angle = math.degrees(math.atan(ne2_ce1_bond_z / ne2_ce1_bond_x))
            except ZeroDivisionError:
                rotation_angle = 90
        elif 'W' == self.aminoacid_name:
            ne1_ce2_bond_x = (self.coordinates['NE1'][0] + self.coordinates['CE2'][0]) / 2
            ne1_ce2_bond_z = (self.coordinates['NE1'][2] + self.coordinates['CE2'][2]) / 2
            try:
                rotation_angle = math.degrees(math.atan(ne1_ce2_bond_z / ne1_ce2_bond_x))
            except ZeroDivisionError:
                rotation_angle = 90
        return rotation_angle

    def z_rotation_angle(self):
        rotation_angle = None
        if 'F' == self.aminoacid_name or 'Y' == self.aminoacid_name:
            try:
                rotation_angle = math.degrees(math.atan(self.coordinates['CZ'][1] / self.coordinates['CZ'][0]))
            except ZeroDivisionError:
                rotation_angle = 90
        elif 'H' == self.aminoacid_name:
            ne2_ce1_bond_x = (self.coordinates['NE2'][0] + self.coordinates['CE1'][0]) / 2
            ne2_ce1_bond_y = (self.coordinates['NE2'][1] + self.coordinates['CE1'][1]) / 2
            try:
                rotation_angle = math.degrees(math.atan(ne2_ce1_bond_y / ne2_ce1_bond_x))
            except ZeroDivisionError:
                rotation_angle = 90
        elif 'W' == self.aminoacid_name:
            ne1_ce2_bond_x = (self.coordinates['NE1'][0] + self.coordinates['CE2'][0]) / 2
            ne1_ce2_bond_y = (self.coordinates['NE1'][1] + self.coordinates['CE2'][1]) / 2
            try:
                rotation_angle = math.degrees(math.atan(ne1_ce2_bond_y / ne1_ce2_bond_x))
            except ZeroDivisionError:
                rotation_angle = 90
        if rotation_angle >= 0:
            return -rotation_angle
        elif rotation_angle <= 0:
            return abs(rotation_angle)
