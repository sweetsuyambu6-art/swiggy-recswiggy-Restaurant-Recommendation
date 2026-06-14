import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd 

project_4 = st.set_page_config(page_title="swiggy", page_icon="🥘",layout="wide")

df=pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\project_4\swiggy.csv")
df1=pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\project_4\swiggy_cleaned01.csv")
# df2=pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\project_4\state_init.csv")
df2=pd.read_pickle(r"C:\Users\velku\Downloads\New folder\DS\project\project_4\encoder.pkl")

#cleaning and drop null 
# df2[df2.duplicated()]
# df2.dropna(inplace=True)
# (df2.isna().sum()/len(df2))*100

# encoding to pickle
# df.drop(columns=["id",'name','rating_count',"cost","rating",'lic_no','link',"address","menu"],axis=1,inplace=True)
# df.drop(["city","cuisine"],axis=1)
# df=pd.get_dummies(df,columns=["city","cuisine"],dtype="int")

#inserting nan rating values 
# df.drop(columns=["id",'name',"city",'rating_count','cost','cuisine','lic_no','link',"address","menu"],axis=1,inplace=True)
# df['rating'] = df['rating'].replace("--",0).astype(float)
# df[df["rating"]== 0 ]=df["rating"].mean().round(1)
# df.dropna(inplace=True)

# kmean and visual in df
selected_column = st.selectbox("Choose your loction ",df1["city"].unique())
selected_city=df1[df1["city"] == selected_column]
x=df.iloc[:,[0,1]].values
for i in range(1,2):
    kmean = KMeans(n_clusters=i,random_state=0)
    kmean.fit(df2)
st.dataframe(selected_city[["cuisine","rating","cost","address"]])  

# import streamlit as st

# st.title("welcome to know order details")

# name = st.text_input("insert order ID")
# detail = df1[df1["id"].astype(str)== name]
# st.dataframe(detail[["rating","cost"]])





