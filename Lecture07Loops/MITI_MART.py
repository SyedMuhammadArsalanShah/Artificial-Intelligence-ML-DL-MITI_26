
import streamlit as st 


st.title("MITI Super Mart 🛒")


price_input = st.text_area("Enter Your All product price with comma sepration ")

if st.button("Bill do bhai "):
    
    item_prices=[int(x.strip()) for x in price_input.split(",")]
    
    finalBill=0
    i=0
    while i< len(item_prices):
        if item_prices[i]==00:
            st.write("Thanks For Shopping In Mart")
            break;
        st.write(f"Item No{i+1}")
        st.write(f"Item Price{item_prices[i]}")
        finalBill=finalBill+item_prices[i]
        i=i+1
    st.write(f"Your Final Bill is {finalBill}")
    
    
    if finalBill <=10000:
        discount= finalBill*0.20
    elif finalBill <=20000:
        discount= finalBill*0.5
    else:
        discount=finalBill*0.75
        
        
    afterDiscBill= finalBill-discount
    st.write(f"After Discount Bill is {afterDiscBill}")
    

    