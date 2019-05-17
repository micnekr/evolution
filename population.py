import DNA

class Population(object):
    """docstring for Population."""

    def __init__(self, organismsNum, genesNum, genesFunsFile):
        super(Population, self).__init__()

        # set variables
        self.genesNum = genesNum
        self.organismsNum = organismsNum
        self.genesFunsFile = genesFunsFile
        self.organisms = []

    def fill(self):
        for i in range(self.organismsNum):

            # make a DNA
            organism = DNA.DNA(self.genesNum, self.genesFunsFile).fill()

            # if list is too short
            if len(self.organisms)-1 < i:

                # add to the end
                self.organisms.append(organism)
            else:

                # else, assign values
                self.organisms[i] = organism

        return self

    def getGenes(self, index):
        if len(self.organisms) - 1 < index:
            return None
        else:
            return self.organisms[index].genes
