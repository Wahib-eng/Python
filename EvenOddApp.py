def tillN(n):
    if n % 2 == 0:  # Check if the number is even
        for i in range(2, n+1, 2):
            print(i)
    else:  # The number is odd
        for i in range(1, n+1, 2):
            print(i)

# Example: If the number is even, print even numbers up to 8; if odd, print odd numbers up to 7



while True: 
    c = int(input("Enter 1 to continue and 0 to stop : " ))
    if c == 1 : 
        a = int (input('Enter a number : '))
        tillN(a)
    else: 
        break

     
   

