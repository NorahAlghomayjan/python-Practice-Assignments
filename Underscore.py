class Underscore:
    def map(self, iterable, callback):
        listX = []
        for i in iterable:
            listX.append(callback(i))
        return listX

    def find(self, iterable, callback):
        for i in iterable:
            if (callback(i)):
                return i

    def filter(self, iterable, callback):
        listX = []
        for i in iterable:
            if(callback(i)):
                listX.append(i)
        return listX

    def reject(self, iterable, callback):
        listX = []
        for i in iterable:
            if(not callback(i)):
                listX.append(i)
        return listX


instance1 = Underscore() 

squares = instance1.map([1,2,3], lambda x: x*2) # should return [2,4,6]
greaterValue = instance1.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
evens = instance1.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)# should return [2, 4, 6]
odds = instance1.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]

print(squares)
print(greaterValue)
print(evens)
print(odds)

