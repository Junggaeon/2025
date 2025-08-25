import streamlit as st
import random

# 감정별 명언 데이터
quotes = {
    "행복": [
        ("행복은 준비된 자에게 찾아온다.", "파스퇴르"),
        ("행복은 우리가 가지는 것이 아니라, 우리가 느끼는 것이다.", "벤자민 프랭클린"),
        ("작은 것에 감사할 때 행복은 커진다.", "에픽테토스"),
    ],
    "슬픔": [
        ("눈물은 슬픔의 언어이다.", "볼테르"),
        ("슬픔은 지나가지만, 그 흔적은 마음에 남는다.", "셰익스피어"),
        ("어둠이 없다면 별도 빛나지 않는다.", "찰리 채플린"),
    ],
    "분노": [
        ("분노는 바람처럼 모든 것을 휩쓴다.", "셰익스피어"),
        ("분노는 한순간의 광기다.", "호라티우스"),
        ("분노를 다스리는 자가 가장 강한 자다.", "공자"),
    ],
    "불안": [
        ("불안은 우리가 아직 미래를 믿지 못하기 때문이다.", "키에르케고르"),
        ("용기란 불안 속에서도 앞으로 나아가는 것이다.", "테오도르 루스벨트"),
        ("불안은 마음의 그림자일 뿐이다.", "무명"),
    ],
    "사랑": [
        ("사랑은 서로 마주보는 것이 아니라, 같은 방향을 바라보는 것이다.", "생텍쥐페리"),
        ("사랑은 나눌수록 커진다.", "파울로 코엘료"),
        ("사랑은 영혼의 햇살이다.", "빅토르 위고"),
    ],
    "외로움": [
        ("외로움은 가장 충실한 친구이다.", "헤밍웨이"),
        ("외로움은 우리를 성숙하게 만든다.", "칼 융"),
        ("가장 큰 고독은 사람들 속에서 느낀다.", "괴테"),
    ],
    "희망": [
        ("희망은 깨어있는 꿈이다.", "아리스토텔레스"),
        ("희망은 영혼의 닻이다.", "에픽테토스"),
        ("희망은 절망의 반대말이다.", "무명"),
    ],
    "두려움": [
        ("두려움은 우리가 상상으로 만든 괴물이다.", "세네카"),
        ("두려움을 극복하는 순간 자유를 얻는다.", "넬슨 만델라"),
        ("두려움은 용기의 시작이다.", "무명"),
    ],
    "자신감": [
        ("자신감을 가지면 이미 반은 성공한 것이다.", "시어도어 루스벨트"),
        ("자신감을 가진 사람은 세상을 움직인다.", "에머슨"),
        ("믿음은 자신감의 또 다른 이름이다.", "무명"),
    ],
    "감사": [
        ("감사는 마음의 기억이다.", "장자크 루소"),
        ("감사는 행복을 배가시킨다.", "에픽테토스"),
        ("감사하는 마음은 기적을 부른다.", "오프라 윈프리"),
    ],
}

encouragements = [
    "오늘도 충분히 잘하고 있어요 🌸",
    "당신의 하루에 작은 기적이 찾아올 거예요 ✨",
    "스스로를 믿으세요, 당신은 충분히 멋진 사람이에요 💪",
    "조금씩 나아가면 돼요, 멈추지만 않는다면 🌈",
]

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 명언 추천", layout="wide")

# CSS (수정 전 기본 디자인 유지)
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
  padding: 40px;
  background: linear-gradient(135deg, #f6d365, #fda085);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin-top: 30px;
}
.quote-text {
  font-size: 28px;
  font-weight: bold;
  color: #2c3e50;
  line-height: 1.4;
}
.quote-author {
  font-size: 20px;
  color: #34495e;
  margin-top: 10px;
}
.quote-extra {
  font-size: 18px;
  color: #16a085;
  margin-top: 15px;
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

# 감정 선택
emotions = list(quotes.keys())
selected_emotion = st.radio("오늘 당신의 기분은 어떤가요?", emotions, index=0, horizontal=True)

# 버튼 클릭 시 명언 카드 출력
if st.button("🌟 추천 받기 🌟", use_container_width=True):
    # 감정별로 명언 2~3개 랜덤 선택
    selected_quotes = random.sample(quotes[selected_emotion], k=min(3, len(quotes[selected_emotion])))
    encouragement = random.choice(encouragements)

    for q, a in selected_quotes:
        st.markdown(f"""
        <div class="sparkle-card">
          <div>
            <div class="quote-text">“{q}”</div>
            <div class="quote-author">– {a} –</div>
            <div class="quote-extra">{encouragement}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
