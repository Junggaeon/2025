import streamlit as st
import random

# 감정별 명언 데이터베이스
quotes = {
    "설렘": [("미래를 꿈꾸는 자에게 현재는 이미 선물이다.", "알베르트 아인슈타인"),
             ("무엇이든 할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "시어도어 루즈벨트")],
    "감사": [("감사는 고결한 영혼의 표시이다.", "에소푸스"),
             ("우리가 감사할 줄 알 때, 행복은 이미 우리 곁에 있다.", "에픽테토스")],
    "만족": [("만족은 우리가 가질 수 있는 가장 큰 부이다.", "소크라테스"),
             ("행복은 우리가 원하는 것을 가지는 것이 아니라, 가진 것을 원하는 것이다.", "오스카 와일드")],
    "기쁨": [("기쁨은 나눌수록 커진다.", "생텍쥐페리"),
             ("순수한 기쁨은 언제나 단순한 것에서 온다.", "톨스토이")],
    "즐거움": [("즐거움은 우리 삶을 지탱하는 가장 큰 힘이다.", "니체"),
               ("즐거움은 사랑과 지혜의 결실이다.", "토마스 아퀴나스")],
    "우울": [("우리가 두려워해야 할 것은 오직 두려움 그 자체뿐이다.", "프랭클린 D. 루즈벨트"),
             ("이 또한 지나가리라.", "페르시아 속담")],
    "외로움": [("고독은 위대한 정신의 학교이다.", "괴테"),
               ("외로움은 위대한 영혼이 지불해야 하는 대가다.", "쇼펜하우어")],
    "그리움": [("추억은 마음의 보물창고다.", "토마스 풀러"),
               ("우정은 떨어져 있어도 그리움으로 연결된다.", "아리스토텔레스")],
    "짜증": [("분노는 바보의 가슴 속에서만 오래 산다.", "알버트 아인슈타인"),
             ("화를 내는 것은 독을 마시고 상대가 죽기를 바라는 것과 같다.", "붓다")],
    "불안": [("불안은 자유의 현기증이다.", "키르케고르"),
             ("걱정은 내일의 슬픔을 덜어주지 못하고 오늘의 힘만 앗아간다.", "코리 텐 붐")],
    "답답함": [("어두운 밤일수록 별은 더 빛난다.", "찰스 A. 비어드"),
               ("고난은 종종 평범한 사람을 비범한 운명으로 이끈다.", "C.S. 루이스")],
    "지침": [("휴식은 게으름이 아니라 준비다.", "아리스토텔레스"),
             ("몸은 잠시 쉬어도, 마음은 더 강해진다.", "마하트마 간디")],
    "무기력": [("천 리 길도 한 걸음부터 시작된다.", "노자"),
               ("작은 행동이 세상을 바꿀 수 있다.", "달라이 라마")],
    "회복": [("상처는 회복될 때 더 강해진다.", "헤밍웨이"),
             ("시간은 모든 상처를 치유한다.", "소포클레스")],
    "기타": [("삶은 자기를 발견하는 여정이다.", "간디"),
             ("가장 큰 영광은 한 번도 실패하지 않는 것이 아니라, 실패할 때마다 다시 일어서는 것이다.", "넬슨 만델라")]
}

# 응원의 말 리스트
encouragements = [
    "🌸 오늘도 당신을 응원합니다!",
    "😊 작은 기쁨이 큰 행복으로 이어지길 바랍니다.",
    "💪 힘든 하루였다면, 내일은 더 밝게 빛날 거예요.",
    "🌈 당신의 마음이 언제나 평온하기를 바랍니다.",
    "☀️ 행복한 하루가 계속되길 바랄게요."
]

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
  animation: sparkle 1.5s ease-in-out 1; /* 한 번만 실행 */
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
  font-size: 36px;
  font-weight: bold;
  color: #2c3e50;
  line-height: 1.4;
}
.quote-author {
  font-size: 22px;
  color: #34495e;
  margin-top: 15px;
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

# 감정 선택
emotions = list(quotes.keys())
selected_emotion = st.radio("오늘 당신의 기분은 어떤가요?", emotions, index=0, horizontal=True)

# 카드 출력용 컨테이너
card_placeholder = st.empty()

# 버튼 클릭 시 카드 출력
if st.button("🌟 추천 받기 🌟", use_container_width=True):
    # 랜덤 명언 + 응원
    quote, author = random.choice(quotes[selected_emotion])
    encouragement = random.choice(encouragements)

    # 카드 새로 렌더링
    card_placeholder.markdown(f"""
    <div class="sparkle-card">
      <div>
        <div class="quote-text">“{quote}”</div>
        <div class="quote-author">– {author} –</div>
        <div class="quote-extra">{encouragement}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
