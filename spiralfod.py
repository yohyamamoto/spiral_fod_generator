from numpy import pi, cos, sin, arccos, arange
import mpl_toolkits.mplot3d
import matplotlib.pyplot as pp


def spiral(num_orb,center):
    for jj in range(0, len(num_orb)):
        match jj:
            case 0:
                radius = 0.0
            case 1:
                radius = -1.0
            case 2:
                radius = 2.0

        num_pts = num_orb[jj]
        indices = arange(0, num_pts, dtype=float) + 0.5
        
        phi = arccos(1 - 2*indices/num_pts)
        theta = pi * (1 + 5**0.5) * indices
    
        x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi);

        pp.figure().add_subplot(111, projection='3d').scatter(x, y, z);
        #pp.show()

        for ii in range(0, num_pts):
            #print("Xx", x[ii]*radius+center[0], y[ii]*radius+center[1], z[ii]*radius+center[2])
            print(x[ii]*radius+center[0], y[ii]*radius+center[1], z[ii]*radius+center[2])


#User inputs
#no. of orbitals in first, second, third shells
num_orb_a = 1, 4, 9
num_orb_b = 1, 4, 3
#center position
pos = 0.0, 0.0, 0.0


print(sum(num_orb_a), sum(num_orb_b))
spiral(num_orb_a, pos)
spiral(num_orb_b, pos)
