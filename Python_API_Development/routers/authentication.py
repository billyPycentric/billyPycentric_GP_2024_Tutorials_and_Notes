# from enum import verify
# from fastapi import APIRouter, HTTPException, status
# import schemas
# import oauth2
# import hashpasswords
# router = APIRouter(
#     tags=["Authentication"]
# )

# @router.post("/login")
# async def login(login_body :schemas.PersonLogin ):
#     password = hashpasswords.hash_password("a.Billy@Pycentric")
#     print(password)
#     password_login = hashpasswords.verify(login_body.password,password)
#     print(password_login)
#     if not password_login:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Invalid Credentials")
    
#    # acccess_token = oauth2.create_access_token(data={"user_email" : "myname"})
    
#     return   "Success"   # {"access_token ": acccess_token,"token_type": "bearer"}   