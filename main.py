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
dlugosc = 400.0
rozwarcie = np.pi/2
prad = 100.0
promien = 110.0
##################################

#przestrzenie liniowe (zbiory wartosci)
ts_prosta = np.linspace(0.0, dlugosc, 100)
ts_luk = np.linspace(0.0, rozwarcie, 100)
print(ts_prosta)
print(ts_luk)

#listy/tablice punktow przewodu:
angle = np.pi/2-rozwarcie/2
vert1_1 = [(promien*np.cos(angle),promien*np.sin(np.pi/2-rozwarcie/2),0),
        (promien*np.cos(np.pi/2-rozwarcie/2),promien*np.sin(np.pi/2-rozwarcie/2),dlugosc)]

vert1_2 = np.c_[promien*np.cos(np.pi/2-rozwarcie/2+ts_luk)+ts_luk*0,
               promien*np.sin(np.pi/2-rozwarcie/2+ts_luk)+ts_luk*0, dlugosc+ts_luk*0]

vert1_3 = [(-promien*np.cos(np.pi/2-rozwarcie/2),promien*np.sin(np.pi/2-rozwarcie/2),dlugosc),
        (-promien*np.cos(np.pi/2-rozwarcie/2),promien*np.sin(np.pi/2-rozwarcie/2),0)]

vert1_4 = np.c_[promien*np.cos(np.pi/2-rozwarcie/2+rozwarcie-ts_luk)+ts_luk*0,
               promien*np.sin(np.pi/2-rozwarcie/2+rozwarcie-ts_luk)+ts_luk*0, ts_luk*0]
#przeciwna strona:

vert2_1 = [(promien*np.cos(np.pi/2-rozwarcie/2),-promien*np.sin(np.pi/2-rozwarcie/2),0),
        (promien*np.cos(np.pi/2-rozwarcie/2),-promien*np.sin(np.pi/2-rozwarcie/2),dlugosc)]

vert2_2 = np.c_[promien*np.cos(np.pi/2-rozwarcie/2+ts_luk)+ts_luk*0,
               -promien*np.sin(np.pi/2-rozwarcie/2+ts_luk)+ts_luk*0, dlugosc+ts_luk*0]

vert2_3 = [(-promien*np.cos(np.pi/2-rozwarcie/2),-promien*np.sin(np.pi/2-rozwarcie/2),dlugosc),
        (-promien*np.cos(np.pi/2-rozwarcie/2),-promien*np.sin(np.pi/2-rozwarcie/2),0)]

vert2_4 = np.c_[promien*np.cos(np.pi/2-rozwarcie/2+rozwarcie-ts_luk)+ts_luk*0,
               -promien*np.sin(np.pi/2-rozwarcie/2+rozwarcie-ts_luk)+ts_luk*0, ts_luk*0]


#utworzenie przewodow:
drut1_1 = magpy.current.Line(current=prad, vertices=vert1_1)
drut1_2 = magpy.current.Line(current=prad, vertices=vert1_2)
drut1_3 = magpy.current.Line(current=prad, vertices=vert1_3)
drut1_4 = magpy.current.Line(current=prad, vertices=vert1_4)
drut2_1 = magpy.current.Line(current=prad, vertices=vert2_1)
drut2_2 = magpy.current.Line(current=prad, vertices=vert2_2)
drut2_3 = magpy.current.Line(current=prad, vertices=vert2_3)
drut2_4 = magpy.current.Line(current=prad, vertices=vert2_4)


cewka = magpy.Collection(drut1_1, drut1_2, drut1_3, drut1_4, drut2_1, drut2_2, drut2_3, drut2_4)

magpy.show(cewka)

#zapis do pliku
f = open("cevque.txt",'w')
f.writelines("dlugosc:"+str(dlugosc)+"mm rozwarcie:"+str(rozwarcie)+" prad:"+str(prad)+"A promien:"+str(promien)+"mm\n")
for x in range (-150, 150, 2):
    for y in range (-150, 150, 2):
        for z in range (0, 400, 2):
            fx = magpy.getB(cewka, [x,y,z])[0]
            fy = magpy.getB(cewka, [x,y,z])[1]
            fz = magpy.getB(cewka, [x,y,z])[2]
            f.writelines(str(x)+" "+str(y)+" "+str(z)+" "+str(fx)+" "+str(fy)+" "+str(fz)+"\n");
f.close()

