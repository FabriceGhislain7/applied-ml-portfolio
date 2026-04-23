import sys
from pathlib import Path

import streamlit as st


PROJECTS = [
    {
        "slug": "air-quality",
        "title": "Air Quality Sensor Calibration",
        "status": "Available now",
        "live_url": "air-quality",
        "location": "Data Analytics / Machine Learning",
        "summary": (
            "Research-oriented dashboard for noisy air-quality sensor data, "
            "reference analyzer measurements, and regression-based sensor calibration."
        ),
        "details": (
            "This project focuses on a real scientific dataset with sensor signals, "
            "meteorological variables, missing-value handling, regression benchmarking, "
            "and technical documentation."
        ),
        "stack": ["Streamlit", "Pandas", "Scikit-learn", "Plotly", "Sphinx"],
        "available": True,
        "cta": "Enter Project",
    },
    {
        "slug": "titanic",
        "title": "Titanic Survival Analysis",
        "status": "Coming soon",
        "live_url": "#",
        "location": "Exploratory Analytics / ML Storytelling",
        "summary": (
            "Exploratory data analysis and machine-learning storytelling around the "
            "Titanic survival dataset."
        ),
        "details": (
            "This slot is reserved for a standalone analytical experience focused on "
            "feature exploration, statistical patterns, and survival modelling."
        ),
        "stack": ["Streamlit", "Pandas", "Seaborn", "Scikit-learn"],
        "available": False,
        "cta": "Availability",
    },
    {
        "slug": "thesis",
        "title": "Thesis Project",
        "status": "Coming soon",
        "live_url": "#",
        "location": "Academic Work / Research",
        "summary": (
            "Dedicated space for thesis-related analysis, methodology, experimental "
            "results, and structured documentation."
        ),
        "details": (
            "The thesis section will be handled as a separate project with its own "
            "identity, documentation flow, and analytical structure."
        ),
        "stack": ["Research", "Documentation", "Analysis"],
        "available": False,
        "cta": "Availability",
    },
    {
        "slug": "future-project",
        "title": "Future Project",
        "status": "Coming soon",
        "live_url": "#",
        "location": "Reserved Slot",
        "summary": (
            "Placeholder for the next applied analytics or machine-learning case study "
            "added to the platform."
        ),
        "details": (
            "The platform is being structured to scale cleanly as new standalone "
            "projects are added without redesigning the full experience."
        ),
        "stack": ["Scalable", "Standalone-ready"],
        "available": False,
        "cta": "Availability",
    },
]

PROJECT_ROOT = Path(__file__).parent / "projects" / "air_quality"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


@st.dialog("Project not available yet")
def show_coming_soon_dialog(project_title: str) -> None:
    st.write(f"`{project_title}` is not available in the platform yet.")
    st.write(
        "The selector is already prepared for it, but the standalone project has not "
        "been connected yet."
    )
    st.info("For now, only Air Quality Sensor Calibration is ready for integration.")

def render_browser() -> None:
    st.set_page_config(page_title="Applied ML Portfolio", page_icon="ML", layout="wide")

    st.markdown(
        """
    <style>
    :root {
        --p2-ink: #173C3B;
        --p2-deep: #0E4548;
        --p2-panel: #D7E7DE;
        --p2-mist: #E6EEE9;
        --p2-paper: #F5F8F6;
        --p2-line: #A8C1B9;
        --p2-accent: #6F9B8E;
        --p2-warning: #B65B4B;
        --p2-white: #FFFFFF;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(111, 155, 142, 0.12), transparent 20%),
            linear-gradient(180deg, var(--p2-paper) 0%, var(--p2-mist) 100%);
        color: var(--p2-ink);
    }

    [data-testid="stHeader"] {
        background: rgba(245, 248, 246, 0.96);
        border-bottom: 1px solid rgba(168, 193, 185, 0.6);
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stToolbar"] * {
        color: #5f6f67 !important;
    }

    .main .block-container {
        max-width: 1320px;
        padding-top: 1.4rem;
        padding-bottom: 2.4rem;
    }

    .portfolio-topbar {
        position: relative;
        margin-bottom: 1.55rem;
        padding: 1.7rem 1.7rem 1.55rem;
        border: 1px solid rgba(168, 193, 185, 0.8);
        border-radius: 20px;
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.94), rgba(230, 238, 233, 0.92));
        box-shadow: 0 22px 42px rgba(14, 69, 72, 0.08);
        text-align: center;
        overflow: hidden;
    }

    .portfolio-topbar::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 10px;
        background: linear-gradient(90deg, var(--p2-deep) 0%, var(--p2-accent) 100%);
        pointer-events: none;
    }

    .portfolio-topbar::after {
        content: "";
        position: absolute;
        left: 1.2rem;
        right: 1.2rem;
        bottom: 1rem;
        height: 1px;
        background: rgba(168, 193, 185, 0.85);
        pointer-events: none;
    }

    .portfolio-kicker {
        position: relative;
        z-index: 1;
        margin: 0 0 0.65rem 0;
        letter-spacing: 0.02em;
        font-size: 3rem;
        color: var(--p2-ink);
        font-weight: 900;
        line-height: 1;
    }

    .portfolio-topbar p {
        position: relative;
        z-index: 1;
        margin: 0;
        color: var(--p2-ink);
        line-height: 1.72;
        max-width: 56rem;
        margin-inline: auto;
        font-size: 1rem;
    }

    .portfolio-list-label {
        margin: 0 0 0.75rem 0;
        color: var(--p2-deep);
        font-size: 0.84rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.09em;
    }

    [data-testid="column"]:first-child {
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.84), rgba(230, 238, 233, 0.82));
        border: 1px solid rgba(168, 193, 185, 0.8);
        border-radius: 18px;
        padding: 1rem 0.95rem 0.95rem;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.48);
    }

    [data-testid="column"]:first-child div[data-testid="stVerticalBlock"] {
        gap: 0.06rem;
    }

    [data-testid="column"] [data-testid="stElementContainer"]:has(.stButton) {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }

    .portfolio-detail-card {
        border: 1px solid rgba(168, 193, 185, 0.95);
        border-radius: 18px;
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(230, 238, 233, 0.96));
        box-shadow: 0 24px 44px rgba(14, 69, 72, 0.08);
        overflow: hidden;
    }

    .portfolio-detail-band {
        height: 12px;
        background: linear-gradient(90deg, var(--p2-deep) 0%, var(--p2-accent) 100%);
        border-radius: 0;
    }

    .portfolio-detail-body {
        padding: 1.28rem 1.9rem 1.8rem;
    }

    .portfolio-status {
        display: inline-block;
        margin: 0 0 0.9rem 0;
        padding: 0.38rem 0.74rem;
        border-radius: 999px;
        background: rgba(111, 155, 142, 0.14);
        color: var(--p2-deep);
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    .portfolio-title-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 0.45rem;
    }

    .portfolio-detail-body h2 {
        margin: 0;
        color: var(--p2-ink);
        font-size: 2.15rem;
        line-height: 1.04;
    }

    .portfolio-location {
        margin-bottom: 1.05rem;
        color: var(--p2-deep);
        font-size: 0.94rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .portfolio-summary,
    .portfolio-details {
        color: var(--p2-ink);
        line-height: 1.74;
        font-size: 1rem;
    }

    .portfolio-summary {
        font-size: 1.04rem;
    }

    .portfolio-section-title {
        margin-top: 1.3rem;
        margin-bottom: 0.5rem;
        color: var(--p2-ink);
        font-size: 0.9rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .portfolio-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.7rem;
    }

    .portfolio-tag {
        display: inline-block;
        padding: 0.38rem 0.66rem;
        border-radius: 999px;
        background: rgba(215, 231, 222, 0.95);
        color: var(--p2-deep);
        font-size: 0.82rem;
        font-weight: 800;
    }

    .portfolio-note {
        margin-top: 1.25rem;
        color: var(--p2-ink);
        font-size: 0.92rem;
        line-height: 1.55;
        padding-top: 0.95rem;
        border-top: 1px dashed rgba(168, 193, 185, 0.9);
    }

    .portfolio-live-link {
        display: inline-block;
        padding: 0.68rem 1rem;
        border: 1px solid var(--p2-deep);
        border-radius: 999px;
        background: var(--p2-deep);
        color: #ffffff !important;
        font-size: 0.92rem;
        font-weight: 800;
        text-decoration: none !important;
        white-space: nowrap;
        box-shadow: 0 10px 18px rgba(14, 69, 72, 0.16);
    }

    .portfolio-live-link:visited {
        color: #ffffff !important;
    }

    .portfolio-live-link:hover {
        background: var(--p2-ink);
        border-color: var(--p2-ink);
        color: #ffffff !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid var(--p2-deep) !important;
        background: var(--p2-deep) !important;
        color: #ffffff !important;
        font-weight: 800;
        padding: 0.46rem 0.9rem;
        text-align: left;
        box-shadow: 0 8px 16px rgba(14, 69, 72, 0.1);
    }

    .stButton > button:hover {
        border-color: var(--p2-ink) !important;
        background: var(--p2-ink) !important;
        color: #ffffff !important;
    }

    @media (max-width: 900px) {
        .portfolio-kicker {
            font-size: 2.45rem;
        }

        .portfolio-title-row {
            flex-direction: column;
            align-items: flex-start;
        }

        .portfolio-detail-body {
            padding: 1.15rem 1.2rem 1.35rem;
        }
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    if "selected_project_slug" not in st.session_state:
        st.session_state.selected_project_slug = "air-quality"

    selected_project = next(
        project for project in PROJECTS if project["slug"] == st.session_state.selected_project_slug
    )

    project_button_styles = []
    for project in PROJECTS:
        is_selected = project["slug"] == selected_project["slug"]
        project_button_styles.append(
            f"""
            .st-key-select-{project["slug"]} {{
                margin-top: 0 !important;
                margin-bottom: 0 !important;
                padding-top: 0 !important;
                padding-bottom: 0 !important;
            }}

            .st-key-select-{project["slug"]} button {{
                border: 2px solid var(--p2-deep) !important;
                background: {"rgba(215, 231, 222, 0.92)" if is_selected else "#0E4548"} !important;
                color: {"#0E4548" if is_selected else "#ffffff"} !important;
            }}
            """
        )

    st.markdown(f"<style>{''.join(project_button_styles)}</style>", unsafe_allow_html=True)

    st.markdown(
        """
        <section class="portfolio-topbar">
            <div class="portfolio-kicker">Applied ML Portfolio</div>
            <p>
                Select a project from the left panel and inspect its details on the right,
                like a professional opportunity browser. Only one project is entered at a time.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    list_col, detail_col = st.columns([0.92, 1.48], gap="large")

    with list_col:
        st.markdown(
            '<div class="portfolio-list-label">Available and planned projects</div>',
            unsafe_allow_html=True,
        )
        for project in PROJECTS:
            label = f'{project["title"]} | {project["status"]}'
            if st.button(label, key=f'select-{project["slug"]}', use_container_width=True):
                st.session_state.selected_project_slug = project["slug"]
                st.rerun()

    with detail_col:
        stack_tags = "".join(
            f'<span class="portfolio-tag">{tag}</span>' for tag in selected_project["stack"]
        )
        live_link_html = ""
        if selected_project["available"]:
            live_link_html = (
                f'<a class="portfolio-live-link" href="./{selected_project["live_url"]}" target="_self">'
                "Open live project"
                "</a>"
            )

        st.markdown(
            f"""
            <section class="portfolio-detail-card">
                <div class="portfolio-detail-band"></div>
                <div class="portfolio-detail-body">
                    <div class="portfolio-status">{selected_project["status"]}</div>
                    <div class="portfolio-title-row">
                        <h2>{selected_project["title"]}</h2>
                        {live_link_html}
                    </div>
                    <div class="portfolio-location">{selected_project["location"]}</div>
                    <div class="portfolio-summary">{selected_project["summary"]}</div>
                    <div class="portfolio-section-title">Project Details</div>
                    <div class="portfolio-details">{selected_project["details"]}</div>
                    <div class="portfolio-section-title">Core Stack</div>
                    <div class="portfolio-tags">{stack_tags}</div>
                    <div class="portfolio-note">
                        Next step: wire the Air Quality project into
                        <code>projects/air_quality/</code> and turn the CTA into a real entry point.
                    </div>
                </div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        if selected_project["available"]:
            if st.button(
                selected_project["cta"],
                type="primary",
                key=f'enter-{selected_project["slug"]}',
            ):
                st.switch_page("projects/air_quality/app.py")
        else:
            if st.button(
                selected_project["cta"],
                key=f'popup-{selected_project["slug"]}',
                type="primary",
            ):
                show_coming_soon_dialog(selected_project["title"])


navigation = st.navigation(
    {
        "Portfolio": [
            st.Page(render_browser, title="Project Browser", url_path="", default=True),
        ],
        "Air Quality": [
            st.Page(
                "projects/air_quality/app.py",
                title="Overview",
                url_path="air-quality",
            ),
            st.Page(
                "projects/air_quality/pages/1_Data_Overview.py",
                title="Data Overview",
                url_path="air-quality-data-overview",
            ),
            st.Page(
                "projects/air_quality/pages/2_Sensor_Analysis.py",
                title="Sensor Analysis",
                url_path="air-quality-sensor-analysis",
            ),
            st.Page(
                "projects/air_quality/pages/3_Modeling.py",
                title="Modeling",
                url_path="air-quality-modeling",
            ),
            st.Page(
                "projects/air_quality/pages/4_Scientific_Notes.py",
                title="Scientific Notes",
                url_path="air-quality-scientific-notes",
            ),
            st.Page(
                "projects/air_quality/pages/5_Documentation.py",
                title="Documentation",
                url_path="air-quality-documentation",
            ),
        ],
    },
    position="sidebar",
    expanded=True,
)
navigation.run()
