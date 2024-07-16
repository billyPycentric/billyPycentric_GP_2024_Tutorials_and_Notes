# Streamlit Execution Model   
## Caching   
1. Minimal Egs   
~~~
@st.cache_data
def long_running_function(param1, param2):
    return …
~~~ 
2. Basic Usage    
~~~
@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
~~~  
3. Advanced Usage   
~~~
@st.cache_data(ttl=3600)  # 👈 Cache data for 1 hour (=3600 seconds)
def get_api_data():
    data = api.get(...)
    return data
~~~   
### Excluding params   
~~~
@st.cache_data
def fetch_data(_db_connection, num_rows):  # 👈 Don't hash _db_connection
    data = _db_connection.fetch(num_rows)
    return data

connection = init_connection()
fetch_data(connection, 10)
~~~

### Hashing a Custom class <Using dict>   
If you dont use it you get an error , so you need to tell the func how to hash a custom class   
~~~
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

def hash_func(obj: MyCustomClass) -> int:
    return obj.my_score  # or any other value that uniquely identifies the object

@st.cache_data(hash_funcs={MyCustomClass: hash_func})
def multiply_score(obj: MyCustomClass, multiplier: int) -> int:
    return obj.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(multiply_score(score, multiplier))
~~~   
### You cant also hash a member of the class -> func in the custom class <unhashable paramError>   
~~~
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data(hash_funcs={"__main__.MyCustomClass": lambda x: hash(x.my_score)})
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))
~~~   
### Hshing a pydantic model   
~~~
import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_data(hash_funcs={Person: lambda p: p.name})
def identity(person: Person):
    return person

person = identity(Person(name="Lee"))
st.write(f"The person is {person.name}")

~~~
4. Migrating from st.cache   
## State-fulness to Applications   

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks   
~~~python

# Normal session.state


# Check if the state var exist , if not initialize
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# crate a varr to store the val
if st.button("Counter"):
    st.session_state.counter += 1

st.write("Here is the new value")

~~~

> Now Using Call back   
#
~~~python
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)
~~~   
> Now Using args and Kwargs   
#
~~~python
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('Enter a value', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

increment = st.button('Increment', on_click=increment_counter,
    args=(increment_value, ))

st.write('Count = ', st.session_state.count)
~~~   
> Forms and Callbacks   
#
~~~python
if 'count' not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key='my_form'):
    st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
    st.number_input('Enter a value', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write('Current Count = ', st.session_state.count)
st.write('Last Updated = ', st.session_state.last_updated)
~~~   
