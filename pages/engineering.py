"""
Engineering page — DV test execution, interactive autoinjector viewer, and files.
"""

import dash
from dash import html, dcc, Input, Output, callback

from components.shell import page_header, card, status_badge, comment_thread
from components.charts import gantt_figure
from data.synthetic_data import TASKS, FILES, COMMENTS, PROJECT

dash.register_page(__name__, path="/engineering", name="Engineering")

ENGINEERING_TASKS = [t for t in TASKS if t["sector"] == "Engineering"]
ENGINEERING_FILES = [f for f in FILES if f["sector"] == "Engineering"]


def layout():
    return html.Div([
        page_header(
            "Project Sycamore · Engineering",
            "Engineering",
            "Design verification test execution, autoinjector component detail, and files.",
        ),

        card("DV test execution", dcc.Graph(
            id="eng-gantt",
            config={"displayModeBar": False},
        )),

        html.Div(style={"marginTop": "20px"}, children=[
            card("Work package detail", html.Div(id="eng-task-table")),
        ]),

        # Sycamore Device — interactive component viewer, full width
        html.Div(style={"marginTop": "20px"}, children=[
            card(
                "Sycamore Device",
                html.Iframe(
                    src="/assets/autoinjector_viewer.html",
                    style={
                        "width": "100%",
                        "height": "560px",
                        "border": "none",
                        "borderRadius": "6px",
                        "display": "block",
                    },
                ),
            ),
        ]),

        html.Div(className="card-grid grid-2", style={"marginTop": "20px"}, children=[
            card("Engineering files", html.Div(id="eng-files")),
            card("Comments", html.Div(id="eng-comments")),
        ]),
    ])


@callback(Output("eng-gantt", "figure"), Input("view-mode-store", "data"))
def update_gantt(mode):
    return gantt_figure(ENGINEERING_TASKS, today=PROJECT["today"], mode=mode)


@callback(Output("eng-task-table", "children"), Input("view-mode-store", "data"))
def update_task_table(_mode):
    rows = []
    for t in ENGINEERING_TASKS:
        waiting = "—"
        if t.get("waiting_on"):
            waiting = "Gilead" if t["waiting_on"] == "client" else "Team Consulting"
        rows.append(html.Tr([
            html.Td(t["id"], style={"fontWeight": "600", "fontFamily": "monospace",
                                     "fontSize": "12px"}),
            html.Td(t["name"]),
            html.Td(t["owner_name"]),
            html.Td(
                html.Div(className="progress-bar-wrap", children=[
                    html.Div(className="progress-bar-fill",
                             style={"width": f"{t['pct_complete']}%"}),
                    html.Span(f"{t['pct_complete']}%", className="progress-bar-label"),
                ])
            ),
            html.Td(waiting if waiting == "—" else html.Span(
                waiting, className="badge badge-amber" if t["waiting_on"] == "client"
                else "badge badge-accent",
            )),
            html.Td(status_badge(t["status"])),
        ]))
    return html.Table(
        className="simple-table",
        children=[
            html.Thead(html.Tr([
                html.Th("ID"), html.Th("Work package"), html.Th("Owner"),
                html.Th("Progress"), html.Th("Waiting on"), html.Th("Status"),
            ])),
            html.Tbody(rows),
        ],
    )


@callback(Output("eng-files", "children"), Input("view-mode-store", "data"))
def update_files(_mode):
    rows = [
        html.Tr([
            html.Td(html.A(f["name"], href=f["url"], target="_blank", className="file-link")),
            html.Td(f["last_edited_by"]),
            html.Td(f["last_edited"].strftime("%d %b %Y")),
            html.Td(status_badge(f["status"])),
        ])
        for f in ENGINEERING_FILES
    ]
    return html.Table(
        className="simple-table",
        children=[
            html.Thead(html.Tr([
                html.Th("File"), html.Th("Edited by"), html.Th("Date"), html.Th("Status"),
            ])),
            html.Tbody(rows),
        ],
    )


@callback(Output("eng-comments", "children"), Input("view-mode-store", "data"))
def update_comments(mode):
    eng_task_ids = {t["id"] for t in ENGINEERING_TASKS}
    eng_file_ids = {f["id"] for f in ENGINEERING_FILES}
    relevant = [
        c for c in COMMENTS
        if (c["target_type"] == "task" and c["target_id"] in eng_task_ids)
        or (c["target_type"] == "file" and c["target_id"] in eng_file_ids)
    ]
    if mode == "client":
        relevant = [c for c in relevant if c["team"] != "team" or not c.get("resolved")]

    if not relevant:
        return html.Div("No comments yet on engineering items.", className="empty-state")

    return comment_thread(relevant, thread_id="eng")
