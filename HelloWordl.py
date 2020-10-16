import datetime
import random
# SetParents


def find_parents(length):
    genes = []
    while len(genes) < length:
        ssize = min(length-len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, ssize))
    return ''.join(genes)


def generate_parent(length):
    return find_parents(length)
# FITNESS


def fitness(guess):
    _sum = 0
    for i in range(len(guess)):
        if (guess[i] == target[i]):
            _sum += 1
    return _sum


# Mutate
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate
    if not newGene == childGenes[index]:
        childGenes[index] = newGene
    return ''.join(childGenes)

# dISPLAY


def display(guess):
    timeDiff = datetime.datetime.now()-startTime
    fitnesres = fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitnesres, str(timeDiff)))


if '__main__' == "__main__":
    # gess Password
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    target = "Hello Wordl!"
    random.seed()
    startTime = datetime.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitnes = fitness(bestParent)
    display(bestParent)
    # First pollution
    # loop
    # -generate
    # -request fitness
    # -compares the fitness
    # -keeps the guess
    while True:
        child = mutate(bestParent)
        childFitness = fitness(child)
        if bestFitnes >= childFitness:
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitnes = childFitness
        bestParent = child
