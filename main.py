from random import randint
import sys, pygame
import DNA as genes
from functions import *

# init pygame
pygame.init()

DNA = genes.DNA(26, "genesControl").fill()
DNA_search = input("which DNA strand do you want?" + "\n")

DNA_search = int(DNA_search)

print()

print(DNA.genes[DNA_search]())

creature_A = [C,A,T]
x = 0
list_length = len(creature_A)
while x < list_length:
  print(creature_A[x]())
  x+=1
