# -*- coding: utf-8 -*-
from __future__ import annotations

import streamlit as st

from services.coordinate_service import (
    DEFAULT_CAPTURE_CITY_NAME,
    format_dd,
)
from tabs.sidebar.entrada import render_sidebar_entrada
from tabs.sidebar.exportar import render_sidebar_exportar
from tabs.sidebar.imagens import render_sidebar_imagens


def _render_mode_summary():
    modo_entrada = st.session_state.get("sb_modo_entrada") or st.session_state.get("modo_entrada") or "-"
    mode_styles = {
        "Empresa / Fazenda": {
            "bg": "linear-gradient(135deg, rgba(16, 201, 187, 0.22), rgba(23, 120, 230, 0.20))",
            "border": "rgba(25, 208, 188, 0.40)",
            "text": "#EAF8FF",
        },
        "Coordenada": {
            "bg": "linear-gradient(135deg, rgba(23, 120, 230, 0.24), rgba(16, 201, 187, 0.16))",
            "border": "rgba(23, 120, 230, 0.38)",
            "text": "#EAF8FF",
        },
        "Arquivo KML/KMZ": {
            "bg": "linear-gradient(135deg, rgba(240, 77, 99, 0.24), rgba(23, 120, 230, 0.14))",
            "border": "rgba(240, 77, 99, 0.34)",
            "text": "#FFF4F6",
        },
    }
    style = mode_styles.get(
        modo_entrada,
        {
            "bg": "linear-gradient(135deg, rgba(142, 168, 194, 0.18), rgba(127, 145, 166, 0.10))",
            "border": "rgba(142, 168, 194, 0.26)",
            "text": "#EDF5FB",
        },
    )

    st.markdown(
        f"""
        <div style="
            margin: 4px 0 8px 0;
            padding: 10px 12px;
            border-radius: 16px;
            border: 1px solid rgba(224,239,251,0.18);
            background: linear-gradient(180deg, rgba(255,255,255,0.09), rgba(255,255,255,0.04));
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
        ">
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <div style="
                    font-size:11px;
                    font-weight:700;
                    letter-spacing:0.08em;
                    color:#FFFFFF;
                    text-transform:uppercase;
                ">
                    Modo ativo
                </div>
                <div style="
                    padding: 5px 10px;
                    border-radius: 999px;
                    font-size: 11px;
                    font-weight: 700;
                    letter-spacing: 0.05em;
                    background: {style["bg"]};
                    border: 1px solid {style["border"]};
                    color: {style["text"]};
                    box-shadow: 0 8px 18px rgba(4, 15, 29, 0.18);
                ">
                    {modo_entrada}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_capture_summary():
    captured = st.session_state.get("captured_coordinate")

    st.markdown("### Coordenada atual")
    st.caption(
        "O ponto inicia em Jaguariaiva, Parana. Voce pode editar no campo de coordenada ou mover o marcador no mapa segurando CTRL."
    )

    if captured:
        source = captured.get("source")
        if source == "default_city_center":
            st.info(f"Ponto inicial carregado em {DEFAULT_CAPTURE_CITY_NAME}.")
        else:
            st.success("Ponto atualmente definido no mapa.")

        st.markdown(f"**DD:** {format_dd(captured.get('latitude'))}, {format_dd(captured.get('longitude'))}")
        st.markdown(
            f"**DMS:** {captured.get('latitude_dms', '-')} | {captured.get('longitude_dms', '-')}"
        )
    else:
        st.info("Nenhum ponto disponivel.")


def render_sidebar(gdf_full, available_images=None):
    if available_images is None:
        available_images = []

    with st.sidebar:
        st.markdown(
            """
            <div class="avant-sidebar-shell">
                <div class="avant-sidebar-shell-mark"></div>
                <div class="avant-sidebar-shell-inner">
                    <div class="avant-sidebar-shell-label">Painel de controle</div>
                    <div class="avant-sidebar-shell-title">Selecione a opcao</div>
                    <div class="avant-sidebar-shell-copy">Filtros espaciais e periodo de analise</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        _render_mode_summary()

        tab_entrada, tab_imagens, tab_exportar = st.tabs(["Entrada", "Imagens", "Exportar"])

        with tab_entrada:
            st.session_state.get("_sidebar_mode_nonce", 0)
            entrada_data = render_sidebar_entrada(gdf_full)
            if entrada_data.get("modo_entrada") == "Coordenada":
                st.markdown("---")
                _render_capture_summary()

        with tab_imagens:
            imagens_data = render_sidebar_imagens(available_images)

        with tab_exportar:
            export_data = render_sidebar_exportar(available_images)

    result = {}
    result.update(entrada_data)
    result.update(imagens_data)
    result.update(export_data)

    result.setdefault("tipo_dado", "Dados Empresa/Fazenda")
    result.setdefault("selected_uf", None)
    result.setdefault("selected_municipio", None)
    result.setdefault("log_container", None)

    return result
