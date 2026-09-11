import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="군필.GG (Gunpil.GG)", page_icon="🪖", layout="wide"
)

# 상단 타이틀
st.title("🪖 군필.GG (Gunpil.GG)")
st.write("대한민국 국군 장병 및 연예인 복무 현황 데이터베이스")

# 샘플 데이터 (군번을 키값으로 사용)
soldier_database = {
    "20-71012345": {
        "name": "김석진 (진)",
        "branch": "육군",
        "rank": "병장 (만기전역)",
        "unit": "제5보병사단 신병교육대 조교",
        "period": "2022.12.13 ~ 2024.06.12",
        "status": "전역 완료",
    },
    "21-72054321": {
        "name": "이찬혁",
        "branch": "해병대",
        "rank": "병장 (만기전역)",
        "unit": "제1해병사단",
        "period": "2017.09.18 ~ 2019.06.17",
        "status": "전역 완료",
    },
    "17-73098765": {
        "name": "이승기",
        "branch": "특수부대",
        "rank": "병장 (만기전역)",
        "unit": "육군 특수전사령부 (특전사)",
        "period": "2016.02.01 ~ 2017.10.31",
        "status": "전역 완료",
    },
    "11-74011111": {
        "name": "조인성",
        "branch": "공군",
        "rank": "병장 (만기전역)",
        "unit": "공군작전사령부 군악전산병",
        "period": "2009.04.06 ~ 2011.05.04",
        "status": "전역 완료",
    },
    "23-75099999": {
        "name": "변백현 (백현)",
        "branch": "사회복무요원 (공익)",
        "rank": "소집해제",
        "unit": "용산구청 근무",
        "period": "2021.05.06 ~ 2023.02.05",
        "status": "소집해제 완료",
    },
}

# 연예인 복무 현황판 데이터 (카테고리별 2명씩)
celebrity_board = {
    "육군": [
        {
            "name": "김석진 (진)",
            "unit": "제5보병사단 조교",
            "serial": "20-71012345",
        },
        {"name": "남주혁", "unit": "제32보병사단 군사경찰단", "serial": "23-xxxxxx"},
    ],
    "해병대": [
        {"name": "이찬혁", "unit": "제1해병사단", "serial": "21-72054321"},
        {"name": "표지훈 (P.O)", "unit": "해병대 군악대", "serial": "22-xxxxxx"},
    ],
    "특수부대": [
        {
            "name": "이승기",
            "unit": "특수전사령부 (특전사)",
            "serial": "17-73098765",
        },
        {
            "name": "박군 (박준우)",
            "unit": "특수전사령부 상사 전역",
            "serial": "05-xxxxxx",
        },
    ],
    "공군": [
        {"name": "조인성", "unit": "공군작전사령부 군악", "serial": "11-74011111"},
        {"name": "지진희", "unit": "공군 자원입대 (시디과)", "serial": "94-xxxxxx"},
    ],
    "사회복무요원 (공익)": [
        {"name": "변백현", "unit": "용산구청 사회복무요원", "serial": "23-75099999"},
        {"name": "규현 (조규현)", "unit": "성북시각장애인복지관", "serial": "17-xxxxxx"},
    ],
}

# 메뉴 탭 구성
tab1, tab2 = st.tabs(["🔍 군번 검색", "🌟 연예인 복무 현황판"])

with tab1:
  st.subheader("군번 기반 장병/연예인 전적 검색")
  st.write("등록된 군번을 입력하여 상세 복무 기록을 조회하세요.")
  st.caption("💡 테스트용 추천 군번: `20-71012345` (진), `17-73098765` (이승기)")

  search_id = st.text_input("군번 입력", placeholder="예: 20-71012345")

  if st.button("검색하기"):
    if search_id in soldier_database:
      info = soldier_database[search_id]
      st.success(f"'{info['name']}'님의 군복무 정보를 찾았습니다!")

      # OP.GG 스타일 카드 레이아웃
      col1, col2 = st.columns([1, 3])
      with col1:
        st.metric(label="군종", value=info["branch"])
        st.metric(label="전역 상태", value=info["status"])
      with col2:
        st.subheader(f"이름: {info['name']}")
        st.write(f"- **계급/역할**: {info['rank']}")
        st.write(f"- **소속 부대**: {info['unit']}")
        st.write(f"- **복무 기간**: {info['period']}")
        st.write(f"- **고유 군번 ID**: `{search_id}`")
    else:
      st.warning(
          "등록되지 않은 군번이거나 올바르지 않은 형식입니다. (테스트 군번을"
          " 입력해보세요!)"
      )

with tab2:
  st.subheader("🌟 부대별 연예인 복무 현황판")
  st.write(
      "육군, 해병대, 특수부대, 공군, 공익 등 출신별 연예인 복무 리스트입니다."
  )

  # 카테고리 선택 셀렉트박스
  selected_category = st.selectbox(
      "복무 분야 선택", list(celebrity_board.keys())
  )

  st.markdown(f"### 📌 {selected_category} 출신 연예인")

  # 해당 카테고리의 2명 정보 출력
  for celebrity in celebrity_board[selected_category]:
    with st.expander(f"👤 {celebrity['name']} ({celebrity['unit']})"):
      st.write(f"- **소속 부대**: {celebrity['unit']}")
      st.write(f"- **대표 군번 ID**: `{celebrity['serial']}`")
      st.info(
          "상세 전적 및 훈련소 성적은 추후 군 API 연동 시 업데이트됩니다."
      )
