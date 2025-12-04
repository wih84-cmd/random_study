import streamlit as st
import random
st.set_page_config(page_title="🎰 랜덤 공부시간", page_icon="🎁", layout="centered")


# 0시간(0분) ~ 10시간(600분) 사이, 30분 간격 리스트 만들기
time_options = list(range(0, 601, 30))

# 랜덤으로 하나 선택
study_time_min = random.choice(time_options)

# 시간으로 변환 (예: 150분 → 2시간 30분)
hours = study_time_min // 60
minutes = study_time_min % 60

print(f"페이지: {page}")
print(f"공부시간: {hours}시간 {minutes}분")
