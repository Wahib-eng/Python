class vector : 
     def __init__(self, a1 , a2 ):
         self.a1=a1
         self.a2=a2

     def __str__(self) :
          return "vector (%d ,%d)" % (self.a1, self.a2)
     def  __add__ (self, other ) : 
          return(vector(self.a1 + other.a1 , self.a2 + other.a2))
vector1 = vector(25,1)
vector2 = vector(1,1)

print(vector1+vector2)
