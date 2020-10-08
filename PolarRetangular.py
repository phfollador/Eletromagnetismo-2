#CONVERTE UM NÚMERO COMPLEXO NA FORMA POLAR PARA RETANGULAR

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def PolarToRetangular(modulo, angulo):
	#CONVERTE CADA TERMO DA EQUAÇÃO COMPLEXA PARA O FORMATO RETANGULAR
	a = round(modulo * np.cos(np.pi * (angulo/180)), 2);
	b = round(modulo * np.sin(np.pi * (angulo/180)), 2);

	print("Forma retangular: ", complex(a, b));

def main():
	PolarToRetangular(2.83, 225);
main();
