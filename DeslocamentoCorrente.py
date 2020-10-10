#LAB001
#PEDRO HENRIQUE RIZZI

'''
CRIE UM PROGRAMA QUE FAÇA O ITEM C DO EXERCÍCIO PRÁTICO 10.1 DO LIVRO
'''

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def main():
    Fs = (10**8);
    l = 2*pi/(0.333);
    T = l/(3*(10**8));
    
    x = np.arange(-1*(l*0.3), l*0.7, l/100);#criando o vetor de tempo    
    
    t1 = 3.92*(10**-9);#esboçando a onda no tempo t1
    H = 0.1*np.cos(2*(Fs*t1) - (2/3)*x);

    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.plot(x, H, 'c-', linewidth = 6, label = "E = 50 * cos(B*x)")
    plt.xlabel("Eixo X"); plt.ylabel("Eixo Y"); ax1.legend();

    plt.show();

main();

