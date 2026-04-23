# -*- coding: utf-8 -*-
import streamlit as st


def apply_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --avant-page-bg: #E7EDF6;
            --avant-page-bg-soft: #F5F8FD;
            --avant-surface: #FFFFFF;
            --avant-surface-muted: #F6F9FD;
            --avant-surface-alt: #EDF3FB;
            --avant-surface-strong: #E0E8F4;
            --avant-text: #1F3146;
            --avant-text-secondary: #556A82;
            --avant-text-muted: #7F91A6;
            --avant-accent: #10C9BB;
            --avant-accent-strong: #17D2BF;
            --avant-blue: #1778E6;
            --avant-danger: #F04D63;
            --avant-ink: #16273C;
            --avant-sidebar: #11243A;
            --avant-sidebar-strong: #0C1B2D;
            --avant-sidebar-text: #FFFFFF;
            --avant-sidebar-muted: #FFFFFF;
            --avant-sidebar-title: #19D0BC;
            --avant-sidebar-active: #10B8A3;
            --avant-border: #D2DEEC;
            --avant-border-strong: #B9C8DB;
            --avant-focus: #93B9D7;
            --avant-shadow-soft: 0 16px 38px rgba(27, 46, 74, 0.12);
            --avant-shadow-card: 0 20px 42px rgba(27, 46, 74, 0.14);
            --avant-radius-card: 16px;
            --avant-radius-panel: 18px;
            --avant-radius-input: 12px;
            --avant-radius-chip: 999px;
            --avant-font: "Segoe UI", "IBM Plex Sans", sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top right, rgba(16, 201, 187, 0.14), transparent 32%),
                radial-gradient(circle at top left, rgba(23, 120, 230, 0.12), transparent 28%),
                linear-gradient(180deg, var(--avant-page-bg) 0%, var(--avant-page-bg-soft) 100%);
            color: var(--avant-text);
            font-family: var(--avant-font);
        }

        [data-testid="stHeader"] {
            background: rgba(0, 0, 0, 0);
        }

        [data-testid="stSidebar"] {
            background:
                radial-gradient(circle at top left, rgba(25, 208, 188, 0.16), transparent 22%),
                linear-gradient(180deg, var(--avant-sidebar) 0%, var(--avant-sidebar-strong) 100%);
            border-right: 1px solid rgba(214, 232, 248, 0.22);
        }

        [data-testid="stSidebar"] > div:first-child {
            background: transparent;
        }

        [data-testid="stSidebar"] .stSidebarUserContent {
            padding-top: 0.55rem;
        }

        [data-testid="stSidebar"] img {
            border-radius: 16px;
        }

        [data-testid="stSidebar"] .avant-sidebar-shell {
            position: relative;
            margin: 0.15rem 0 0.8rem 0;
            padding-left: 12px;
        }

        [data-testid="stSidebar"] .avant-sidebar-shell-mark {
            position: absolute;
            left: 0;
            top: 8px;
            bottom: 8px;
            width: 4px;
            border-radius: 999px;
            background: linear-gradient(180deg, #19D0BC 0%, #1778E6 100%);
            box-shadow: 0 0 18px rgba(25, 208, 188, 0.22);
        }

        [data-testid="stSidebar"] .avant-sidebar-shell-inner {
            padding: 14px 14px 12px 14px;
            border-radius: 18px;
            border: 1px solid rgba(223, 238, 251, 0.26);
            background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04));
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.08),
                0 10px 24px rgba(6, 18, 33, 0.14);
        }

        [data-testid="stSidebar"] .avant-sidebar-shell-label {
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #EDF5FB;
            margin-bottom: 6px;
        }

        [data-testid="stSidebar"] .avant-sidebar-shell-title {
            font-size: 22px;
            font-weight: 800;
            line-height: 1.05;
            color: #FFFFFF;
            margin-bottom: 5px;
        }

        [data-testid="stSidebar"] .avant-sidebar-shell-copy {
            font-size: 12px;
            line-height: 1.35;
            color: #FFFFFF;
        }

        [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.045), rgba(255, 255, 255, 0.022));
            border: 1px solid rgba(220, 235, 249, 0.15);
            border-radius: 14px;
            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.06),
                0 8px 22px rgba(5, 14, 27, 0.12);
            margin-bottom: 0.8rem;
        }

        [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] > div {
            background: transparent;
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 1.1rem;
        }

        [data-testid="stMainBlockContainer"] {
            padding-left: 1.4rem;
            padding-right: 1.4rem;
        }

        h1, h2, h3, h4, h5, h6 {
            color: var(--avant-text) !important;
            font-family: var(--avant-font);
            letter-spacing: 0.05em;
        }

        h2, h3 {
            text-transform: uppercase;
            font-weight: 800 !important;
        }

        p, li, label, .stMarkdown, .stCaption {
            color: var(--avant-text-secondary);
            font-family: var(--avant-font);
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.35rem;
            padding: 0.1rem 0 0.75rem 0;
        }

        [data-testid="stSidebar"] .stTabs [data-baseweb="tab-list"] {
            gap: 0.45rem;
            padding: 0.15rem 0 0.8rem 0;
        }

        .stTabs [data-baseweb="tab"] {
            min-height: 40px;
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.82), rgba(237, 243, 251, 0.98));
            color: var(--avant-text-secondary);
            border: 1px solid var(--avant-border);
            border-radius: var(--avant-radius-chip);
            box-shadow: var(--avant-shadow-soft);
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(16, 201, 187, 0.18), rgba(23, 120, 230, 0.15));
            color: var(--avant-ink);
            border-color: rgba(23, 120, 230, 0.28);
        }

        [data-testid="stSidebar"] .stTabs [data-baseweb="tab"] {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.10), rgba(255, 255, 255, 0.05));
            color: #F2F8FE;
            border: 1px solid rgba(223, 238, 251, 0.18);
            border-radius: var(--avant-radius-chip);
            margin-right: 0.35rem;
            padding: 0.42rem 0.92rem;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.06);
            min-height: 38px;
        }

        [data-testid="stSidebar"] .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(16, 201, 187, 0.34), rgba(23, 120, 230, 0.38));
            color: #F7FCFF;
            border-color: rgba(232, 244, 255, 0.30);
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.12),
                0 12px 26px rgba(10, 28, 51, 0.24);
        }

        [data-testid="stSidebar"] .avant-sidebar-input-label {
            margin: 0 0 0.45rem 0;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.04em;
            color: #FFFFFF;
        }

        [data-testid="stSidebar"] .avant-sidebar-section-header {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin-bottom: 0.85rem;
        }

        [data-testid="stSidebar"] .avant-sidebar-section-bar {
            width: 4px;
            min-width: 4px;
            min-height: 30px;
            border-radius: 999px;
            background: linear-gradient(180deg, #19D0BC 0%, #10B8A3 100%);
            box-shadow: 0 0 18px rgba(25, 208, 188, 0.18);
        }

        [data-testid="stSidebar"] .avant-sidebar-section-title {
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #FFFFFF;
            margin-bottom: 2px;
        }

        [data-testid="stSidebar"] .avant-sidebar-section-subtitle {
            font-size: 11px;
            line-height: 1.35;
            color: #FFFFFF;
        }

        [data-testid="stSidebar"] .avant-sidebar-summary-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 0.9rem;
        }

        [data-testid="stSidebar"] .avant-sidebar-summary-card {
            padding: 10px 12px;
            border-radius: 14px;
            border: 1px solid rgba(223, 238, 251, 0.18);
            background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04));
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
        }

        [data-testid="stSidebar"] .avant-sidebar-summary-label {
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #FFFFFF;
            margin-bottom: 5px;
        }

        [data-testid="stSidebar"] .avant-sidebar-summary-value {
            font-size: 12px;
            font-weight: 700;
            line-height: 1.3;
            color: #F4FAFF;
        }

        .stButton > button,
        .stDownloadButton > button {
            background: linear-gradient(135deg, #FFFFFF 0%, #EAF2FB 100%);
            color: var(--avant-ink);
            border: 1px solid var(--avant-border-strong);
            border-radius: 14px;
            box-shadow: var(--avant-shadow-soft);
            font-weight: 700;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            border-color: rgba(23, 120, 230, 0.36);
            color: var(--avant-blue);
            background: linear-gradient(135deg, #FFFFFF 0%, #F3F8FE 100%);
        }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        .stDateInput > div,
        .stTextInput > div > div,
        .stNumberInput > div > div {
            background: linear-gradient(180deg, #FFFFFF 0%, #F6F9FD 100%) !important;
            color: var(--avant-text) !important;
            border: 1px solid var(--avant-border) !important;
            border-radius: var(--avant-radius-input) !important;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 8px 18px rgba(27, 46, 74, 0.05) !important;
        }

        [data-testid="stSidebar"] [data-baseweb="select"] > div,
        [data-testid="stSidebar"] [data-baseweb="input"] > div,
        [data-testid="stSidebar"] .stDateInput > div,
        [data-testid="stSidebar"] .stTextInput > div > div,
        [data-testid="stSidebar"] .stNumberInput > div > div {
            background: linear-gradient(180deg, rgba(19, 39, 63, 0.92), rgba(13, 29, 47, 0.92)) !important;
            color: #F2F8FE !important;
            border: 1px solid rgba(228, 241, 252, 0.22) !important;
            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.08),
                0 6px 14px rgba(5, 14, 27, 0.16) !important;
        }

        [data-testid="stSidebar"] .stDateInput input,
        [data-testid="stSidebar"] .stTextInput input,
        [data-testid="stSidebar"] .stNumberInput input,
        [data-testid="stSidebar"] [data-baseweb="select"] input {
            color: #F5FAFF !important;
        }

        [data-testid="stSidebar"] [data-testid="stFileUploader"] {
            color: #FFFFFF !important;
        }

        [data-testid="stSidebar"] [data-testid="stFileUploader"] section {
            background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04)) !important;
            border: 1px solid rgba(228, 241, 252, 0.18) !important;
            border-radius: 14px !important;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.06),
                0 8px 18px rgba(5, 14, 27, 0.12) !important;
        }

        [data-testid="stSidebar"] [data-testid="stFileUploader"] small,
        [data-testid="stSidebar"] [data-testid="stFileUploader"] span,
        [data-testid="stSidebar"] [data-testid="stFileUploader"] p,
        [data-testid="stSidebar"] [data-testid="stFileUploader"] label {
            color: #FFFFFF !important;
        }

        [data-testid="stSidebar"] [data-testid="stFileUploader"] button {
            color: #FFFFFF !important;
            background: linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0.07)) !important;
            border: 1px solid rgba(228, 241, 252, 0.24) !important;
            border-radius: 12px !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.08) !important;
        }

        [data-testid="stSidebar"] [data-testid="stFileUploader"] button:hover {
            color: #FFFFFF !important;
            border-color: rgba(255,255,255,0.34) !important;
            background: linear-gradient(180deg, rgba(255,255,255,0.18), rgba(255,255,255,0.09)) !important;
        }

        [data-testid="stSidebar"] .stButton > button {
            min-height: 44px;
            border-radius: 14px;
            border-width: 1px;
        }

        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #10C9BB 0%, #10B8A3 100%);
            color: #FFFFFF;
            border: 1px solid rgba(239, 249, 255, 0.24);
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.14),
                0 14px 28px rgba(7, 168, 156, 0.22);
        }

        [data-testid="stSidebar"] .stButton > button[kind="secondary"] {
            background: linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05));
            color: #EDF5FB;
            border: 1px solid rgba(226, 240, 251, 0.18);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
        }

        [data-testid="stSidebar"] .stButton > button[kind="secondary"]:hover {
            color: #FFFFFF;
            border-color: rgba(240, 248, 255, 0.26);
            background: linear-gradient(180deg, rgba(255,255,255,0.13), rgba(255,255,255,0.07));
        }

        [data-testid="stSidebar"] .stDownloadButton > button {
            min-height: 44px;
            border-radius: 14px;
            color: #FFFFFF !important;
            background: linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05)) !important;
            border: 1px solid rgba(226, 240, 251, 0.18) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05) !important;
        }

        [data-testid="stSidebar"] .stDownloadButton > button:hover {
            color: #FFFFFF !important;
            border-color: rgba(240, 248, 255, 0.26) !important;
            background: linear-gradient(180deg, rgba(255,255,255,0.13), rgba(255,255,255,0.07)) !important;
        }

        [data-testid="stSidebar"] .stButton > button:disabled,
        [data-testid="stSidebar"] .stDownloadButton > button:disabled {
            opacity: 1 !important;
            color: rgba(255,255,255,0.72) !important;
            -webkit-text-fill-color: rgba(255,255,255,0.72) !important;
            background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04)) !important;
            border: 1px solid rgba(226, 240, 251, 0.14) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.04) !important;
            cursor: not-allowed !important;
        }

        .stMultiSelect label,
        .stDateInput label,
        .stTextInput label,
        .stNumberInput label,
        .stSlider label,
        .stRadio label,
        .stSubheader {
            color: var(--avant-text) !important;
        }

        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] .stRadio label,
        [data-testid="stSidebar"] .stSlider label {
            color: #FFFFFF !important;
        }

        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] li,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] small,
        [data-testid="stSidebar"] .stText,
        [data-testid="stSidebar"] .st-emotion-cache-ue6h4q,
        [data-testid="stSidebar"] .st-emotion-cache-1pbsqtx {
            color: #FFFFFF !important;
        }

        [data-baseweb="tag"] {
            background: rgba(255, 255, 255, 0.10) !important;
            color: #F3F9FF !important;
            border: 1px solid rgba(223, 238, 251, 0.18) !important;
        }

        div[data-testid="stMetric"] {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.94), rgba(241, 246, 252, 0.98));
            border: 1px solid var(--avant-border);
            border-radius: var(--avant-radius-card);
            padding: 12px 16px;
            box-shadow: var(--avant-shadow-card);
        }

        div[data-testid="stMetric"] label {
            color: var(--avant-text-secondary) !important;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            font-weight: 700;
            font-size: 0.75rem;
        }

        div[data-testid="stMetricValue"] {
            color: var(--avant-text) !important;
            font-weight: 800;
        }

        [data-testid="stInfo"],
        [data-testid="stSuccess"],
        [data-testid="stWarning"],
        [data-testid="stError"] {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.95), rgba(245, 248, 253, 0.98));
            color: var(--avant-text);
            border: 1px solid var(--avant-border);
            border-radius: var(--avant-radius-card);
            box-shadow: var(--avant-shadow-soft);
        }

        [data-testid="stSidebar"] [data-testid="stInfo"],
        [data-testid="stSidebar"] [data-testid="stSuccess"],
        [data-testid="stSidebar"] [data-testid="stWarning"],
        [data-testid="stSidebar"] [data-testid="stError"] {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.09), rgba(255, 255, 255, 0.05));
            color: #F1F8FE;
            border: 1px solid rgba(223, 238, 251, 0.16);
        }

        [data-testid="stDataFrame"],
        .stTable {
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid var(--avant-border);
            border-radius: var(--avant-radius-card);
            box-shadow: var(--avant-shadow-soft);
            overflow: hidden;
        }

        [data-testid="stDataFrame"] [role="columnheader"] {
            background: #E8F0FA !important;
            color: var(--avant-text) !important;
        }

        [data-testid="stDataFrame"] [role="gridcell"] {
            color: var(--avant-text-secondary) !important;
        }

        .stSlider [data-baseweb="slider"] [role="slider"] {
            background: var(--avant-accent) !important;
            border-color: var(--avant-accent) !important;
        }

        [data-testid="stSidebar"] .stSlider [data-baseweb="slider"] > div > div {
            background: rgba(226, 240, 251, 0.18) !important;
        }

        [data-testid="stSidebar"] .stSlider [data-baseweb="slider"] [role="slider"] {
            background: #10C9BB !important;
            box-shadow: 0 0 0 4px rgba(16, 201, 187, 0.14) !important;
        }

        *:focus-visible {
            outline: 2px solid rgba(23, 120, 230, 0.28) !important;
            outline-offset: 2px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
