class Even : 

    
    def __next__(self): 
        
        self.n += 2 
        return self.n
           
    def  __iter__ (self): 
        self.n = 0 
        return self 



i = iter(Even())
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


