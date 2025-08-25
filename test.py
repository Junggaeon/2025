import streamlit as st
import random

st.set_page_config(page_title="오늘의 명언 추천", layout="wide")

# 반짝이는 카드 CSS
st.markdown("""
<style>
@keyframes sparkle {
  0% { box-shadow: 0 0 10px rgba(255,255,255,0.3); }
  50% { box-shadow: 0 0 25px rgba(255,255,255,0.8); }
  100% { box-shadow: 0 0 10px rgba(255,255,255,0.3); }
}
.sparkle-card {
  animation: sparkle 1.5s ease-in-out 1;
  border-radius: 25px;
  padding: 60px;
  background: linear-gradient(135deg, #f6d365, #fda085);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin-top: 40px;
}
.quote-text {
  font-size: 30px;
  font-weight: bold;
  color: #2c3e50;
  line-height: 1.4;
  margin-bottom: 10px;
}
.quote-author {
  font-size: 20px;
  color: #34495e;
  margin-bottom: 25px;
}
.quote-extra {
  font-size: 20px;
  color: #16a085;
  margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown("""
<h1 style='text-align:center; color:#ff6600; font-family:"Nanum Gothic", sans-serif; font-size:50px;'>
✨ 오늘의 기분 & 명언 ✨
</h1>
<p style='text-align:center; color:gray; font-size:18px;'>
오늘의 기분을 선택하면 어울리는 명언과 응원의 말을 드려요 🌷
</p>
""", unsafe_allow_html=True)

# 감정 & 명언 데이터 (12개 감정, 명언 2~3개씩)
quotes = {
    "기쁨": [
        ("행복은 준비된 자에게 온다.", "파스퇴르"),
        ("큰 기쁨은 작은 감사에서 시작된다.", "에픽테토스"),
        ("웃음은 영혼의 햇살이다.", "토마스 모어")
    ],
    "슬픔": [
        ("슬픔은 영혼을 깊게 만든다.", "칼 융"),
        ("눈물은 마음의 언어다.", "볼테르"),
        ("고통 없는 성장은 없다.", "어니스트 헤밍웨이")
    ],
    "분노": [
        ("분노는 바람과 같아, 모든 것을 무너뜨린다.", "셰익스피어"),
        ("화를 다스리는 자가 세상을 다스린다.", "공자"),
        ("분노를 품으면 두 번 죽는다.", "불교 경전")
    ],
    "두려움": [
        ("우리가 두려워해야 할 것은 두려움 그 자체뿐이다.", "프랭클린 루스벨트"),
        ("두려움은 용기의 출발점이다.", "에리카 종"),
        ("용기는 두려움의 부재가 아니라, 그것을 극복하는 것이다.", "넬슨 만델라")
    ],
    "놀람": [
        ("놀라움은 호기심의 시작이다.", "아리스토텔레스"),
        ("호기심이 위대한 발견을 만든다.", "아인슈타인")
    ],
    "사랑": [
        ("사랑은 두 영혼이 하나로 자라는 것이다.", "플라톤"),
        ("사랑은 세상에서 가장 강력한 힘이다.", "간디"),
        ("사랑은 나눌수록 커진다.", "생텍쥐페리")
    ],
    "혐오": [
        ("혐오는 무지에서 비롯된다.", "에픽테토스"),
        ("타인을 미워하는 것은 결국 자신을 해치는 것이다.", "부처"),
        ("증오는 무거운 짐이다.", "마틴 루터 킹")
    ],
    "희망": [
        ("희망은 깨어 있는 꿈이다.", "아리스토텔레스"),
        ("희망은 영혼의 닻이다.", "히브리서"),
        ("어두운 밤에도 별은 빛난다.", "빅토르 위고")
    ],
    "자신감": [
        ("자신감을 가지면 반은 성공이다.", "세오도르 루스벨트"),
        ("믿음은 산을 옮긴다.", "성경"),
        ("자신을 믿는 순간 길이 열린다.", "괴테")
    ],
    "외로움": [
        ("외로움은 인간의 본질이다.", "장 폴 사르트르"),
        ("혼자 있을 줄 아는 사람이 진정 자유롭다.", "니체"),
        ("외로움은 자기 자신과의 만남이다.", "칼 융")
    ],
    "안도": [
        ("평화는 미소에서 시작된다.", "마더 테레사"),
        ("마음이 고요하면 세상도 고요하다.", "노자"),
        ("안도는 신뢰에서 나온다.", "에픽테토스")
    ],
    "불안": [
        ("불안은 자유의 현기증이다.", "키에르케고르"),
        ("내일을 두려워하지 마라, 오늘이 너의 것이다.", "호라티우스"),
        ("불안은 준비된 자에게 기회가 된다.", "에머슨")
    ]
}

encouragements = [
    "당신은 이미 충분히 잘하고 있어요 💪",
    "오늘도 당신의 하루가 반짝이길 바랍니다 ✨",
    "조금 느려도 괜찮아요, 당신만의 속도로 🌷",
    "힘든 날도 결국 지나갑니다 ☀️",
    "당신의 가능성은 무한해요 🚀"
]

# 감정 선택
emotions = list(quotes.keys())
selected_emotion = st.radio("오늘 당신의 기분은 어떤가요?", emotions, index=0, horizontal=True)

# 버튼 클릭 시 명언 카드 출력
if st.button("🌟 추천 받기 🌟", use_container_width=True):
    quote, author = random.choice(quotes[selected_emotion])
    encouragement = random.choice(encouragements)

    st.markdown(f"""
    <div class="sparkle-card">
      <div>
        <div class="quote-text">“{quote}”</div>
        <div class="quote-author">– {author} –</div>
        <div class="quote-extra">{encouragement}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
