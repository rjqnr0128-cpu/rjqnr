import random
import streamlit as st

# 1. 사이트 제목 설정
st.title("🍀 행운의 로또 번호 추첨기 & 오늘의 운세")
st.write("버튼을 누르면 1부터 45까지의 숫자 중 겹치지 않는 6개 번호와 오늘의 운세를 뽑아드립니다!")

# 2. 로또 번호 생성 버튼
if st.button("로또 번호 고르기!"):
  # 1부터 45까지의 숫자 중에서 겹치지 않게 6개 랜덤 추출 후 정렬
  lotto_numbers = sorted(random.sample(range(1, 46), 6))

  # 3. 결과 예쁘게 출력하기
  st.success("✨ 오늘의 행운 번호가 나왔습니다!")

  # 번호를 가로로 예쁘게 보여주기
  col1, col2, col3, col4, col5, col6 = st.columns(6)

  with col1:
    st.metric(label="1번", value=lotto_numbers[0])
  with col2:
    st.metric(label="2번", value=lotto_numbers[1])
  with col3:
    st.metric(label="3번", value=lotto_numbers[2])
  with col4:
    st.metric(label="4번", value=lotto_numbers[3])
  with col5:
    st.metric(label="5번", value=lotto_numbers[4])
  with col6:
    st.metric(label="6번", value=lotto_numbers[5])

  # 4. 오늘의 운세 기능 추가
  st.markdown("---")
  st.subheader("🔮 오늘의 운세")

  # 랜덤 운세 문구 리스트
  fortunes = [
      "오늘은 뜻밖의 행운이 찾아오는 날입니다! 작은 일에도 기분 좋은 하루가 될 거예요.",
      (
          "노력한 만큼의 결실을 맺을 수 있는 하루입니다. 자신감을 가지세요!"
      ),
      "주위 사람들과의 소통이 중요한 날입니다. 좋은 인연을 만날 수 있어요.",
      (
          "잠깐의 여유와 휴식이 필요한 하루입니다. 무리하지 말고 재충전해 보세요."
      ),
      "재물운과 행운이 따르는 찬란한 하루입니다! 좋은 기회를 놓치지 마세요.",
  ]

  # 무작위로 하나 선택
  todays_fortune = random.choice(fortunes)
  st.info(todays_fortune)