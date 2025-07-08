#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\User\Desktop\ABC\dirty_cafe_sales.csv")
df1 = df.copy()
df1["Transaction Date"] = pd.to_datetime(df1["Transaction Date"] , errors="coerce")
df1 = df1.dropna(subset=['Transaction ID', 'Transaction Date'])
df1=df1[(df1["Transaction ID"].astype('str').str.strip()!='') & (df1['Transaction Date'].astype('str').str.strip()!='')]
print("Reamining Rows After Intial cleaning ",df1.shape[0])
df1["Quantity"] = pd.to_numeric(df1["Quantity"],errors="coerce") 
df1["Price Per Unit"] = pd.to_numeric(df1["Price Per Unit"],errors="coerce") 
df1["Total Spent"] = pd.to_numeric(df1["Total Spent"],errors="coerce")
df1["Payment Method"] = np.where(df1["Payment Method"].isnull(),"Not Provided",df1["Payment Method"])
df1["Payment Method"] = np.where(df1["Payment Method"]=='ERROR',"Not Provided",df1["Payment Method"])
df1["Location"] = np.where(df1["Location"]=='ERROR',"Not Provided",df1["Location"])
df1["Location"] = np.where(df1["Location"].isnull(),"Not Provided",df1["Location"])
df1["Price Per Unit"] = np.where(df1["Price Per Unit"].isnull(),df1["Total Spent"]/df1["Quantity"],df1["Price Per Unit"])
df1["Payment Method"]=df1["Payment Method"].replace("UNKNOWN","Not Provided")
df1["Location"]=df1["Location"].replace("UNKNOWN","Not Provided")
df1["Item"]=df1["Item"].fillna("UNKNOWN")
price_to_item_map={
    1.0:"Cookie",
    1.5:"Tea",
    2.0:"Coffee",
    3.0:"Juice/Cake",
    4.0:"Smoothie/Sandwich",
    5.0:"Salad"
}
df1["Item"]=np.where(df1["Item"].isin(["ERROR","UNKNOWN"]),df1["Price Per Unit"].map(price_to_item_map),df1["Item"])
print(df1["Item"].isin(["ERROR","UNKNOWN"]).sum())
df1=df1.dropna(subset=["Quantity","Total Spent"],how = 'all')
df1=df1.dropna(subset=["Item","Price Per Unit"],how = 'all')
item_to_price_map={
    "Cookie":1.0,
    "Tea":1.5,
    "Coffee":2.0,
    "Juice":3.0,
    "Cake":3.0,
    "Smoothie":4.0,
    "Sandwich":4.0,
    "Salad":5.0
}
df1["Price Per Unit"]=np.where(df1["Price Per Unit"].isnull(),df1["Item"].map(item_to_price_map),df1["Price Per Unit"])
df1["Total Spent"] = np.where(df1["Total Spent"].isnull(),df1["Quantity"]*df1["Price Per Unit"],df1["Total Spent"])
df1["Quantity"] = np.where(df1["Quantity"].isnull(),df1["Total Spent"]/df1["Price Per Unit"],df1["Quantity"])
#missing=df1[df1["Price Per Unit"].isnull()|df1["Total Spent"].isnull()|df1["Quantity"].isnull()|df1["Item"].isnull()]
#print(missing)
#print((df1.isnull()|(df1.astype(str).map(str.strip)=='')).sum())
#df1.head(10)
df1.to_csv("Full_Cleaned_Data.csv",index=False)


# In[ ]:




