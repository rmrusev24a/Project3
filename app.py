import streamlit as st
import pandas as pd

st.title("📊 Класна анкета – оценки и ученици")

if "grades" not in st.session_state:
    st.session_state.grades = {
        "Отличен (6)": 0,
        "Много добър (5)": 0,
        "Добър (4)": 0,
        "Среден (3)": 0,
        "Слаб (2)": 0
    }

if "students" not in st.session_state:
    st.session_state.students = {
        "Иван": 0,
        "Мария": 0,
        "Георги": 0,
        "Анна": 0
    }

st.subheader("Избери")

grade = st.selectbox("Оценка:", list(st.session_state.grades.keys()))
student = st.selectbox("Ученик:", list(st.session_state.students.keys()))

if st.button("Запази избора"):
    st.session_state.grades[grade] += 1
    st.session_state.students[student] += 1
    st.success("Изборът е записан!")

st.divider()

st.subheader("☑️ Резултати")

st.write("Оценки")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(grades_df)

st.write("Ученици")
students_df = pd.DataFrame.from_dict(
    st.session_state.students, orient="index", columns=["Брой"]
)
st.bar_chart(students_df)
