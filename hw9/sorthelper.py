
def sortNumbers(listN):       
    for indexNumber in range(len(listN)-1,0,-1):        
        for i in range(int(indexNumber)):            
            if listN[i] > listN[i+1]:
                temp = listN[i]
                listN[i] = listN[i+1]
                listN[i+1] = temp
        

### END CODE