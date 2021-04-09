# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:23:27 2021

@author: User
"""
from math import *
from Error import error

from random import seed
from random import randint

import random

import numpy as np



import myModule

import pylab


#note : changer le deuxième for car complexité de n², on peut transformer en n
def crossOverPath5(nbrElementTab1,tabPath1, tabPath2):
    newTabPathCO=[]
    for i in range(nbrElementTab1):
        newTabPathCO.append(tabPath1[i])

    for i in range(np.size(tabPath2)):
        if tabPath2[i] not in newTabPathCO:
            newTabPathCO.append(tabPath2[i])

    return newTabPathCO


def crossOverPath3(nbr,path1, path2):
    child = []
    seen = []
    temp = [-1]*len(path1)
    miss = []
    
    l = len(path1)
    for i in range(0,l,2):
        if i < l:
            child.append(path1[i])
        if i+1 < l:
            child.append(path2[i+1])
    
    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child


#note : sous forme n et non n^2
def crossOverPath(nbr,path1, path2):
    #child from the cross_over
    child=path2.copy()
    #tab of already present values (but only their coordinates)
    seen=[]
    temp = [-1]*len(path1)
    #tab of missing value in the order of path2
    miss = []
    
    #copy piece of path1 in path2
    for i in range(nbr):
        child[i] = path1[i]

    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child	


#cross over hasardeux
def crossOverPath2(path1, path2):
    #child from the cross_over
    child=path2.copy()
    #tab of already present values (but only their coordinates)
    seen=[]
    temp = [-1]*len(path1)
    #tab of missing value in the order of path2
    miss = []
    
    p1 = randint(0,len(path1))
    p2 = randint(0,len(path1))
    
    if (p1 > p2):
        tmp = p1
        p1 = p2
        p2 = tmp
        
    
    
    #copy piece of path1 in path2
    for i in range(p1,p2):
        child[i] = path1[i]

    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child






           
def matriceUnion(mat1,mat2):
    #print("matrice union")
    #print("------------mat1")
    #print(mat1)
    #print("------------mat2")
    #print(mat2)
    final_mat = list(set(mat1) | set(mat2))
    return final_mat




#crossover ERO 
def matriceConversion(path1,path2):
    mat1 = [-1]*len(path1)
    mat2 = [-1]*len(path2)
    
    
    #mat3 = [-1]*len(path3)
    matFinal = []

    
    for i in range(len(path1)):
        if i== (len(path1))-1:
            mat1[path1[i]] = [path1[len(path1)-2],path1[0]]
            mat2[path2[i]] = [path2[len(path2)-2],path2[0]]
            
            #mat3[path3[i]] = [path3[len(path3)-2],path3[0]]
            
        else :
            mat1[path1[i]] = [path1[i-1],path1[i+1]]
            mat2[path2[i]] = [path2[i-1],path2[i+1]]
            
            #mat3[path3[i]] = [path3[i-1],path3[i+1]]
  
    for i in range(len(path1)):
        matFinal.append(matriceUnion(mat1[i], mat2[i]))
    
    return matFinal

#complexité n² voir si on peut faire mieux
def crossOverERO(parent1, parent2):
    k = []
    N = parent1[0]
    
    
    
    matrice = matriceConversion(parent1, parent2)
    
    #print(matrice)
    smallest = [1,2]
    while(len(k) < len(parent1)):
        
        #print(k)
        k.append(N)
        
        for i in matrice:
            if N in i:
                i.remove(N)
    
        if len(matrice[N]) != 0:
            #print("-----")
            #print(N)
            #print(matrice[N])
            #print(len(matrice[N]))
            smallest = [matrice[N][0],len(matrice)]
            
            for i in matrice[N]:
                if ((len(matrice[i]) < smallest[1]) and (len(matrice[i]) != 0)):
                    smallest[0] = i
                    smallest[1] = len(matrice[i])
        else:
            #print("-----else")
            #print(N)
            #print(matrice[N])
            #print(len(matrice[N]))
            m = len(parent1)
            for i in range(len(matrice)):
                if ((i not in k)):
                    #print("condition remplie")
                    smallest[0] = i #random.choice([x for x in range(m) if x not in k])
                    smallest[1] = len(matrice[i])
                    i = len(matrice) + 1            
        N = smallest[0]
        
    return k
        
        






























#force brute
def crossOverLoopBRUT(nbrPath, tab):
    crossedTabs = []
    iteration = 0
    for i in range(nbrPath - len(tab)):
        for j in range(i,len(tab)):
            if(iteration + len(tab) < nbrPath):                
                iteration += 1
                crossedTabs.append(
                                        crossOverPath2(tab[i],tab[j]))
            else:
                if crossedTabs:
                    return crossedTabs
                else:
                    error("Le cross_over ne s'est fait pas fait")
                
    return crossedTabs
















#-------------------------------------ESSAYEZ EN SUPPRIMANT LA GENERATION PRECEDENTE
#-------------------------------------EN NE GARDANT QUE LES ENFANTS 
def crossOverLoop1(nbrPath, tab,Map):
    crossedTabs = []
    iteration = 0
    for i in range(nbrPath - len(tab)):
         parent1 = tab[randint(0, len(tab)-1)]
         parent2 =tab[randint(0, len(tab)-1)]
         
         child1 = crossOverPath2(parent1, parent2)
         child2 = crossOverPath2(parent2, parent1)
         child = []
         if Map.pathLength(child1) < Map.pathLength(child2):
            child = child1
         else:
            child = child2 
             
         crossedTabs.append(child)
    return crossedTabs





#par pair au hasard
def crossOverLoop(nbrPath, tab):
    crossedTabs = []
    iteration = 0
    for i in range(nbrPath - len(tab)):
         parent1 = tab[randint(0, len(tab)-1)]
         parent2 =tab[randint(0, len(tab)-1)]

         
         crossedTabs.append(child)
    return crossedTabs















#par random
def crossOverLoopRAND(nbrPath, tab):
    crossedTabs = []
    iteration = 0
    for i in range(len(tab)):
        if(randint(0,len(tab)) > i +3):
            for j in range(i,len(tab)):
                if(iteration + len(tab) < nbrPath):                
                    iteration += 1
                    crossedTabs.append(
                                        crossOverPath2(tab[i],tab[j]))
                else:
                    if crossedTabs:
                        return crossedTabs
                    else:
                        error("Le cross_over ne s'est fait pas fait")
    return crossedTabs
        


 




#mega mutation
def mutation(population,P, Map):
    mutant = []
    for i in population:
        for j in range(len(i)):
            l = random.random()*100
            #print("---")
            #print(P)
            #print(l)
            if (100*P >= l):
                #print("mutation")
                pos = randint(0,len(i)-1)
                swapPositions(i, j, pos)
        mutant.append(i);
                

    return mutant
    
    
def mutation1(population,P, Map):
    mutant = []
    best = Map.pathLength(population[0])
    prob = 0
    for i in population[1:]:
        prob = best/Map.pathLength(i)
        #print(prob)
        for j in range(len(i)):
            l = random.random()*100
            if (100*prob >= l):
                #print("mutation")
                pos = randint(0,len(i)-1)
                swapPositions(i, j, pos)
        mutant.append(i);
                

    return mutant        
    
    
















#mutation d'un chemin
def mutationPath(tabPath):
    element1 = randint(0 , len(tabPath)-1)
    element2 = randint(0 , len(tabPath)-1)
    swapPositions(tabPath, element1, element2)
    return tabPath



def mutationLoop(tab):
    for i in range(len(tab)):
        if randint(0,10) > 1:
            tab[i] = mutationPath(tab[i])
    return tab

# Swap function 
def swapPositions(tab, pos1, pos2):
    tab[pos1], tab[pos2] = tab[pos2], tab[pos1] 




#selection
def FUSS(paths,nbr):
    final = []
    chunk = floor(len(paths)/5)
    prop = floor(0.5*chunk)

    for i in range(5):
        for j in range(prop):
            final.append(paths[(chunk*i)+j][0])
        #l = random.sample(range(chunk*i, chunk*i + chunk),prop) #sans double essayer avec prob = 1/2
        #for i in l:
            #final.append(paths[i][0])
            
            
            
        
    #print("taille")
    #print(len(final))
    return final

from bisect import bisect_left

#selection
def FUSS2(paths,nbr):
    final = []
    mini = paths[0][1]
    maxi = paths[-1][1]
    intervalle = maxi-mini
    
    keys = [r[1] for r in paths]
    
    for i in range(floor(len(paths)/2)):
        l = random.uniform(mini, maxi)
        final.append(paths[bisect_left(keys,l)][0])
      

        
    return final


def hardSelector(paths,nbr):
    chosens = 0
    tab = []
    for i in range(len(paths)):
        if (chosens < nbr):
            if(randint(0,len(paths)) > i):
                chosens += 1
                tab.append(paths[i][0])
    return tab
        



def selectionPath(nbrPath, Map, bestElementsSize):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    import time
    start = time.process_time()
    
    
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    path = []
    
    
    while (iteration < 200):
        generation += 1
        
        
        tabBestPath = []
        
        
        
        
        
        best = tabPath[0][0]

        
        chosens = 0

        for i in range(len(tabPath)):
            if (chosens < bestElementsSize):
                if(randint(0,len(tabPath)) > i):
                    chosens += 1
                    tabBestPath.append(tabPath[i][0])
         
        """for i in range(bestElementsSize):
            tabBestPath.append(tabPath[i][0])"""
         
        #tabBestPath = FUSS(tabPath,bestElementsSize)
        
       #RAPPEL faire la mutation APRES le crossover et la descendanse (!) (!)
        average = 0
        minimum = Map.pathLength(tabBestPath[0])
        
        for i in tabBestPath:
            average += Map.pathLength(i)
        
        average = average/len(tabBestPath)
    
        p = (1 - ((average - minimum)/minimum))**5
        

        
        genCrossed = crossOverLoop1(nbrPath, tabBestPath,Map)

        newSet = tabBestPath[1:]
        
        genMutated = mutation(newSet,p,Map)
   
        
       
        tabBestPath = genMutated + genCrossed
        tabBestPath.append(best)
       
        
        tabPath = []
        
        
        
        
        for i in tabBestPath:
            tabPath.append([i,Map.pathLength(i)])
            
        tabPath.sort(key=lambda x:x[1])
        
        if tabPath[0][1] < bestScore:
            iteration = 0
            bestScore = tabPath[0][1]
            path = tabPath[0][0].copy()
        else:
            iteration +=1
    
        
    

    print("Taille population final")
    print(len(tabPath))
    #print("population")
    #for i in tabPath:
        #print(i)

    tabPath.sort(key=lambda x:x[1])
    print("RESULTAT FINAL")
    print(path)
    print(bestScore)
    print("TEMPS")
    print(time.process_time() - start)
    print("Nombre de Generation : ")
    print(generation)
    return path

    
    
    '''
    print("RESULTAT FINAL")
    resultat = myModule.genalgo(Map.cities, nbrPath)
    print(resultat)
    print(Map.pathLength(resultat))
    print("TEMPS")
    print(time.process_time() - start)
    
    
    return resultat'''







































#--------------------------------------------------------- POUR FAIRE DES GRAPHES




def selectionPath1(nbrPath,Map,bestElementsSize):
    print("JE FAIS DES GRAPHES")
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    tabPath = []
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    
    arrayP = []
    arrayG = []
    
    arrayS = []


    arrayERO = []
    arrayRC = []
    gen1 = 0
    gen2 = 0
    g1 = []
    g2 = []
    
    gen1 = algoGene(nbrPath,Map,tabPath,bestElementsSize,arrayERO,FUSS,crossOverLoop1)
    print("fin 1")
    gen2 = algoGene(nbrPath,Map,tabPath,bestElementsSize,arrayRC,hardSelector,crossOverLoop1)
    
    for i in range(gen1):
        g1.append(i)
        
    
    for i in range(gen2):
        g2.append(i)
    
    pylab.plot(g1, arrayERO, color= 'black' )
    pylab.plot(g2, arrayRC,color= 'red')
    pylab.show()
    
    print("generation ERO :")
    print(gen1)
    print("generation RCM :")
    print(gen2)
    
    
    print("score finale ERO:")
    print(arrayERO[-1])
    print("score finale RCM:")
    print(arrayRC[-1])



def algoGene(nbrPath, Map,tabPath, bestElementsSize,array,selector,crossOver):
    cityTab = Map.cities
    tabBestPath =[]
    print("NOUVELLE SELECTION")

    

    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    path = []
    
    while (iteration < 200):
        generation += 1
        
        
        tabBestPath = []
     
        
        #RAPPEL faire la mutation APRES le crossover et la descendanse (!) (!)
        average = 0
        minimum = tabPath[0][1]
        
        for i in tabPath:
            average += i[1]
        
        average = average/len(tabPath)
    
        p = (1 - ((average - minimum)/minimum))**10
        
        best = tabPath[0][0]

        
        chosens = 0

        for i in range(len(tabPath)):
            if (chosens < bestElementsSize):
                if(randint(0,len(tabPath)) > i):
                    chosens += 1
                    tabBestPath.append(tabPath[i][0])
                    
        #tabBestPath = selector(tabPath,bestElementsSize)
        
       
        
        
        genCrossed = crossOverRAND(nbrPath, tabBestPath)

        newSet = tabBestPath[1:] 
        
        genMutated = mutation(newSet,p,Map)
   
        
       
        tabBestPath = genMutated + genCrossed
        tabBestPath.append(best)
       
        
        tabPath = []
        
        
        
        for i in tabBestPath:
            tabPath.append([i,Map.pathLength(i)])
            
        tabPath.sort(key=lambda x:x[1])
        
        if tabPath[0][1] < bestScore:
            iteration = 0
            bestScore = tabPath[0][1]
            path = tabPath[0][0].copy()
        else:
            iteration +=1
        
        array.append(bestScore)
    
    return generation
    
        
    
    """
    print("Taille population final")
    print(len(tabPath))
    tabPath.sort(key=lambda x:x[1])
    print("RESULTAT FINAL")
    print(path)
    print(bestScore)
    print("TEMPS")
    print(time.process_time() - start)
    print("Nombre de Generation : ")
    print(generation)
    return path"""























    
    