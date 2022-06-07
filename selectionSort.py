from itertools import count


mylist = [2,1,3,5,4]
count = 0
def selectionSort(listX):
    count = 0
    for j in range (len(listX)):
        i = j
        while (i<len(listX)):
            if listX[i] < listX[j]:
                listX[j],listX[i] = listX[i],listX[j]
            i +=1
            count +=1
    print(count)
    return listX

print(selectionSort(mylist))