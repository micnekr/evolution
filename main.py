from random import randint
import sys, pygame
from functions import *

# init pygame
pygame.init()

DNA = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
DNA_search = input("which DNA strand do you want?" + "\n")

DNA_search = int(DNA_search)

print()

print(DNA[DNA_search]())

creature_A = [C,A,T]
x = 0
list_length = len(creature_A)
while x < list_length:
  print(creature_A[x]())
  x+=1
