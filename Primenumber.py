

while True :
   
    c = int(input('0 to continue 1 to exit ')) 
      
    if c == 0 : 
        sayi = int(input('Asal olup olmadigi test etmek istedigin sayiyi giriniz : ')) 
        asal = True
        for i in range (2,sayi): 
            if sayi% i == 0 : 
                print(i)
                asal=False
                break
        if asal == True: 
            print( f'sayi',sayi, 'Asal sayidir .') 
        else:
            print(f'sayi', sayi , 'asal degildir') 
    elif c ==1 : 
        print ('Thanks for using my program WAHIB ^ ^'); break
    else : 
        print('you entered different number '); continue
