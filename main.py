import streamlit as st
st.title("MBTI 기반 직업 추천")
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_data.keys()))

if mbti:
    st.subheader("추천 직업")
    for job in mbti_data[mbti]["직업"]:
        st.write(f"- {job}")

    st.subheader("왜 이 직업이 적합한가?")
    st.write(mbti_data[mbti]["이유"])

    st.subheader("미래 전망")
    st.write(mbti_data[mbti]["미래전망"])
