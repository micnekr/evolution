from functions import *
from random import choice

# all genes
genes = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

def randomOf(list):
    return choice(list)

def genGene(index):
    #return randomOf(genes)
    return genes[index]
