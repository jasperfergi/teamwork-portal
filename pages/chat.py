"""
Chat page — internal messaging for Team Consulting (TC mode) and
Gilead Sciences (client mode).
"""

import dash
from dash import html, dcc, Input, Output, State, callback, no_update

from components.shell import page_header, card, internal_only_tag
from data.synthetic_data import INTERNAL_MESSAGES, GILEAD_INTERNAL_MESSAGES, PROJECT

dash.register_page(__name__, path="/chat", name="Chat")


def layout():
    return html.Div([
        page_header(
            "Project Sycamore · Chat",
            "Chat",
            "Internal team messaging — visible only within each organisation.",
        ),
        html.Div(id="chat-page-content"),
    ])


def _build_bubbles(messages):
    bubbles = []
    for m in messages:
        initials = "".join(p[0] for p in m["author"].split()[:2])
        date_str = m["date"].strftime("%d %b %Y") if hasattr(m["date"], "strftime") else m["date"]
        bubbles.append(
            html.Div(className="internal-msg", children=[
                html.Div(initials, className="internal-msg-avatar"),
                html.Div(className="internal-msg-body", children=[
                    html.Div(className="internal-msg-meta", children=[
                        html.Span(m["author"], className="internal-msg-author"),
                        html.Span(date_str, className="internal-msg-date"),
                    ]),
                    html.Div(m["text"], className="internal-msg-text"),
                ]),
            ])
        )
    return bubbles


@callback(Output("chat-page-content", "children"),
          Input("view-mode-store", "data"),
          Input("internal-msg-store", "data"),
          Input("gilead-msg-store", "data"))
def render_chat(mode, tc_extra, gilead_extra):
    if mode == "client":
        all_msgs = list(GILEAD_INTERNAL_MESSAGES) + (gilead_extra or [])
        bubbles = _build_bubbles(all_msgs)
        panel = html.Div([
            html.Div(className="internal-chat-header", children=[
                html.Span("Gilead internal messages", className="internal-chat-title"),
            ]),
            html.Div(bubbles, className="internal-chat-messages chat-page-messages",
                     id="chat-gilead-messages"),
            html.Div(className="internal-chat-input-row", children=[
                dcc.Input(id="chat-gilead-input", type="text",
                          placeholder="Message the Gilead team…",
                          className="internal-chat-input", debounce=False, n_submit=0),
                html.Button("Send", id="chat-gilead-send", n_clicks=0,
                            className="internal-chat-send-btn"),
            ]),
        ], className="internal-chat-panel")
        return card("Gilead internal messages", panel, title_right=internal_only_tag())

    all_msgs = list(INTERNAL_MESSAGES) + (tc_extra or [])
    bubbles = _build_bubbles(all_msgs)
    panel = html.Div([
        html.Div(className="internal-chat-header", children=[
            html.Span("Team Consulting internal chat", className="internal-chat-title"),
        ]),
        html.Div(bubbles, className="internal-chat-messages chat-page-messages",
                 id="chat-tc-messages"),
        html.Div(className="internal-chat-input-row", children=[
            dcc.Input(id="chat-tc-input", type="text",
                      placeholder="Message the team…",
                      className="internal-chat-input", debounce=False, n_submit=0),
            html.Button("Send", id="chat-tc-send", n_clicks=0,
                        className="internal-chat-send-btn"),
        ]),
    ], className="internal-chat-panel")
    return card("Team Consulting internal messages", panel, title_right=internal_only_tag())


@callback(
    Output("internal-msg-store", "data"),
    Output("chat-tc-input", "value"),
    Input("chat-tc-send", "n_clicks"),
    Input("chat-tc-input", "n_submit"),
    State("chat-tc-input", "value"),
    State("internal-msg-store", "data"),
    prevent_initial_call=True,
)
def send_tc_message(_send, _submit, text, current):
    if not text or not text.strip():
        return no_update, no_update
    current = current or []
    new_msg = {"id": f"M{len(current)+100}", "author": "You",
               "date": PROJECT["today"].strftime("%d %b %Y"), "text": text.strip()}
    return current + [new_msg], ""


@callback(
    Output("gilead-msg-store", "data"),
    Output("chat-gilead-input", "value"),
    Input("chat-gilead-send", "n_clicks"),
    Input("chat-gilead-input", "n_submit"),
    State("chat-gilead-input", "value"),
    State("gilead-msg-store", "data"),
    prevent_initial_call=True,
)
def send_gilead_message(_send, _submit, text, current):
    if not text or not text.strip():
        return no_update, no_update
    current = current or []
    new_msg = {"id": f"GM{len(current)+100}", "author": "You",
               "date": PROJECT["today"].strftime("%d %b %Y"), "text": text.strip()}
    return current + [new_msg], ""
