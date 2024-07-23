# streamlit_app.py

import streamlit as st
from sqlalchemy import text

st.title("Database Connections ") 

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('Employee_db', type='sql')
# conn = st.connection("env:DB_CONN", "sql")

# Insert some data with conn.session.
with conn.session as s:
    s.execute(text('CREATE TABLE IF NOT EXISTS Employees (Names TEXT, Role TEXT , Sex TEXT , Experience TEXT);'))
    s.execute(text('DELETE FROM Employees;'))
    pycentric_emp = {
        'Abongile Billy': {
            "Role":"Software Engineer",
            "Sex":"M",
            "Experience":"1",
        },
        'Khanyi': {
            "Role":"Software Engineer",
            "Sex":"F",
            "Experience":"1",
        },
        'Ifalanga': {
            "Role":"Software Engineer",
            "Sex":"M",
            "Experience":"1",
        },
        'Vhutali': {
            "Role":"Director/Engineer",
            "Sex":"M",
            "Experience":"40",
        },
        }
    for k in pycentric_emp:
        s.execute(text(
            'INSERT INTO Employees (Names , Role  , Sex , Experience) VALUES (:names, :role, :sex, :exp);'),
            # params=dict(names="Abongile", role="Billy" , sex ="Yes")
            params=dict(names=k, role=pycentric_emp[k]["Role"] , sex =pycentric_emp[k]["Sex"] , exp = pycentric_emp[k]["Experience"])
        )
    s.commit()

# Query and display the data you inserted
pycentric_emp = conn.query('select * from Employees')
st.dataframe(pycentric_emp)