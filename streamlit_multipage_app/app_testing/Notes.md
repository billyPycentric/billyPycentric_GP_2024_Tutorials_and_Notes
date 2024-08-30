<<<<<<< HEAD
# App Testing   
~~~
# install pytest
pip install pytest
~~~   
### How **pytest** is structured   
It is good practice to have a dir for test na duse consistant naming , i.e test_myapp.py | myapp_test.py , ***myapp_test.py*** works for me   
~~~
myproject/
├── app.py
└── tests/
    └── test_app.py
~~~   
### File Paths   
Suppose you have this project structure   
~~~
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
~~~   
since there is .streamlit dir -> the simulated app will have accesss to .toml(s)   
And you must always call the ***pytest*** command in the root dir   
~~~
cd myproject
pytest tests/
~~~   
 
=======
# App Testing   
~~~
# install pytest
pip install pytest
~~~   
### How **pytest** is structured   
It is good practice to have a dir for test na duse consistant naming , i.e test_myapp.py | myapp_test.py , ***myapp_test.py*** works for me   
~~~
myproject/
├── app.py
└── tests/
    └── test_app.py
~~~   
### File Paths   
Suppose you have this project structure   
~~~
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
~~~   
since there is .streamlit dir -> the simulated app will have accesss to .toml(s)   
And you must always call the ***pytest*** command in the root dir   
~~~
cd myproject
pytest tests/
~~~    
## Test Code Break Down   
~~~
"""test_app.py"""
from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    """A user increments the number input, then clicks Add"""
    at = AppTest.from_file("app.py").run()
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 1"
~~~   
why are we using " ***number_input[0]*** " instead of the actual variable name    
~~~
"""app.py"""
import streamlit as st

# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 0, 10)
if st.button("Add"):
    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")
~~~   
answer : The reason we use at.number_input[0].increment().run() instead of at.addend[0].increment().run() is because AppTest interacts with Streamlit widgets based on their type and index rather than their variable names in the code.      
## Using secrets in App testing  
Dont include secrets into your tests   
~~~
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
~~~   
you don't want to commit your secrets to your repository, you may need to write tests where you securely pull your secrets into memory or use dummy secrets.   
~~~
db_username = "Jane"
db_password = "mypassword"

[my_other_secrets]
things_i_like = ["Streamlit", "Python"]
~~~   
~~~
### Test file 
# Initialize an AppTest instance.
at = AppTest.from_file("app.py")
# Declare the secrets.
at.secrets["db_username"] = "Jane"
at.secrets["db_password"] = "mypassword"
at.secrets["my_other_secrets.things_i_like"] = ["Streamlit", "Python"]
# Run the app.
at.run()
assert at.secrets["db_username"] = "Jane"
assert at.secrets["db_password"] = "mypassword"
assert at.secrets["my_other_secrets.things_i_like"] = ["Streamlit", "Python"]
~~~   
***Use assert to compare the secrets***   
~~~
~~~

~~~
 
>>>>>>> dd11abea7ce3a5cd4b5e6bbea264814f04a269a8
