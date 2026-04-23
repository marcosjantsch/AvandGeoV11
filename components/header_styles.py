# -*- coding: utf-8 -*-
from __future__ import annotations


def build_header_styles() -> str:
    return f"""
    <style>
    section.main > div.block-container {{
        padding-top: 0.45rem;
    }}

    .ag-header-wrap {{
        margin: -2px 0 14px 0;
        padding: 0;
    }}

    .ag-header-card {{
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(210, 222, 236, 0.95);
        border-radius: 24px;
        padding: 16px 18px;
        background:
            radial-gradient(circle at top right, rgba(16, 201, 187, 0.12), transparent 24%),
            radial-gradient(circle at left center, rgba(23, 120, 230, 0.08), transparent 22%),
            linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(243, 247, 252, 0.98));
        box-shadow: 0 20px 42px rgba(27, 46, 74, 0.14);
    }}

    .ag-header-card::after {{
        content: "";
        position: absolute;
        inset: 0 auto 0 0;
        width: 5px;
        background: linear-gradient(180deg, #10C9BB 0%, #1778E6 100%);
        opacity: 0.95;
    }}

    .ag-header-logo-slot img {{
        display: block;
        border-radius: 18px;
    }}

    .ag-header-logo-fallback {{
        width: 60px;
        height: 60px;
        border-radius: 18px;
        background: linear-gradient(135deg, #10C9BB, #1778E6);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #F7FCFF;
        font-size: 18px;
        font-weight: 800;
        letter-spacing: 0.08em;
        box-shadow: 0 12px 30px rgba(23, 120, 230, 0.22);
    }}

    .ag-header-eyebrow {{
        margin: 0 0 6px 0;
        font-size: 11px;
        font-weight: 800;
        line-height: 1;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #19D0BC;
    }}

    .ag-header-title-row {{
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
        margin: 0;
    }}

    .ag-header-title {{
        margin: 0;
        font-size: 23px;
        font-weight: 800;
        line-height: 1.02;
        letter-spacing: 0.08em;
        color: #1F3146;
        text-transform: uppercase;
    }}

    .ag-header-version {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 28px;
        padding: 5px 10px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 800;
        line-height: 1;
        color: #F7FCFF;
        background: linear-gradient(135deg, #10C9BB, #1778E6);
        border: 1px solid rgba(23, 120, 230, 0.16);
        box-shadow: 0 10px 22px rgba(23, 120, 230, 0.18);
    }}

    .ag-header-subtitle {{
        margin: 8px 0 0 0;
        font-size: 13px;
        line-height: 1.45;
        color: #556A82;
        max-width: 760px;
    }}

    .ag-header-meta-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
    }}

    .ag-header-chip {{
        display: inline-flex;
        align-items: center;
        min-height: 28px;
        padding: 5px 10px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        line-height: 1;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: #556A82;
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.84), rgba(237, 243, 251, 0.96));
        border: 1px solid #D2DEEC;
    }}

    .ag-header-chip-strong {{
        color: #0F2940;
        background: linear-gradient(135deg, rgba(16, 201, 187, 0.16), rgba(23, 120, 230, 0.14));
        border: 1px solid rgba(23, 120, 230, 0.18);
    }}

    .ag-header-user-card {{
        height: 100%;
        border: 1px solid rgba(210, 222, 236, 0.95);
        border-radius: 18px;
        padding: 12px 14px;
        background: linear-gradient(180deg, rgba(248, 251, 255, 0.94), rgba(237, 243, 251, 0.98));
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.7);
        display: flex;
        align-items: center;
    }}

    .ag-header-user-inline {{
        font-size: 12.5px;
        line-height: 1.35;
        color: #556A82;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }}

    .ag-header-user-inline strong {{
        color: #1F3146;
        font-weight: 800;
    }}

    .ag-header-separator {{
        color: #8AA1BA;
        margin: 0 4px;
    }}

    .ag-header-action-slot {{
        display: flex;
        align-items: stretch;
        justify-content: flex-end;
        height: 100%;
    }}

    .ag-header-action-slot div[data-testid="stButton"] {{
        width: 100%;
    }}

    .ag-header-action-slot div[data-testid="stButton"] > button[kind="secondary"] {{
        width: 100%;
        min-height: 48px;
        border-radius: 14px;
        font-weight: 800;
        letter-spacing: 0.04em;
        background: linear-gradient(135deg, #10C9BB, #1778E6);
        color: #F7FCFF;
        border: 1px solid rgba(23, 120, 230, 0.18);
        box-shadow: 0 14px 28px rgba(23, 120, 230, 0.18);
    }}

    .ag-header-action-slot div[data-testid="stButton"] > button[kind="secondary"]:hover {{
        filter: saturate(1.08) brightness(1.02);
    }}

    @media (max-width: 1100px) {{
        .ag-header-title {{
            font-size: 20px;
        }}

        .ag-header-subtitle {{
            font-size: 12.5px;
        }}

        .ag-header-user-inline {{
            white-space: normal;
        }}
    }}

    @media (max-width: 900px) {{
        .ag-header-card {{
            padding: 14px;
        }}

        .ag-header-title {{
            font-size: 18px;
        }}

        .ag-header-meta-row {{
            margin-top: 8px;
        }}
    }}
    </style>
    """
