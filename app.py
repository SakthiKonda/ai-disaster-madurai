import streamlit as st

st.set_page_config(page_title="Madurai Flood AI System", layout="wide")

# TITLE
st.title("🌊 AI Flood Resource Allocation System")
st.markdown("### 📍 Tamil Nadu → Madurai")

st.info("""
Flood situation detected in Madurai.
AI analyzes all areas and allocates limited resources:
- 🚁 Rescue Team (Evacuation)
- 🍱 Food Supply Unit (Relief)
""")

# DATA
areas = [
    {"name": "Anna Nagar", "population": 12000, "women": 6000, "elderly": 1800,
     "vulnerability": ["Flood-prone", "Limited hospital"], "severity": 7, "accessibility": 6},

    {"name": "KK Nagar", "population": 9000, "women": 4500, "elderly": 1200,
     "vulnerability": ["Good roads"], "severity": 4, "accessibility": 8},

    {"name": "Keelavasal", "population": 8000, "women": 3800, "elderly": 1500,
     "vulnerability": ["Low-lying area", "Flood risk"], "severity": 8, "accessibility": 5},

    {"name": "Kalavasal", "population": 13000, "women": 6500, "elderly": 2000,
     "vulnerability": ["Traffic congestion", "Delayed rescue"], "severity": 8, "accessibility": 4},

    {"name": "Therkuvasal", "population": 7000, "women": 3400, "elderly": 1200,
     "vulnerability": ["Poor drainage"], "severity": 7, "accessibility": 5},

    {"name": "Ellis Nagar", "population": 10000, "women": 5000, "elderly": 1700,
     "vulnerability": ["Waterlogging"], "severity": 6, "accessibility": 6},

    {"name": "Periyar", "population": 11000, "women": 5200, "elderly": 1600,
     "vulnerability": ["Crowded area"], "severity": 7, "accessibility": 5},

    {"name": "Villapuram", "population": 11000, "women": 5200, "elderly": 1600,
     "vulnerability": ["Narrow roads"], "severity": 6, "accessibility": 5},

    {"name": "Avaniyapuram", "population": 15000, "women": 7000, "elderly": 2500,
     "vulnerability": ["No hospitals", "Flood risk", "Poor roads"], "severity": 9, "accessibility": 3},

    {"name": "Mattuthavani", "population": 9000, "women": 4200, "elderly": 1300,
     "vulnerability": ["Bus stand congestion"], "severity": 5, "accessibility": 6},

    {"name": "Simmakkal", "population": 8500, "women": 4000, "elderly": 1400,
     "vulnerability": ["Commercial crowd"], "severity": 6, "accessibility": 5},

    {"name": "Goripalayam", "population": 9500, "women": 4700, "elderly": 1500,
     "vulnerability": ["Bridge flood risk"], "severity": 7, "accessibility": 5},

    {"name": "Tallakulam", "population": 10000, "women": 4800, "elderly": 1600,
     "vulnerability": ["Water stagnation"], "severity": 6, "accessibility": 6},

    {"name": "Annupanadi", "population": 10500, "women": 5100, "elderly": 1700,
     "vulnerability": ["Low infrastructure"], "severity": 7, "accessibility": 4},

    {"name": "Vandiyur", "population": 11500, "women": 5600, "elderly": 1800,
     "vulnerability": ["Lake overflow risk"], "severity": 8, "accessibility": 5},
]

# =========================
# 🔥 AI ANALYSIS FOR ALL AREAS
# =========================

results = []

for a in areas:
    rescue_score = (a["severity"] * 1000 + a["elderly"] * 2) / a["accessibility"]
    food_score = (a["population"] + a["women"]) / a["accessibility"]

    results.append({
        "name": a["name"],
        "rescue_score": rescue_score,
        "food_score": food_score
    })

# SORTING
rescue_sorted = sorted(results, key=lambda x: x["rescue_score"], reverse=True)
food_sorted = sorted(results, key=lambda x: x["food_score"], reverse=True)

top_rescue = rescue_sorted[0]
top_food = food_sorted[0]

# =========================
# 🚧 RESOURCE ALLOCATION
# =========================

st.subheader("🚧 AI Resource Allocation Decision")

st.warning("""
Available Resources:
- 1 Rescue Team 🚁
- 1 Food Supply Unit 🍱
""")

st.success(f"🚁 Rescue Team → {top_rescue['name']}")
st.success(f"🍱 Food Supply → {top_food['name']}")

# =========================
# 📊 PRIORITY RANKINGS
# =========================

st.divider()

st.subheader("📊 Priority Rankings")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚁 Rescue Priority")
    for i, r in enumerate(rescue_sorted, 1):
        st.write(f"{i}. {r['name']} (Score: {round(r['rescue_score'],2)})")

with col2:
    st.markdown("### 🍱 Food Supply Priority")
    for i, f in enumerate(food_sorted, 1):
        st.write(f"{i}. {f['name']} (Score: {round(f['food_score'],2)})")

# =========================
# 📍 AREA DETAILS (OPTIONAL VIEW)
# =========================

st.divider()

st.subheader("📍 Area Intelligence Viewer")

area_names = [a["name"] for a in areas]
selected_area = st.selectbox("Select Area", area_names)

area = next(a for a in areas if a["name"] == selected_area)

col1, col2 = st.columns(2)

with col1:
    st.write(f"👥 Population: {area['population']}")
    st.write(f"👩 Women: {area['women']}")
    st.write(f"👴 Elderly: {area['elderly']}")

with col2:
    st.markdown("### ⚠️ Vulnerabilities")
    for v in area["vulnerability"]:
        st.write(f"- {v}")

# =========================
# 🌍 IMPACT
# =========================

st.divider()

st.subheader("🌍 Impact")

st.write("""
This AI system:
- Analyzes all areas simultaneously
- Allocates limited rescue & food resources intelligently
- Prioritizes vulnerable populations
- Helps disaster response teams act faster and smarter
""")