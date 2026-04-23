



from google import genai
import streamlit as st

st.title("MITI CHAT BOT SYSTEM APKY SAWAL OR UNKA TASALI BAKHS JAwAB")

googleAPIKEY="YOUR_API_KEY "


client = genai.Client(api_key=googleAPIKEY)

userKaSawal= st.text_input(label="Enter Your Question Here ")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=userKaSawal
)
# print(response.text)

if st.button("Submit"):
    st.markdown(response.text)