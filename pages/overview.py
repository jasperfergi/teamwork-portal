"""
Overview page (route "/") — programme status at a glance.
Stat blocks, milestone timeline (iframe), who's-waiting-on-whom, recent files.
"""

import dash
from dash import html, Input, Output, callback

from components.shell import page_header, card, stat_block, status_badge, ai_overview_panel
from data.synthetic_data import PROJECT, TASKS, MILESTONES, BUDGET, AI_OVERVIEW, FILES, ACTIONS

dash.register_page(__name__, path="/", name="Overview")


def _clickable_card(href, title, content):
    """Wrap a card in a link so the whole card is clickable."""
    return html.A(
        href=href,
        className="card-clickable-link",
        children=[card(title, content)],
    )


def layout():
    budget_spent = BUDGET["fees_spent"] + BUDGET["me_spent"]
    budget_remaining = BUDGET["total"] - budget_spent

    upcoming = [m for m in MILESTONES if m["date"] >= PROJECT["today"]]
    next_milestone = min(upcoming, key=lambda m: m["date"]) if upcoming else MILESTONES[-1]
    days_to_next = (next_milestone["date"] - PROJECT["today"]).days

    waiting_count = len([t for t in TASKS if t.get("waiting_on")])
    open_actions  = len([a for a in ACTIONS if a["status"] in ("Open", "In Progress")])
    active_files  = len([f for f in FILES if f["status"] != "Superseded"])

    return html.Div([
        page_header(
            "Project Sycamore · Gilead",
            "Overview",
            "The shared programme dashboard for Team Consulting and Gilead — "
            "where the project stands today.",
        ),

        # AI overview panel + interactive device viewer side by side
        html.Div(
            className="overview-ai-row",
            children=[
                html.Div(id="overview-ai-panel"),
                html.Div(
                    className="overview-device-panel",
                    children=[
                        html.A(
                            href="/engineering",
                            style={"display": "block", "width": "100%"},
                            children=html.Img(
                                src="/assets/img/autoinjector_device.svg",
                                className="overview-device-img",
                                alt="Sycamore autoinjector device",
                            ),
                        ),
                        html.A(
                            "View Sycamore Device →",
                            href="/engineering",
                            className="overview-device-link",
                        ),
                    ],
                ),
            ],
        ),

        # Stat boxes — 6 cards in a 3-column grid
        html.Div(
            className="card-grid grid-3",
            style={"marginBottom": "20px"},
            children=[
                card("Programme phase", stat_block(
                    "Current phase", PROJECT["phase"],
                    f"Started {PROJECT['start_date'].strftime('%d %b %Y')}",
                )),
                card("Next milestone", stat_block(
                    next_milestone["name"], f"{days_to_next}d",
                    next_milestone["date"].strftime("%d %b %Y"),
                )),
                _clickable_card("/finance", "Budget spent", stat_block(
                    "Of £3.0m total", f"£{budget_spent / 1_000_000:.2f}m",
                    f"£{budget_remaining / 1_000_000:.2f}m remaining",
                )),
                _clickable_card("/decisions", "Awaiting decisions", stat_block(
                    "Open items", str(waiting_count),
                    "Tap to view open decisions",
                )),
                _clickable_card("/project-management", "Open actions", stat_block(
                    "Action log", str(open_actions),
                    "Tap to view action log",
                )),
                _clickable_card("/files", "Active files", stat_block(
                    "Documents", str(active_files),
                    "Tap to browse all files",
                )),
            ],
        ),

        html.Div(
            className="card-grid grid-2",
            children=[
                card("Milestones", html.Div(id="overview-milestone-iframe")),
                card("Who we're waiting on", html.Div(id="overview-waiting-on")),
            ],
        ),

        html.Div(style={"marginTop": "20px"}, children=[
            card(
                "Recently active files",
                html.Div(id="overview-files"),
                title_right=html.A(
                    "View all →",
                    href="/files",
                    style={"fontSize": "12px", "color": "var(--accent)",
                           "fontWeight": "600", "textDecoration": "none"},
                ),
            ),
        ]),
    ])


@callback(Output("overview-milestone-iframe", "children"), Input("view-mode-store", "data"))
def update_milestone_iframe(mode):
    src = "/assets/milestone_viewer.html?mode=client" if mode == "client" else "/assets/milestone_viewer.html?mode=team"
    return html.Iframe(
        src=src,
        style={"width": "100%", "height": "420px", "border": "none", "display": "block"},
    )


@callback(Output("overview-ai-panel", "children"), Input("view-mode-store", "data"))
def update_ai_panel(mode):
    if mode == "client":
        ov = AI_OVERVIEW["client"]
        return ai_overview_panel(
            ov["summary"], ov["detail"],
            mode_label="Gilead view",
            panel_id="overview-ai",
        )
    ov = AI_OVERVIEW["internal"]
    return ai_overview_panel(
        ov["summary"], ov["detail"],
        mode_label="Team Consulting view",
        panel_id="overview-ai",
    )


@callback(Output("overview-waiting-on", "children"), Input("view-mode-store", "data"))
def update_waiting_on(mode):
    waiting_tasks = [t for t in TASKS if t.get("waiting_on")]
    if not waiting_tasks:
        return html.Div(
            "Nothing currently blocked — all work packages progressing.",
            className="empty-state",
        )

    rows = []
    for t in waiting_tasks:
        who = "Gilead" if t["waiting_on"] == "client" else "Team Consulting"
        badge_cls = "badge badge-amber" if t["waiting_on"] == "client" else "badge badge-accent"
        rows.append(
            html.Div(
                className="waiting-row",
                children=[
                    html.Div([
                        html.Div(t["name"], className="waiting-task-name"),
                        html.Div(t["waiting_note"], className="muted small",
                                 style={"marginTop": "3px"}),
                    ]),
                    html.Span(f"Waiting on {who}", className=badge_cls),
                ],
            )
        )
    return html.Div(rows)


@callback(Output("overview-files", "children"), Input("view-mode-store", "data"))
def update_recent_files(mode):
    recent = sorted(FILES, key=lambda f: f["last_edited"], reverse=True)[:5]
    rows = []
    for f in recent:
        rows.append(html.Tr([
            html.Td(html.A(f["name"], href=f["url"], target="_blank", className="file-link")),
            html.Td(f["sector"], className="muted"),
            html.Td(f["last_edited_by"]),
            html.Td(f["last_edited"].strftime("%d %b %Y")),
            html.Td(status_badge(f["status"])),
        ]))
    return html.Table(
        className="simple-table",
        children=[
            html.Thead(html.Tr([
                html.Th("File"), html.Th("Sector"), html.Th("Last edited by"),
                html.Th("Date"), html.Th("Status"),
            ])),
            html.Tbody(rows),
        ],
    )
