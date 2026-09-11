import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="군필.GG - 대한민국 장병/연예인 전적 검색", page_icon="🪖", layout="wide"
)

# 커스텀 CSS (특수부대 금색 테두리 및 명예의 전당 스타일)
st.markdown(
    """
    <style>
    .branch-box {
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        background-color: #ffffff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }
    .branch-box:hover {
        transform: translateY(-5px);
    }
    .special-gold {
        border: 3px solid #FFD700 !important;
        background: linear-gradient(135deg, #fffdf0 0%, #fff8d6 100%) !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4) !important;
    }
    .hof-card {
        border: 3px solid #ff4b4b;
        border-radius: 15px;
        padding: 20px;
        background: linear-gradient(135deg, #fff5f5 0%, #ffe3e3 100%);
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2);
        margin-bottom: 20px;
    }
    .grid-title {
        font-weight: bold;
        font-size: 16px;
        margin-top: 8px;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 상단 타이틀
st.title("🪖 군필.GG (Gunpil.GG)")
st.caption("대한민국 국군 장병 및 연예인 복무 전적 검색 플랫폼")
st.markdown("---")

# 샘플 데이터베이스 (표민석 포함)
soldier_database = {
    "14-70123456": {
        "name": "표민석",
        "branch": "육군 수색대대",
        "rank": "병장 (만기전역)",
        "unit": "제X사단 수색대대",
        "period": "2014.03.10 ~ 2015.12.09",
        "status": "전역 완료 (명예의 전당)",
        "title": "👑 유격왕 (Legendary Ranger)",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=PyoMinseok",
    },
    "20-71012345": {
        "name": "김석진 (진)",
        "branch": "육군",
        "rank": "병장 (만기전역)",
        "unit": "제5보병사단 신병교육대 조교",
        "period": "2022.12.13 ~ 2024.06.12",
        "status": "전역 완료",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=Jin",
    },
    "21-72054321": {
        "name": "이찬혁",
        "branch": "해병대",
        "rank": "병장 (만기전역)",
        "unit": "제1해병사단",
        "period": "2017.09.18 ~ 2019.06.17",
        "status": "전역 완료",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=Chanhyuk",
    },
    "17-73098765": {
        "name": "이승기",
        "branch": "특수부대",
        "rank": "병장 (만기전역)",
        "unit": "육군 특수전사령부 (특전사)",
        "period": "2016.02.01 ~ 2017.10.31",
        "status": "전역 완료",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=Seunggi",
    },
}

# 탭 메뉴 구성 (명예의 전당 추가)
tab1, tab2, tab3 = st.tabs(
    ["🏆 명예의 전당", "🔍 전적 검색 (군번)", "🌟 연예인 복무 랭킹/현황판"]
)

with tab1:
  st.subheader("🏆 군필.GG 명예의 전당 (Hall of Fame)")
  st.write(
      "엄격한 심사와 전설적인 업적을 세운 대한민국 국군의 최고 전사들을"
      " 소개합니다."
  )

  # 표민석 명예의 전당 카드 출력
  st.markdown(
      """
        <div class="hof-card">
            <h2 style="color: #d32f2f; margin-top: 0;">🔥 [전설의 용사] 표민석 병장</h2>
            <p style="font-size: 16px; font-weight: bold; color: #555;">소속: 육군 수색대대 | 타이틀: <span style="color: #ff8c00;">👑 유격왕</span></p>
            <hr style="border: 1px solid #ff4b4b;">
            <p><b>업적 설명:</b> 극한의 유격 훈련을 완벽히 소화하며 부대 내 전설적인 '유격왕' 타이틀을 획득. 적진 침투 및 수색 작전의 에이스로 활약함.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  col_hof1, col_hof2 = st.columns(2)
  with col_hof1:
    st.info("🎯 **특기사항**: 수색대대 실전 훈련 우수 포상 다수 수여")
  with col_hof2:
    st.success("🎖️ **인증 군번**: `14-70123456` (검색 가능)")

with tab2:
  st.subheader("장병 및 연예인 군번 통합 검색")
  st.write("군번을 입력해 실시간 복무 전적과 타이틀을 조회합니다.")
  st.info("💡 **추천 테스트 군번**: `14-70123456` (표민석), `20-71012345` (진)")

  col_search1, col_search2 = st.columns([3, 1])
  with col_search1:
    search_id = st.text_input(
        "군번 입력",
        placeholder="예: 14-70123456",
        label_visibility="collapsed",
    )
  with col_search2:
    search_btn = st.button("전적 검색", use_container_width=True)

  if search_btn or search_id:
    if search_id in soldier_database:
      info = soldier_database[search_id]
      st.success(f"성공! '{info['name']}'님의 전적 데이터 로드 완료.")

      c1, c2, c3 = st.columns([1, 2, 2])
      with c1:
        st.image(info["img"], width=120)
      with c2:
        st.markdown(f"### {info['name']}")
        st.write(f"🏷️ **군종**: {info['branch']}")
        st.write(f"🎖️ **계급**: {info['rank']}")
        if "title" in info:
          st.markdown(f"🔥 **특별 칭호**: {info['title']}")
      with c3:
        st.metric(label="복무 상태", value=info["status"])
        st.write(f"🏢 **부대**: {info['unit']}")
        st.write(f"📅 **기간**: {info['period']}")
    elif search_id:
      st.warning("등록되지 않은 군번입니다. 상단의 테스트 군번을 확인해 보세요!")

with tab3:
  st.subheader("🌟 부대별 연예인 복무 현황판")
  celebrity_board = {
      "육군": [
          {"name": "김석진 (진)", "unit": "제5보병사단 조교"},
          {"name": "남주혁", "unit": "제32보병사단 군사경찰단"},
      ],
      "해병대": [
          {"name": "이찬혁", "unit": "제1해병사단"},
          {"name": "표지훈 (P.O)", "unit": "해병대 군악대"},
      ],
      "특수부대 (★)": [
          {"name": "이승기", "unit": "특수전사령부 (특전사)"},
          {"name": "박군 (박준우)", "unit": "특수전사령부 상사"},
      ],
      "공군": [
          {"name": "조인성", "unit": "공군작전사령부 군악"},
          {"name": "지진희", "unit": "공군 자원입대"},
      ],
  }
  selected_cat = st.selectbox(
      "조회할 부대/군종 선택", list(celebrity_board.keys())
  )
  for celeb in celebrity_board[selected_cat]:
    st.info(f"👤 **{celeb['name']}** — 소속: {celeb['unit']}")

# 메인 화면 하단: 부대 마크 그리드 (특수부대 금색 테두리)
st.markdown("---")
st.subheader("🛡️ 대한민국 국군 부대 & 특수부대 바로가기")

grid_cols = st.columns(5)
branches_data = [
    {"name": "육군 (ROKA)", "icon": "🛡️", "special": False},
    {"name": "해병대 (ROKMC)", "icon": "⚓", "special": False},
    {"name": "특수부대 (SWC)", "icon": "⭐", "special": True},
    {"name": "공군 (ROKAF)", "icon": "✈️", "special": False},
    {"name": "수색대대 (HOF)", "icon": "👑", "special": True},
]

for idx, branch in enumerate(branches_data):
  with grid_cols[idx]:
    if branch["special"]:
      st.markdown(
          f"""
            <div class="branch-box special-gold">
                <div style="font-size: 35px;">{branch['icon']}</div>
                <div class="grid-title" style="color: #b8860b;">{branch['name']}</div>
                <div style="font-size: 11px; color: #d4af37; font-weight: bold;">✨ ELITE EDITION</div>
            </div>
            """,
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          f"""
            <div class="branch-box">
                <div style="font-size: 35px;">{branch['icon']}</div>
                <div class="grid-title">{branch['name']}</div>
                <div style="font-size: 11px; color: #888;">상태: 정상 복무</div>
            </div>
            """,
          unsafe_allow_html=True,
      )
