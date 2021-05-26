import math
import numpy as np


def translocation(x_translocation, y_translocation, z_translocation, **kwargs):
    coordinates = kwargs
    keys_list = coordinates.keys()
    for t in range(len(keys_list)):
        new_x = round(coordinates[keys_list[t]][0] + x_translocation, 3)
        new_y = round(coordinates[keys_list[t]][1] + y_translocation, 3)
        new_z = round(coordinates[keys_list[t]][2] + z_translocation, 3)
        coordinates[keys_list[t]] = [new_x, new_y, new_z]
    return coordinates


def x_axis_rotation(rotation_angle, **kwargs):
    coordinates = kwargs
    teta_x = [[1, 0, 0], [0, math.cos(math.radians(rotation_angle)), -math.sin(math.radians(rotation_angle))],
              [0, math.sin(math.radians(rotation_angle)), math.cos(math.radians(rotation_angle))]]
    teta_x = np.matrix(teta_x)
    keys_list = list(coordinates.keys())
    for x in range(len(keys_list)):
        coordinate_matrix = [[coordinates[keys_list[x]][0]], [coordinates[keys_list[x]][1]],
                             [coordinates[keys_list[x]][2]]]
        coordinate_matrix = np.matrix(coordinate_matrix)
        after_x_rotation = teta_x * coordinate_matrix
        coordinates[keys_list[x]] = [round(after_x_rotation.item(0), 3), round(after_x_rotation.item(1), 3),
                                     round(after_x_rotation.item(2), 3)]
    return coordinates


def y_axis_rotation(rotation_angle, **kwargs):
    coordinates = kwargs
    teta_y = [[math.cos(math.radians(rotation_angle)), 0, math.sin(math.radians(rotation_angle))], [0, 1, 0],
              [-math.sin(math.radians(rotation_angle)), 0, math.cos(math.radians(rotation_angle))]]
    teta_y = np.matrix(teta_y)
    keys_list = list(kwargs.keys())
    for y in range(len(keys_list)):
        coordinate_matrix = [[coordinates[keys_list[y]][0]], [coordinates[keys_list[y]][1]],
                             [coordinates[keys_list[y]][2]]]
        coordinate_matrix = np.matrix(coordinate_matrix)
        after_y_rotation = teta_y * coordinate_matrix
        coordinates[keys_list[y]] = [round(after_y_rotation.item(0), 3), round(after_y_rotation.item(1), 3),
                                     round(after_y_rotation.item(2), 3)]
    return coordinates


def z_axis_rotation(rotation_angle, **kwargs):
    coordinates = kwargs
    teta_z = [[math.cos(math.radians(rotation_angle)), -math.sin(math.radians(rotation_angle)), 0],
              [math.sin(math.radians(rotation_angle)), math.cos(math.radians(rotation_angle)), 0], [0, 0, 1]]
    teta_z = np.matrix(teta_z)
    keys_list = list(kwargs.keys())
    for z in range(len(keys_list)):
        coordinate_matrix = [[coordinates[keys_list[z]][0]], [coordinates[keys_list[z]][1]],
                             [coordinates[keys_list[z]][2]]]
        coordinate_matrix = np.matrix(coordinate_matrix)
        after_z_rotation = teta_z * coordinate_matrix
        coordinates[keys_list[z]] = [round(after_z_rotation.item(0), 3), round(after_z_rotation.item(1), 3),
                                     round(after_z_rotation.item(2), 3)]
    return coordinates
