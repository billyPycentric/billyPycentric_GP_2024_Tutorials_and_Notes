"""app.py"""
import streamlit as st

# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 6)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 7, 598)
if st.button("Add"):
    st.session_state.beans += addend
st.write(f"Beans counted: {st.session_state.beans}")
