# -*- coding: utf-8 -*-
from __future__ import annotations

import streamlit as st

from tabs.sidebar.entrada_coordenada_tab import render_coordenada_tab
from tabs.sidebar.entrada_empresa_tab import render_empresa_tab
from tabs.sidebar.entrada_fields import (
    render_dates,
    render_parameters,
    render_satellites,
)
from tabs.sidebar.entrada_kml_tab import render_kml_tab
from tabs.sidebar.entrada_nav import render_mode_tabs
from tabs.sidebar.entrada_state import (
    MODO_COORDENADA,
    MODO_EMPRESA_FAZENDA,
    MODO_KML,
    ensure_capture_coordinate_initialized,
)


def _render_section_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="avant-sidebar-section-header">
            <div class="avant-sidebar-section-bar"></div>
            <div>
                <div class="avant-sidebar-section-title">{title}</div>
                <div class="avant-sidebar-section-subtitle">{subtitle}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_entrada(gdf_full):
    ensure_capture_coordinate_initialized()

    modo_entrada = render_mode_tabs()
    selected_empresa = None
    selected_fazenda = None
    parsed_coordinates = None
    uploaded_kml = None

    with st.container(border=True):
        _render_section_header("Filtro principal", "Defina a abrangencia dos dados")

        if modo_entrada == MODO_EMPRESA_FAZENDA:
            selected_empresa, selected_fazenda = render_empresa_tab(gdf_full)
        elif modo_entrada == MODO_COORDENADA:
            parsed_coordinates = render_coordenada_tab()
        elif modo_entrada == MODO_KML:
            uploaded_kml = render_kml_tab()

    with st.container(border=True):
        _render_section_header("Janela temporal", "Selecione satelites e periodo da consulta")
        selected_satellites = render_satellites()
        start_date, end_date = render_dates(selected_satellites)

    with st.container(border=True):
        _render_section_header("Parametros", "Ajuste o raio da ROI e a cobertura de nuvem")
        buffer_m, cloud_pct = render_parameters()

    with st.container(border=True):
        st.markdown(
            f"""
            <div class="avant-sidebar-summary-row">
                <div class="avant-sidebar-summary-card">
                    <div class="avant-sidebar-summary-label">Modo</div>
                    <div class="avant-sidebar-summary-value">{modo_entrada}</div>
                </div>
                <div class="avant-sidebar-summary-card">
                    <div class="avant-sidebar-summary-label">Janela</div>
                    <div class="avant-sidebar-summary-value">{start_date:%d/%m/%Y} - {end_date:%d/%m/%Y}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        apply = st.button(
            "Aplicar filtros",
            use_container_width=True,
            key="sb_apply_query",
            type="primary",
        )

    return {
        "modo_entrada": modo_entrada,
        "selected_empresa": selected_empresa,
        "selected_fazenda": selected_fazenda,
        "selected_satellites": selected_satellites,
        "start_date": start_date,
        "end_date": end_date,
        "buffer_m": buffer_m,
        "cloud_pct": cloud_pct,
        "apply": apply,
        "parsed_coordinates": parsed_coordinates,
        "uploaded_kml": uploaded_kml,
    }
