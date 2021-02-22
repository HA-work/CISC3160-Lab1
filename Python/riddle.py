"""

This is a program to solve the farmer, fox, goose, grain problem where a farmer needs
needs to get all 3 items across a river without leaving
the fox and the goose without him or the goose and the grain without him.




"""




farmer = "farmer"
fox = "fox"
goose = "goose"
grain = "grain"

rightSide = [farmer, fox, goose, grain]

leftSide = []

currentSide = rightSide

otherSide = leftSide

lastItem = ""

print("Initial state")

print("Right Side:   ", rightSide)

print ("Left Side:   ", leftSide)



step = 1



while (len(leftSide) != 4):
    
    # examine each item
    
    # avoid repitition by checking what the last item was
    
    # is there a way to fix it so the order of the ifs does not matter?
    

    
    for i in range(0,len(currentSide)):
        consideredItem = currentSide[i]
        
        
        if(consideredItem == "farmer" and lastItem != "nothing"):
            # check for farmer to go alone
            # focus on current side since that is what you can change
            
            # Doing nothing is an optimal move so it should be prioritized.
            # this is because we only ever take nothing on the way back
            
          
            
            if(((fox in currentSide and not(goose in currentSide))
               or (goose in currentSide and not(fox in currentSide)))
               and ((goose in currentSide and not(grain in currentSide))
               or (grain in currentSide and not(goose in currentSide))) ):
                
                selectedItem = "nothing"
                break
                
                
                # sees if the farmer can go alone
                
                # make break leave the for loop as once we have a selected item
                # we can stop comparing
                
                # there might be multiple legal moves though
                
                
              
        
        elif(consideredItem == "fox" and lastItem != "fox" ):
            if (goose in currentSide and grain in currentSide):
                print() # checks to not leave goose with grain
                # not safe to take fox
            
            
            else :
                selectedItem = fox
                break
            # is safe to take fox
            
        
        
        elif(consideredItem == "grain" and lastItem != "grain"):
            if (fox in currentSide and goose in currentSide):
                print() # not safe to take grain
                # will leave the fox with the goose
            
            else :
                selectedItem = grain
                break
        
        
        elif(consideredItem == "goose" and lastItem != "goose"):
            
            # it is always safe to take the goose
        
            selectedItem = goose
            break
        
        
            
    currentSide.remove(farmer)
    otherSide.insert(0, farmer)
    # good to insert farmer at the start of the new side
    # so to check if it is safe to leave alone first
    
    
    if(selectedItem != "nothing"):
        currentSide.remove(selectedItem)
        otherSide.append(selectedItem)
        
        
        
    
    print("Step : ", step)
    
    lastItem = selectedItem
    
    print("Move the farmer and", selectedItem)
    
    print("Right Side:   ", rightSide)

    print ("Left Side:   ", leftSide)
    

    
    print()
    
    step = step + 1
    
    #Swap the current side and selected side
    
    
    
    if(farmer in rightSide):
        currentSide = rightSide
        otherSide = leftSide
    elif(farmer in leftSide):
        currentSide = leftSide
        otherSide = rightSide
        # could just be else
    
            
    
print("Final state") 
print("Right Side:   ", rightSide)

print ("Left Side:   ", leftSide)

