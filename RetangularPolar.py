#LAB001
#PEDRO HENRIQUE RIZZI

'''
CONSTRUA EM PYTHON UMA FUNÇÃO QUE TRANSFORME O NÚMERO COMPLEXO
NA FORMA RETANGULAR PARA A FORMA POLAR
'''

import numpy as np
from numpy import pi
import scipy  as sp
import matplotlib.pyplot as plt

def RetangularParaPolar(parteReal, parteImaginaria):
    retang = complex(parteReal, parteImaginaria)    
    modulo = np.hypot(retang.real, retang.imag)
    angulo = np.arctan(retang.imag/retang.real) * 180/pi

    angulo = AnalisaQuadrante(parteReal, parteImaginaria, angulo);
    
    print("Forma Polar: ", round(modulo, 2), "theta: ", round(angulo, 2))

def AnalisaQuadrante(r, i, a):
    if(r > 0): #quarto quadrante
        if(i < 0):
            a = 360 + a

    if(r < 0): #terceiro quadrante
        if(i < 0):
            a = 180 + a

    if(r < 0): #segundo quadrante
        if(i > 0):
            a = 180 + a

    return a;

def main():
    RetangularParaPolar(-2, -2);
    RetangularParaPolar(2, 2);
    RetangularParaPolar(-2, 2);
    RetangularParaPolar(2, -2);
main();
