import streamlit as st
import pandas as pd
import time

## Using st.empty() 

placeholder = st.empty()
placeholder.text("My Name Is Abongile Billy")
time.sleep(4)
placeholder.text("And I Am A Software Engineer")


## Using dataframes and tables  
import streamlit as st
import pandas as pd
import numpy as np
import time

time.sleep(4)

df = pd.DataFrame(np.random.randint(1, 7, size=(2, 2)), columns=("A", "B"))
my_data_element = st.table(df)
time.sleep(4)

for tick in range(10):
    time.sleep(.9)
    add_df = pd.DataFrame(np.random.randint(1, 7, size=(2, 2)), columns=("A", "B"))
    my_data_element.add_rows(add_df)

st.button("Regenerate")