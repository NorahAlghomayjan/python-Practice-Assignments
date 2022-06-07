mylist = [0,3,4,5,3,2,1,1]
def insertionSort(listX):
    insertionindex = -1
    for i in range(len(listX)):
        for j in range (i): #sub-list (from 0 - i )
            if listX[j] > listX[i]: #searching sub-list to look for any value < value (i).
                insertionindex = j
                break # skip for when 1st value < (i) is encountred.
        if (insertionindex!=-1): #if no value < (i) is found -> keep (i) in its place and skip the next steps.
            shiftingIndex = i #where to shift 
            temp = listX[i] 
            while(shiftingIndex>insertionindex): #shifting from insertion index to i
                listX[shiftingIndex] = listX[shiftingIndex-1]
                shiftingIndex -=1
            
            listX[insertionindex] = temp
            insertionindex = -1
    return listX
print(insertionSort(mylist))