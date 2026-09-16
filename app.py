import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="동맥경화 위험도 시뮬레이터", page_icon="🫀", layout="wide"
)

st.title("🫀 동맥경화 위험도 & 혈관 상태 시뮬레이터")
st.markdown(
    "입력하신 건강 데이터를 바탕으로 **10년 내 심뇌혈관 질환 위험도**와 **혈관"
    " 협착 정도**를 예측합니다."
)

# 대시보드 레이아웃
col_input, col_result = st.columns([1, 1.2])

with col_input:
  st.subheader("📋 건강 정보 입력")

  age = st.slider("나이 (세)", min_value=30, max_value=80, value=55)
  bp = st.slider(
      "수축기 혈압 (mmHg)", min_value=90, max_value=180, value=135
  )
  ldl = st.slider(
      "LDL 콜레스테롤 (mg/dL)", min_value=70, max_value=220, value=140
  )

  col_cb1, col_cb2 = st.columns(2)
  with col_cb1:
    is_smoker = st.checkbox("현재 흡연 중")
  with col_cb2:
    has_diabetes = st.checkbox("당뇨병 진단 받음")

# 위험도 가중치 계산 (간이 가중치 알고리즘)
risk_score = 0
risk_score += (age - 30) * 0.4
risk_score += max(0, bp - 120) * 0.25
risk_score += max(0, ldl - 100) * 0.15
if is_smoker:
  risk_score += 12
if has_diabetes:
  risk_score += 10

# 위험도 판정 및 혈관 좁아짐 비율(%) 추정
risk_percent = round(min(max(risk_score * 0.6, 2.0), 45.0), 1)
narrowing_percent = min(int(risk_score * 1.3), 85)

with col_result:
  st.subheader("📊 시뮬레이션 결과")

  # 지표 카드 출력
  c1, c2 = st.columns(2)
  with c1:
    st.metric("10년 내 심뇌혈관 위험도", f"{risk_percent}%")
  with c2:
    st.metric("추정 혈관 좁아짐(협착율)", f"약 {narrowing_percent}%")

  # 위험 단계별 색상 및 메시지
  if risk_percent < 10:
    st.success(
        "🟢 **저위험군**: 현재 관리가 잘 되고 있습니다. 유기적인 생활 습관을"
        " 유지하세요."
    )
  elif risk_percent < 20:
    st.info(
        "🟡 **중등도 위험군**: 식단 개선과 정기적인 운동이 필요합니다."
    )
  elif risk_percent < 30:
    st.warning(
        "🟠 **고위험군**: 전문의 상담을 통한 고혈압/지질 관리 및 정밀 검사를"
        " 권장합니다."
    )
  else:
    st.error(
        "🔴 **초고위험군**: 적극적인 약물 치료와 즉각적인 생활 습관 교정이"
        " 필요합니다."
    )

  # 혈관 단면도 Visualizing (Matplotlib)
  fig, ax = plt.subplots(figsize=(4, 4))

  # 외벽 (정상 혈관)
  outer_circle = plt.Circle(
      (0, 0), 1.0, color="#E74C3C", fill=True, alpha=0.3
  )
  # 플라크 (지방 축적)
  plaque_radius = 1.0
  inner_radius = max(0.15, 1.0 - (narrowing_percent / 100))

  plaque_circle = plt.Circle((0, 0), plaque_radius, color="#F1C40F", fill=True)
  # 통로 (혈류)
  blood_circle = plt.Circle((0, 0), inner_radius, color="#900C3F", fill=True)

  ax.add_patch(outer_circle)
  ax.add_patch(plaque_circle)
  ax.add_patch(blood_circle)

  ax.set_xlim(-1.2, 1.2)
  ax.set_ylim(-1.2, 1.2)
  ax.set_aspect("equal")
  ax.axis("off")

  plt.title(
      f"혈관 단면 시뮬레이션 (통로 유효 면적: {100-narrowing_percent}%)",
      fontsize=10,
  )
  st.pyplot(fig)

st.markdown("---")
st.caption(
    "※ 본 시뮬레이터는 예측 참고용이며, 정확한 진단을 위해서는 경동맥 초음파"
    " 및 혈액 검사가 필요합니다."
)
