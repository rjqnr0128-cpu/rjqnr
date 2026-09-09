import random
import streamlit as st

# 사이드바 메뉴 구성
st.sidebar.title("📚 파이썬 웹 개발 수업")
step = st.sidebar.radio(
    "학습 단계를 선택하세요:",
    [
        "1단계: 화면 기본 뼈대 만들기",
        "2단계: 로또 번호 추첨 기능",
        "3단계: 오늘의 운세 추가 및 완성",
    ],
)

if step == "1단계: 화면 기본 뼈대 만들기":
  st.title("🍀 1단계: 나만의 웹페이지 시작하기")
  st.write(
      "가장 먼저 웹사이트의 제목과 간단한 설명을 화면에 띄우는 코드를"
      " 작성합니다."
  )

  st.code("""
    import streamlit as st

    st.title("🍀 행운의 로또 번호 추첨기")
    st.write("버튼을 누르면 번호가 나와요!")
    """, language="python")

  st.markdown("---")
  st.subheader("💡 실습 결과 미리보기")
  st.title("🍀 행운의 로또 번호 추첨기")
  st.write("버튼을 누르면 번호가 나와요!")

elif step == "2단계: 로또 번호 추첨 기능":
  st.title("🔢 2단계: 로또 번호 뽑기 기능 추가")
  st.write(
      "파이썬의 `random` 모듈을 사용해 1부터 45 사이의 번호 6개를 겹치지 않게"
      " 뽑고, 화면에 예쁘게 배치합니다."
  )

  st.code("""
    import streamlit as st
    import random

    st.title("🍀 행운의 로또 번호 추첨기")

    if st.button("로또 번호 고르기!"):
        numbers = sorted(random.sample(range(1, 46), 6))
        st.success("번호가 생성되었습니다!")
        
        # 6개의 컬럼으로 나누어 예쁘게 출력
        cols = st.columns(6)
        for i, col in enumerate(cols):
            col.metric(label=f"{i+1}번", value=numbers[i])
    """, language="python")

  st.markdown("---")
  st.subheader("💡 실습 결과 미리보기")
  if st.button("로또 번호 고르기! (2단계 테스트)"):
    numbers = sorted(random.sample(range(1, 46), 6))
    st.success("번호가 생성되었습니다!")
    cols = st.columns(6)
    for i, col in enumerate(cols):
      col.metric(label=f"{i+1}번", value=numbers[i])

elif step == "3단계: 오늘의 운세 추가 및 완성":
  st.title("🔮 3단계: 오늘의 운세 기능 추가 및 완성")
  st.write(
      "리스트와 무작위 선택(`random.choice`) 기능을 활용해 로또 번호 아래에"
      " 오늘의 운세를 함께 띄워 완성합니다."
  )

  st.code("""
    import streamlit as st
    import random

    st.title("🍀 행운의 로또 번호 추첨기 & 오늘의 운세")

    if st.button("운세와 로또 번호 뽑기!"):
        numbers = sorted(random.sample(range(1, 46), 6))
        st.success("오늘의 행운 번호!")
        
        cols = st.columns(6)
        for i, col in enumerate(cols):
            col.metric(label=f"{i+1}번", value=numbers[i])
            
        st.markdown("---")
        st.subheader("🔮 오늘의 운세")
        fortunes = [
            "뜻밖의 행운이 찾아오는 날입니다!",
            "노력한 만큼 결실을 맺는 하루입니다.",
            "주위 사람들과 소통이 좋은 하루예요."
        ]
        st.info(random.choice(fortunes))
    """, language="python")

  st.markdown("---")
  st.subheader("💡 최종 완성본 미리보기")
  if st.button("운세와 로또 번호 뽑기! (3단계 최종)"):
    numbers = sorted(random.sample(range(1, 46), 6))
    st.success("오늘의 행운 번호!")
    cols = st.columns(6)
    for i, col in enumerate(cols):
      col.metric(label=f"{i+1}번", value=numbers[i])

    st.markdown("---")
    st.subheader("🔮 오늘의 운세")
    fortunes = [
        "뜻밖의 행운이 찾아오는 날입니다!",
        "노력한 만큼 결실을 맺는 하루입니다.",
        "주위 사람들과 소통이 좋은 하루예요.",
    ]
    st.info(random.choice(fortunes))
