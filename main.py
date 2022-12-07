import magpylib as magpy
import numpy as np
#loop1 = magpy.current.Loop(current=100, diameter=400, position=(0,0,-110))
#prad w A, wymiary w mm
#loop2 = magpy.current.Loop(current=100, diameter=400, position=(0,0,+110))
#sensor = magpy.Sensor(position=(0,0,0))
#B=sensor.getB(loop1, loop2, sumup=True)
#pole w mT
#print(B)

#cewka siodlowa
#########parametry################
length_of_wire_mm = 400.0  # [mm]
angle_rad = np.pi/2
current_A = 100.0
radius_mm = 110.0
##################################

#przestrzenie liniowe (zbiory wartosci) length
points_on_straight_part = np.linspace(0.0, length_of_wire_mm, 100)
points_on_arc = np.linspace(0.0, angle_rad, 100)
print(points_on_straight_part)
print(points_on_arc)

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

magpy.show(coil)

# write data to file
filename = "coil.txt"
f = open(filename,'w')
# write length of wire, angle, current, radius to file
f.write(f"length = {length_of_wire_mm} mm, angle = {angle_rad} rad, I = {current_A} A, radius = {radius_mm} mm\n")
for x in range (-150, 150, 2):
    for y in range (-150, 150, 2):
        for z in range (0, 400, 2):
            fx, fy, fz = magpy.getB(coil, [x,y,z])
            f.write(f"{x} {y} {z} {fx} {fy} {fz}\n")
f.close()

