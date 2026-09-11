import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="군필.GG - 대한민국 장병/연예인 전적 검색 & 랭킹", page_icon="🪖", layout="wide"
)

# 세션 상태 초기화 (게시판 및 랭킹 투표 데이터)
if "board_posts" not in st.session_state:
  st.session_state.board_posts = [
      {
          "writer": "표민석",
          "title": "유격 훈련 꿀팁 공유한다",
          "content": "화이팅입니다. 각개전투 할 때 무조건 무릎 보호대 두 개 차세요.",
      },
      {
          "writer": "김다솔",
          "title": "PX 냉동만두 추천좀",
          "content": "이번에 새로 들어온 신제품 뭐가 제일 맛있나요?",
      },
  ]

# 투표 데이터 초기화
if "votes" not in st.session_state:
  st.session_state.votes = {
      "girl_group": {"브레이브걸스 (Rollin')": 1420, "뉴진스 (NewJeans)": 1150, "아이브 (IVE)": 980, "에스파 (aespa)": 890, "트와이스 (TWICE)": 750},
      "lunch": {"철판제육볶음 + 김부각": 2100, "치킨마요덮밥": 1950, "군대리아 (버거너겟 조합)": 1800, "짜장소스 + 탕수육": 1420, "삼계탕 (말년 혹은 복날)": 1100},
      "px_combo": {"슈냉(슈프림치킨 + 냉동볶음밥)": 2500, "맛다시 + 참치 + 밥 (비빔밥)": 2300, "냉동삼겹살 + 불닭볶음면": 1980, "몽쉘 + 딸기잼 + 우유 (군대리아 업그레이드)": 1450}
  }

# 커스텀 CSS (카드 디자인 및 텍스트 가독성 개선)
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
        color: #2b2b2b !important;
    }
    .jjul-card {
        border: 3px solid #9e9e9e;
        border-radius: 15px;
        padding: 20px;
        background: linear-gradient(135deg, #f1f1f1 0%, #e0e0e0 100%);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        color: #2b2b2b !important;
    }
    .exempt-card {
        border: 3px solid #607d8b;
        border-radius: 15px;
        padding: 20px;
        background: linear-gradient(135deg, #eceff1 0%, #cfd8dc 100%);
        box-shadow: 0 4px 15px rgba(96, 125, 139, 0.2);
        margin-bottom: 20px;
        color: #2b2b2b !important;
    }
    /* 카드 내부 텍스트 가독성을 위한 강제 색상 지정 */
    .hof-card p, .jjul-card p, .exempt-card p {
        color: #333333 !important;
        font-size: 15px;
    }
    .ranking-card {
        border: 2px solid #ffaa00;
        border-radius: 12px;
        padding: 15px;
        background: linear-gradient(135deg, #fffcf5 0%, #fff3d6 100%);
        margin-bottom: 12px;
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
st.caption("대한민국 국군 장병 및 연예인 복무 전적 검색 및 랭킹 플랫폼")
st.markdown("---")

# 샘플 데이터베이스 (장병 검색용)
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
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏆 종합 전당", 
    "🔍 전적 검색", 
    "📊 군대 꿀맛/인기 랭킹", 
    "🌟 연예인 현황", 
    "💬 장병 소통 게시판"
])

with tab1:
  st.subheader("🏛️ 군필.GG 종합 전당 (세로 뷰)")
  st.write("국군 최고의 전사들부터 꿀보직, 그리고 면제자들까지 한 화면에서 세로로 쭉 확인할 수 있습니다.")

  # 1. 명예의 전당 섹션
  st.markdown("### 🌟 1. 명예의 전당 (Hall of Fame)")
  st.markdown("""
        <div class="hof-card">
            <h3 style="color: #c62828; margin-top: 0;">🔥 [전설의 용사] 표민석 병장</h3>
            <p style="font-size: 15px; font-weight: bold; color: #444444;">소속: 육군 수색대대 | 타이틀: <span style="color: #d35400;">👑 유격왕</span></p>
            <hr style="border: 1px solid #ff4b4b;">
            <p style="color: #2b2b2b !important;"><b>업적:</b> 극한의 유격 훈련을 완벽히 소화하며 부대 내 전설적인 '유격왕' 타이틀 획득. 수색 작전의 에이스.</p>
        </div>
        """, unsafe_allow_html=True)

  # 2. 쩌리의 전당 섹션
  st.markdown("### 🥔 2. 쩌리의 전당 (Hall of JJUL)")
  st.markdown("""
        <div class="jjul-card">
            <h3 style="color: #424242; margin-top: 0;">💤 [관상용 용사] 김다솔 병장</h3>
            <p style="font-size: 15px; font-weight: bold; color: #444444;">소속: 육군 | 타이틀: <span style="color: #6d4c41;">💤 건빵 수집가</span></p>
            <hr style="border: 1px solid #9e9e9e;">
            <p style="color: #2b2b2b !important;"><b>업적:</b> PX 냉동식품 재고 조사 전문. 생활관 침대와 한 몸이 되어 주말마다 사단장급 숙면을 선보인 전설의 인물.</p>
        </div>
        """, unsafe_allow_html=True)
  st.markdown("""
        <div class="jjul-card">
            <h3 style="color: #424242; margin-top: 0;">🍩 [냉동 파괴자] 박성진 병장</h3>
            <p style="font-size: 15px; font-weight: bold; color: #444444;">소속: 육군 | 타이틀: <span style="color: #6d4c41;">🍩 냉동식품 마니아</span></p>
            <hr style="border: 1px solid #9e9e9e;">
            <p style="color: #2b2b2b !important;"><b>업적:</b> 야간 경계근무 후 반드시 냉동만두를 흡입하여 체중계 고장을 유발함. 운전병이지만 핸들보다 숟가락이 더 익숙했던 자.</p>
        </div>
        """, unsafe_allow_html=True)

  # 3. 면제의 전당 섹션
  st.markdown("### 🚫 3. 면제의 전당 (Hall of Exemption)")
  st.markdown("""
        <div class="exempt-card">
            <h3 style="color: #263238; margin-top: 0;">🎤 [면제 힙합퍼] 저스디스</h3>
            <p style="font-size: 15px; font-weight: bold; color: #444444;">소속: 면제 | 타이틀: <span style="color: #37474f;">🎤 힙합 국방부 장관</span></p>
            <hr style="border: 1px solid #607d8b;">
            <p style="color: #2b2b2b !important;"><b>특징:</b> 가사와 랩으로 대한민국 군문화를 평정하려 했으나, 실상은 면제 판정을 받아 리스너들의 놀림거리가 된 전설.</p>
        </div>
        """, unsafe_allow_html=True)
  st.markdown("""
        <div class="exempt-card">
            <h3 style="color: #263238; margin-top: 0;">🏋️ [조기전역의 아이콘] 스윙스</h3>
            <p style="font-size: 15px; font-weight: bold; color: #444444;">소속: 보충역 / 의가사 전역 | 타이틀: <span style="color: #37474f;">🏋️ 정신건강 조기 전역</span></p>
            <hr style="border: 1px solid #607d8b;">
            <p style="color: #2b2b2b !important;"><b>특징:</b> 현역으로 입대하였으나 심리적 사유로 의가사(복무부적합) 전역을 하며 한국 힙합계에 엄청난 밈과 파장을 남김.</p>
        </div>
        """, unsafe_allow_html=True)
  st.markdown("""
        <div class="exempt-card">
            <h3 style="color: #263238; margin-top: 0;">✈️ [레전드 귀화] 유승준 (Steve Yoo)</h3>
            <p style="font-size: 15px; font-weight: bold; color: #444444;">소속: 입국금지 | 타이틀: <span style="color: #37474f;">✈️ 아름다운 청년 (거부)</span></p>
            <hr style="border: 1px solid #607d8b;">
            <p style="color: #2b2b2b !important;"><b>특징:</b> 군대에 간다며 온국민과 약속한 뒤 입대 직전 미국 시민권을 취득하여 대한민국 국적 상실 및 영구 입국 금치 처분을 받은 역사적 인물.</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
  st.subheader("장병 및 연예인 군번 통합 검색")
  st.write("군번을 입력해 실시간 복무 전적과 타이틀을 조회합니다.")
  st.info("💡 **추천 테스트 군번**: `14-70123456` (표민석), `18-70555555` (김다솔), `19-70666666` (박성진), `00-00000001` (저스디스)")

  col_search1, col_search2 = st.columns([3, 1])
  with col_search1:
    search_id = st.text_input("군번 입력", placeholder="예: 14-70123456 또는 00-00000001", label_visibility="collapsed")
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
  st.subheader("📊 장병 피셜 군대 실시간 랭킹")
  st.write("국군 장병들이 직접 꼽은 '군통령 걸그룹', '최애 점심(짬밥) 메뉴', 그리고 'PX 전설의 물품 및 조합' 순위입니다.")

  ranking_sub_tab1, ranking_sub_tab2, ranking_sub_tab3 = st.tabs([
      "🎶 군통령 걸그룹 순위", 
      "🍲 점심(짬밥) 메뉴 순위", 
      "🛒 PX 물품 & 꿀조합 순위"
  ])

  with ranking_sub_tab1:
    st.markdown("### 👑 대한민국 국군 장병이 뽑은 군통령 걸그룹 TOP 5")
    sorted_gg = sorted(st.session_state.votes["girl_group"].items(), key=lambda x: x[1], reverse=True)
    
    for rank, (name, votes) in enumerate(sorted_gg, 1):
      medal = "🥇" if rank == 1 else ("🥈" if rank == 2 else ("🥉" if rank == 3 else "🔸"))
      st.markdown(f"""
      <div class="ranking-card">
          <h4 style="margin: 0; color: #333;">{medal} 제{rank}위: {name}</h4>
          <p style="margin: 5px 0 0 0; color: #666; font-size: 14px;">누적 지지 투표수: <b>{votes:,}표</b></p>
      </div>
      """, unsafe_allow_html=True)
    
    if st.button("💖 우리 팀(걸그룹)에 한 표 던지기 (+100표)", key="vote_gg"):
      st.session_state.votes["girl_group"]["브레이브걸스 (Rollin')"] += 100
      st.rerun()

  with ranking_sub_tab2:
    st.markdown("### 🍛 국방의 의무를 버티게 하는 점심(짬밥) 메뉴 TOP 5")
    sorted_lunch = sorted(st.session_state.votes["lunch"].items(), key=lambda x: x[1], reverse=True)

    for rank, (name, votes) in enumerate(sorted_lunch, 1):
      medal = "🥇" if rank == 1 else ("🥈" if rank == 2 else ("🥉" if rank == 3 else "🔸"))
      st.markdown(f"""
      <div class="ranking-card">
          <h4 style="margin: 0; color: #333;">{medal} 제{rank}위: {name}</h4>
          <p style="margin: 5px 0 0 0; color: #666; font-size: 14px;">장병 선호도 점수: <b>{votes:,}점</b></p>
      </div>
      """, unsafe_allow_html=True)

    if st.button("🍲 최애 점심 메뉴 투표하기 (+150표)", key="vote_lunch"):
      st.session_state.votes["lunch"]["철판제육볶음 + 김부각"] += 150
      st.rerun()

  with ranking_sub_tab3:
    st.markdown("### 🛒 PX 냉동식품 & 전설의 레시피 조합 TOP 4")
    sorted_px = sorted(st.session_state.votes["px_combo"].items(), key=lambda x: x[1], reverse=True)

    for rank, (name, votes) in enumerate(sorted_px, 1):
      medal = "🥇" if rank == 1 else ("🥈" if rank == 2 else ("🥉" if rank == 3 else "🔸"))
      st.markdown(f"""
      <div class="ranking-card">
          <h4 style="margin: 0; color: #333;">{medal} 제{rank}위: {name}</h4>
          <p style="margin: 5px 0 0 0; color: #666; font-size: 14px;">추천 및 구매 횟수: <b>{votes:,}회</b></p>
      </div>
      """, unsafe_allow_html=True)

    if st.button("🛒 PX 꿀조합 추천 누르기 (+200표)", key="vote_px"):
      st.session_state.votes["px_combo"]["슈냉(슈프림치킨 + 냉동볶음밥)"] += 200
      st.rerun()

with tab4:
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
  selected_cat = st.selectbox("조회할 부대/군종 선택", list(celebrity_board.keys()))
  for celeb in celebrity_board[selected_cat]:
    st.info(f"👤 **{celeb['name']}** — 소속: {celeb['unit']}")

with tab5:
  st.subheader("💬 장병 소통 게시판 (익명 자유게시판)")
  st.write("군생활 썰, 꿀팁, 고민 등을 자유롭게 나누는 공간입니다. (서버 세션에 실시간 저장)")

  # 글 작성 폼
  with st.form("write_form"):
    st.markdown("#### ✍️ 새 글 작성하기")
    writer_name = st.text_input("작성자 (이름 또는 계급/이름)", placeholder="예: 표민석 병장")
    post_title = st.text_input("제목", placeholder="제목을 입력하세요")
    post_content = st.text_area("내용", placeholder="내용을 입력하세요...")
    submit_btn = st.form_submit_button("게시하기")

    if submit_btn:
      if writer_name and post_title and post_content:
        st.session_state.board_posts.insert(
            0,
            {
                "writer": writer_name,
                "title": post_title,
                "content": post_content,
            },
        )
        st.success("게시글이 성공적으로 등록되었습니다!")
      else:
        st.warning("작성자, 제목, 내용을 모두 입력해주세요!")

  st.markdown("---")
  st.markdown("### 📜 실시간 올라온 글 목록")

  if len(st.session_state.board_posts) == 0:
    st.info("아직 등록된 게시글이 없습니다. 첫 글을 작성해보세요!")
  else:
    for idx, post in enumerate(st.session_state.board_posts):
      with st.expander(f"📌 [{post['writer']}] {post['title']}"):
        st.write(post["content"])
        st.caption(f"게시글 번호: #{len(st.session_state.board_posts) - idx}")

# 메인 화면 하단: 부대 마크 그리드
st.markdown("---")
st.subheader("🛡️ 대한민국 국군 부대 & 플랫폼 바로가기")

grid_cols = st.columns(5)
branches_data = [
    {"name": "육군 (ROKA)", "icon": "🛡️", "special": False},
    {"name": "해병대 (ROKMC)", "icon": "⚓", "special": False},
    {"name": "특수부대 (SWC)", "icon": "⭐", "special": True},
    {"name": "공군 (ROKAF)", "icon": "✈️", "special": False},
    {"name": "종합 랭킹 & 소통", "icon": "📊", "special": True},
]

for idx, branch in enumerate(branches_data):
  with grid_cols[idx]:
    if branch["special"]:
      st.markdown(
          f"""
            <div class="branch-box special-gold">
                <div style="font-size: 35px;">{branch['icon']}</div>
                <div class="grid-title" style="color: #b8860b;">{branch['name']}</div>
                <div style="font-size: 11px; color: #d4af37; font-weight: bold;">✨ RANKING & TALK</div>
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
