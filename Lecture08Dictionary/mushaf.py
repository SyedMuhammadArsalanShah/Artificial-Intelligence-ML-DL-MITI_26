import streamlit as st
import requests


st.title("Mushaf AL  Quran ")

surahNamesLo= requests.get("https://api.alquran.cloud/v1/surah").json()["data"]
surahNamesList=[f"{s["number"]}.{s["name"]} {s["englishName"]}"  for s in surahNamesLo]
bhaeSurahNumberDo=  st.selectbox("choose a surah",surahNamesList)


surahNumber=bhaeSurahNumberDo.split(".")[0]



surahDo= requests.get(f"https://api.alquran.cloud/v1/surah/{surahNumber}/ar.abdurrahmaansudais").json()["data"]["ayahs"]



for a in surahDo:
    st.success(a["numberInSurah"])
    st.info(a["text"])
    st.audio(a["audio"])






