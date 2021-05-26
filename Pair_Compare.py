from Geometry import Reference_Parameters
import Rotation_Transition


def reference(aminoacid_info, **kwargs):
    COORDINATES = kwargs
    Reference = Reference_Parameters(aminoacid_info=aminoacid_info, **COORDINATES)
    transition = Reference.transition()
    after_transition = Rotation_Transition.translocation(transition['x_transition'], transition['y_transition'],
                                                         transition['z_transition'], **COORDINATES)
    Reference = Reference_Parameters(aminoacid_info=aminoacid_info, **after_transition)
    z_angle = Reference.z_rotation_angle()
    after_z_rotation = Rotation_Transition.z_axis_rotation(z_angle, **after_transition)
    Reference = Reference_Parameters(aminoacid_info=aminoacid_info, **after_z_rotation)
    y_angle = Reference.y_rotation_angle()
    after_y_rotation = Rotation_Transition.y_axis_rotation(y_angle, **after_z_rotation)
    Reference = Reference_Parameters(aminoacid_info=aminoacid_info, **after_y_rotation)
    x_angle = Reference.x_rotation_angle()
    after_x_rotation = Rotation_Transition.x_axis_rotation(x_angle, **after_y_rotation)
    parameters = {'transitions': transition, 'x_angle': x_angle, 'y_angle': y_angle, 'z_angle': z_angle,
                  'reference_coordinates': after_x_rotation}
    return parameters


def partner(*args):
    PARTNER_COORDINATES = args[0]
    parameters = args[1]
    after_transition = Rotation_Transition.translocation(parameters['transitions']['x_transition'],
                                                         parameters['transitions']['y_transition'],
                                                         parameters['transitions']['z_transition'],
                                                         **PARTNER_COORDINATES)
    after_z_rotation = Rotation_Transition.z_axis_rotation(parameters['z_angle'], **after_transition)
    after_y_rotation = Rotation_Transition.y_axis_rotation(parameters['y_angle'], **after_z_rotation)
    after_x_rotation = Rotation_Transition.x_axis_rotation(parameters['x_angle'], **after_y_rotation)
    return after_x_rotation

