import hashlib 
import secrets 

# this code will hash the passwrod and add the salt to it so it is a littile hard to find to password have the the same hased code 
password = "wahib128987_Ha"
salt = secrets.token_hex(16)

hashed_password = hashlib.sha512((password +salt).encode()).hexdigest()
print(f"password : {password}, \n hashed password : {hashed_password} , \n salt : {salt}")


