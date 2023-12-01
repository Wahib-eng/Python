class Nokta (): 
    def __init__(self, x =0 , y =0): 
        self.x = x 
        self.y=0 
    def __del__(self): 
        class_name = self.__class__.__name__
        print(class_name)
        print("kasdjasd")

p = Nokta()
p1 = p 
p2 = p 
print("\n",p , p1 , p2 )
