import streamlit as st
import pandas as pd
page_2 = st.set_page_config(page_title="swiggy", page_icon="🥘",layout="wide")
# Define the pages  

st.sidebar.markdown("order 🥘")

df1=pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\project_4\swiggy_cleaned01.csv")

st.title("welcome to know order details")
name = st.text_input("insert order ID")
detail = df1[df1["id"].astype(str)== name]
st.dataframe(detail[["name","rating_count","lic_no","city","address"]])


