# Streamlit Connections  
streamlit has ***st.connection()*** for connecting streamlit apps to data/APIs with just few lines of Code  
For more comprehensive info about the **st.connection ()** :    
[st.connection()](https://youtu.be/xQwDfW7UHMo?list=TLGGAxN0dA-LUZ8yMjA3MjAyNA)   
### Using Connections Demo   
1. Install the SQLAlchemy   
~~~
pip install sqlalchemy
~~~   
2. Setup the DB url   
Create a .streamlit Dir and secrets.toml file in the main app dir
~~~
# .streamlit/secrets.toml

[connections.pets_db]
url = "sqlite:///pets.db"
~~~   
3. Setting up the connection   
~~~
import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('pets_db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
~~~    
## Global Secrets   
~~~
# ~/.streamlit/secrets.toml

[connections.local]
url = "mysql://me:****@localhost:3306/local_db"

[connections.staging]
url = "mysql://jdoe:******@staging.acmecorp.com:3306/staging_db"
~~~   
The configure your application   
~~~
# streamlit_app.py
import streamlit as st

conn = st.connection("env:DB_CONN", "sql")
df = conn.query("select * from mytable")
# ...
~~~   
Specify the Url during/@ Runtime   
~~~
# connect to local
DB_CONN=local streamlit run streamlit_app.py

# connect to staging
DB_CONN=staging streamlit run streamlit_app.py
~~~    
