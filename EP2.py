
from math import*
from tkinter.filedialog import SaveFileDialog
import random
import dados
d = dados.DADOS
EARTH_RADIUS = 6371

def sorteia_pais(dic1):
    
    lista = list(dic1.keys())
    x = random.choice(lista)  

    return x

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

def esta_na_lista(pais,lista):

    contador = 0

    for i in range(len(lista)):
        if pais == lista[i][0]:
            contador += 1
    
    if contador > 0:
        return True
    else:
        return False

def sorteia_letra(palavra,r):  
    
    lista = []
    a = ['.', ',', '-', ';', ' ']

    for i in range(len(palavra)):
        if palavra[i] not in a and palavra[i] not in r:
            lista.append(palavra[i])

    x = random.choice(lista)

    return x

def normaliza(d):

    dic2 = {}

    for continente in d:
        for paises in d[continente]:
            dic2[paises] = d[continente][paises]
            dic2[paises]['continente'] = continente
    print (dic2)       
    return dic2
