import streamlit as st
import pandas as pd
import numpy as np

st.text("Hi I am Abongile Billy , Software Engineer")
df = pd.DataFrame({
    'Names':["Abongile","khanyi","Ifalanga","Vhutali"],
    'Years_Work_Experience':[1,1,1,5],
    'Married':[True,False,True,False]
})
st.write("Here is the table :",df)

st.write("How To Plot A Chart")

chart_data = pd.DataFrame(
     np.random.randn(3, 3),
     columns=['Khanyi','Abongile','Ifalanga']
     #columns=['a', 'b', 'c']
     )

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(10, 2) / 1 + [-26.5614,  27.8507],
    columns=['lat', 'lon'])

st.map(map_data)

y=9
x = st.slider('Billy')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.write(y, 'squared is', y* y)

st.text_input("Your name", key="billy")
st.session_state.billy

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    'third column':["Gauteng","Free State","Cape Town","Limpopo"]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['third column'])

st.write('You selected: ', option)
if(option == 'Gauteng'):
    st.write("you won   !!!!")


import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
st.button("RunYes")


my_text = "Hi my name is Abongile billy"
my_text