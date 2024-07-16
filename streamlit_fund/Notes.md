# Introduction to streamlit   
streamlit application can be run in 2 ways   
1. As a Python module   
~~~
python -m streamlit run my_app.py
~~~   
2. Via termail -> as an application   
~~~
streamlit run my_app.py
~~~   
streamlit also supports magic commands -> meaning you can write an application without calling stramlit methods   
i.e lets say i have a text:   
~~~python
my_text = "Hi there my name is Abongile"
~~~   
instead of me using streamlit.write(my_text) i can also just call that var/func
my_text , and it will display the value that is stored   
## Using Pandas   
Pandas is a powerful and widely-used open-source data manipulation and analysis library for Python. It provides data structures and functions needed to manipulate structured data seamlessly   
~~~python
import streamlit as st
import pandas as pd

table = pd.Dataframe(
{  
   "Col1":[1,2,3,4],
   "Col2":[4,3,2,1]

}
)
# datafram is a 2D tubular dataStructure



~~~    
## Using numpy(numerical python)   
NumPy is a foundational library for numerical and scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently   
## Streamlit Advanced Concepts   
Caching -> allows ypu to save an output of a function, to avoid re-calculations  
To cache a function in Streamlit, you need to apply a caching decorator to it. You have two choices :
* st.cache_data -> it is for serializable objects(Objects that can me changed)
* st.cache_resource -> it is for unserializable objects(Db Connections)   
## Sessions State   
A session is a single instance of viewing an app. If you view an app from two different tabs in your browser, each tab will have its own session.   
~~~python


if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
~~~
# Additional features   
## Pages   

