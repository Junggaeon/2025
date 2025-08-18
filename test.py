import streamlit as st
import random

# 감정별 명언 데이터베이스 (명언, 저자)
quotes = {
    "설렘": [
        ("기대는 삶을 빛나게 한다.", "익명"),
        ("새로운 시작은 언제나 두근거림과 함께 온다.", "익명")
    ],
    "감사": [
        ("감사하는 마음은 행복의 문을 연다.", "에픽테토스"),
        ("행복은 감사하는 마음에서 자란다.", "익명")
    ],
    "만족": [
        ("이미 가진 것에 만족하는 자가 가장 부자다.", "소크라테스"),
        ("작은 기쁨에 만족하는 삶이 큰 행복이다.", "익명")
    ],
    "우울": [
        ("우울은 영혼이 잠시 쉬고 싶다는 신호일지도 모른다.", "익명"),
        ("희망은 가장 어두운 순간에도 꺼지지 않는다.", "익명")
    ],
    "외로움": [
        ("외로움은 나 자신을 만나는 시간이다.", "익명"),
        ("깊은 고독 속에서 진정한 나를 발견한다.", "익명")
    ],
    "그리움": [
        ("그리움은 사랑이 머물렀던 자리다.", "익명"),
        ("추억은 그리움의 또 다른 이름이다.", "익명")
    ],
    "짜증": [
        ("짜증은 잠깐의 감정일 뿐, 내가 아니다.", "익명"),
        ("마음을 다스리는 자가 세상을 다스린다.", "익명")
    ],
    "불안": [
        ("불안은 아직 오지 않은 미래를 끌어안으려는 몸부림이다.", "익명"),
        ("지금 이 순간에 집중하면 불안은 줄어든다.", "익명")
    ],
    "답답함": [
        ("답답할 땐 한 걸음 물러서서 바라보라.", "익명"),
        ("모든 길은 결국 열리게 되어 있다.", "익명")
    ],
    "지침": [
        ("지쳤다면 잠시 쉬어가도 좋다.", "익명"),
        ("쉬는 것도 노력의 일부다.", "소크라테스")
    ],
    "무기력": [
        ("작은 행동 하나가 무기력을 깨운다.", "익명"),
        ("움직이지 않으면 아무것도 변하지 않는다.", "익명")
    ],
    "회복": [
        ("회복에는 시간이 필요하다. 조급해하지 말라.", "익명"),
        ("스스로를 돌보는 것이 가장 중요한 투자다.", "익명")
    ],
    "기타": [
        ("삶은 스스로 만들어가는 모험이다.", "익명"),
        ("작은 습관이 큰 변화를 만든다.", "익명")
    ]
}

# Streamlit UI
st.set_page_config(page_title="오늘의 명언 추천", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center; color: #ff6600; font-family: "Nanum Gothic", sans-serif;'>
        🌸 오늘의 기분 일기 & 명언 추천 🌸
    </h1>
    <p style='text-align: center; color: gray; font-size:18px;'>
        오늘의 기분을 선택하면 어울리는 명언을 추천해드릴게요.
    </p>
    """,
    unsafe_allow_html=True
)

# 감정 목록
emotions = list(quotes.keys())
selected_emotion = st.radio("오늘 당신의 기분은 어떤가요?", emotions, index=0, horizontal=True)

if st.button("✨ 추천 받기 ✨", use_container_width=True):
    quote, author = random.choice(quotes[selected_emotion])
    st.markdown(
        f"""
        <div style="
            display:flex; 
            justify-content:center; 
            align-items:center; 
            height:400px; 
            background: linear-gradient(135deg, #ffecd2, #fcb69f); 
            border-radius: 20px; 
            padding: 50px;
            margin-top:30px;
            ">
            <div style="text-align:center;">
                <h2 style="font-size: 36px; color:#333;">“{quote}”</h2>
                <p style="font-size: 22px; color:#555; margin-top:20px;">– {author}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
