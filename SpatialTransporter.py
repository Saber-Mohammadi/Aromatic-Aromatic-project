import sys
sys.path.insert(0, r'C:\Users\saber\PycharmProjects\BioPythonPDBParser\Orientation_modules')
import Pair_Compare
import orientation_analysis


def Transporter(RefName, *args):
    RefCoords = args[0]
    ParCoords = args[1]
    ref_analysis = Pair_Compare.reference(RefName, **RefCoords)
    partner_coords = Pair_Compare.partner(ParCoords, ref_analysis)
    ref_part_coord_after_y_check = orientation_analysis.y_orientation_check(RefName,
                                                                            ref_analysis['reference_coordinates'],
                                                                            partner_coords)

    final_coord = orientation_analysis.x_orientation_check(RefName, ref_part_coord_after_y_check[0],
                                                           ref_part_coord_after_y_check[1])
    return final_coord