import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.xlabel("Angle")
plt.ylabel("Efficiency")
plt.title("Angle vs Efficiency")

plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False


st.title("🌞 태양광 효율 최적화 시스템")

# 메뉴 선택
menu = st.sidebar.selectbox(
    "기능 선택",
    ["현재 효율 계산", "자동 최적화", "시뮬레이션"]
)

# 공통 함수
def calculate_efficiency(sun_angle, panel_angle, temp):
    angle_diff = abs(panel_angle - sun_angle)
    efficiency = math.cos(math.radians(angle_diff))
    temp_loss = max(0, (temp - 25) * 0.005)
    return max(0, efficiency - temp_loss)

# ------------------------
# 1️⃣ 현재 효율 계산
# ------------------------
if menu == "현재 효율 계산":
    st.header("📊 현재 효율 계산")

    sun_angle = st.number_input("태양 각도", 0, 90, 45)
    panel_angle = st.number_input("패널 각도", 0, 90, 30)
    temp = st.number_input("온도", 0, 80, 25)

    if st.button("계산"):
        eff = calculate_efficiency(sun_angle, panel_angle, temp)
        st.success(f"👉 효율: {round(eff*100,2)} %")

# ------------------------
# 2️⃣ 자동 최적화
# ------------------------
elif menu == "자동 최적화":
    st.header("⚡ 자동 최적화 (Sun Tracking)")

    sun_angle = st.number_input("태양 각도", 0, 90, 45)

    if st.button("최적화 실행"):
        st.success(f"👉 최적 패널 각도: {sun_angle}°")

# ------------------------
# 3️⃣ 시뮬레이션
# ------------------------
elif menu == "시뮬레이션":
    st.header("📈 시뮬레이션")

    sun_angle = st.slider("태양 각도", 0, 90, 45)
    temp = st.slider("온도", 0, 80, 25)

    # 각도 vs 효율
    st.subheader("각도 vs 효율")
    angles = np.linspace(0, 90, 100)
    eff_list = [calculate_efficiency(sun_angle, a, temp) for a in angles]

    plt.figure()
    plt.plot(angles, eff_list)
    plt.xlabel("Panel Angle (°)")
    plt.ylabel("Efficiency")
    plt.title("Angle vs Efficiency")
    st.pyplot(plt)

    # 온도 vs 효율
    st.subheader("온도 vs 효율")
    temps = np.linspace(0, 80, 100)
    eff_temp = [calculate_efficiency(sun_angle, sun_angle, t) for t in temps]

    plt.figure()
    plt.plot(temps, eff_temp)
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Efficiency")
    plt.title("Temperature vs Efficiency")
    st.pyplot(plt)
    plt.grid(True)
