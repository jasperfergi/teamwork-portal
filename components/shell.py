"""
Reusable layout fragments: top bar, side nav, AI overview panel, badges,
stat blocks, and card containers.

All layout functions return Dash component trees — no callbacks live here.
"""

from dash import html, dcc
from data.tokens import SECTORS


_TC_PROJECTS = ["Project Sycamore", "Project Cleopatra", "Project ISLA", "Project Newo"]
_GILEAD_PROJECTS = ["Project Sycamore", "Project Sequoia", "Project Myanmar", "Project Otis"]


def topbar(project_name, project_phase):
    return html.Div(
        className="topbar",
        children=[
            html.Div(
                className="topbar-left",
                children=[
                    html.A(
                        href="/",
                        className="topbar-brand",
                        children=[
                            html.Img(
                                src="/assets/img/teamwork_logo.svg",
                                className="topbar-brand-img",
                                style={"height": "22px", "width": "auto"},
                            ),
                        ],
                    ),
                    html.Div(className="topbar-divider"),
                    # Project switcher — options change per mode
                    html.Div(
                        className="topbar-project",
                        children=[
                            html.Div(
                                className="project-switcher",
                                children=[
                                    html.Select(
                                        id="project-switcher",
                                        children=[html.Option(p, value=p) for p in _TC_PROJECTS],
                                        className="topbar-project-name",
                                        style={"fontWeight": "600", "fontSize": "13.5px",
                                               "background": "transparent", "border": "none",
                                               "outline": "none", "cursor": "pointer",
                                               "fontFamily": "inherit", "color": "var(--ink)"},
                                    ),
                                ],
                            ),
                            html.Span(f"Teamwork Portal · {project_phase}", className="topbar-project-sub"),
                        ],
                    ),
                ],
            ),
            html.Div(
                className="topbar-right",
                children=[
                    html.Div(
                        id="transparency-panel-wrapper",
                        children=[
                            html.Button(
                                "⚙ Visibility",
                                id="transparency-toggle-btn",
                                n_clicks=0,
                                className="transparency-btn",
                            ),
                            html.Div(
                                id="transparency-panel",
                                className="transparency-panel",
                                style={"display": "none"},
                                children=[
                                    html.Div("What Gilead can see", className="transparency-panel-title"),
                                    html.Div(className="transparency-options", children=[
                                        _visibility_checkbox("vis-internal-messages", "Internal team messages", False),
                                        _visibility_checkbox("vis-budget-notes", "Internal budget notes", True),
                                        _visibility_checkbox("vis-risk-notes", "Risk register notes", True),
                                        _visibility_checkbox("vis-tech-detail", "Detailed technical notes", True),
                                    ]),
                                ],
                            ),
                        ],
                    ),
                    # Two-button pill toggle — both visible, active fills
                    html.Div(
                        id="mode-toggle",
                        className="mode-toggle",
                        children=[
                            html.Button(
                                id="mode-btn-team", n_clicks=0, className="active team",
                                children=[
                                    html.Img(src="/assets/img/team_toggle_logo.svg",
                                             className="mode-toggle-logo",
                                             style={"height": "16px", "width": "auto"}),
                                ],
                            ),
                            html.Button(
                                id="mode-btn-client", n_clicks=0, className="",
                                children=[
                                    html.Img(src="/assets/img/gilead_logo_white.svg",
                                             className="mode-toggle-logo",
                                             style={"height": "18px", "width": "auto"}),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )


def _visibility_checkbox(id_, label, default_checked):
    return html.Label(
        className="visibility-option",
        children=[
            dcc.Checklist(
                id=id_,
                options=[{"label": "", "value": "on"}],
                value=["on"] if default_checked else [],
                className="visibility-check",
            ),
            html.Span(label, className="visibility-label"),
        ],
    )


def sidenav(active_key="overview"):
    links = []
    for s in SECTORS:
        cls = "sidenav-link active" if s["key"] == active_key else "sidenav-link"
        links.append(
            dcc.Link(
                href=s["path"],
                className=cls,
                children=s["label"],
            )
        )
    return html.Div(
        className="sidenav",
        children=[
            html.Div("Navigation", className="sidenav-section-label"),
            *links,
        ],
    )



def page_header(eyebrow, title, subtitle=None):
    children = [
        html.Div(eyebrow, className="page-eyebrow"),
        html.H1(title, className="page-title"),
    ]
    if subtitle:
        children.append(html.P(subtitle, className="page-subtitle"))
    return html.Div(className="page-header", children=children)


def badge(text, kind="grey", dot=False):
    dot_colors = {
        "accent": "#3D5A73", "amber": "#C17817", "good": "#3E6B4F", "grey": "#6B6B6B",
    }
    children = []
    if dot:
        children.append(html.Span(className="badge-dot",
                                   style={"background": dot_colors.get(kind, "#6B6B6B")}))
    children.append(html.Span(text))
    return html.Span(children, className=f"badge badge-{kind}")


def status_badge(status_key):
    mapping = {
        "on_track": ("On track", "good"),
        "complete": ("Complete", "good"),
        "in_progress": ("In progress", "accent"),
        "at_risk": ("At risk", "amber"),
        "not_started": ("Not started", "grey"),
        "Approved": ("Approved", "good"),
        "Pending approval": ("Pending", "amber"),
        "Withdrawn": ("Withdrawn", "grey"),
        "Paid": ("Paid", "good"),
        "Draft — not yet issued": ("Draft", "grey"),
        "Final": ("Final", "good"),
        "Awaiting client approval": ("Awaiting client", "amber"),
        "In progress": ("In progress", "accent"),
    }
    label, kind = mapping.get(status_key, (status_key, "grey"))
    return badge(label, kind=kind, dot=True)


def stat_block(label, value, caption=None):
    children = [
        html.Span(label, className="stat-label"),
        html.Span(value, className="stat-value"),
    ]
    if caption:
        children.append(html.Span(caption, className="stat-caption"))
    return html.Div(children, className="stat-block")


def card(title, content, title_right=None):
    if title_right is not None:
        header = html.Div(className="card-title",
                          children=[html.Span(title), title_right])
    else:
        header = html.Div(title, className="card-title")
    return html.Div(className="card", children=[header, content])


def ai_overview_panel(summary, detail, mode_label="Team Consulting view", panel_id="ai-panel-detail"):
    """Expandable AI overview: summary visible always; click to see full detail."""
    return html.Div(
        className="ai-panel",
        children=[
            html.Div(
                className="ai-panel-label",
                children=[
                    html.Span(className="ai-spark"),
                    html.Span(f"AI overview · {mode_label}"),
                ],
            ),
            html.Div(summary, className="ai-panel-text"),
            html.Button(
                "Show full analysis ▾",
                id={"type": "ai-expand-btn", "index": panel_id},
                className="ai-expand-btn",
                n_clicks=0,
            ),
            html.Div(
                id={"type": "ai-detail", "index": panel_id},
                className="ai-panel-detail",
                style={"display": "none"},
                children=html.Pre(detail, className="ai-panel-detail-text"),
            ),
        ],
    )


def internal_only_tag():
    return html.Span("Internal only", className="internal-only-tag")


def comment_thread(comments, thread_id, show_input=True):
    """Render a comment thread with resolve buttons and an add-comment input."""
    items = []
    for c in sorted(comments, key=lambda x: x["date"]):
        initials = "".join(p[0] for p in c["author"].split()[:2])
        resolved_cls = " resolved" if c.get("resolved") else ""
        items.append(
            html.Div(
                className=f"comment {c['team']}{resolved_cls}",
                children=[
                    html.Div(initials, className="comment-avatar"),
                    html.Div(className="comment-body", children=[
                        html.Div(className="comment-meta", children=[
                            html.Span(c["author"], className="comment-author"),
                            html.Span(c["date"].strftime("%d %b %Y"), className="comment-date"),
                            html.Span("· Resolved", className="comment-resolved-tag") if c.get("resolved") else None,
                        ]),
                        html.Div(c["text"], className="comment-text"),
                    ]),
                ],
            )
        )

    children = [html.Div(items, className="comment-thread")] if items else []

    if show_input:
        children.append(
            html.Div(
                className="comment-input-row",
                children=[
                    dcc.Input(
                        id={"type": "comment-input", "index": thread_id},
                        type="text",
                        placeholder="Add a comment…",
                        className="comment-input",
                        debounce=False,
                    ),
                    html.Button(
                        "Post",
                        id={"type": "comment-submit", "index": thread_id},
                        n_clicks=0,
                        className="comment-submit-btn",
                    ),
                ],
            )
        )

    return html.Div(children, className="comment-section")
