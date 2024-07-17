# Multi Page Application   
You can either use the st.page or st.nagivation for creating multipage application   
When things must know hen you work with pages   
1. Page lable -> usually for python file name   
2. page title -> the html title name   
3. page url path name -> come on   
4. page favicon   
5. page icon   
## Using Navigation Method   
~~~
your-repository/
├── page_1.py
├── page_2.py
└── streamlit_app.py
~~~   
~~~
#streamlit_app.py file

import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
pg.run()
~~~   
## Using Page/<page_dir>   
~~~
# create a hilding inside your root dir name it "pages"
# create files<.py files> 
# Done   

~~~   
Difference between the two approached is that with the first one the "page_1.py" addss on top of your root/welcome page while with page/ the pages are separated from your welcome or your root .py page      
## Adding sections   
~~~
# Directory Structure
your-repository/
├── reports
│   ├── alerts.py
│   ├── bugs.py
│   └── dashboard.py
├── tools
│   ├── history.py
│   └── search.py
└── streamlit_app.py
~~~   
~~~python
# Welcome page code
import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="System alerts", icon=":material/notification_important:"
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()

~~~     
## Working with Widgets   
File structure   
~~~
your-repository/
├── page_1.py
├── page_2.py
└── streamlit_app.py
~~~   
Code   
~~~
import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])


st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")

pg.run()
~~~