
ad1 , ad2 , ad3 ,age  ='wahib' ,'wael' ,'saeed' ,10

print(age ,'\n' ,ad3)
# id تطبع عنوان المتغيرات في الذاكرة
print(id(ad1) ,'\n',id(age) ) 
# يطبع العنصر الاول
# يطبع العنصر الثالث في اللستة الى الاخير 
#يطبع من العنصر الثالث الى العنصر الخامس  
# يطبع المتغير الا سترينج الى 3 مرات 
print(ad1[0], '\n', ad1[2:] ,'\n', ad1[2:4] , '\n', ad1*3)


ls1 = ["omar", 180.0, 66, "E Muh. "]

#Tuple can not be changed .. لا يمكن تحديث معلومات التبل 
ls2 = ("wahib", 170.0 , 60 , "B muh.") 

print(ls1)
print(ls2)
print(ls1[0], ls2[0])
print(ls1*3) 
print(ls1[1:])
print(ls1[1:3])



ls1[0] = "Wael"
print(ls1)

#يحذف اسماء المتغيرات ولايمكن اسخدامها بعد ذلك 
del ad1 , ad2 , ad3
