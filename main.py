import streamlit as st

mbti_data = {
    "ENFP": {
        "직업": ["마케팅 전문가", "콘텐츠 크리에이터", "광고 기획자"],
        "이유": "ENFP는 창의적이고 사교적이며 아이디어 발산에 강점이 있습니다.",
        "미래전망": "디지털 마케팅 산업은 향후 10년간 연평균 8% 성장할 것으로 예상됩니다."
    },
    "ISTJ": {
        "직업": ["회계사", "데이터 분석가", "공무원"],
        "이유": "ISTJ는 계획적이고 신중하며 규칙을 잘 따릅니다.",
        "미래전망": "데이터 분석과 행정 분야는 안정적인 수요가 유지될 전망입니다."
    }
}

mbti_list = [
    "ENFP","ENTP","ENFJ","ENTJ",
    "INFP","INTP","INFJ","INTJ",
    "ESFP","ESTP","ESFJ","ESTJ",
    "ISFP","ISTP","ISFJ","ISTJ"
]

st.title("MBTI 기반 직업 추천")
mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

if mbti in mbti_data:
    st.subheader("추천 직업")
    for job in mbti_data[mbti]["직업"]:
        st.write(f"- {job}")

    st.subheader("왜 이 직업이 적합한가?")
    st.write(mbti_data[mbti]["이유"])

    st.subheader("미래 전망")
    st.write(mbti_data[mbti]["미래전망"])
else:
    st.warning("아직 이 MBTI에 대한 데이터가 준비되지 않았습니다.")
