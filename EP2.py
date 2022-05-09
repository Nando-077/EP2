print ('nando')
print ('japa')

from math import*

def haversine (r, fi1, y1, fi2, y2):

   x_1 = sin(((fi2-fi1)/2)*(pi/180))**2
   x_2 = cos(fi1*(pi/180))
   x_3 = cos(fi2*(pi/180))
   x_4 = sin(((y2-y1)/2)*(pi/180))**2

   d = 2*r * asin((x_1+x_2*x_3*x_4)**0.5)
   
   return d

def adiciona_em_ordem(np, dist, lista):

    x = [np, dist]
    t = len(lista)
    lx = []
    i = 0

    if t == 0:
        lx.append(x)

    else:
        while i != t :
            
            y = lista[i]
            k = y[1]

            if dist > k:
                lx.append(y)
                i = i+1
            
            else:
                lx.append(x)
                
                while i != t :
                    y = lista[i]
                    lx.append(y)
                    i = i+1
    return lx