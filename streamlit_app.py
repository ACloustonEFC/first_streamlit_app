import streamlit
import pandas

streamlit.title("EFC Snowflake Test")

streamlit.header("Test")
streamlit.text("Text text text")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
