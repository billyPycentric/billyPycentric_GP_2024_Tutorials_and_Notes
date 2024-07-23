import streamlit as st
from streamlit.runtime.state import session_state

st.title('Counter Example')

increment = st.button('Increment')

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("TapHere"):
    st.session_state.count+=1
st.write(st.session_state.count) 


st.write("Now Using Call Backs")
## first initialize
if 'counter' not in st.session_state:
    st.session_state.counter = 0

## Create a increment func
def increment_counter():
    st.session_state.counter+=1

st.button("Update", on_click=increment_counter())
st.write("Here is the new Update" , st.session_state.counter)

