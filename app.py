import streamlit as st


PROJECTS = [
    {
        "slug": "air-quality",
        "title": "Air Quality Sensor Calibration",
        "status": "Available now",
        "live_url": "#",
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


@st.dialog("Project not available yet")
def show_coming_soon_dialog(project_title: str) -> None:
    st.write(f"`{project_title}` is not available in the platform yet.")
    st.write(
        "The selector is already prepared for it, but the standalone project has not "
        "been connected yet."
    )
    st.info("For now, only Air Quality Sensor Calibration is ready for integration.")


st.set_page_config(page_title="Applied ML Portfolio", page_icon="ML", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(188, 117, 82, 0.12), transparent 20%),
            linear-gradient(180deg, #f8f3ec 0%, #efe8dd 100%);
        color: #1f2723;
    }

    [data-testid="stHeader"] {
        background: rgba(248, 243, 236, 0.92);
        border-bottom: 1px solid rgba(47, 90, 73, 0.08);
    }

    [data-testid="stToolbar"] * {
        color: #5f6f67 !important;
    }

    .main .block-container {
        max-width: 1280px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .portfolio-topbar {
        margin-bottom: 1rem;
        padding: 1.2rem 1.4rem;
        border: 1px solid rgba(43, 70, 57, 0.1);
        border-radius: 22px;
        background: rgba(255, 251, 246, 0.92);
        box-shadow: 0 18px 40px rgba(58, 45, 28, 0.08);
        text-align: center;
    }

    .portfolio-kicker {
        margin: 0 0 0.55rem 0;
        color: #9b5e46;
        letter-spacing: 0.04em;
        font-size: 2.6rem;
        color: #1f2723;
        font-weight: 900;
    }

    .portfolio-topbar p {
        margin: 0;
        color: #5c615b;
        line-height: 1.55;
        max-width: 52rem;
        margin-inline: auto;
    }

    .portfolio-list-label {
        margin: 0 0 0.85rem 0;
        color: #6d726c;
        font-size: 0.9rem;
        font-weight: 700;
    }

    [data-testid="column"]:first-child div[data-testid="stVerticalBlock"] {
        gap: 0.08rem;
    }

    [data-testid="column"] [data-testid="stElementContainer"]:has(.stButton) {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }

    .portfolio-detail-card {
        border: 2px solid #2f5a49;
        border-radius: 24px;
        background: rgba(47, 90, 73, 0.12);
        box-shadow: 0 24px 54px rgba(58, 45, 28, 0.08);
        overflow: hidden;
    }

    .portfolio-detail-band {
        height: 14px;
        background: linear-gradient(90deg, #e5cdb3 0%, #a8bab1 100%);
        border-radius: 16px 16px 0 0;
    }

    .portfolio-detail-body {
        padding: 1.1rem 1.7rem 1.5rem;
    }

    .portfolio-status {
        display: inline-block;
        margin: 0 0 0.9rem 0;
        padding: 0.35rem 0.68rem;
        border-radius: 999px;
        background: rgba(188, 117, 82, 0.16);
        color: #8d563e;
        font-size: 0.8rem;
        font-weight: 700;
    }

    .portfolio-title-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 0.35rem;
    }

    .portfolio-detail-body h2 {
        margin: 0;
        color: #1f2723;
        font-size: 2rem;
    }

    .portfolio-location {
        margin-bottom: 1rem;
        color: #697068;
        font-size: 0.96rem;
        font-weight: 700;
    }

    .portfolio-summary,
    .portfolio-details {
        color: #4d554f;
        line-height: 1.68;
        font-size: 1rem;
    }

    .portfolio-section-title {
        margin-top: 1.25rem;
        margin-bottom: 0.45rem;
        color: #1f2723;
        font-size: 0.98rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .portfolio-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.6rem;
    }

    .portfolio-tag {
        display: inline-block;
        padding: 0.35rem 0.62rem;
        border-radius: 999px;
        background: rgba(47, 90, 73, 0.12);
        color: #2f5a49;
        font-size: 0.82rem;
        font-weight: 700;
    }

    .portfolio-note {
        margin-top: 1.15rem;
        color: #6a6e69;
        font-size: 0.92rem;
        line-height: 1.55;
    }

    .portfolio-live-link {
        display: inline-block;
        padding: 0.58rem 0.9rem;
        border: 1px solid #2e7d32;
        border-radius: 999px;
        background: #2e7d32;
        color: #ffffff !important;
        font-size: 0.92rem;
        font-weight: 800;
        text-decoration: none !important;
        white-space: nowrap;
    }

    .portfolio-live-link:visited {
        color: #ffffff !important;
    }

    .portfolio-live-link:hover {
        background: #256728;
        border-color: #256728;
        color: #ffffff !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid #2f5a49 !important;
        background: #2f5a49 !important;
        color: #ffffff !important;
        font-weight: 800;
        padding: 0.4rem 0.86rem;
        text-align: left;
    }

    .stButton > button:hover {
        border-color: #26483a !important;
        background: #26483a !important;
        color: #ffffff !important;
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
            border: 2px solid #2f5a49 !important;
            background: {"rgba(47, 90, 73, 0.12)" if is_selected else "#2f5a49"} !important;
            color: {"#2f5a49" if is_selected else "#ffffff"} !important;
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
    st.markdown('<div class="portfolio-list-label">Available and planned projects</div>', unsafe_allow_html=True)
    for project in PROJECTS:
        label = f'{project["title"]} | {project["status"]}'
        if st.button(label, key=f'select-{project["slug"]}', use_container_width=True):
            st.session_state.selected_project_slug = project["slug"]
            st.rerun()

with detail_col:
    stack_tags = "".join(
        f'<span class="portfolio-tag">{tag}</span>' for tag in selected_project["stack"]
    )
    st.markdown(
        f"""
        <section class="portfolio-detail-card">
            <div class="portfolio-detail-band"></div>
            <div class="portfolio-detail-body">
                <div class="portfolio-status">{selected_project["status"]}</div>
                <div class="portfolio-title-row">
                    <h2>{selected_project["title"]}</h2>
                    <a class="portfolio-live-link" href="{selected_project["live_url"]}" target="_blank">
                        Open live project
                    </a>
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
        st.button(
            selected_project["cta"],
            type="primary",
            disabled=True,
            help="Project wiring will be connected next.",
            key=f'enter-{selected_project["slug"]}',
        )
    else:
        if st.button(selected_project["cta"], key=f'popup-{selected_project["slug"]}', type="primary"):
            show_coming_soon_dialog(selected_project["title"])



