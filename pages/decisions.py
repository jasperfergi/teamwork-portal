"""
Decisions page — interactive flow diagram of programme decisions.

Team mode:  TC's technical and management decisions rendered as a flowchart
            showing what led to what and alternatives considered.
Client mode: Gilead's approvals and sign-offs rendered as a status flow.
"""

import dash
from dash import html, Input, Output, callback

from components.shell import page_header

dash.register_page(__name__, path="/decisions", name="Decisions")


def layout():
    return html.Div([
        html.Div(id="decisions-page-header"),
        html.Div(id="decisions-flow"),
    ])


@callback(Output("decisions-page-header", "children"), Input("view-mode-store", "data"))
def render_header(mode):
    if mode == "client":
        return page_header(
            "Project Sycamore · Gilead Approvals",
            "Decisions",
            "Gilead approvals and sign-offs — formal QA, regulatory, and clinical approvals "
            "tracked across the programme. Drag to pan.",
        )
    return page_header(
        "Project Sycamore · Decisions",
        "Decisions",
        "Programme decision log — every technical and commercial decision recorded with "
        "rationale and alternatives. Drag to pan.",
    )


@callback(Output("decisions-flow", "children"), Input("view-mode-store", "data"))
def render_flow(mode):
    if mode == "client":
        src = "/assets/decision_flow_gilead.html"
    else:
        src = "/assets/decision_flow_tc.html"

    return html.Iframe(
        src=src,
        style={
            "width": "100%",
            "height": "calc(100vh - 200px)",
            "border": "none",
            "borderRadius": "8px",
            "display": "block",
        },
    )
