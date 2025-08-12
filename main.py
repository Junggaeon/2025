import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="MBTI 직업 추천", layout="wide")

# --- 스타일 (CSS) -------------------------------------------------
st.markdown(
    """
    <style>
    /* 배경 그라디언트 */
    .stApp {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 25%, #fbc2eb 50%, #a6c1ee 100%);
        background-attachment: fixed;
    }
    /* 카드 스타일 */
    .mbti-card{
        background: rgba(255,255,255,0.85);
        border-radius: 16px;
        padding: 20px 24px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    .title-anim{
        font-size: 48px;  /* 기존 40px -> 48px */
        font-weight:700;
        letter-spacing:1px;
        animation: glow 2.5s ease-in-out infinite alternate;
        margin-bottom: 0.1em;
    }
    @keyframes glow{
        from {text-shadow: 0 0 6px rgba(255,255,255,0.6);} 
        to {text-shadow: 0 0 20px rgba(255,255,255,0.95);} 
    }
    .small-muted{color:#555;font-size:14px;}
    .mbti-card h2, .mbti-card h3 {
        font-size: 26px;
        margin-bottom: 0.2em;
    }
    .mbti-card p, .mbti-card li {
        font-size: 18px;
        line-height: 1.5em;
    }
    ul.job-list {
        padding-left: 20px;
        margin-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- MBTI 데이터 (설명 + 직업 목록 + 이미지 URL) -------------------
mbti_data = {
    "INTJ": {
        "설명": "전략적 사고와 장기 계획을 잘 세우며 복잡한 문제를 체계적으로 해결합니다.",
        "직업": [
            "데이터 사이언티스트", "전략 컨설턴트", "연구원", "R&D 매니저",
            "투자 분석가", "도시 계획가", "기술 개발자", "시스템 아키텍트"
        ],
        "이미지": "https://images.unsplash.com/photo-1581090700227-4c4f50b1d6d5"
    },
    "INTP": {
        "설명": "호기심이 많고 분석적인 사고로 새로운 가능성을 탐구합니다.",
        "직업": [
            "연구 개발자", "소프트웨어 엔지니어", "발명가", "데이터 엔지니어",
            "시스템 설계자", "AI 연구원", "과학 저널리스트"
        ],
        "이미지": "https://images.unsplash.com/photo-1518770660439-4636190af475"
    },
    "ENTJ": {
        "설명": "결단력 있고 조직을 효율적으로 이끄는 리더형입니다.",
        "직업": [
            "경영자", "프로젝트 매니저", "정치가", "경영 컨설턴트",
            "사업개발 총괄", "기업 전략가", "벤처 캐피탈리스트"
        ],
        "이미지": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a"
    },
    "ENTP": {
        "설명": "창의적이고 논리적 토론을 즐기며 새로운 아이디어를 구현합니다.",
        "직업": [
            "창업가", "마케팅 전략가", "방송인", "혁신 컨설턴트",
            "벤처 투자자", "광고 크리에이터", "기술 전략가"
        ],
        "이미지": "https://images.unsplash.com/photo-1551836022-d5d88e9218df"
    },
"INFJ": {
    "설명": "깊이 있는 통찰과 이상주의로 사람들의 성장을 돕습니다.",
    "직업": [
        "심리상담사", "작가", "인권운동가", "교육 컨설턴트",
        "브랜드 전략가", "사회 연구원", "종교 지도자"
    ],
    "이미지": "https://images.unsplash.com/photo-1507679799987-c73779587ccf"
},
    "INFP": {
        "설명": "가치와 신념을 중시하며 창의적으로 변화를 만듭니다.",
        "직업": [
            "소설가", "예술가", "NGO 활동가", "번역가",
            "콘텐츠 크리에이터", "편집자", "시인"
        ],
        "이미지": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2"
    },
    "ENFJ": {
        "설명": "사람들의 잠재력을 이끌어내고 협력을 조직하는 데 능합니다.",
        "직업": [
            "교사", "리더십 코치", "홍보 전문가", "HR 매니저",
            "문화 기획자", "공공 관계 전문가", "사회 운동가"
        ],
        "이미지": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
    },
    "ENFP": {
        "설명": "에너지가 넘치고 창의적인 아이디어로 사람들을 고무시키는 타입입니다.",
        "직업": [
            "광고 기획자", "크리에이티브 디렉터", "이벤트 기획자", "콘텐츠 크리에이터",
            "관광 가이드", "작가", "사회 활동가"
        ],
        "이미지": "https://images.unsplash.com/photo-1492724441997-5dc865305da7"
    },
    "ISTJ": {
        "설명": "책임감이 강하고 체계적으로 일을 처리하는 타입입니다.",
        "직업": [
            "회계사", "법률가", "행정 공무원", "감사원",
            "품질 관리자", "재무 분석가", "프로젝트 관리자"
        ],
        "이미지": "https://images.unsplash.com/photo-1554224154-22dec7ec8818"
    },
    "ISFJ": {
        "설명": "타인을 돕고 안정적인 환경을 유지하는 데 헌신합니다.",
        "직업": [
            "간호사", "사회복지사", "사서", "보육교사",
            "의료 행정", "고객 서비스 매니저", "교회 봉사자"
        ],
        "이미지": "https://images.unsplash.com/photo-1588776814546-8a1d9e49637e"
    },
    "ESTJ": {
        "설명": "실용적이고 조직적인 방식으로 목표를 달성하는 리더형입니다.",
        "직업": [
            "경영 관리자", "군 장교", "프로젝트 리더", "운영 관리자",
            "행정 책임자", "품질 관리자", "법 집행관"
        ],
        "이미지": "https://images.unsplash.com/photo-1556740738-b6a63e27c4df"
    },
    "ESFJ": {
        "설명": "사람들을 돌보고 조화로운 관계를 만드는 데 능합니다.",
        "직업": [
            "간호사", "교사", "이벤트 플래너", "고객 서비스 매니저",
            "커뮤니티 매니저", "행사 코디네이터", "판매 대표"
        ],
        "이미지": "https://images.unsplash.com/photo-1521790361488-9e74f2f2e6a1"
    },
    "ISTP": {
        "설명": "문제 해결과 기술 습득에 능한 실용주의자입니다.",
        "직업": [
            "엔지니어", "정비사", "응급 구조사", "드론 조종사",
            "시스템 정비 엔지니어", "기계 기사", "자동차 기술자"
        ],
        "이미지": "https://images.unsplash.com/photo-1591696205602-2f950c417cb9"
    },
    "ISFP": {
        "설명": "예술적 감각이 뛰어나고 감정을 섬세하게 표현합니다.",
        "직업": [
            "사진작가", "디자이너", "음악가", "플로리스트",
            "핸드메이드 작가", "일러스트레이터", "무대 미술가"
        ],
        "이미지": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
    },
    "ESTP": {
        "설명": "도전과 변화를 즐기며 즉흥적으로 문제를 해결합니다.",
        "직업": [
            "기업가", "스포츠 코치", "세일즈 전문가", "현장 관리자",
            "방송 리포터", "응급 의료 기술자", "부동산 중개인"
        ],
        "이미지": "https://images.unsplash.com/photo-1521412644187-c49fa049e84d"
    },
    "ESFP": {
        "설명": "사람들과 함께 즐기고 새로운 경험을 만드는 것을 좋아합니다.",
        "직업": [
            "배우", "이벤트 진행자", "여행 가이드", "퍼포머",
            "모델", "뮤지션", "파티 플래너"
        ],
        "이미지": "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91"
    }
}

# --- UI : 타이틀 영역 -----------------------------------------------
col1, col2 = st.columns([3,1])
with col1:
    st.markdown('<div class="title-anim">MBTI 기반 직업 추천</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-muted">당신의 MBTI에 어울리는 다양한 분야의 직업과 간단한 설명을 제공합니다.</div>', unsafe_allow_html=True)
with col2:
    st.image('https://images.unsplash.com/photo-1499951360447-b19be8fe80f5', width=140)

st.markdown("---")

# --- 선택 UI -------------------------------------------------------
mbti_list = list(mbti_data.keys())
selected = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list, index=mbti_list.index('ENFP'))

# --- 결과 카드 -----------------------------------------------------
if selected in mbti_data:
    data = mbti_data[selected]
    left_col, right_col = st.columns([2,3])
    with left_col:
        st.markdown('<div class="mbti-card">', unsafe_allow_html=True)
        st.markdown(f"<h2>{selected} — {data['설명']}</h2>", unsafe_allow_html=True)
        st.markdown("**추천 직업 (다양한 분야):**")
        st.markdown("<ul class='job-list'>", unsafe_allow_html=True)
        for job in data['직업']:
            st.markdown(f"<li>{job}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="mbti-card">', unsafe_allow_html=True)
        st.markdown("**이미지 예시**")
        try:
            resp = requests.get(data['이미지'] + '?auto=format&fit=crop&w=1200&q=80', timeout=6)
            img = Image.open(BytesIO(resp.content))
            st.image(img, caption=f"{selected} 컨셉 이미지", use_column_width=True)
        except Exception:
            st.info("이미지를 불러오지 못했습니다. 네트워크를 확인하거나 로컬 이미지를 사용하세요.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.write("원한다면 이 직업군별로 더 자세한 스킬, 추천 전공, 관련 자격증 정보도 추가해줄게요.")
else:
    st.warning("데이터가 없습니다.")

# --- 하단 : 사용 팁 ------------------------------------------------
with st.expander("사용 팁과 커스터마이징 방법 (열기)"):
    st.write("- 이미지 교체: Unsplash나 Pexels에서 원하는 이미지를 찾아 '이미지' URL을 바꾸세요.")
    st.write("- 로컬 이미지 사용: 프로젝트 폴더에 images/ 폴더를 만들고 st.image(f'images/{selected}.jpg')로 로드하세요.")
    st.write("- 디자인 변경: 상단 CSS 블록을 수정하여 색상, 그림자, 글꼴 등을 바꿀 수 있습니다.")

# --- 실행 안내 -----------------------------------------------------
st.markdown('<div class="small-muted">실행: 터미널에서 <code>streamlit run mbti_streamlit_app.py</code></div>', unsafe_allow_html=True)
