class kupAl : 

    def __init__(self, finished = 0 ) -> None:
        self.finished = finished

    def __next__(self): 
        if self.n <= self.finished: 
            result = 2 ** self.n
            self.n += 1 
            return result
        else: 
            raise StopIteration
    def  __iter__ (self): 
        self.n = 0 
        return self 
    
numbers = kupAl(5)


i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))

for i in kupAl(11): 
    print(i)
