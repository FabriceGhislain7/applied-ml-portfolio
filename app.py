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
            linear-gradient(180deg, #f5f0e6 0%, #ebe1d1 100%);
        color: #243028;
    }

    [data-testid="stHeader"] {
        background: rgba(245, 240, 230, 0.96);
        border-bottom: 1px solid rgba(86, 99, 86, 0.12);
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
        border: 1px solid rgba(111, 95, 71, 0.16);
        border-radius: 20px;
        background:
            repeating-linear-gradient(
                180deg,
                rgba(255, 250, 243, 0.96),
                rgba(255, 250, 243, 0.96) 34px,
                rgba(216, 207, 190, 0.22) 35px,
                rgba(255, 250, 243, 0.96) 36px
            );
        box-shadow: 0 22px 42px rgba(79, 63, 44, 0.08);
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
        background: linear-gradient(90deg, #516555 0%, #8a9b7f 58%, #bc8f63 100%);
        pointer-events: none;
    }

    .portfolio-topbar::after {
        content: "";
        position: absolute;
        left: 1.2rem;
        right: 1.2rem;
        bottom: 1rem;
        height: 1px;
        background: rgba(111, 95, 71, 0.14);
        pointer-events: none;
    }

    .portfolio-kicker {
        position: relative;
        z-index: 1;
        margin: 0 0 0.65rem 0;
        letter-spacing: 0.02em;
        font-size: 3rem;
        color: #243028;
        font-weight: 900;
        line-height: 1;
    }

    .portfolio-topbar p {
        position: relative;
        z-index: 1;
        margin: 0;
        color: #645f57;
        line-height: 1.72;
        max-width: 56rem;
        margin-inline: auto;
        font-size: 1rem;
    }

    .portfolio-list-label {
        margin: 0 0 0.75rem 0;
        color: #6a6258;
        font-size: 0.84rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.09em;
    }

    [data-testid="column"]:first-child {
        background:
            linear-gradient(180deg, rgba(255, 250, 244, 0.82), rgba(245, 237, 225, 0.8));
        border: 1px solid rgba(111, 95, 71, 0.12);
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
        border: 1px solid rgba(111, 95, 71, 0.18);
        border-radius: 18px;
        background:
            linear-gradient(180deg, rgba(255, 251, 246, 0.98), rgba(246, 238, 227, 0.98));
        box-shadow: 0 24px 44px rgba(79, 63, 44, 0.08);
        overflow: hidden;
    }

    .portfolio-detail-band {
        height: 12px;
        background: linear-gradient(90deg, #516555 0%, #81907a 55%, #bc8f63 100%);
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
        background: rgba(188, 143, 99, 0.16);
        color: #8a5b32;
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
        color: #243028;
        font-size: 2.15rem;
        line-height: 1.04;
    }

    .portfolio-location {
        margin-bottom: 1.05rem;
        color: #676057;
        font-size: 0.94rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .portfolio-summary,
    .portfolio-details {
        color: #4e4a43;
        line-height: 1.74;
        font-size: 1rem;
    }

    .portfolio-summary {
        font-size: 1.04rem;
    }

    .portfolio-section-title {
        margin-top: 1.3rem;
        margin-bottom: 0.5rem;
        color: #243028;
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
        background: rgba(81, 101, 85, 0.12);
        color: #516555;
        font-size: 0.82rem;
        font-weight: 800;
    }

    .portfolio-note {
        margin-top: 1.25rem;
        color: #675f56;
        font-size: 0.92rem;
        line-height: 1.55;
        padding-top: 0.95rem;
        border-top: 1px dashed rgba(111, 95, 71, 0.18);
    }

    .portfolio-live-link {
        display: inline-block;
        padding: 0.68rem 1rem;
        border: 1px solid #516555;
        border-radius: 999px;
        background: #516555;
        color: #ffffff !important;
        font-size: 0.92rem;
        font-weight: 800;
        text-decoration: none !important;
        white-space: nowrap;
        box-shadow: 0 10px 18px rgba(81, 101, 85, 0.16);
    }

    .portfolio-live-link:visited {
        color: #ffffff !important;
    }

    .portfolio-live-link:hover {
        background: #445647;
        border-color: #445647;
        color: #ffffff !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid #516555 !important;
        background: #516555 !important;
        color: #ffffff !important;
        font-weight: 800;
        padding: 0.46rem 0.9rem;
        text-align: left;
        box-shadow: 0 8px 16px rgba(81, 101, 85, 0.1);
    }

    .stButton > button:hover {
        border-color: #445647 !important;
        background: #445647 !important;
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



