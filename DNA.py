import importlib

class DNA(object):
    """docstring for DNA."""

    def __init__(self, genesNum, genesFunsFile):
        # import functions for work with genes
        genesFunsFile = importlib.import_module(genesFunsFile)

        super(DNA, self).__init__()

        # store variables
        self.genesNum = genesNum
        self.genes = []
        self.genesFunsFile = genesFunsFile
        self.fitness = 0

    def fill(self):

        # loop through all
        for i in range(self.genesNum):

            # generate a gene
            newGene = self.genesFunsFile.genGene(i)

            # if list is too short
            if len(self.genes)-1 < i:

                # add to the end
                self.genes.append(newGene)
            else:

                # else, assign values
                self.genes[i] = newGene

        return self

    def calcFitness(self):
        self.fitness = genesFunsFile.fitness(self)
        return self.fitness
