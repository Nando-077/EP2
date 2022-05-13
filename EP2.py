from math import*
from tkinter.filedialog import SaveFileDialog
import random

#from sklearn.isotonic import check_increasing
from dados import DADOS
EARTH_RADIUS = 6371
y = []

def sorteia_pais(dic1):
    
    lista = list(dic1.keys())
    x = random.choice(lista)  

    return x

def haversine (r, fi1, y1, fi2, y2):

   x_1 = sin(((fi2-fi1)/2)*(pi/180))**2
   x_2 = cos(fi1*(pi/180))
   x_3 = cos(fi2*(pi/180))
   x_4 = sin(((y2-y1)/2)*(pi/180))**2

   dist = 2*r * asin((x_1+x_2*x_3*x_4)**0.5)
   
   return dist

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

    return dic2


dicionario = normaliza(DADOS)

#Interface
print(' ============================') 
print('|                            |')
print('| Bem-vindo ao Insper Países |')
print('|                            |')
print('==== Design de Software ====') 
print('Comandos:')
print('dica       - entra no mercado de dicas')
print('desisto    - desiste da rodada')
print('inventario - exibe sua posição')
print('Um país foi escolhido, tente adivinhar!')

#Sortear um país aleatório

lista = list(dicionario.keys())
x = random.choice(lista)

#Mostrar número de tentativas

Tentativas = 20
print('Você tem: {} ''tentativas'.format(Tentativas))

#Comprar uma dica ou chutar um país
# haver = haversine(EARTH_RADIUS,dicionario[x]['geo']['latitude'],dicionario[x]['geo']['longitude'],dicionario['chute']['latitude'],dicionario['chute']['longitude'])

for i in range(Tentativas):
    chute = input('Qual é o país?')  
    if chute != x and chute not in y and chute!= 'dica':
        Tentativas -= 1
        # y = adiciona_em_ordem(chute,haver,y)
        print(f'Voce ainda tem {Tentativas}')

    if chute == 'dica':
        print(f'Voce ainda tem {Tentativas}')
        print('Mercado de Dicas')
        print('----------------------------------------')
        print('1. Cor da bandeira  - custa 4 tentativas')
        print('2. Letra da capital - custa 3 tentativas')
        print('3. Área             - custa 6 tentativas')
        print('4. População        - custa 5 tentativas')
        print('5. Continente       - custa 7 tentativas')
        print('0. Sem dica')
        print('----------------------------------------')
        print('Escolha sua opção [0|1|2|3|4|5]: ')
        qual = int(input('qual dica?'))

        if qual == '1':
            Tentativas = Tentativas - 4
            print(f'Voce ainda tem {Tentativas}')
        if qual == '2':
            Tentativas = Tentativas - 3
            print(f'Voce ainda tem {Tentativas}')
        if qual == '3':
            Tentativas = Tentativas - 6
            print(f'Voce ainda tem {Tentativas}')
        if qual == '4':
            Tentativas = Tentativas - 5
            print(f'Voce ainda tem {Tentativas}')
        if qual == '5':
            Tentativas = Tentativas - 7
            print(f'Voce ainda tem {Tentativas}')
            