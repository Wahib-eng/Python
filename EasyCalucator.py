while True : 

        try: 

            user= int(input('Enter 0 to continue and 1 to exit'))

            if (user == 0 ): 

                x = float(input("Enter the first oprand : "))
                y= float(input("Enter the second operand : "))

                c = str(input("Enter the opreator like (* / + - % ** ) :  "))


                if (c == '+') :
                    x+=y 
                    print("Result : ", x)
                elif (c == '-'):
                    print("Result : ", x-y)
                elif (c == '*'):
                    print("Result : ", x*y)
                elif (c == '/'):
                    print("Result : ", x/y)
                elif (c == '%'):
                    print("Result : ", x%y)
                elif (c == '**'):
                    print("Result : ", x**y)
                    
                else : 
                    print("You have to choose a corecct oprator ")
                 
            elif(user == 1 ): 
                print("Goodbye")

                break
            else : 
                print("You Entered different number ")
                continue 

                
                
        except ValueError:
                print("please Enter a number value !!! ")
