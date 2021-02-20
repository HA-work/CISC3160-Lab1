#import numpy as np
import random

from matplotlib import pyplot as plt

#This code shows my sort can work with any number
# I will make another code that compares my code with selection sort

#This code serves more as a proof of concept

print("This is a program to test my \
selection sort against normal selection sort")
#Normal selection sort selects the largest value one at a time
#I want to do one that uses tournaments to see if it is better

#I wanted to create a function that will randomly generate
# an amout of numbers that you specify with a limit you specify
#It turn out there already exists such a function though
# I guess that is why Python libraries are so useful to data science

# There are 2 ways to do this
# One with random and the other with numpy


# multiply by 100 and truncate

#num = int(input("Enter the number of elements you want in the array:    "))
#array1 = np.random.rand(num)
#print("The array we will be working with is:   " , array1)

#Should reverse order
# For worst case scenario



#for i in range(len(array1)):
#    array1[i] = int(array1[i] * 100)
    
   
#Getting ints from 0 to 100

#array1 = array1.astype(int)
#converted the floats to ints


# Random is easier






#num = random.randrange(2,10)

#At least 2 elements is good because 0 and 1 are trivially sorted

#Can fix the array size or set it randomly

#num = 5000
num = 5
#num = 5000

# 16

# from 16 and up my sorting method requires less
# compares than normal selection sort
# Can try to plot these


# Can also ask a user for input


testArray = []

#randomizer

for i in range(num):
    testArray.append(random.randrange(0,101))



array1 = testArray.copy()
array2 = testArray.copy()


#print(testArray)




testArray.sort()

#Could reverse the arrays for worst case performance


#array1 = array1[::-1]

#Will always do the same number of comparrisons though


#Use the built in sort to have a properly sorted array as refrence

#print(testArray)
#print()


print("Normal Selection sort")
print("Starting array")
print(array1)


numCompares1 = 0

#Normal selection sort
#Count the number of compares
#Follows the formula ) 0.5 * (n^2 - n)

#Technically doesnt a for loop have compares?

for i in range(len(array1)):
    minInd = i
    
    for j in range(i+1, len(array1)):
        numCompares1 = numCompares1 + 1
        if (array1[minInd] > array1[j]):
            minInd = j
           
        
    array1[i], array1[minInd] = array1[minInd], array1[i]
    
  
print ("Final array")
print(array1)
print("Number of compares needed:   ", numCompares1) 
    


print()




















#array1 = [19, 5, 4, 6, 0]
#The test array I used before moving onto random

#array1 = [19, 5, 4, 84, 0]

#could use seeds






print("My Selection sort with tournaments")
print("Starting array")

#I did an inplace sort and an out of place sort


print(array2)

#My method
#Mine can do inplace sorting




numCompares2 = 0



start = 0
end = len(array2)

#Could make end - 1
#so we relate the index numbers

size = len(array2)

arrayToPut = [None] * size

arrayToPut2 = [None] * size
# Out of place sort
# less space efficient than in place sorting


i = start

while(start <= i < end ):  
    #for i in range( end//2 ):
    #Also works
    #possible even better since while
    # seems like a comparisson check and for is not
    
#while(start <= i < end and start != end ):
    
# The last element should be sorted

#Needed a while loop as a for loop would not work
# would not let me update the range after subsequent runs
# can probably fix this my making it go through half the size of the loop instead
# of trying to increment and adjust start and end
# for i in range(start, size/2)
    
    
        
    numCompares2 = numCompares2 + 1
    
    if(size % 2 == 0):
        
        
        
        numCompares2 = numCompares2 + 1
        
        if(array2[start] < array2[start + 1]):
            
            
            maxInd = start + 1
            minInd = start
            
            maxVal = array2[start + 1]
            minVal = array2[start]
        
        else:
             
            maxInd = start
            minInd = start + 1
            
            maxVal = array2[start]
            minVal = array2[start + 1]
            
            
            
            
            
        checkStart = start + 2
            
    
            
        
    
    else:
        
            
        maxInd = start
        minInd = start
        
        maxVal = array2[start]
        minVal = array2[start]
            
        checkStart = start + 1
        
    while(checkStart < end):
        
        # for checkStart2 in range(checkStart, end - 1, 2)
        
        #This works now
        # To get to work change the next checkstarts to checkStart2
        
        
        
        #while(checkStart < end):
        
        #having some trouble converting this to a for loop
        
        # are fors and whiles comparissons?
        
        # find a way to convert to for
        
        numCompares2 = numCompares2 + 3
        
        #maybe find a way to not compare for start = end?
        
        #Are while loops comparissons?
        
        
        
        #remove 2
        
        
            
        if (array2[checkStart] < array2[checkStart + 1]):
            
            if(array2[checkStart] < array2[minInd]):
                
                minInd = checkStart
                minVal = array2[checkStart]
                
            if (array2[checkStart + 1] > array2[maxInd]):
                maxInd = checkStart + 1
                maxVal = array2[checkStart + 1]
                
        else:
            
            if(array2[checkStart + 1] < array2[minInd]):
                
                minInd = checkStart + 1
                minVal = array2[checkStart + 1]
            if(array2[checkStart] > array2[maxInd]):
                maxInd = checkStart
                maxVal = array2[checkStart]
            
            
            
           
        checkStart = checkStart + 2
        # if for loop remove this
            
            
    
    
    #print(maxVal, minVal)
    
    arrayToPut[start] = array2[minInd]
    arrayToPut[end - 1] = array2[maxInd]
    
    #print(arrayToPut)
    
    
    arrayToPut2[start] = minVal
    arrayToPut2[end - 1] = maxVal
    
    #print(arrayToPut2)
    
    
    
    
    #could use val instead of int
    
    
    
    
    
    numCompares2 = numCompares2 + 2
    
    # only added to compares as the 4th compare is unneded and the 3rd can then
    # be changed to an else meaning onlt 2 compares are done
    
    #maybe the double swapping is the only important one but do not think so
    
    if (minInd == end - 1 and maxInd == start ):
        array2[start], array2[minInd] = array2[minInd], array2[start]
    
    elif (minInd == end - 1 ) :
        
        array2[start], array2[minInd] = array2[minInd], array2[start]
        array2[end - 1], array2[maxInd] = array2[maxInd], array2[end - 1]
        
    else :
        array2[end - 1], array2[maxInd] = array2[maxInd], array2[end - 1]
        array2[start], array2[minInd] = array2[minInd], array2[start]
    
        
        
        

        
        
    #print(array2)
        
        
        
    
    
    
    
    
    #There is a problem here with double switching
    # will need to account for it
    #save value instead of indices
    
    start = start + 1 
    end = end - 1
    
    size = size - 2
    
    i = i + 1
    
   
    
    #If in order will swap with itself

print("Final array") 

print(array2)

print("Number of compares needed:   ", numCompares2) 

#array2[0] = 99999

print("Is the array my selection sort produced the same as the built in sort? ",
      array2 == testArray)


#plt.plot(array1, array2)
#plt.show()


"""

elif(maxInd == start) :
        array2[end - 1], array2[maxInd] = array2[maxInd], array2[end - 1]
        array2[start], array2[minInd] = array2[minInd], array2[start]
    else :
        array2[end - 1], array2[maxInd] = array2[maxInd], array2[end - 1]
        array2[start], array2[minInd] = array2[minInd], array2[start]
        
        #Works without these




"""
#Python because of indentation makes it difficult to alter code
#This is also because ot is a compiler language
#This would have been easier to do in Java
#Making a graph would be harder though


