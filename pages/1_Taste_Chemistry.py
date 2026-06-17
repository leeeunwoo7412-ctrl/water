import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="당곡고 물맛 탐구 - 농도별 물맛",
    page_icon="🧪",
    layout="wide"
)

st.sidebar.info("🏫 **당곡고등학교 과학탐구**\n\n학생들의 주도적인 탐구를 돕는 탐구 도우미 프로그램입니다.")

st.title("🧪 농도에 따른 물맛 시뮬레이터")
st.write("슬라이더를 통해 물 속 화학 성분의 양을 조절하며 물맛의 변화를 과학적으로 예측해봅니다.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛠️ 이온 농도 미세 조정")
    ca = st.slider("칼슘 이온 (Ca²⁺) 농도 (mg/L)", 0.0, 100.0, 8.0, step=0.5)
    mg = st.slider("마그네슘 이온 (Mg²⁺) 농도 (mg/L)", 0.0, 50.0, 2.0, step=0.1)
    so4 = st.slider("황산 이온 (SO₄²⁻) 농도 (mg/L)", 0.0, 100.0, 4.0, step=0.5)
    cl = st.slider("염소 이온 (Cl⁻) 농도 (mg/L)", 0.0, 150.0, 8.6, step=0.1)
    ph = st.slider("수소이온농도 (pH)", 5.0, 9.0, 6.9, step=0.1)
    
with col2:
    st.subheader("📊 물맛 화학적 진단")
    
    # 1. 경도 계산: (Ca * 2.497) + (Mg * 4.118)
    hardness = (ca * 2.497) + (mg * 4.118)
    
    # 2. 하시모토 물맛 지수 (O-Index) 계산
    # 공식: O-Index = (Ca + K + SiO2) / (Mg + SO4)
    # 일반 수돗물의 칼륨 K=1.5, 규산 SiO2=10.0 상수로 대입
    o_index = (ca + 1.5 + 10.0) / (mg + so4 + 1.0)
    
    st.metric(label="🥛 계산된 총 경도 (mg/L as CaCO₃)", value=f"{hardness:.2f} mg/L")
    if hardness < 75:
        st.info("💧 **연수 (Soft Water)**: 목넘김이 매우 부드럽고 가볍지만, 미네랄 특유의 청량한 맛은 적을 수 있습니다.")
    elif 75 <= hardness < 150:
        st.success("🥛 **적당한 경수 (Moderately Hard)**: 맛이 가장 균형 잡히고 마시기 편한 최적의 상태입니다.")
    else:
        st.error("🧱 **경수 (Hard Water)**: 텁텁하고 쓴맛이 나며 목넘김이 무겁고 뻑뻑하게 느껴집니다.")
        
    st.metric(label="📊 하시모토 물맛 지수 (O-Index)", value=f"{o_index:.2f}", help="2.0 이상일 때 사람이 맛있다고 느낍니다.")
    if o_index >= 2.0:
        st.success("✨ **평가: 매우 맛있는 물!** 칼슘에 비해 마그네슘과 황산염의 비율이 낮아 청량하고 맛있습니다.")
    else:
        st.warning("⚠️ **평가: 맛이 덜한 물** 마그네슘이나 황산이온 비율이 높아 혀끝에 미세한 쓴맛이나 텁텁함이 남을 수 있습니다.")
        
    # pH 진단
    if ph < 6.5:
        st.warning("🍋 **pH 상태**: 약산성입니다. 미세한 신맛이 느껴질 수 있으며 배관 부식 위험이 존재합니다.")
    elif ph > 7.5:
        st.warning("🧼 **pH 상태**: 약알칼리성입니다. 약간 매끄럽거나 미끈거리는 쓴맛이 날 수 있습니다.")
    else:
        st.success("⚖️ **pH 상태**: 중성입니다. 산도에 의한 이물감이 전혀 없는 깔끔한 물맛입니다.")
