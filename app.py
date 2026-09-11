import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="군필.GG - 대한민국 장병/연예인 전적 검색", page_icon="🪖", layout="wide"
)

# 커스텀 CSS (세로 정렬 및 각 전당 카드 스타일링)
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
    .jjul-card {
        border: 3px solid #9e9e9e;
        border-radius: 15px;
        padding: 20px;
        background: linear-gradient(135deg, #f1f1f1 0%, #e0e0e0 100%);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .exempt-card {
        border: 3px solid #607d8b;
        border-radius: 15px;
        padding: 20px;
        background: linear-gradient(135deg, #eceff1 0%, #cfd8dc 100%);
        box-shadow: 0 4px 15px rgba(96, 125, 139, 0.2);
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

# 샘플 데이터베이스
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
    "18-70555555": {
        "name": "김다솔",
        "branch": "육군 (취사병/행정)",
        "rank": "병장 (조기진급 누락)",
        "unit": "어딘가의 꿀보직",
        "period": "2018.05.01 ~ 2020.01.01",
        "status": "전역 완료 (쩌리의 전당)",
        "title": "💤 건빵 수집가",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=KimDasol",
    },
    "19-70666666": {
        "name": "박성진",
        "branch": "육군 (운전병)",
        "rank": "상병 연장선",
        "unit": "수송부",
        "period": "2019.06.01 ~ 2021.03.01",
        "status": "전역 완료 (쩌리의 전당)",
        "title": "🍩 냉동식품 마니아",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=ParkSungjin",
    },
    "00-00000001": {
        "name": "저스디스 (JUSTHIS)",
        "branch": "면제 / 공익 논란",
        "rank": "면제",
        "unit": "해당 없음 (면제)",
        "period": "없음",
        "status": "면제 (면제의 전당)",
        "title": "🎤 힙합 국방부 장관 (말만)",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=Justhis",
    },
    "00-00000002": {
        "name": "스윙스 (Swings)",
        "branch": "제2국민역 (현역 조기전역)",
        "rank": "이병 (의가사 전역)",
        "unit": "보충역 전환 / 면제 사유 보유",
        "period": "2014.11 ~ 2015.09",
        "status": "조기전역 (면제의 전당)",
        "title": "🏋️ 멘탈치료 / 정신건강 면제",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=Swings",
    },
    "00-00000003": {
        "name": "유승준 (Steve Yoo)",
        "branch": "입국 금지",
        "rank": "없음",
        "unit": "미국 국적 취득으로 인한 입국제한",
        "period": "없음",
        "status": "입국금지 (면제의 전당)",
        "title": "✈️ 아름다운 청년(?) / 입국 거부",
        "img": "https://api.dicebear.com/7.x/avataaars/svg?seed=SteveYoo",
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
}

# 탭 메뉴 구성
tab1, tab2, tab3 = st.tabs(
    ["🏆 명예/쩌리/면제의 전당", "🔍 전적 검색 (군번)", "🌟 연예인 복무 랭킹/현황판"]
)

with tab1:
  st.subheader("🏛️ 군필.GG 종합 전당 (세로 뷰)")
  st.write(
      "국군 최고의 전사들부터 꿀보직, 그리고 면제자들까지 한 화면에서 세로로"
      " 쭉 확인할 수 있습니다."
  )

  # 1. 명예의 전당 섹션
  st.markdown("### 🌟 1. 명예의 전당 (Hall of Fame)")
  st.markdown(
      """
        <div class="hof-card">
            <h3 style="color: #d32f2f; margin-top: 0;">🔥 [전설의 용사] 표민석 병장</h3>
            <p style="font-size: 15px; font-weight: bold; color: #555;">소속: 육군 수색대대 | 타이틀: <span style="color: #ff8c00;">👑 유격왕</span></p>
            <hr style="border: 1px solid #ff4b4b;">
            <p><b>업적:</b> 극한의 유격 훈련을 완벽히 소화하며 부대 내 전설적인 '유격왕' 타이틀 획득. 수색 작전의 에이스.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # 2. 쩌리의 전당 섹션
  st.markdown("### 🥔 2. 쩌리의 전당 (Hall of JJUL)")
  st.markdown(
      """
        <div class="jjul-card">
            <h3 style="color: #616161; margin-top: 0;">💤 [관상용 용사] 김다솔 병장</h3>
            <p style="font-size: 15px; font-weight: bold; color: #555;">소속: 육군 | 타이틀: <span style="color: #795548;">💤 건빵 수집가</span></p>
            <hr style="border: 1px solid #9e9e9e;">
            <p><b>업적:</b> PX 냉동식품 재고 조사 전문. 생활관 침대와 한 몸이 되어 주말마다 사단장급 숙면을 선보인 전설의 인물.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  st.markdown(
      """
        <div class="jjul-card">
            <h3 style="color: #616161; margin-top: 0;">🍩 [냉동 파괴자] 박성진 병장</h3>
            <p style="font-size: 15px; font-weight: bold; color: #555;">소속: 육군 | 타이틀: <span style="color: #795548;">🍩 냉동식품 마니아</span></p>
            <hr style="border: 1px solid #9e9e9e;">
            <p><b>업적:</b> 야간 경계근무 후 반드시 냉동만두를 흡입하여 체중계 고장을 유발함. 운전병이지만 핸들보다 숟가락이 더 익숙했던 자.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # 3. 면제의 전당 섹션
  st.markdown("### 🚫 3. 면제의 전당 (Hall of Exemption)")
  st.markdown(
      """
        <div class="exempt-card">
            <h3 style="color: #37474f; margin-top: 0;">🎤 [면제 힙합퍼] 저스디스</h3>
            <p style="font-size: 15px; font-weight: bold; color: #555;">소속: 면제 | 타이틀: <span style="color: #455a64;">🎤 힙합 국방부 장관</span></p>
            <hr style="border: 1px solid #607d8b;">
            <p><b>특징:</b> 가사와 랩으로 대한민국 군문화를 평정하려 했으나, 실상은 면제 판정을 받아 리스너들의 놀림거리가 된 전설.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  st.markdown(
      """
        <div class="exempt-card">
            <h3 style="color: #37474f; margin-top: 0;">🏋️ [조기전역의 아이콘] 스윙스</h3>
            <p style="font-size: 15px; font-weight: bold; color: #555;">소속: 보충역 / 의가사 전역 | 타이틀: <span style="color: #455a64;">🏋️ 정신건강 조기 전역</span></p>
            <hr style="border: 1px solid #607d8b;">
            <p><b>특징:</b> 현역으로 입대하였으나 심리적 사유로 의가사(복무부적합) 전역을 하며 한국 힙합계에 엄청난 밈과 파장을 남김.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  st.markdown(
      """
        <div class="exempt-card">
            <h3 style="color: #37474f; margin-top: 0;">✈️ [레전드 귀화] 유승준 (Steve Yoo)</h3>
            <p style="font-size: 15px; font-weight: bold; color: #555;">소속: 입국금지 | 타이틀: <span style="color: #455a64;">✈️ 아름다운 청년 (거부)</span></p>
            <hr style="border: 1px solid #607d8b;">
            <p><b>특징:</b> 군대에 간다며 온국민과 약속한 뒤 입대 직전 미국 시민권을 취득하여 대한민국 국적 상실 및 영구 입국 금치 처분을 받은 역사적 인물.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

with tab2:
  st.subheader("장병 및 연예인 군번 통합 검색")
  st.write("군번을 입력해 실시간 복무 전적과 타이틀을 조회합니다.")
  st.info(
      "💡 **추천 테스트 군번**: `14-70123456` (표민석), `18-70555555`"
      " (김다솔), `19-70666666` (박성진), `00-00000001` (저스디스)"
  )

  col_search1, col_search2 = st.columns([3, 1])
  with col_search1:
    search_id = st.text_input(
        "군번 입력",
        placeholder="예: 14-70123456 또는 00-00000001",
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
        st.write(f"🏷️ **소속/군종**: {info['branch']}")
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

# 메인 화면 하단: 부대 마크 그리드
st.markdown("---")
st.subheader("🛡️ 대한민국 국군 부대 & 전당 바로가기")

grid_cols = st.columns(5)
branches_data = [
    {"name": "육군 (ROKA)", "icon": "🛡️", "special": False},
    {"name": "해병대 (ROKMC)", "icon": "⚓", "special": False},
    {"name": "특수부대 (SWC)", "icon": "⭐", "special": True},
    {"name": "공군 (ROKAF)", "icon": "✈️", "special": False},
    {"name": "종합 전당 세로뷰", "icon": "🏛️", "special": True},
]

for idx, branch in enumerate(branches_data):
  with grid_cols[idx]:
    if branch["special"]:
      st.markdown(
          f"""
            <div class="branch-box special-gold">
                <div style="font-size: 35px;">{branch['icon']}</div>
                <div class="grid-title" style="color: #b8860b;">{branch['name']}</div>
                <div style="font-size: 11px; color: #d4af37; font-weight: bold;">✨ HALL OF FAME</div>
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
