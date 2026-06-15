
---

## 3. 🐍 `app.py` (전체 소스 코드)
아래 코드는 4개의 페이지를 한눈에 볼 수 있도록 사이드바 메뉴로 분기처리한 전체 파이썬 코드입니다. 그대로 복사하여 실행할 수 있습니다.

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Matplotlib 시각화 시 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic' # Windows용 (Mac 환경인 경우 'AppleGothic' 등으로 변경 가능)
plt.rcParams['axes.unicode_minus'] = False

# 페이지 기본 설정
st.set_page_config(
    page_title="당곡고 물맛 탐구 프로젝트",
    page_icon="💧",
    layout="wide"
)

# 사이드바를 이용한 멀티페이지 네비게이션
st.sidebar.title("🔍 탐구 메뉴")
page = st.sidebar.radio(
    "이동할 페이지를 선택하세요:",
    ["1. 탐구 홈 (초기 화면)", 
     "2. 농도에 따른 물맛의 화학", 
     "3. 실제 데이터 분석 및 결론", 
     "4. 의료/보건 영향 및 기계 설계"]
)

# 당곡고등학교 AI 도우미 브랜딩 시그니처
st.sidebar.markdown("---")
st.sidebar.info("🏫 **당곡고등학교 과학탐구 도우미**\n\n학생들의 주도적인 탐구를 돕기 위해 개발된 교육용 AI 모델입니다.")

# ==========================================================
# PAGE 1: 초기 화면 (Home)
# ==========================================================
if page == "1. 탐구 홈 (초기 화면)":
    st.title("💧 수돗물의 화학 성분이 결정하는 물맛의 비밀")
    st.subheader("당곡고등학교 자율 탐구 프로젝트 - 화학 및 생명과학/보건 융합 탐구")
    
    st.markdown("""
    ### 📌 탐구의 시작
    우리가 매일 마시는 물은 단순한 $H_2O$가 아닙니다. 물 속에는 다양한 **미네랄 이온(칼슘, 마그네슘, 염소, 황산 등)**이 녹아 있으며, 이들의 농도와 비율에 따라 물의 '맛'과 '체내 영향'이 크게 달라집니다.
    
    본 시뮬레이터 프로그램은 공공 수질 데이터를 기반으로 **화학적 수치와 생명과학적 영향, 그리고 기계공학적 제어 기법**을 유기적으로 연결하여 탐구하기 위해 개발되었습니다.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        #### 🧪 주요 화학적 물리량
        - **수소이온농도 (pH)**: 물의 산도 및 알칼리도 조절
        - **경도 (Hardness)**: 물속 칼슘($Ca^{2+}$)과 마그네슘($Mg^{2+}$)의 총합 질량
        - **염소이온 ($Cl^-$)**: 소독 및 짠맛의 지표
        - **증발잔류물 (TDS)**: 총 용존 고형물의 양
        """)
    with col2:
        st.success("""
        #### 🗺️ 탐구 여정 안내
        - **2페이지**: 화학 성분 조절에 따른 물맛 지수 시뮬레이터
        - **3페이지**: 수집된 수돗물 정밀 분석 데이터 확인 및 비교
        - **4페이지**: 인체 내 대사 작용 영향 분석 및 이온 제어 정수 장치 설계
        """)

# ==========================================================
# PAGE 2: 농도에 따른 물맛의 화학 (Taste & Chemistry)
# ==========================================================
elif page == "2. 농도에 따른 물맛의 화학":
    st.title("🧪 농도에 따른 물맛의 화학적 시뮬레이션")
    st.write("슬라이더를 조절하여 다양한 미네랄 농도가 물맛에 주는 영향을 실시간으로 확인해보세요!")
    
    # 이온 슬라이더 입력창
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🛠️ 수질 성분 농도 미세 조정")
        ca = st.slider("칼슘 이온 (Ca2+) 농도 (mg/L)", 0.0, 100.0, 15.0)
        mg = st.slider("마그네슘 이온 (Mg2+) 농도 (mg/L)", 0.0, 50.0, 5.0)
        so4 = st.slider("황산 이온 (SO4 2-) 농도 (mg/L)", 0.0, 100.0, 4.0)
        cl = st.slider("염소 이온 (Cl-) 농도 (mg/L)", 0.0, 150.0, 8.5)
        ph = st.slider("수소이온농도 (pH)", 5.0, 9.0, 7.0, step=0.1)

    with col2:
        st.subheader("👅 물맛 종합 진단 결과")
        
        # 1. 계산식 적용
        # 하시모토 물맛 지수 (O-Index): (Ca + K + SiO2) / (Mg + SO4). K와 SiO2는 대표값(상수) 처리
        # O-Index가 2.0 이상이면 물맛이 좋다고 알려져 있음.
        o_index = (ca + 2.0 + 10.0) / (mg + so4 + 1.0)
        
        # 총 경도 계산식: (Ca * 2.497) + (Mg * 4.118)
        hardness = (ca * 2.497) + (mg * 4.118)
        
        # 2. 물맛 텍스트 설명 및 평가
        st.metric(label="📊 하시모토 물맛 지수 (O-Index)", value=f"{o_index:.2f}", help="2.0 이상일 때 물맛이 훌륭함")
        if o_index >= 2.0:
            st.success("✨ **평가: 맛있는 물!** 미네랄의 밸런스가 뛰어나 단맛과 청량감이 좋습니다.")
        else:
            st.warning("⚠️ **평가: 맛이 다소 떨어지는 물** 마그네슘이나 황산이온이 많아 약간의 쓴맛이나 텁텁함이 있을 수 있습니다.")
            
        st.metric(label="🧪 계산된 총 경도 (mg/L)", value=f"{hardness:.2f} mg/L")
        if hardness < 75:
            st.info("💧 **연수(Soft Water)**: 매우 부드럽고 가볍지만, 미네랄 맛이 밋밋할 수 있습니다.")
        elif 75 <= hardness < 150:
            st.success("🥛 **적당한 경수**: 가장 균형 잡히고 청량감이 우수한 상태입니다.")
        else:
            st.error("🧱 **강경수(Hard Water)**: 무겁고 텁텁하며 미끈거리는 느낌이 남습니다.")

        # pH의 영향
        if ph < 6.5:
            st.warning("🍋 **pH 산성 경향**: 물에서 약간 신맛이 날 수 있으며 관로 부식 우려가 있습니다.")
        elif ph > 7.5:
            st.warning("🧼 **pH 알칼리성 경향**: 약간 미끈거리거나 쓴맛, 비누맛 같은 느낌을 줄 수 있습니다.")
        else:
            st.success("⚖️ **pH 중성 상태**: 물맛에 미치는 산도의 영향이 거의 없는 쾌적한 상태입니다.")

# ==========================================================
# PAGE 3: 실제 데이터 분석 및 결론 (Data Analysis)
# ==========================================================
elif page == "3. 실제 데이터 분석 및 결론":
    st.title("📊 실제 수돗물 수질 검사 데이터 분석")
    st.write("학생님이 제시해주신 원본 수질 데이터를 기초로 다른 물들과 화학적 프로파일을 전격 비교해봅니다.")

    # 사용자 업로드 이미지 데이터 대입
    my_data = {
        '항목': ['경도', 'pH', '염소이온', '증발잔류물(TDS)', '황산이온'],
        '학생 수돗물 데이터': [25.5, 6.9, 8.6, 45.5, 4.0],
        '수질 기준치 (최대)': [300.0, 8.5, 250.0, 500.0, 200.0],
        '유럽 유명 광천수 (참고)': [250.0, 7.2, 20.0, 350.0, 120.0]
    }
    df = pd.DataFrame(my_data)
    
    st.subheader("📋 성분 비교 표 (mg/L, 단 pH는 무단위)")
    st.dataframe(df, use_container_width=True)
    
    st.subheader("📈 국가 기준 대비 안전성 및 농도 프로파일")
    
    # 시각화 그래프 작성 (Matplotlib 이용)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # 그래프 1: 경도 및 증발잔류물 비교
    items1 = ['경도', '증발잔류물(TDS)']
    student_val1 = [25.5, 45.5]
    std_val1 = [300.0, 500.0]
    
    x = np.arange(len(items1))
    width = 0.35
    
    axes[0].bar(x - width/2, student_val1, width, label='우리 지역 수돗물', color='dodgerblue')
    axes[0].bar(x + width/2, std_val1, width, label='먹는물 법적 기준치', color='tomato', alpha=0.5)
    axes[0].set_ylabel('농도 (mg/L)')
    axes[0].set_title('경도 및 총 용존량(TDS) 비교')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(items1)
    axes[0].legend()
    
    # 그래프 2: 미네랄 이온 농도 비교
    items2 = ['염소이온', '황산이온']
    student_val2 = [8.6, 4.0]
    std_val2 = [250.0, 200.0]
    
    x2 = np.arange(len(items2))
    axes[1].bar(x2 - width/2, student_val2, width, label='우리 지역 수돗물', color='teal')
    axes[1].bar(x2 + width/2, std_val2, width, label='먹는물 법적 기준치', color='tomato', alpha=0.5)
    axes[1].set_ylabel('농도 (mg/L)')
    axes[1].set_title('소독성 및 쓴맛 유발 이온 비교')
    axes[1].set_xticks(x2)
    axes[1].set_xticklabels(items2)
    axes[1].legend()
    
    st.pyplot(fig)
    
    st.markdown("""
    ### 📝 실제 분석 결론 및 토론거리
    1. **극도의 청정성 및 저자극성**: 
       분석 데이터에 드러난 우리 지역 수돗물은 경도(25.5 mg/L), 증발잔류물(45.5 mg/L)이 법적 허용 기준보다 압도적으로 낮습니다. 이는 중금속이나 과도한 염류가 들어있지 않은 매우 깨끗한 물(연수)임을 과학적으로 증명합니다.
    2. **청량감과 목넘김**: 
       경도가 낮아 목넘김이 매끄러우나, 미네랄(칼슘, 마그네슘) 함량이 다소 적어 풍부하고 깊은 미네랄 맛보다는 **'깔끔하고 가벼운 맛'**에 가깝습니다.
    3. **낮은 황산 및 염소이온 농도**:
       황산이온(4 mg/L)과 염소이온(8.6 mg/L)이 현저히 낮아 물 특유의 비린 맛, 쓴맛 또는 소독약 맛이 전혀 느껴지지 않는 고품질의 먹는 물 조건입니다.
    """)

# ==========================================================
# PAGE 4: 의료/보건 영향 및 기계 설계 (Health & Design)
# ==========================================================
elif page == "4. 의료/보건 영향 및 기계 설계":
    st.title("🩺 의료/보건학적 영향 및 맞춤형 정수 시스템 설계")
    
    tab1, tab2 = st.tabs(["🧬 의료/보건학적 영향", "⚙️ 미네랄 제어 정수 기계 설계"])
    
    with tab1:
        st.subheader("인체 대사 및 보건학적 영향 분석")
        st.write("해당 미네랄 성분이 인체에 미치는 긍정적/부정적 영향을 정리한 학술적 데이터입니다.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.error("⚠️ 특정 농도가 너무 높을 때 (과다 섭취)")
            st.markdown("""
            - **고칼슘($Ca^{2+}$) 및 고마그네슘($Mg^{2+}$) (강경수)**:
              - 일시적인 위장 장애 및 설사 유발 (특히 마그네슘 황산염 작용).
              - 신장 결석(Urinary Calculi) 환자에게 요로 결석 재발 빈도 증가 위험.
            - **과다 염소이온 ($Cl^-$)**:
              - 체내 염소 농도 축적으로 혈압 상승 및 신장 부담 가능성.
            - **강산성 / 강알칼리성**:
              - 식도 및 위 점막 자극, 만성적인 위장 장애 유발.
            """)
        with col2:
            st.warning("📉 특정 농도가 지나치게 낮을 때 (결핍 섭취)")
            st.markdown("""
            - **저칼슘/저마그네슘 (초연수 / 증류수 수준)**:
              - 식수로부터 보충되어야 할 필수 전해질의 부족으로 골밀도 저하 야기.
              - 역학 조사 결과, 지나치게 미네랄이 없는 연수를 장기 음용 시 심혈관계 질환(Cardiovascular Disease) 발생률 증가 보고.
            - **미네랄 완전 제로 상태**:
              - 삼투압 작용에 의해 인체 내 세포 전해질이 역으로 빠져나가는 역삼투 유도 가능성.
            """)
            
    with tab2:
        st.subheader("🛠️ 맞춤형 이온 제어 정수 기계 (Re-mineralizer System) 개념 설계")
        st.write("물이 너무 깨끗하여 미네랄이 부족할 때는 올려주고, 너무 많을 때는 걸러내는 지능형 피드백 제어 장치 구상도입니다.")
        
        # Streamlit 내장 Graphviz를 활용한 기계 제어 흐름 설계도 시각화
        st.graphviz_chart('''
        digraph G {
            rankdir=LR;
            node [shape=box, style=filled, color=lightblue, fontname="Malgun Gothic"];
            "원수 유입 (Inlet)" -> "필터 1: 활성탄/침전 (Pre-Filter)" -> "스마트 제어 밸브 (Sensing & Bypass)"
            "스마트 제어 밸브 (Sensing & Bypass)" -> "필터 2: RO 필터 (이온 전체 제거)" [label="경도 150 이상시"]
            "스마트 제어 밸브 (Sensing & Bypass)" -> "필터 3: 미네랄 카트리지 (Ca/Mg 용해)" [label="경도 50 이하시"]
            "필터 2: RO 필터 (이온 전체 제거)" -> "최종 혼합 챔버 (Mixing Tank)"
            "필터 3: 미네랄 카트리지 (Ca/Mg 용해)" -> "최종 혼합 챔버 (Mixing Tank)"
            "최종 혼합 챔버 (Mixing Tank)" -> "pH 미세 보정기 (Alkalizer)" -> "최종 청량 음용수 출수 (Outlet)"
        }
        ''')
        
        st.markdown("""
        ### 💡 기계공학적 설계 설명 (수행평가 제출용 팁)
        - **스마트 센싱(Sensing)**: 원수의 전기전도도(EC) 센서를 달아 실시간으로 물의 대략적인 이온 양을 측정합니다.
        - **하이브리드 바이패스(Bypass) 시스템**: 
          - 측정한 경도가 지나치게 높으면 역삼투압(RO) 필터로 물을 통과시켜 미네랄을 완벽하게 걸러냅니다.
          - 측정한 경도가 지나치게 낮으면(학생님의 데이터처럼 25mg/L 수준) 천연 방해석(Calcite)과 마그네슘이 들어있는 미네랄 주입 필터로 통과시켜 **맛있는 물의 최적 포인트(경도 100 mg/L 부근)로 재합성**합니다.
        """)
