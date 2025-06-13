"""Common UI components adhering to the design guideline."""

from typing import Any, Optional
import streamlit as st

from .constants import COLOR_PALETTE, FONT_STACK


def load_global_styles() -> None:
    """Inject global CSS styles for the application."""
    st.markdown(
        f"""
        <style>
        body {{
            background-color: {COLOR_PALETTE['background']};
            color: {COLOR_PALETTE['text_primary']};
            font-family: {FONT_STACK};
            font-size: 16px;
            font-weight: 300;
        }}
        .primary-button > button {{
            background-color: {COLOR_PALETTE['primary']};
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.4rem 1rem;
            font-weight: 400;
        }}
        .primary-button > button:hover {{
            background-color: {COLOR_PALETTE['primary']};
        }}
        .input-block {{
            background-color: #f0f2f6;
            padding: 1rem;
            border: none;
            border-radius: 6px;
            margin-bottom: 1rem;
        }}
        .explanation {{
            font-size: 14px;
            color: {COLOR_PALETTE['text_secondary']};
            margin-bottom: 0.5rem;
        }}
        .function-section {{
            background-color: {COLOR_PALETTE['surface']};
            padding: 1rem;
            border: 1px solid {COLOR_PALETTE['secondary']};
            border-radius: 8px;
            margin-bottom: 1rem;
        }}
        .explanation-section {{
            background-color: {COLOR_PALETTE['background']};
            padding: 1rem;
            border-left: 4px solid {COLOR_PALETTE['primary']};
            border-radius: 4px;
            font-size: 12px;
            color: {COLOR_PALETTE['text_secondary']};
        }}
        .stMetric {{
            overflow-wrap: anywhere;
        }}
        .stTabs [data-baseweb='tab'] {{
            min-width: 130px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def primary_button(label: str, key: Optional[str] = None) -> bool:
    """Create a styled primary button."""
    return st.button(label, key=key, use_container_width=True, help=label, type="primary",)


def text_input(label: str, key: Optional[str] = None, **kwargs: Any) -> str:
    """Text input wrapped in a styled block."""
    with st.container():
        st.markdown("<div class='input-block'>", unsafe_allow_html=True)
        value = st.text_input(label, key=key, **kwargs)
        st.markdown("</div>", unsafe_allow_html=True)
        return value

