import Rotation_Transition


def y_orientation_check(reference_info, *args):
    reference = str(reference_info).split('_')
    reference = reference[0]
    reference_coordinates = args[0]
    partner_coordinates = args[1]
    if 'F' == reference or 'Y' == reference:
        if reference_coordinates['CZ'][0] < 0:
            reference_coordinates = Rotation_Transition.y_axis_rotation(180, **reference_coordinates)
            partner_coordinates = Rotation_Transition.y_axis_rotation(180, **partner_coordinates)
    elif 'H' == reference:
        if reference_coordinates['CE1'][0] < 0:
            reference_coordinates = Rotation_Transition.y_axis_rotation(180, **reference_coordinates)
            partner_coordinates = Rotation_Transition.y_axis_rotation(180, **partner_coordinates)
    elif 'W' == reference:
        if reference_coordinates['NE1'][0] < 0:
            reference_coordinates = Rotation_Transition.y_axis_rotation(180, **reference_coordinates)
            partner_coordinates = Rotation_Transition.y_axis_rotation(180, **partner_coordinates)
    return reference_coordinates, partner_coordinates


def x_orientation_check(reference_info, *args):
    reference = str(reference_info).split('_')
    reference = reference[0]
    reference_coordinates = args[0]
    partner_coordinates = args[1]
    if 'F' == reference or 'Y' == reference:
        if reference_coordinates['CE2'][1] < 0:
            reference_coordinates = Rotation_Transition.x_axis_rotation(180, **reference_coordinates)
            partner_coordinates = Rotation_Transition.x_axis_rotation(180, **partner_coordinates)
    elif 'H' == reference:
        if reference_coordinates['ND1'][1] < 0:
            reference_coordinates = Rotation_Transition.x_axis_rotation(180, **reference_coordinates)
            partner_coordinates = Rotation_Transition.x_axis_rotation(180, **partner_coordinates)
    elif 'W' in reference:
        if reference_coordinates['CZ3'][1] < 0:
            reference_coordinates = Rotation_Transition.x_axis_rotation(180, **reference_coordinates)
            partner_coordinates = Rotation_Transition.x_axis_rotation(180, **partner_coordinates)
    return reference_coordinates, partner_coordinates
