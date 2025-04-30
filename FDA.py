import streamlit as st
import pandas as pd
import joblib
import time

# === PAGE CONFIGURATION ===
st.set_page_config(
    page_title="OTT Fraud Detection Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# === CUSTOM CSS STYLING ===
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .main {
        background-color: #0e1117;
        color: white;
    }
    h1, h2, h3 {
        color: #00C7E0;
        text-align: center;
    }
    h4 {
        color: #8be9fd;
        text-align: center;
        font-weight: normal;
    }
    .stButton > button {
        background: linear-gradient(90deg, #00C7E0 0%, #007f9b 100%);
        color: white;
        font-weight: bold;
        font-size: 18px;
        border-radius: 12px;
        padding: 0.6em 2em;
        transition: 0.4s;
        border: none;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #007f9b 0%, #005f70 100%);
        transform: scale(1.05);
    }
    .stNumberInput input {
        background-color: #1c1e25;
        color: white;
        border-radius: 8px;
    }
    footer {
        text-align: center;
        color: #777;
        font-size: 0.9em;
        margin-top: 3em;
        padding: 1em 0;
        border-top: 1px solid #333;
    }
    /* Common Animation */
    @keyframes glow {
        from { text-shadow: 0 0 5px; }
        to { text-shadow: 0 0 20px; }
    }
    .glow-shield {
        text-align: center;
        font-size: 60px;
        margin-top: 20px;
        color: #00C7E0;
        text-shadow: 0 0 10px #00C7E0;
        animation: glow 2s ease-in-out infinite alternate;
    }
    .glow-fraud {
        text-align: center;
        font-size: 60px;
        margin-top: 20px;
        color: #ff4b4b;
        text-shadow: 0 0 10px #ff4b4b;
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    .glow-suspicious {
        text-align: center;
        font-size: 60px;
        margin-top: 20px;
        color: #ffc107;
        text-shadow: 0 0 10px #ffc107;
        animation: glow 2s ease-in-out infinite alternate;
    }
    /* Progress Bar Styling */
    .progress-bar {
        width: 100%;
        height: 10px;
        background: #1e1e1e;
        border-radius: 10px;
        margin-top: 20px;
    }
    .progress-bar-fill {
        height: 100%;
        background: #00C7E0;
        border-radius: 10px;
        width: 0;
        transition: width 1s;
    }
    </style>
""", unsafe_allow_html=True)

# === MODEL LOADING ===
@st.cache_resource
def load_model():
    return joblib.load("best_rf_model.pkl")

model = load_model()

# === HEADER SECTION ===
st.title("🛡️ OTT Fraud Detection Dashboard")
st.markdown("<h4>Real-Time Intelligence for Network Safety</h4>", unsafe_allow_html=True)
st.markdown("---")

# === INPUT FORM SECTION ===
with st.form("fraud_form"):
    st.subheader("🔍 Input Network Data")

    col1, col2 = st.columns(2)

    with col1:
        FLOWS = st.number_input("🌐 Number of FLOWS", min_value=0, max_value=2500, value=1)
        FLOW_DURATION_MEAN = st.number_input("⏱️ Flow Duration Mean", min_value=0, max_value=999999999, value=4535235)

    with col2:
        AVG_PACKET_SIZE = st.number_input("📦 Average Packet Size", min_value=0, max_value=1600, value=120)
        FLOW_BYTES_PER_SEC = st.number_input("⚡ Flow Bytes Per Second", min_value=0, max_value=999999999, value=20)

    submitted = st.form_submit_button("🔎 Predict Now")

# === PREDICTION OUTPUT ===
if submitted:
    with st.spinner('🛡️ Analyzing network data...'):
        time.sleep(2)

        features = pd.DataFrame([[FLOWS, AVG_PACKET_SIZE, FLOW_DURATION_MEAN, FLOW_BYTES_PER_SEC]],
                                columns=["YOUTUBE.FLOWS", "YOUTUBE.AVG.PACKET.SIZE", "YOUTUBE.FLOW.DURATION.MEAN", "YOUTUBE.FLOW.BYTES.PER.SEC"])

        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0][int(prediction)]

    st.markdown("---")
    st.markdown("### 📊 Prediction Result")

    if prediction == 2:
        st.error("🚨 High Risk: Fraudulent Activity Detected")
        st.markdown(f"""
            <div class="glow-fraud">
                🧨
            </div>
            <div style='text-align: center; font-size: 24px; color: #ff4b4b;'>
                Probability of Fraud: <b>{prediction_proba:.2%}</b><br><br>
                Immediate Action Required
            </div>
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: {prediction_proba * 100}%"></div>
            </div>
        """, unsafe_allow_html=True)

    elif prediction == 1:
        st.warning("⚠️ Medium Risk: Suspicious Activity Detected")
        st.markdown(f"""
            <div class="glow-suspicious">
                🔍
            </div>
            <div style='text-align: center; font-size: 24px; color: #ffc107;'>
                Probability of Suspicion: <b>{prediction_proba:.2%}</b><br><br>
                Monitoring Recommended
            </div>
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: {prediction_proba * 100}%"></div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.success("✅ Low Risk: No Fraud Detected")
        st.markdown(f"""
            <div class="glow-shield">
                🛡️✨
            </div>
            <div style='text-align: center; font-size: 24px; color: #00C7E0;'>
                Probability of No Fraud: <b>{prediction_proba:.2%}</b><br><br>
                Network is Safe
            </div>
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: {prediction_proba * 100}%"></div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

# === FOOTER ===
st.markdown("<footer>© 2025 OTT Fraud Detection System • All rights reserved.</footer>", unsafe_allow_html=True)