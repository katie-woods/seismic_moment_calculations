""" python3 script to calculate required fault plane displacement given the earthquake moment
    magnitude, rectangular fault dimensions, and assumed shear modulus """

def calc_displacement_rect(fault_length, fault_width, shear_mod, mom_mag):
    """ fault length and width in kilometres, shear modulus in GPa
    """

    # calculate rectangle area in metres-squared
    area = fault_length * fault_width * 1E6

    # convert shear modulus from GPa to Pa
    shear_mod *= 1E9

    # calculate displacement in metres
    # seismic moment (Mo) = shear_mod * fault_area * displacement       in N m
    # seismic moment (Mo) = 10 ^ ( 3/2 * (moment_magnitude + 10.7 ) )   in dyne cm
    displacement = (10 ** ((3/2) * (mom_mag + 10.7))) * 1E-7 / (area * shear_mod)

    # print area, shear modulus, and displacement
    print("Area: ", area, " metres-squared")
    print("Shear modulus: ", shear_mod, " Pa")
    print("Displacement: ", displacement, " metres")
    return displacement


# calculate Mw 6.3 Eketahuna earthquake fault (11.5 by 11.5 km plane) displacement
eke_disp = calc_displacement_rect(11.5, 11.5, 30, 6.3)
