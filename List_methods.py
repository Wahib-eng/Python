L = [1,1,2,3,4,5,6]
T = (8,9,10)

print("size of the list ", len(L))
print("max element in the list ", max(L))
print("mini element in the list ", min(L))


L2= list(T)
print("change the tuple to a list  ", L2)

L.append(20)
print("add 20 to the list : ", L)

print("How many times the number 1 is found in the list",L.count(1))

New_T = (21,22)
L.extend(New_T)
print("Add a new list to the old one ",L )
print("The tuple that was added to the list : ", New_T)

print("index of the element 3  : ", L.index(3))

L.insert(2,55)
print("Add 55 to 2. index : ", L )

deleted_element = L.pop(2)

print("Removed element : ", deleted_element)
print("updated List: ",L )

deleted_element = L.pop()

print("updated List Here the last element will be poped up : ",L )


L.remove(20)
print("updated List: ",L )


L.reverse()
print("updated List: ",L )

L.sort()
print("updated List: ",L )

