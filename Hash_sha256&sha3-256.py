import hashlib 


def hash_password (password, algorithm='sha256'): 
    # password will be hashed here 
    if algorithm == 'sha256' : 
        hash_obj = hashlib.sha256()
    elif algorithm=='sha3':
        hash_obj = hashlib.sha3_256()
    else : 
        raise ValueError("Error in the algorithm ")
    
    hash_obj.update(password.encode())
    hashed_password = hash_obj.hexdigest()
    return hashed_password 



# main code

username = 'Saeed Qasem '
password = 'Saeeb_9281029381029'

# call function to hash using sha256 algorithm and print it with username 
hashed_password = hash_password(password , algorithm='sha256')
print(f"username : {username}, Password : {password}, hashed password: {hashed_password}")

# call function to hash using sha3-256 algorithm and print it with username 
hash_passwordsha3_256 = hash_password(password ,algorithm='sha3')
print(f"username : {username}, Password : {password}, hased password: {hashed_password}")
