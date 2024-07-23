import time
import streamlit as st
import pandas as pd
import numpy as np


st.write("Hi There My Name is Abongile Billy And I Am A Software Engineer")
## Pandas Part
dataframe = pd.DataFrame({

    'Names' : ["Abongile","Khanyi","ifalanga","Vhutali"],
    'Roles': ["Grad","Grad","Grad","Director"],
    'Years_Exp':[1,1,1,"Not_Relevant"]
})

dataframe
## Numpy Part
data = np.random.randn(3,3)
data


### Complex
dataframe1 = pd.DataFrame(
    np.random.randn(3, 10),
    columns=('col %d' % i for i in range(10)))

st.dataframe(dataframe1.style.highlight_max(axis=0))
st.line_chart(dataframe1)



#####
st.title("EPL Data")

# Load the data

def load_data():
    url = "E0.csv"  # Replace with your CSV file path or URL
    data = pd.read_csv(url)
    return data

data = load_data()
print("Who are you")
# Display the data in a tabular format
st.write(data)  
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.write("The value you Entered is "+ st.session_state.name)
if(st.session_state.name == "Abongile"):
    st.write("I see you bgi dawg")

if st.button('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


left_column, right_column, middle_column= st.columns(3)
# You can use a column just like st.sidebar:
left_column.button('Press me!')
middle_column.checkbox("Yes Sir!!!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

with middle_column:
    chosen2 = st.radio(
        'Sorting What',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen2} house!")    



latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.5)

'...and now we\'re done!'