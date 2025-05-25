import streamlit as st

st.title("ATP 생성 계산기 - 다양한 기준 선택 가능")

# 기준 선택
criteria = st.selectbox("기준 선택", ["포도당", "해당과정", "피루브산 산화", "TCA 회로"])

# 입력창 기준별 분기
if criteria == "포도당":
    glucose = st.number_input("포도당 분자 수 (정수)", min_value=1, value=1, step=1, format="%d")
    
    glycolysis_runs = glucose
    pyruvate_oxidations = glucose * 2
    tca_cycles = glucose * 2
    
elif criteria == "해당과정":
    glycolysis_runs = st.number_input("해당과정 반복 횟수 (정수)", min_value=1, value=1, step=1, format="%d")
    
    glucose = glycolysis_runs
    pyruvate_oxidations = glucose * 2
    tca_cycles = glucose * 2

elif criteria == "피루브산 산화":
    pyruvate_oxidations = st.number_input("피루브산 산화 반복 횟수 (짝수만 입력 가능)", min_value=2, value=2, step=2, format="%d")
    
    glucose = pyruvate_oxidations // 2  # 정수 나누기
    glycolysis_runs = glucose
    tca_cycles = glucose * 2

elif criteria == "TCA 회로":
    tca_cycles = st.number_input("TCA 회로 반복 횟수 (짝수만 입력 가능)", min_value=2, value=2, step=2, format="%d")
    
    glucose = tca_cycles // 2
    glycolysis_runs = glucose
    pyruvate_oxidations = glucose * 2

# 계산

# 해당과정
glycolysis_atp = 2 * glycolysis_runs
glycolysis_nadh = 2 * glycolysis_runs

# 피루브산 산화
pyruvate_nadh = 1 * pyruvate_oxidations

# TCA 회로
tca_atp = 1 * tca_cycles
tca_nadh = 3 * tca_cycles
tca_fadh2 = 1 * tca_cycles

# 산화적 인산화
atp_per_nadh = 2.5
atp_per_fadh2 = 1.5
oxidative_atp = (glycolysis_nadh + pyruvate_nadh + tca_nadh) * atp_per_nadh + tca_fadh2 * atp_per_fadh2

# 총 ATP
total_atp = glycolysis_atp + tca_atp + oxidative_atp

# 결과 출력
st.subheader("계산 결과")
st.write(f"포도당 분자 수 기준: {glucose} 분자")
st.write(f"해당과정: ATP {glycolysis_atp}개, NADH {glycolysis_nadh}개")
st.write(f"피루브산 산화: NADH {pyruvate_nadh}개")
st.write(f"TCA 회로: ATP {tca_atp}개, NADH {tca_nadh}개, FADH2 {tca_fadh2}개")
st.write(f"산화적 인산화: {(glycolysis_nadh + pyruvate_nadh + tca_nadh)} NADH × 2.5 + {tca_fadh2} FADH2 × 1.5 = {oxidative_atp:.1f} ATP")
st.markdown(f"### 🧪 총 ATP 생성량: {total_atp:.1f} 개")
