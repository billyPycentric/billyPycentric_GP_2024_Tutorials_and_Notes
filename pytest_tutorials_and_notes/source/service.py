## creating a dummy DB

database = {
    1:"One" ,
    2: "Two" ,
    3: "Three"
    }

# Create a function which will get user from db , using user_id
def get_user_from_db(user_id):
    return database.get(user_id)