import datetime
import streamlit as st

if "login" not in st.session_state:
    st.session_state.login = False

login_page = st.Page("login.py" , title="login Page")
logout_page = st.Page("logout.py" , title="logout Page")
billy_widget = st.Page("widget.py", title="Experiment")

if st.session_state.login:
    pg = st.navigation(

        {
            "Logout" : [logout_page],
            "Widget" : [billy_widget],
        }
    )
    st.sidebar.selectbox("Group", ["A","B","C"], key="group")
    st.sidebar.slider("Size", 5, 8, key="size")
    st.sidebar.date_input("When's your birthday", datetime.date(2019, 7, 6))
    
else:
    pg = st.navigation([login_page])


pg.run()