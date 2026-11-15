import streamlit as st

st.set_page_config(
    page_title="FIREWATCH | Area 52",
    page_icon="🔥",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: #e8eef7;
}
[data-testid="stSidebar"] {
    background-color: #111c2e;
}
.hero {
    padding: 30px;
    border: 1px solid #29415d;
    border-radius: 16px;
    background: linear-gradient(120deg, #14243a, #102d35);
}
.status {
    color: #ffd28a;
    background: #392b18;
    padding: 7px 12px;
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🔥 FIREWATCH")
st.sidebar.caption("NASA Space Apps Challenge 2026")
st.sidebar.caption("Team Area 52")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Data Explorer",
        "Comparative Analysis",
        "Results",
        "Methodology",
        "Limitations"
    ]
)

if page == "Overview":

    st.markdown("""
    <div class="hero">
    <h1>🔥 FIREWATCH</h1>
    <h3>Satellite Fire Detection Analysis</h3>
    <p>
    Investigating differences between MODIS
    and VIIRS active-fire detections.
    </p>
    <span class="status">
    PROTOTYPE | RESULTS UNDER VALIDATION
    </span>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Research Objective")

    st.write("""
    FIREWATCH investigates whether disagreements
    between MODIS and VIIRS satellite fire detections
    can provide useful information about fire observations.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Data Sources", "2")
        st.caption("MODIS and VIIRS")

    with col2:
        st.metric("Validation Status", "Pending")
        st.caption("Results under audit")

    with col3:
        st.metric("Research Status", "Prototype")
        st.caption("Analysis in progress")

    st.info(
        "Quantitative results are not yet available. "
        "No unverified measurements are presented."
    )

elif page == "Data Explorer":

    st.title("Data Explorer")

    st.warning("Dataset recovery and validation pending.")

    st.write("""
    This section will present:
    - Original data sources
    - Temporal coverage
    - Geographic coverage
    - Data quality
    - Missing observations
    """)

elif page == "Comparative Analysis":

    st.title("Comparative Analysis")

    st.warning("Comparative analysis pending validation.")

    st.write("""
    This section will examine:
    - MODIS detections
    - VIIRS detections
    - Temporal differences
    - Spatial matching
    - Detection disagreements
    """)

elif page == "Results":

    st.title("Research Results")

    st.warning("Results pending recovery and scientific audit.")

    st.write("""
    Only validated experimental outputs
    will be presented here.
    """)

elif page == "Methodology":

    st.title("Research Methodology")

    st.write("""
    Research pipeline:

    1. Data acquisition
    2. Data validation
    3. Preprocessing
    4. Satellite detection comparison
    5. Quantitative analysis
    6. Interpretation
    """)

elif page == "Limitations":

    st.title("Limitations and Uncertainty")

    st.write("""
    - Satellite observations have different characteristics.
    - Missing detections do not automatically indicate absence of fire.
    - Disagreement does not automatically mean sensor failure.
    - Quantitative conclusions require validation.
    """)

st.divider()

st.caption(
    "FIREWATCH | Team Area 52 | NASA Space Apps Challenge 2026"
)
