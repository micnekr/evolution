from random import randint
import sys, pygame
import DNA as genes
from functions import *
import population as pop

# init pygame
pygame.init()

population = pop.Population(organismsNum = 100, genesNum = 26, genesFunsFile = "genesControl").fill()

DNA_search = input("which DNA strand do you want?" + "\n")

DNA_search = int(DNA_search)

print()

print(population.getGenes(0)[DNA_search]())

creature_A = [C,A,T]
x = 0
list_length = len(creature_A)
while x < list_length:
  print(creature_A[x]())
  x+=1
