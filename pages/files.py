"""
Files page — full document browser across all sectors.
Includes recently opened section, sector filter, and comment threads per file.
"""

import dash
from dash import html, dcc, Input, Output, callback

from components.shell import page_header, card, status_badge, comment_thread
from data.synthetic_data import FILES, COMMENTS, PRESENTATIONS, ISSUES

dash.register_page(__name__, path="/files", name="Files")

ALL_SECTORS = sorted({f["sector"] for f in FILES})


def layout():
    recent = sorted(FILES, key=lambda f: f["last_edited"], reverse=True)[:4]

    return html.Div([
        page_header(
            "Project Sycamore · Files",
            "Files",
            "All project documents — filter by sector, view status, and leave comments.",
        ),

        # Recently opened
        html.Div(style={"marginBottom": "20px"}, children=[
            card("Recently opened", html.Div([
                html.Div(className="recent-files-grid", children=[
                    _recent_file_card(f) for f in recent
                ]),
            ])),
        ]),

        # Sector filter
        html.Div(
            className="filter-bar",
            children=[
                html.Span("Filter:", className="filter-label"),
                dcc.RadioItems(
                    id="files-sector-filter",
                    options=[{"label": "All", "value": "all"}] +
                            [{"label": s, "value": s} for s in ALL_SECTORS],
                    value="all",
                    inline=True,
                    className="filter-radio",
                    inputStyle={"marginRight": "4px"},
                    labelStyle={"marginRight": "16px"},
                ),
            ],
        ),

        html.Div(id="files-table-container", style={"marginTop": "16px"}),

        # Issue tracker
        html.Div(style={"marginTop": "20px"}, children=[
            card("Issue tracker", _issue_tracker_table()),
        ]),

        # Presentations
        html.Div(style={"marginTop": "20px"}, children=[
            card("Presentations & transcripts", _presentations_table()),
        ]),
    ])


def _recent_file_card(f):
    return html.A(
        href=f["url"],
        target="_blank",
        className="recent-file-card",
        children=[
            html.Div(className="recent-file-info", children=[
                html.Div(f["name"], className="recent-file-name"),
                html.Div(
                    f"{f['last_edited_by']} · {f['last_edited'].strftime('%d %b')}",
                    className="recent-file-meta",
                ),
                status_badge(f["status"]),
            ]),
        ],
    )


def _issue_tracker_table():
    priority_cls = {"High": "action-badge action-pri-high", "Medium": "action-badge action-pri-med", "Low": "action-badge action-pri-low"}
    status_cls   = {"Open": "action-badge action-status-open", "In Progress": "action-badge action-status-prog", "Resolved": "action-badge po-status-closed"}
    rows = [
        html.Tr([
            html.Td(html.Span(iss["id"], className="risk-id")),
            html.Td(iss["title"], className="risk-title"),
            html.Td(html.Span(iss["type"], className="risk-category-chip")),
            html.Td(html.Span(iss["priority"], className=priority_cls.get(iss["priority"], "action-badge"))),
            html.Td(iss["assigned_to"]),
            html.Td(iss["raised_date"].strftime("%d %b %Y")),
            html.Td(html.Span(iss["status"], className=status_cls.get(iss["status"], "action-badge"))),
            html.Td(iss["description"], className="risk-comment"),
        ])
        for iss in sorted(ISSUES, key=lambda x: x["raised_date"], reverse=True)
    ]
    return html.Table(className="simple-table risk-table", children=[
        html.Thead(html.Tr([
            html.Th("ID"), html.Th("Issue"), html.Th("Type"),
            html.Th("Priority"), html.Th("Assigned to"),
            html.Th("Raised"), html.Th("Status"), html.Th("Description"),
        ])),
        html.Tbody(rows),
    ])


def _presentations_table():
    rows = [
        html.Tr([
            html.Td(html.A(p["name"], href=p["url"], target="_blank", className="file-link")),
            html.Td(p["date"].strftime("%d %b %Y")),
            html.Td(html.A("View transcript →", href=p["transcript_url"], target="_blank")),
        ])
        for p in sorted(PRESENTATIONS, key=lambda x: x["date"], reverse=True)
    ]
    return html.Table(
        className="simple-table",
        children=[
            html.Thead(html.Tr([
                html.Th("Presentation"), html.Th("Date"), html.Th(""),
            ])),
            html.Tbody(rows),
        ],
    )


@callback(
    Output("files-table-container", "children"),
    Input("files-sector-filter", "value"),
    Input("view-mode-store", "data"),
)
def update_files_table(sector, mode):
    filtered = FILES if sector == "all" else [f for f in FILES if f["sector"] == sector]
    filtered = sorted(filtered, key=lambda f: f["last_edited"], reverse=True)

    rows = []
    for f in filtered:
        file_comments = [c for c in COMMENTS if c["target_type"] == "file"
                         and c["target_id"] == f["id"]]
        if mode == "client":
            file_comments = [c for c in file_comments if c["team"] == "client"]

        comment_count = len(file_comments)
        comment_badge = html.Span(
            f"💬 {comment_count}", className="comment-count-badge"
        ) if comment_count > 0 else None

        rows.append(
            html.Details(
                className="file-row-expandable",
                children=[
                    html.Summary(
                        className="file-row-summary",
                        children=[
                            html.Span(
                                html.A(f["name"], href=f["url"], target="_blank",
                                       className="file-link"),
                                className="file-row-name",
                            ),
                            html.Span(f["sector"], className="file-row-sector muted small"),
                            html.Span(f["last_edited_by"], className="file-row-editor"),
                            html.Span(f["last_edited"].strftime("%d %b %Y"),
                                      className="file-row-date muted"),
                            status_badge(f["status"]),
                            comment_badge,
                        ],
                    ),
                    html.Div(
                        className="file-row-comments",
                        children=[comment_thread(file_comments, thread_id=f["id"])],
                    ) if file_comments else html.Div(
                        comment_thread([], thread_id=f["id"]),
                        className="file-row-comments",
                    ),
                ],
            )
        )

    return card(
        f"Documents ({len(filtered)})",
        html.Div(rows, className="files-list"),
    )
