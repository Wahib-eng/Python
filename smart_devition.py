def smart_dev(fun): 
    def inner(x,y):
        print("Devition process : ", x , y )
        if  y == 0 : 
            print("there is no devition like this ")
            return
        return fun(x,y) 
    return inner 


@smart_dev
def dev(x,b): 
    return x/b
print(dev(6,2)) 
print(dev(0,5))
print(dev(6,10)) 
print(dev(6,112))  
