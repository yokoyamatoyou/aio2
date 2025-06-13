# -*- coding: utf-8 -*-
"""Chart helper functions for Streamlit UI."""
from typing import Dict
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

from .constants import COLOR_PALETTE


def create_score_gauge(score: float, title: str, color: str) -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
        }
    ))
    fig.update_layout(height=250)
    return fig


def create_aio_score_chart_vertical(data: Dict[str, Dict[str, float]], labels_map: Dict[str, str], title: str) -> go.Figure:
    labels = [labels_map.get(k, k.title()) for k in labels_map.keys()]
    values = [data.get(k, {"score": 0}).get("score", 0) for k in labels_map.keys()]

    fig = make_subplots()
    fig.add_trace(go.Bar(x=values, y=labels, orientation='h', marker_color=COLOR_PALETTE['accent']))
    fig.update_layout(title=title, xaxis_title="スコア", yaxis_title="項目", height=400)
    fig.update_yaxes(autorange="reversed")
    return fig
