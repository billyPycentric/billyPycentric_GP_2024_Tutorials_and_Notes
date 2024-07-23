# This App is about updating elements as the applications runs   

import streamlit as st
import pandas as pd
import numpy as np
import time
st.write("Count to Hundred")
st.button("Start")

for i in range(100):
    if i % 2 == 0:
        st.write(f"{i+1}" )
        st.write("Billy")
    if i ==100:
        st.write(f"{i+1}" )
        break
    time.sleep(1.9)

# df = pd.DataFrame(np.random.randn(15, 2), columns=(["A", "B"]))
# my_data_element = st.bar_chart(df)

# for tick in range(50):
#     time.sleep(.9)
#     add_df = pd.DataFrame(np.random.randn(1, 2), columns=(["A", "B"]))
#     my_data_element.add_rows(add_df)

# st.button("Want")