# App Testing   
~~~
# install pytest
pip install pytest
~~~   
### How **pytest** is structured   
It is good practice to have a dir for test na duse consistant naming , i.e test_myapp.py | myapp_test.py , ***myapp_test.py*** works for me   
~~~
myproject/
├── app.py
└── tests/
    └── test_app.py
~~~   
### File Paths   
Suppose you have this project structure   
~~~
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
~~~   
since there is .streamlit dir -> the simulated app will have accesss to .toml(s)   
And you must always call the ***pytest*** command in the root dir   
~~~
cd myproject
pytest tests/
~~~   
 
