
from typing_extensions import deprecated
from passlib.context import CryptContext


## hashing algo we want to use
pwd_context = CryptContext(schemes=["bcrypt"] , deprecated = "auto")

## create a hash of a password

def hash_password(password : str):
    return pwd_context.hash(password)

pwd = hash_password("Abilly@99")
print("\n")
print(pwd)

#### Verifying a hashed password with login/User password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)   
