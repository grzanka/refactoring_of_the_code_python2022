import magpylib as magpy
import numpy as np
import sys

def setup_coil(length_of_wire_mm : float = 400., angle_rad : float = np.pi/2, current_A : float = 100., radius_mm : float = 110.) -> magpy.Collection:
    """Setup coil with given parameters."""

    points_on_straight_part = np.linspace(0.0, length_of_wire_mm, 100)
    points_on_arc = np.linspace(0.0, angle_rad, 100)
    # print(points_on_straight_part)
    # print(points_on_arc)

    #listy/tablice punktow przewodu:
    current_angle_rad = np.pi/2-angle_rad/2
    vert1_1 = [(radius_mm*np.cos(current_angle_rad),radius_mm*np.sin(np.pi/2-angle_rad/2),0),
            (radius_mm*np.cos(np.pi/2-angle_rad/2),radius_mm*np.sin(np.pi/2-angle_rad/2),length_of_wire_mm)]

    vert1_2 = np.c_[radius_mm*np.cos(np.pi/2-angle_rad/2+points_on_arc)+points_on_arc*0,
                radius_mm*np.sin(np.pi/2-angle_rad/2+points_on_arc)+points_on_arc*0, length_of_wire_mm+points_on_arc*0]

    vert1_3 = [(-radius_mm*np.cos(np.pi/2-angle_rad/2),radius_mm*np.sin(np.pi/2-angle_rad/2),length_of_wire_mm),
            (-radius_mm*np.cos(np.pi/2-angle_rad/2),radius_mm*np.sin(np.pi/2-angle_rad/2),0)]

    vert1_4 = np.c_[radius_mm*np.cos(np.pi/2-angle_rad/2+angle_rad-points_on_arc)+points_on_arc*0,
                radius_mm*np.sin(np.pi/2-angle_rad/2+angle_rad-points_on_arc)+points_on_arc*0, points_on_arc*0]
    #przeciwna strona:

    vert2_1 = [(radius_mm*np.cos(np.pi/2-angle_rad/2),-radius_mm*np.sin(np.pi/2-angle_rad/2),0),
            (radius_mm*np.cos(np.pi/2-angle_rad/2),-radius_mm*np.sin(np.pi/2-angle_rad/2),length_of_wire_mm)]

    vert2_2 = np.c_[radius_mm*np.cos(np.pi/2-angle_rad/2+points_on_arc)+points_on_arc*0,
                -radius_mm*np.sin(np.pi/2-angle_rad/2+points_on_arc)+points_on_arc*0, length_of_wire_mm+points_on_arc*0]

    vert2_3 = [(-radius_mm*np.cos(np.pi/2-angle_rad/2),-radius_mm*np.sin(np.pi/2-angle_rad/2),length_of_wire_mm),
            (-radius_mm*np.cos(np.pi/2-angle_rad/2),-radius_mm*np.sin(np.pi/2-angle_rad/2),0)]

    vert2_4 = np.c_[radius_mm*np.cos(np.pi/2-angle_rad/2+angle_rad-points_on_arc)+points_on_arc*0,
                -radius_mm*np.sin(np.pi/2-angle_rad/2+angle_rad-points_on_arc)+points_on_arc*0, points_on_arc*0]


    #utworzenie przewodow:
    wire1_1 = magpy.current.Line(current=current_A, vertices=vert1_1)
    wire1_2 = magpy.current.Line(current=current_A, vertices=vert1_2)
    wire1_3 = magpy.current.Line(current=current_A, vertices=vert1_3)
    wire1_4 = magpy.current.Line(current=current_A, vertices=vert1_4)
    wire2_1 = magpy.current.Line(current=current_A, vertices=vert2_1)
    wire2_2 = magpy.current.Line(current=current_A, vertices=vert2_2)
    wire2_3 = magpy.current.Line(current=current_A, vertices=vert2_3)
    wire2_4 = magpy.current.Line(current=current_A, vertices=vert2_4)


    coil = magpy.Collection(wire1_1, wire1_2, wire1_3, wire1_4, wire2_1, wire2_2, wire2_3, wire2_4)
    
    return coil


def write_magnetic_field_to_file(filename : str, coil : magpy.Collection):
    """Write magnetic field to file."""

    print(f"Writing magnetic field to file: {filename}")
    f = open(filename,'w')
    # write length of wire, angle, current, radius to file
    # f.write(f"length = {length_of_wire_mm} mm, angle = {angle_rad} rad, I = {current_A} A, radius = {radius_mm} mm\n")
    for x in range (-150, 150, 2):
        for y in range (-150, 150, 2):
            for z in range (0, 400, 2):
                fx, fy, fz = magpy.getB(coil, [x,y,z])
                f.write(f"{x} {y} {z} {fx} {fy} {fz}\n")
    f.close()
    print("Done writing to file")



if __name__ == '__main__':

    args = sys.argv

    if len(args) != 2:
        print("Usage: python main.py <command>")
    else:
        command = args[1]

        coil = setup_coil(angle_rad=3*np.pi/4)
        if command == "show":
            magpy.show(coil)
        elif command == "write":
            write_magnetic_field_to_file("magnetic_field.txt", coil)
        else:
            print("Unknown command")