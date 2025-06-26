import streamlit as st
import pandas as pd

st.title("lab1")
url = "https://github.com/myoh0623/dataset/blob/main/student-mat.csv"
df = pd.read_csv(url)

# 성별 평균 성적 비교(G3 컬럼은 성적을 나타낸다)
st.subheader("1. 성별에 따른 평균 최종 성적 (G3 컬럼)")
gender_score = df.groupby("sex")["G3"].mean()

st.bar_chart(gender_score)

# stduy time mean
st.subheader("2. 공부 시간에 따른 평균 최종 성적")
studytime_score = df.groupby("studytime")["G3"].mean()

# walc mean

st.subheader("3. 주말 알콜 섭취에 따른 평균 최종 성적")
walc_score = df.groupby("walc")["G3"].mean()