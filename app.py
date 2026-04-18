"""Main Streamlit entry point for the applied ML portfolio."""

import streamlit as st


PROJECT_SLUGS = {
    "air-quality": "Air Quality Sensor Calibration",
    "titanic": "Titanic Survival Dashboard",
}

PROJECT_PAGES = {
    "Air Quality Sensor Calibration": [
        st.Page("projects/air_quality/app.py", title="Overview", icon=":material/air:", url_path="air-quality"),
        st.Page("projects/air_quality/pages/1_Data_Overview.py", title="Data Overview", icon=":material/table_chart:", url_path="air-quality-data-overview"),
        st.Page("projects/air_quality/pages/2_Sensor_Analysis.py", title="Sensor Analysis", icon=":material/sensors:", url_path="air-quality-sensor-analysis"),
        st.Page("projects/air_quality/pages/3_Modeling.py", title="Modeling", icon=":material/model_training:", url_path="air-quality-modeling"),
        st.Page("projects/air_quality/pages/4_Scientific_Notes.py", title="Scientific Notes", icon=":material/science:", url_path="air-quality-scientific-notes"),
        st.Page("projects/air_quality/pages/5_Documentation.py", title="Documentation", icon=":material/article:", url_path="air-quality-documentation"),
    ],
    "Titanic Survival Dashboard": [
        st.Page("projects/titanic/app.py", title="Overview", icon=":material/dashboard:", url_path="titanic"),
        st.Page("projects/titanic/pages/1_Data_Overview.py", title="Data Overview", icon=":material/table_chart:", url_path="titanic-data-overview"),
        st.Page("projects/titanic/pages/2_Univariate_Analysis.py", title="Univariate Analysis", icon=":material/bar_chart:", url_path="titanic-univariate-analysis"),
        st.Page("projects/titanic/pages/3_Bivariate_Analysis.py", title="Bivariate Analysis", icon=":material/scatter_plot:", url_path="titanic-bivariate-analysis"),
        st.Page("projects/titanic/pages/4_Advanced_Analytics.py", title="Advanced Analytics", icon=":material/analytics:", url_path="titanic-advanced-analytics"),
        st.Page("projects/titanic/pages/5_ML_Predictions.py", title="ML Predictions", icon=":material/model_training:", url_path="titanic-ml-predictions"),
    ],
}

DEFAULT_SLUG = "air-quality"
current_slug = st.query_params.get("project", DEFAULT_SLUG)
if current_slug not in PROJECT_SLUGS:
    current_slug = DEFAULT_SLUG

current_project = PROJECT_SLUGS[current_slug]

st.markdown(
    f"""
    <style>
    [data-testid="stSidebarNav"]::before {{
        content: "{current_project}";
        display: block;
        padding: 0.75rem 1rem 0.25rem;
        font-weight: 700;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

header_cols = st.columns([1, 4])
with header_cols[0]:
    with st.popover(f"Project: {current_project}", use_container_width=True):
        st.caption("Choose a project")
        for slug, name in PROJECT_SLUGS.items():
            if st.button(name, key=f"project-{slug}", use_container_width=True, disabled=slug == current_slug):
                st.query_params["project"] = slug
                st.rerun()

navigation = st.navigation(PROJECT_PAGES[current_project], position="sidebar", expanded=True)
navigation.run()
