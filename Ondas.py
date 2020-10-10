#LAB001
#PEDRO HENRIQUE RIZZI

'''
CRIE UM PROGRAMA QUE FAÇA O ITEM C DO EXEMPLO 10.1 DO LIVRO
'''

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def main():
    Fs = (10**8);
    l = 2*pi/(0.333);
    T = l/(3*(10**8));
    
    x = np.arange(-1*(l*1.5), l*1.5, l/100);
    
    t = 0;
    E1 = 50*np.cos(Fs*t + (0.333)*x);#esboçando a onda em t = 0
    
    t = T/4;
    E2 = 50*np.cos(Fs*t + (0.333)*x);#esboçando a onda em T/4
    
    t = T/2;
    E3 = 50*np.cos(Fs*t + (0.333)*x);#esboçando a onda em T/2

    fig = plt.figure()    
    ax1 = fig.add_subplot(3,1,1)
    ax1.plot(x, E1, 'orange', linewidth = 6, label = "E1 = 50 * cos(B*x)")
    plt.xlabel("Eixo X"); plt.ylabel("Eixo Y"); ax1.legend(); plt.axvline(x=0, color="k");

    ax2 = fig.add_subplot(3,1,2)
    ax2.plot(x, E2, 'c-', linewidth = 6, label = "E2 = 50 * cos(B*x + pi/4)")
    plt.xlabel("Eixo X"); plt.ylabel("Eixo Y"); ax2.legend(); plt.axvline(x=0, color="k");

    ax3 = fig.add_subplot(3,1,3)
    ax3.plot(x, E3, 'y', linewidth = 6, label = "E3 = 50 * cos(B*x + pi/2)")
    plt.xlabel("Eixo X"); plt.ylabel("Eixo Y"); ax3.legend(); plt.axvline(x=0, color="k");
    
    plt.show()
    
main();
