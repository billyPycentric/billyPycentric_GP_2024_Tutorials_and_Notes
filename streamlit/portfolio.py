import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon=":briefcase:",
    layout="centered",
    initial_sidebar_state="expanded",
)


# Header
st.title("My Portfolio")

# Introduction
st.header("Introduction")
st.image('billy.jpg', caption='Abonglie Billy', width=234, use_column_width=None)
#st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.write("""
    Hi, I'm Abongile Billy I'm a Software Development Engineer at PyCentric with a passion for Programming.
    This is a simple portfolio webpage I created with Streamlit. Here, you can find
    information about my skills, projects, and how to contact me.
""")

# Skills
st.header("Skills")
st.write("""
    - **Programming Languages**: Python, JavaScript,Java
    - **Frameworks**: FastApi, springboot
    - **Tools**: Git, Docker, linux
""")

# Projects
st.header("Projects")


# Contact Information
st.header("Contact Information")
st.write("""
    - **Email**: abo-billy09@outlook.com
    - **GitHub**: http://localhost:8080
""")

# Footer
st.write("---")
st.write("Built with Streamlit by Abongile")
