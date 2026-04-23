# -*- coding: utf-8 -*-
from __future__ import annotations

import streamlit as st

from components.header_helpers import render_logo_or_fallback, sanitize_header_inputs
from components.header_styles import build_header_styles


def render_header(
    logo_path: str,
    app_name: str,
    version: str,
    user: str,
    role: str,
    current_mode: str = "",
    username=None,
    authenticator=None,
    subtitle: str = "",
):
    values = sanitize_header_inputs(app_name, version, user, role, current_mode, subtitle, username)
    title_block = (
        '<div class="ag-header-left">'
        "<div>"
        '<div class="ag-header-eyebrow">Executive Climate Intelligence</div>'
        '<div class="ag-header-title-row">'
        f'<div class="ag-header-title">{values["app_name"]}</div>'
        f'<div class="ag-header-version">{values["version"]}</div>'
        "</div>"
        + (
            f'<div class="ag-header-subtitle">{values["subtitle"]}</div>'
            if values["subtitle"] and values["subtitle"] != "-"
            else ""
        )
        +
        "</div>"
        "</div>"
    )
    user_block = (
        '<div class="ag-header-user-card">'
        '<div class="ag-header-user-inline">'
        '<strong>Sessao atual</strong>'
        f' <span class="ag-header-separator">|</span> <strong>Usuario:</strong> {values["user"]}'
        f' <span class="ag-header-separator">|</span> <strong>Perfil:</strong> {values["role"]}'
        f' <span class="ag-header-separator">|</span> <strong>Login:</strong> {values["username"]}'
        "</div>"
        "</div>"
    )

    with st.container():
        st.markdown(
            build_header_styles(),
            unsafe_allow_html=True,
        )

        st.markdown('<div class="ag-header-wrap">', unsafe_allow_html=True)
        st.markdown('<div class="ag-header-card">', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.09, 0.55, 0.36], vertical_alignment="center")

        with col1:
            st.markdown('<div class="ag-header-logo-slot">', unsafe_allow_html=True)
            render_logo_or_fallback(logo_path)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown(title_block, unsafe_allow_html=True)

        with col3:
            inner1, inner2 = st.columns([0.74, 0.26], vertical_alignment="center")

            with inner1:
                st.markdown(user_block, unsafe_allow_html=True)

            with inner2:
                st.markdown('<div class="ag-header-action-slot">', unsafe_allow_html=True)
                if authenticator is not None:
                    try:
                        authenticator.logout("Logout", "main")
                    except Exception:
                        pass
                st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
