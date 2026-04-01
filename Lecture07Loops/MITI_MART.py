import streamlit as st
st.title("Super MITI MART 🛒")
price_input=st.text_area("Enter Your Product Price by Comma and stop by 0")
if st.button("Calculate Bill"):
    item_price=[int(x.strip())for x in price_input.split(",")]

    
    