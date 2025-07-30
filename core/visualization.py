# -*- coding: utf-8 -*-
"""Chart helper functions for Streamlit UI."""
from typing import Dict

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import plotly.express as px
except Exception:  # pragma: no cover - fallback when plotly is missing
    go = None
    make_subplots = None


class SimpleFigure:
    """Minimal stand-in for plotly.graph_objects.Figure."""

    def __init__(self):
        self.data = []
        self.layout = {}

    def add_trace(self, trace):
        self.data.append(trace)

    def update_layout(self, **kwargs):
        self.layout.update(kwargs)

    def update_yaxes(self, **kwargs):
        self.layout.setdefault("yaxis", {}).update(kwargs)


class SimpleBar(dict):
    """Minimal bar trace representation."""

    def __init__(self, x=None, y=None, orientation=None, marker_color=None):
        super().__init__(x=x, y=y, orientation=orientation, marker_color=marker_color)

from .constants import COLOR_PALETTE


def create_score_gauge(score: float, title: str, color: str):
    if go is None:
        return SimpleFigure()

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


def create_aio_score_chart_vertical(
    data: Dict[str, Dict[str, float]], labels_map: Dict[str, str], title: str
):
    labels = [labels_map.get(k, k.title()) for k in labels_map.keys()]
    values = [data.get(k, {"score": 0}).get("score", 0) for k in labels_map.keys()]

    if go is None or make_subplots is None:
        fig = SimpleFigure()
        fig.add_trace(SimpleBar(x=values, y=labels, orientation="h", marker_color=COLOR_PALETTE["accent"]))
        fig.update_layout(title=title, xaxis_title="スコア", yaxis_title="項目", height=400)
        fig.update_yaxes(autorange="reversed")
        return fig

    fig = make_subplots()
    fig.add_trace(
        go.Bar(x=values, y=labels, orientation="h", marker_color=COLOR_PALETTE["accent"])
    )
    fig.update_layout(title=title, xaxis_title="スコア", yaxis_title="項目", height=400)
    fig.update_yaxes(autorange="reversed")
    return fig


def create_aio_radar_chart(data: Dict[str, float], labels_map: Dict[str, str]):
    """Return radar chart with 6 axes including 業種適合性."""
    labels = [labels_map.get(k, k) for k in labels_map.keys()]
    values = [data.get(k, 0) for k in labels_map.keys()]

    if go is None:
        fig = SimpleFigure()
        fig.add_trace({"type": "scatterpolar", "r": values, "theta": labels, "fill": "toself"})
        fig.update_layout(polar={"radialaxis": {"range": [0, 100]}}, showlegend=False)
        return fig

    plot_fig = go.Figure()
    plot_fig.add_trace(
        go.Scatterpolar(r=values, theta=labels, fill="toself", marker_color=COLOR_PALETTE["accent"])
    )
    plot_fig.update_layout(polar=dict(radialaxis=dict(range=[0, 100])), showlegend=False)

    simple = SimpleFigure()
    simple.data = [trace.to_plotly_json() for trace in plot_fig.data]
    simple.layout = plot_fig.layout.to_plotly_json()
    return simple
