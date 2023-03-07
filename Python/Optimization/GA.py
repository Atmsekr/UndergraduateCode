# Genetic Algorithm
# max f(x) = x**2 x \in [0,y]
import numpy as np
import random
import math

y = 31

inf = 1e9
p_mutation = 0.99

Maxtimes = 100
Population_Size = 100
Population = []
Matingpool = []

class individual:
    def __init__(self):
        self.num = ""
        self.fx = ""
        self.bin = ""
        self.fitness = ""

def f(x):
    return x**2

def Start():
    for i in range(1,Population_Size+1):
        myrand = random.randint(0,y)
        indiv = individual()
        indiv.num = myrand
        indiv.fx = f(indiv.num)
        indiv.bin = format(indiv.num,'b')
        while len(indiv.bin)<=math.log2(y):
            indiv.bin = '0'+indiv.bin
        Population.append(indiv)
        # print(indiv.bin)
    return
 
def Fitness():
    mx,mn = -1,1e9
    for indiv in Population:
        mx = max(mx,indiv.fx)
        mn = min(mn,indiv.fx)
    # print('mx:%d,mn:%d'%(mx,mn))

    sumfitness = 0
    for indiv in Population:
        indiv.fitness = (indiv.fx-mn)/(mx-mn)
        sumfitness += indiv.fitness
        # print(indiv.fitness)
    # print('sumfitness:%lf'%sumfitness)

    lastfitness = 0
    for indiv in Population:
        indiv.fitness = indiv.fitness/sumfitness
        lastfitness += indiv.fitness
        indiv.fitness = lastfitness
        # print('lastfitness:%lf'%lastfitness)
    return

def Select():
    Matingpool.clear()
    for i in range(0,Population_Size):
        rd = random.uniform(0,1)
        for indiv in Population:
            if indiv.fitness >= rd:
                Matingpool.append(indiv)
                break
    return

def Crossover():
    for i in range(0,len(Matingpool),2):
        Crossoverpoint = random.randint(1,len(Matingpool[0].bin)-1)
        # print(Crossoverpoint)
        # print(Matingpool[i].bin,Matingpool[i+1].bin)
        i_head = Matingpool[i].bin[0:Crossoverpoint]
        i_tail = Matingpool[i].bin[Crossoverpoint:]
        iplus_head = Matingpool[i+1].bin[0:Crossoverpoint]
        iplus_tail = Matingpool[i+1].bin[Crossoverpoint:]
        Matingpool[i].bin = i_head + iplus_tail
        Matingpool[i+1].bin = iplus_head + i_tail

        # print(Matingpool[i].bin, Matingpool[i+1].bin)
    return

def Mutation():
    for i in range(0,len(Matingpool)):
        for bit in Matingpool[i].bin:
            if random.uniform(0,1) > p_mutation:
                # print(bit)
                if bit == '1':
                    bit = '0'
                else:
                    bit = '0'
                # print(bit)

def Accepting():
    Population = Matingpool

    for indiv in Population:
        indiv.num = int(indiv.bin,2)
        indiv.fx = f(indiv.num)
    
    Matingpool.clear()
    mx = -1
    mn = 1e9

def print_plot():
    mx = -1
    for indiv in Population:
        # print(indiv.num)
        # print(indiv.bin)
        mx = max(mx,indiv.fx)
    print(mx)
if __name__ == "__main__":
    Start()
    for i in range(0,Maxtimes):
        Fitness()
        Select()
        Crossover()
        Mutation()
        Accepting()
    print_plot()

    