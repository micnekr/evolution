import importlib

class DNA(object):
    """docstring for DNA."""

    def __init__(self, genesNum, genesFunsFile):
        genesFunsFile = importlib.import_module(genesFunsFile)
        super(DNA, self).__init__()
        self.genesNum = genesNum
        self.genes = []
        self.genesFunsFile = genesFunsFile

    def fill(self):
        for i in range(self.genesNum):

            newGene = self.genesFunsFile.genGene(i)

            if len(self.genes)-1 < i:
                self.genes.append(newGene)
            else:
                self.genes[i] = newGene

        return self
