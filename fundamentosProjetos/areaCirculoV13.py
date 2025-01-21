#!/usr/local/bin/python3
from math import pi
import sys
import errno


def circulo(raio):
    return  pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))
        
         
if __name__ == '__main__':
    if len(sys.argv) < 2:
       help() 
    #    sys.exit(errno.EPERM)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo', area)
    

