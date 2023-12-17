import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MaxNLocator
import seaborn as sns 

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# Streamlit 페이지 설정
st.set_page_config(
    page_title="나에게 맞는 직업",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("나에게 맞는 직업찾기")

st.divider()

st.subheader("나에게 중요한 가치는 무엇일까?")
st.write("직업가치관 검사 결과 다시 확인하기: www.career.go.kr")

student_thought = st.text_area("예) 나는 **돈**이 중요해!, 나는 **워라밸**이 중요해!")

if st.button("제출"):
    if 'student_thoughts.csv' not in os.listdir():
        student_thoughts_df = pd.DataFrame({'학생 생각': [student_thought]})
    else:
        student_thoughts_df = pd.read_csv('student_thoughts.csv', encoding='utf-8')
        student_thoughts_df = student_thoughts_df.append({'학생 생각': student_thought}, ignore_index=True)

    student_thoughts_df.to_csv('student_thoughts.csv', index=False, encoding='utf-8')

    st.subheader("나의 생각:")
    st.write(student_thought)

st.divider()

st.subheader("나의 가치에 맞는 직업을 찾기 위한 선그래프 그리기📈")
st.write("통계자료 찾기: http://laborstat.moel.go.kr/hmp/index.do")




st.title("엑셀 데이터 시각화")

# 엑셀 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요.", type=["xlsx", "xls"])

# 엑셀 파일 불러오기 및 데이터 확인
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, header=0, index_col=0)

    # 데이터의 일부 출력
    st.write("데이터 미리보기:", df.head())

    st.success('파일 업로드 성공!')

    # 행과 열 선택 옵션
    row_options = df.index.tolist()
    column_options = df.columns.tolist()

    selected_rows = st.multiselect("행 선택", options=row_options)
    selected_columns = st.multiselect("열 선택", options=column_options)

    if selected_rows and selected_columns:
        # 선택된 행과 열에 대한 데이터프레임
        selected_df = df.loc[selected_rows, selected_columns]

        # 데이터를 정수형으로 변환
        selected_df = selected_df.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

        # 데이터 시각화
        st.subheader("선택한 데이터 시각화")
        fig, ax = plt.subplots()
        selected_df.plot(ax=ax, kind='line', marker='o')
        st.pyplot(fig)


st.divider()

st.subheader("어떤 직업의 나의 가치와 맞는 것 같나요?")
student_thought = st.text_area("그래프를 통해 발견한 내용을 적어주세요🖊️")

if st.button("제출", key="submit_button"):
    if 'student_thoughts.csv' not in os.listdir():
        student_thoughts_df = pd.DataFrame({'학생 생각': [student_thought]})
    else:
        student_thoughts_df = pd.read_csv('student_thoughts.csv', encoding='utf-8')
        student_thoughts_df = student_thoughts_df.append({'학생 생각': student_thought}, ignore_index=True)

    student_thoughts_df.to_csv('student_thoughts.csv', index=False, encoding='utf-8')

    st.subheader("나의 생각")
    st.write(student_thought)
