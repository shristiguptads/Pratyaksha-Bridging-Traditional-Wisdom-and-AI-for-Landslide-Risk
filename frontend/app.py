import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Pratyaksha Soil Data", layout="wide")
st.title("🌱 Pratyaksha – Soil Feature Collection")

features = [
    'color_red', 'color_brown', 'color_black', 'color_white', 'color_green', 'color_yellow',
    'texture_sand', 'texture_silt', 'texture_gravel', 'texture_clay', 'texture_rocks_debris', 'texture_coarseness',
    'water_retention', 'water_drainage', 'water_moisture', 'water_dryness', 'water_hardness', 'water_smoothness', 'water_density',
    'smell_earthy', 'smell_musty', 'smell_foul',
    'taste_sweetness', 'taste_saltiness',
    'fertility_fertile', 'fertility_plant_health', 'fertility_deforestation', 'fertility_vegetation_cover',
    'field_stickiness', 'field_crumbling', 'field_clump'
]

if 'ratings' not in st.session_state:
    st.session_state.ratings = {f: 3 for f in features}

col1, col2 = st.columns(2)
mid = len(features) // 2
left = features[:mid]
right = features[mid:]

with col1:
    st.subheader("Feature Group A")
    for f in left:
        label = f.replace('_', ' ').title()
        st.session_state.ratings[f] = st.selectbox(label, [1,2,3,4,5], index=2, key=f"a_{f}")

with col2:
    st.subheader("Feature Group B")
    for f in right:
        label = f.replace('_', ' ').title()
        st.session_state.ratings[f] = st.selectbox(label, [1,2,3,4,5], index=2, key=f"b_{f}")

col_btn1, col_btn2, _ = st.columns([1,1,2])
with col_btn1:
    check = st.button("🔍 Check Risk")
with col_btn2:
    save = st.button("💾 Save Observation")

st.markdown("---")
result_placeholder = st.empty()

if check:
    with st.spinner("Calling risk model..."):
        try:
            resp = requests.post(f"{BACKEND_URL}/predict-risk/", json=st.session_state.ratings, timeout=10)
            if resp.status_code == 200:
                res = resp.json()
                level = res['risk_level']
                score = res['risk_score']
                top = res['top_factors']
                color = "green" if level=="Low" else "orange" if level=="Moderate" else "red"
                result_placeholder.markdown(f"""
                <div style="padding:20px; border-radius:10px; background-color:{color}20; border:2px solid {color};">
                    <h2 style="color:{color};">Risk Level: {level}</h2>
                    <h3>Score: {score:.2f}</h3>
                    <p><b>Top contributing factors:</b></p>
                    <ul>{"".join(f'<li>{f}</li>' for f in top)}</ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                result_placeholder.error(f"Error {resp.status_code}: {resp.text}")
        except Exception as e:
            result_placeholder.error(f"Request failed: {e}")

if save:
    payload = {
        "latitude": 31.5,  # you can replace with actual GPS later
        "longitude": 76.9,
        "traditional_features": st.session_state.ratings,
        "photos": [],
        "user_id": "streamlit_user"
    }
    with st.spinner("Saving..."):
        try:
            resp = requests.post(f"{BACKEND_URL}/observations/", json=payload, timeout=10)
            if resp.status_code == 200:
                result_placeholder.success("Observation saved successfully!")
            else:
                result_placeholder.error(f"Error {resp.status_code}: {resp.text}")
        except Exception as e:
            result_placeholder.error(f"Request failed: {e}")