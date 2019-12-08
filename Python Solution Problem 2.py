# machine problem 2

import numpy as np
import math as math
def circle(x1, y1, x2, y2, x3, y3): 
    
    f1 = 1
    rhs1 = (x1**2) + (y1**2)
    
    f2 = 1
    rhs2 = (x2**2) + (y2**2)
    
    f3 = 1
    rhs3 = (x3**2) + (y3**2)
    
    #solve Dx, Ey, F
    a = np.array([(x1, y1, f1), (x2, y2, f2), (x3, y3, f3)])
    d = np.array([(rhs1, y1, f1), (rhs2, y2, f2), (rhs3, y3, f3)])
    e = np.array([(rhs1, x1, f1), (rhs2, x2, f2), (rhs3, x3, f3)])
    f = np.array([(rhs1, x1, y1), (rhs2, x2, y2), (rhs3, x3, y3)])
    
    a2 = np.linalg.det(a)
    d2 = np.linalg.det(d)
    e2 = np.linalg.det(e)
    f2 = np.linalg.det(f)
    
    d3 = round((-d2 / a2),2)
    e3 = round((e2 / a2),2)
    f3 = round((-f2 / a2),2)

    # solving for center of circle 
    h = round((d2 / (a2*2)),2)
    k = round(-e2 / (a2*2),2)
    
    # solving for radius of circle
    r = ((h - x1)**2) + ((k - y1)**2)
    radius = round(math.sqrt(r), 2)
      
    
    # print results
    print ('The center of the circle is at: (', h, ' , ', k, ')')
    print ('The radius of the circle is: ', radius, 'units')
    print ('The vector [D, E, F]:     [', d3, ', ', e3, ', ', f3, ']' )