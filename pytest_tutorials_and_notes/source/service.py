import requests


## creating a dummy DB

database = {
    1:"One" ,
    2: "Two" ,
    3: "Three"
    }

# Create a function which will get user from db , using user_id
def get_user_from_db(user_id):
    return database.get(user_id)


# Get users from an API
def get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    # if not 200 raise HTTPError
    raise requests.HTTPError

# getting comments using an API
def get_comments():
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    if (response.status_code == 200):
        return response.json()
    
    # arise an error if the request was not successful
    raise requests.HTTPError