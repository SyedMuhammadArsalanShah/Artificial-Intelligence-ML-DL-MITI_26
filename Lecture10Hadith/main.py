import streamlit as st
import requests





st.title("Hadith APP")


booksList= requests.get("https://hadithapi.com/api/books?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e").json()["books"]

# st.write(booksList)

booksListNames= [f"{b["bookName"]} | {b["bookSlug"]}" for b in booksList]


booksListSelection = st.selectbox("Choose  a Book", booksListNames)





bookSlug= booksListSelection.split(" | ")[1]


chapterList=requests.get(f"https://hadithapi.com/api/{bookSlug}/chapters?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e").json()["chapters"]

chapterListNames=[f"{c["chapterNumber"]} | {c["chapterEnglish"]} | {c["chapterArabic"]}" for c in chapterList]


chapterListSelection =st.selectbox("Choose a Chapter ",chapterListNames)

chapterNumber=int(chapterListSelection.split(" | ")[0])







hadith=requests.get(f"https://hadithapi.com/api/hadiths/?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e&book={bookSlug}&chapter={chapterNumber}&paginate={100000}").json()["hadiths"]["data"]



for i in hadith:
    
    
    st.success(f"Hadith No :{i["hadithNumber"]} | Status :{i["status"]}")
    st.success(f"{i["headingArabic"]}")
    st.success(f"{i["hadithArabic"]}")


  
    st.info(f"{i["headingUrdu"]}")
    st.info(f"{i["urduNarrator"]}")
    st.info(f"{i["hadithUrdu"]}")
    
    
      
    st.warning(f"{i["headingEnglish"]}")
    st.warning(f"{i["englishNarrator"]}")
    st.warning(f"{i["hadithEnglish"]}")