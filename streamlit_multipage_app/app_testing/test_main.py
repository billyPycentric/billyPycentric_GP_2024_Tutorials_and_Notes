"""test_app.py"""
from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    """A user increments the number input, then clicks Add"""
    at = AppTest.from_file("main.py").run()
    at.number_input[0].increment().run()
    # at.addend[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 14"

def test_secrets():
    # Initialize an AppTest instance.
    at = AppTest.from_file("main.py")
    # Declare the secrets.
    at.secrets["db_username"] = "Jane" # i added 2 to jane , so the test should fail
    at.secrets["db_password"] = "mypassword"
    at.secrets["my_other_secrets.things_i_like"] = ["Streamlit", "Python"]


    assert at.secrets["db_username"] == "Jane"
    assert at.secrets["db_password"] == "mypassword"
    assert at.secrets["my_other_secrets.things_i_like"] == ["Streamlit", "Python"]
    # Run the app.
    at.run()