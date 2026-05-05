import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.title("🌞 태양광 효율 최적화 시스템")

st.sidebar.header("환경 설정")

sun_angle = st.sidebar.slider("태양 각도 (°)", 0, 90, 45)
panel_angle = st.sidebar.slider("패널 각도 (°)", 0, 90, 30)
temp = st.sidebar.slider("온도 (°C)", 0, 80, 25)

# 효율 계산
angle_diff = abs(panel_angle - sun_angle)
efficiency = math.cos(math.radians(angle_diff))
temp_loss = max(0, (temp - 25) * 0.005)
final_eff = max(0, efficiency - temp_loss)

st.subheader("📊 현재 효율")
st.write(f"👉 {round(final_eff*100, 2)} %")

# 자동 최적화
if st.button("⚡ 자동 최적화 실행"):
    st.success(f"최적 패널 각도: {sun_angle}°")

# 각도 그래프
st.subheader("📈 각도 vs 효율")

angles = np.linspace(0, 90, 100)
eff_list = []

for a in angles:
    diff = abs(a - sun_angle)
    eff = math.cos(math.radians(diff)) - temp_loss
    eff_list.append(max(0, eff))

plt.figure()
plt.plot(angles, eff_list)
plt.xlabel("패널 각도")
plt.ylabel("효율")
st.pyplot(plt)

# 온도 그래프
st.subheader("🌡 온도 vs 효율")

temps = np.linspace(0, 80, 100)
eff_temp = []

for t in temps:
    loss = max(0, (t - 25) * 0.005)
    eff_temp.append(max(0, efficiency - loss))

plt.figure()
plt.plot(temps, eff_temp)
plt.xlabel("온도")
plt.ylabel("효율")
st.pyplot(plt)
