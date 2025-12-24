import streamlit as st
import joblib
import os
import plotly.graph_objects as go
from dotenv import load_dotenv

# 1. MODULAR IMPORTS
from backend.services.engine import WaterTwinCore
from backend.ai.advisor import AIAdvisor

# 2. CONFIGURATION & STYLING
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="WaterTwin AI | Digital Twin Dashboard",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Industrial Dashboard Theme
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #00ccff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #00ccff;
        color: black;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0099cc;
        color: white;
    }
    .report-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #1e2130;
        border: 1px solid #00ccff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. RESOURCE CACHING
@st.cache_resource
def load_engine():
    model_path = 'models/watertwin_engine.joblib'
    if os.path.exists(model_path):
        try:
            return joblib.load(model_path)
        except Exception as e:
            st.error(f"Engine Load Error: {e}")
            return None
    return None

# Initialization
engine = load_engine()

if "advisor" not in st.session_state and GEMINI_API_KEY:
    try:
        st.session_state.advisor = AIAdvisor()
    except Exception as e:
        st.error(f"AI Advisor Init Failure: {e}")

# 4. APPLICATION LOGIC
if engine and GEMINI_API_KEY:
    # --- SIDEBAR CONTROLS ---
    with st.sidebar:
        st.title("System Controls")
        
        with st.expander("Physical Parameters", expanded=True):
            engine.roof_area = st.number_input("Roof Area (m2)", value=float(engine.roof_area), step=10.0)
            engine.tank_capacity = st.number_input("Tank Capacity (L)", value=float(engine.tank_capacity), step=100.0)
        
        st.divider()
        st.subheader("Environmental Inputs")
        rain_val = st.slider("Forecasted Rainfall (mm)", 0.0, 100.0, 25.0)
        temp_val = st.slider("Ambient Temperature (°C)", -10.0, 50.0, 25.0)
        current_fill = st.slider("Current Tank Storage (%)", 0, 100, 40)
        
        st.info("Adjust sliders to simulate real-time catchment scenarios.")

    # --- COMPUTATION ---
    results = engine.run_simulation(rain_val, current_fill, temp_val)

    # --- UPDATED STATUS LOGIC (LOW WATER WARNING) ---
    # JSON'dan gelen kritik eşiği alıyoruz (Varsayılan: %15)
    threshold = engine.config.get('critical_threshold_pct', 15.0)
    
    if results['overflow_L'] > 0:
        results['status'] = "OVERFLOW RISK"
        status_color = "normal" # Delta inverse olduğu için kırmızı yanar
    elif results['final_fill_rate'] < threshold:
        results['status'] = "CRITICAL LOW"
        status_color = "inverse" # Düşük seviye uyarısı
    else:
        results['status'] = "STABLE"
        status_color = "normal"

    # --- MAIN DASHBOARD ---
    st.title("WaterTwin AI Dashboard")
    
    # Kritik seviye uyarısı için görsel banner
    if results['status'] == "CRITICAL LOW":
        st.error(f"SYSTEM ALERT: Tank level is below critical threshold ({threshold}%). Strategic conservation required.")
    elif results['status'] == "OVERFLOW RISK":
        st.warning(f"SYSTEM ALERT: High inflow detected. Predicted overflow of {results['overflow_L']} L.")

    # Row 1: Key Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Predicted Inflow", f"{results['inflow_L']} L")
    m2.metric("Predicted Usage", f"{results['predicted_usage_L']} L")
    
    # Dinamik durum rengi ile Metric gösterimi
    m3.metric("Storage Status", results['status'], delta=results['status'] if results['status'] != "STABLE" else None, delta_color=status_color)
    m4.metric("Overflow Prediction", f"{results['overflow_L']} L", delta=results['overflow_L'], delta_color="inverse")

    st.divider()

    # Row 2: Visualizations
    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.markdown("#### Storage Level Prediction")
        # Gauge Chart'ta kırmızı bölgeyi eşik değerimize göre ayarlıyoruz
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = results['final_fill_rate'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            number = {'suffix': "%"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#00ccff"},
                'steps': [
                    {'range': [0, threshold], 'color': "#ff4b4b"}, # Kırmızı Bölge (Kritik Eşik)
                    {'range': [threshold, 80], 'color': "#1e2130"},
                    {'range': [80, 100], 'color': "#00ccff"}
                ],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': 95
                }
            }
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white", 'family': "Arial"})
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.markdown("#### Strategic AI Analysis")
        st.write("Click below to generate an AI-driven management report based on the current simulation.")
        
        if st.button("Generate Strategy Report"):
            if "advisor" in st.session_state:
                with st.spinner("Analyzing simulation telemetry via Gemini 2.0 Flash..."):
                    try:
                        report = st.session_state.advisor.get_strategic_advice(results)
                        st.markdown(f'<div class="report-container">{report}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"AI Service Interruption: {e}")
            else:
                st.warning("AI Advisor is not ready. Check system logs.")

    st.divider()
    st.caption("WaterTwin AI Project | Powered by Gemini 2.0 Flash and Scikit-Learn")

else:
    if not GEMINI_API_KEY:
        st.warning("Missing Configuration: Set GEMINI_API_KEY in the .env file.")
    if not engine:
        st.error("Engine Offline: models/watertwin_engine.joblib not found.")