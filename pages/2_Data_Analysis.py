import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform

# 페이지 기본 설정
st.set_page_config(
    page_title="당곡고 물맛 탐구 - 실제 데이터 분석",
    page_icon="📊",
    layout="wide"
)

st.sidebar.info("🏫 **당곡고등학교 과학탐구**\n\n학생들의 주도적인 탐구를 돕는 탐구 도우미 프로그램입니다.")

# 한글 폰트 설정 (운영체제 맞춤형 깨짐 방지)
system_os = platform.system()
if system_os == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif system_os == 'Darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
else:  # Linux (서버용)
    plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

st.title("📊 실제 정수장 수질 데이터 분석 및 과학적 결론")
st.write("학생이 제시한 실제 수질 성적표의 화학 데이터를 기반으로 기준치 및 타 수질과 정밀 비교합니다.")

# 실제 사진 데이터 기반 입력
real_data = {
    '화학 수질 항목': ['경도 (mg/L)', '수소이온농도 (pH)', '염소이온 (mg/L)', '증발잔류물 (mg/L)', '황산이온 (mg/L)', '탁도 (NTU)'],
    '먹는물 수질 기준': ['300 이하', '5.8 ~ 8.5', '250 이하', '500 이하', '200 이하', '0.5 이하'],
    '우리 지역 측정치 1': [26.0, 6.8, 8.8, 44.0, 4.0, 0.07],
    '우리 지역 측정치 2': [25.0, 7.0, 8.4, 47.0, 4.0, 0.06]
}
df = pd.DataFrame(real_data)

st.subheader("📋 수집된 실제 수질 데이터 테이블")
st.dataframe(df, use_container_width=True)

st.subheader("📈 기준치 대비 우리 지역 수돗물 이온 농도 수준")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 1. 경도 및 증발잔류물 비교 그래프
labels1 = ['경도', '증발잔류물']
my_val1 = [25.5, 45.5]  # 측정 평균치
limit_val1 = [300.0, 500.0]

x = np.arange(len(labels1))
width = 0.35

axes[0].bar(x - width/2, my_val1, width, label='우리 지역 평균', color='royalblue')
axes[0].bar(x + width/2, limit_val1, width, label='법적 최대 허용 기준', color='lightcoral', alpha=0.6)
axes[0].set_ylabel('농도 (mg/L)')
axes[0].set_title('경도 및 총 잔류물량 비교')
axes[0].set_xticks(x)
axes[0].set_xticklabels(labels1)
axes[0].legend()

# 2. 염소이온 및 황산이온 비교 그래프
labels2 = ['염소이온', '황산이온']
my_val2 = [8.6, 4.0]
limit_val2 = [250.0, 200.0]

x2 = np.arange(len(labels2))
axes[1].bar(x2 - width/2, my_val2, width, label='우리 지역 평균', color='teal')
axes[1].bar(x2 + width/2, limit_val2, width, label='법적 최대 허용 기준', color='lightcoral', alpha=0.6)
axes[1].set_ylabel('농도 (mg/L)')
axes[1].set_title('맛에 악영향을 주는 이온 농도 비교')
axes[1].set_xticks(x2)
axes[1].set_xticklabels(labels2)
axes[1].legend()

st.pyplot(fig)

st.markdown("""
### 📝 과학적 분석 및 탐구 결론
1. **뛰어난 청정성과 연수성**:
   우리 지역의 수돗물 경도는 평균 약 **25.5 mg/L**로, 법적 기준치인 300 mg/L보다 압도적으로 낮으며 전형적인 **단물(연수, Soft Water)**에 해당합니다. 칼슘과 마그네슘의 농도가 매우 낮아 보일러나 파이프에 스케일(때)이 끼지 않으며, 목넘김이 걸림 없이 극도로 부드럽습니다.
2. **불쾌한 맛 유발 성분의 최소화**:
   짠맛과 소독약 맛을 유발하는 염소이온(평균 8.6 mg/L)과 쓴맛을 내는 황산이온(4.0 mg/L) 역시 허용 기준치 대비 3~4% 미만 수준으로 매우 미미합니다. 따라서 수돗물 특유의 불쾌한 잔류 맛이 거의 나지 않습니다.
3. **완벽한 중성 평형**:
   pH가 **6.8 ~ 7.0**으로 순수한 중성에 완벽히 수렴합니다. 이는 물속 탄산 물질과 미네랄이 이상적인 화학적 평형 상태를 이루고 있음을 보여주며, 신맛이나 쓴맛 등의 이물감을 전혀 느끼지 않게 해 줍니다.
""")
