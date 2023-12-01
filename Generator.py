

def my_gen (): 
    n = 1 
    print("Firist")
    yield n

    n+=1
    print("Second")
    yield n

    n+=1
    print("third")
    yield n

    n+=1
    print("fourth")
    yield n


x = my_gen()


print(next(x))
print(next(x))
print(next(x))
print(next(x))






