import time

import pyautogui
import streamlit as st
import pandas as pd
import pywhatkit as kit



st.title("WhatsApp Automation")


st.write("Contact choose karen")

uploadkaro= st.file_uploader("Choose an excel file ",type=["xlsx"])


portfolioLink= st.text_input("Enter Your Portfolio Here ",value="https://syedmuhammadarsalanshah.com/")
customMessage=st.text_area("Enter Your Custom Message ", value="Explore me on this web")

if uploadkaro is not None:
    st.write("contacts are uploaded !")
    df=pd.read_excel(uploadkaro)
    st.dataframe(df)
    
    if st.button("Send Message "):
        st.write("working ")
        for i , row in df.iterrows():
            phoneNumber=f"+92{row["Phone"]}"
            message=f"{customMessage}\n{portfolioLink}"
            
            kit.sendwhatmsg_instantly(phoneNumber,message,35)
            
            time.sleep(10)
            
            pyautogui.press("enter")
            
            time.sleep(10)
            
            pyautogui.press("enter")
            
            
st.info("copyright alright reserved by SMASB")