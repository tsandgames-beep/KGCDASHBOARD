import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 기본 설정 (가장 위에 위치해야 함)
st.set_page_config(page_title="KGC 브랜드전략실 - 3월 4주차 대시보드", layout="wide")

# 2. 커스텀 CSS (정관장 고유 색상 및 스타일 미세 조정)
st.markdown("""
    <style>
    .reportview-container .main .block-container{ max-width: 1200px; }
    .kpi-title { font-size: 14px; color: #64748b; }
    .kpi-value { font-size: 28px; font-weight: bold; color: #A6192E; }
    .kpi-value-dark { font-size: 28px; font-weight: bold; color: #1e293b; }
    .kpi-value-blue { font-size: 28px; font-weight: bold; color: #2563eb; }
    </style>
""", unsafe_allow_html=True)

# 3. 헤더 영역
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.title("📈 에브리타임 밸런스 마케팅 대시보드")
    st.markdown("**2026년 3월 4주차 | 리뉴얼 제품 판매 현황 분석**")
with col_header2:
    st.write("") # 간격 맞추기
    st.info("👤 **팀장: 인선미** (Brand Strategy)")

st.markdown("---")

# 4. KPI 카드 영역 (4개의 컬럼)
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(label="수도권 판매량", value="+15.0%", delta="전주 대비 강세")
with kpi2:
    # 델타(변화량) 색상을 비활성화하여 HTML과 유사한 회색 텍스트 효과
    st.metric(label="핵심 타겟층(2030)", value="45.0%", delta="사회초년생 구매 비중", delta_color="off")
with kpi3:
    st.metric(label="스포츠 키워드 언급", value="+30%", delta="등산/테니스 중심 급증")
with kpi4:
    st.metric(label="긍정 리뷰 비율", value="82.4%", delta="패키지/맛 만족도 상승", delta_color="off")

st.markdown("<br>", unsafe_allow_html=True)

# 5. 차트 영역 (2개의 컬럼)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("지역별 판매 성장률 (%)")
    df_region = pd.DataFrame({
        "지역": ['수도권 (편의점)', '지방 (대형마트)'],
        "성장률": [15, -2]
    })
    # 막대 그래프 (Plotly)
    fig_region = px.bar(
        df_region, x="지역", y="성장률", text="성장률", 
        color="지역", color_discrete_sequence=['#A6192E', '#94a3b8']
    )
    fig_region.update_layout(showlegend=False, margin=dict(t=20, b=20, l=0, r=0))
    st.plotly_chart(fig_region, use_container_width=True)

with chart_col2:
    st.subheader("소비자 연령대 분포")
    df_age = pd.DataFrame({
        "연령대": ['2030 사회초년생', '4050 부모세대', '기타'],
        "비중": [45, 35, 20]
    })
    # 도넛 차트 (Plotly)
    fig_age = px.pie(
        df_age, values="비중", names="연령대", hole=0.5,
        color_discrete_sequence=['#A6192E', '#C5A059', '#cbd5e1']
    )
    fig_age.update_layout(margin=dict(t=20, b=20, l=0, r=0), legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(fig_age, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. 피드백, 인사이트 및 사이드바 영역
bottom_col1, bottom_col2 = st.columns([2, 1])

with bottom_col1:
    st.subheader("💬 실시간 고객 VOC 분석")
    voc1, voc2 = st.columns(2)
    with voc1:
        st.success("**🟢 Positive**\n\n- 포장이 세련되어 선물용으로 최고입니다.\n- 기존 홍삼보다 쓴맛이 덜해서 먹기 편해요.")
    with voc2:
        st.error("**🔴 Improvement**\n\n- 리뉴얼 후 가격이 조금 오른 것 같아요.\n- **박스 개봉 시 가끔 뻑뻑함이 느껴집니다.**")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("💡 팀장 전략 제언 (Action Items)")
    st.info("""
    1. **아웃도어 마케팅:** 테니스/등산 커뮤니티 연계 '오운완' 캠페인 즉시 실행
    2. **채널 최적화:** 지방권 대형마트 '가족 건강 키트' 번들 기획 구성
    3. **품질 개선:** 패키지 개봉 편의성(Easy-off) 관련 생산 파트 피드백 전달
    """)

with bottom_col2:
    st.subheader("🔥 트렌드 키워드")
    # 마크다운을 활용한 태그 스타일링
    st.markdown("""
    `#사회초년생` `#테니스` `#오운완` `#선물추천` `#등산` `#에너지부스터`
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("##### 📌 Today's Summary")
    st.caption("2030 라이프스타일 깊숙이 침투하는 것이 이번 리뉴얼의 핵심입니다. 단순 건강기능식품을 넘어 패션과 스포츠의 영역으로 확장합시다.")
