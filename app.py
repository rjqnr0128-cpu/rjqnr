import streamlit as st

# OP.GG 스타일의 상단 검색 바 흉내내기
st.title("🎮 LOL Search (OP.GG 스타일 모형)")
st.write("소환사명을 입력하여 전적을 검색해보세요.")

# 검색 입력창
summoner_name = st.text_input(
    "소환사명 + 태그라인", placeholder="예: Hide on bush#KR1"
)

if st.button("전적 검색"):
  if summoner_name:
    st.success(f"'{summoner_name}'님의 정보를 불러왔습니다!")

    # 대시보드 형태의 레이아웃 (콜롬 활용)
    col1, col2, col3 = st.columns([1, 2, 2])

    with col1:
      st.image(
          "https://via.placeholder.com/100", caption="프로필 아이콘"
      )  # 임시 이미지

    with col2:
      st.subheader(summoner_name)
      st.write("티어: **챌린저 (999 LP)**")
      st.write("승률: **65%** (최근 20경기 13승 7패)")

    with col3:
      st.metric(label="KDA", value="4.25:1")
      st.write("주요 포지션: 미드 / 원딜")

    st.markdown("---")
    st.subheader("최근 게임 기록")
    st.info("승리 · 승급전 · 킬/데스/어시스트: 8/2/10")
  else:
    st.warning("소환사 이름을 입력해주세요!")
