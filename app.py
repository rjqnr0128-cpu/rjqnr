import streamlit as st
import random

# 1. 사이트 제목 설정
st.title("🍀 행운의 로또 번호 추첨기")
st.write("버튼을 누르면 1부터 45까지의 숫자 중 겹치지 않는 6개 번호를 뽑아드립니다!")

# 2. 버튼 만들기
if st.button("로또 번호 고르기!"):
    # 1부터 45까지의 숫자 중에서 겹치지 않게 6개 랜덤 추출 후 정렬
    lotto_numbers = sorted(random.sample(range(1, 46), 6))
    
    # 3. 결과 예쁘게 출력하기
    st.success("🎉 오늘의 행운 번호가 나왔습니다!")
    
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