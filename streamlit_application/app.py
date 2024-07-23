import streamlit as st
import pandas as pd
import numpy as np


@st.cache_data  # Cache data for better performance
def load_data():
    df = pd.read_csv('crime-stats-all-2011-2012-to-2022-2023.csv')
    return df

# Main function to run the app
def main():
    st.title('Crime Statistics Analysis')

    # Load data
    df = load_data()

    # Display the dataset
    st.subheader('Crime Statistics Data')
    st.write(df)

    # Perform basic statistics
    st.subheader('Basic Statistics')
    st.write(df.describe())  # Displays basic statistics (mean, std, min, max, etc.)
main()