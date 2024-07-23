import streamlit as st



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

login_page = st.Page("login.py", title="Log in")
logout_page = st.Page("logout.py", title="Log out")

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard"
)
bugs = st.Page("reports/bugs.py", title="Bug reports")
alerts = st.Page(
    "reports/alerts.py", title="System alerts")

search = st.Page("tools/search.py", title="Search")
history = st.Page("tools/history.py", title="History")
billy = st.Page("billy.py", title="Yes")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
            "Billy" : [],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()