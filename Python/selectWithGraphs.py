#import numpy as np
import random

from matplotlib import pyplot as plt



comparesArray1 = []
comparesArray2 = []
sampleSize = []




#Could turn sorts into functions

#this code clculates the compares to see the efficiency of my sort and
#plots a graph




for sample in range(0, 50):
    sampleSize.append(sample)
    testArray = []
    num = sample
    for i in range(num):
        testArray.append(random.randrange(0,101))
    
    
    array1 = testArray.copy()
    
    array2 = testArray.copy()
    
    #Normal selection sort
    
    numCompares1 = 0
    
    for i in range(len(array1)):
        minInd = i
        
        for j in range(i+1, len(array1)):
            numCompares1 = numCompares1 + 1
            if (array1[minInd] > array1[j]):
                minInd = j
        array1[i], array1[minInd] = array1[minInd], array1[i]
        
    comparesArray1.append(numCompares1)
    
    
    
    
    
    #My selection sort with tournaments
    
    numCompares2 = 0
    start = 0
    end = len(array2)
    size = len(array2)
    i = start
    
    while(start <= i < end ):
        #for i in range( end//2 ):
        # also works
        #perhaps even better
        numCompares2 = numCompares2 + 1
        if(size % 2 == 0):
            numCompares2 = numCompares2 + 1
            
            if(array2[start] < array2[start + 1]):
                maxInd = start + 1
                minInd = start
                
                
                
            else:
                maxInd = start
                minInd = start + 1
                
                
                
            checkStart = start + 2
            
        else:
            maxInd = start
            minInd = start
            
            
            
            checkStart = start + 1
            
        while(checkStart < end):
            
        # for checkStart2 in range(checkStart, end - 1, 2)
        
        #This works now
        # To get to work change the next checkstarts to checkStart2
        # also remove the incrementation
            
            
            numCompares2 = numCompares2 + 3
            
            if (array2[checkStart] < array2[checkStart + 1]):
                
                if(array2[checkStart] < array2[minInd]):
                    minInd = checkStart
                    
                    # change to checkstart2 for foorloop
                    
                    
                if (array2[checkStart + 1] > array2[maxInd]):
                    maxInd = checkStart + 1
                    
            else:
                if(array2[checkStart + 1] < array2[minInd]):
                    minInd = checkStart + 1
                    
                    
                if(array2[checkStart] > array2[maxInd]):
                    maxInd = checkStart
                    
                    
            checkStart = checkStart + 2
            # remove this for a for loop
            
            
        numCompares2 = numCompares2 + 2
        
        if (minInd == end - 1 and maxInd == start ):
            array2[start], array2[minInd] = array2[minInd], array2[start]
        elif (minInd == end - 1 ) :
            array2[start], array2[minInd] = array2[minInd], array2[start]
            array2[end - 1], array2[maxInd] = array2[maxInd], array2[end - 1]
        else :
            array2[end - 1], array2[maxInd] = array2[maxInd], array2[end - 1]
            array2[start], array2[minInd] = array2[minInd], array2[start]
        
            
            
            
        start = start + 1
        end = end - 1
        
        size = size - 2
        i = i + 1
        
        
        
        
    comparesArray2.append(numCompares2)
    
    
    
    
    
    
#plot graphs
    
    
plt.plot(sampleSize, comparesArray1, label = "Normal Selection Sort")

plt.plot(sampleSize, comparesArray2, label = "My Selection Sort") 
        
plt.legend()

plt.xlabel("Elements in array")

plt.ylabel("Number of comparrisons")

plt.show()
        
    
    
         




    


