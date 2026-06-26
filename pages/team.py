"""
Team page — profile cards for Team Consulting and Gilead.
Two view modes:
  "By Team"        — TC and Gilead shown separately (default)
  "Collaboration"  — visual hierarchy showing who works with whom across teams
"""

import dash
from dash import html, dcc, Input, Output, callback, ctx

from components.shell import page_header, card
from data.synthetic_data import TEAM_PEOPLE, CLIENT_PEOPLE

dash.register_page(__name__, path="/team", name="Team")

_STATUS_LABEL = {
    "active": "Active",
    "rolling_off": "Rolling off",
    "rolling_on": "Rolling on",
}
_STATUS_CLS = {
    "active": "team-status-active",
    "rolling_off": "team-status-off",
    "rolling_on": "team-status-on",
}

_ALL_PEOPLE = {p["id"]: p for p in TEAM_PEOPLE + CLIENT_PEOPLE}

# Collaboration groups — who works with whom, with hierarchy info
_COLLAB_GROUPS = [
    {
        "label": "Programme Leadership",
        "color": "#282727",
        "tc": [
            {"id": "T01", "reports": "Programme Lead", "is_lead": True},
        ],
        "gilead": [
            {"id": "G01", "reports": "Programme Sponsor", "is_lead": True},
        ],
        "connection": "John Burke reports to Anita Devereux for programme direction",
    },
    {
        "label": "Engineering & Device Development",
        "color": "#003057",
        "tc": [
            {"id": "T02", "reports": "Lead Engineer", "is_lead": True},
            {"id": "T03", "reports": "Test execution — reports to T02", "is_lead": False},
            {"id": "T05", "reports": "Intern — reports to T02", "is_lead": False},
        ],
        "gilead": [
            {"id": "G02", "reports": "Gilead device lead", "is_lead": True},
            {"id": "G05", "reports": "HF & clinical liaison", "is_lead": False},
        ],
        "connection": "Tom Grant is counterpart to James Okonkwo · Jasper works with Sofia Alvarez on device testing",
    },
    {
        "label": "Quality, Regulatory & Design",
        "color": "#2D5A3D",
        "tc": [
            {"id": "T04", "reports": "DHF & risk file — reports to T01", "is_lead": True},
        ],
        "gilead": [
            {"id": "G03", "reports": "QA sign-off authority", "is_lead": True},
            {"id": "G04", "reports": "Regulatory strategy lead", "is_lead": False},
        ],
        "connection": "Louis DeCleyn interfaces daily with Mei Lin Tan for QA approvals",
    },
]


def _person_card(person, side="tc", show_allocation=False):
    initials = "".join(p[0] for p in person["name"].split()[:2])
    status_cls = _STATUS_CLS.get(person["status"], "team-status-active")
    status_label = _STATUS_LABEL.get(person["status"], person["status"])

    if side == "tc":
        brand_el = html.Img(
            src="/assets/img/team_icon_mark.svg",
            className="team-card-brand-logo",
        )
    else:
        brand_el = html.Span("Gilead Sciences", className="team-card-brand-text")

    if person.get("photo") and side == "tc":
        photo_el = html.Img(
            src=person["photo"],
            className="team-card-photo-img",
            alt=person["name"],
        )
    elif side == "gilead":
        photo_el = html.Img(
            src="/assets/img/avatar_blank.svg",
            className="team-card-photo-img",
            alt="",
        )
    else:
        photo_el = html.Span(initials, className="team-card-initials-lg")

    alloc_block = None
    if show_allocation and person.get("allocation_pct"):
        alloc_block = html.Div(
            className="team-card-allocation",
            children=[
                html.Div(className="alloc-bar-track", children=[
                    html.Div(className="alloc-bar-fill",
                             style={"width": f"{person['allocation_pct']}%"}),
                ]),
                html.Span(f"{person['allocation_pct']}% allocated", className="alloc-label"),
            ],
        )

    return html.Div(
        className="team-card",
        children=[
            html.Div(className="team-card-header", children=[
                brand_el,
                html.Span(person["role"], className="team-card-role-text"),
            ]),
            html.Div(className="team-card-photo", children=[photo_el]),
            html.Div([
                html.Div(person["name"], className="team-card-name"),
                html.Div(person["discipline"], className="team-card-discipline"),
                html.Div(className="team-card-status-text", children=[
                    html.Span(className=f"team-card-status-dot {status_cls}"),
                    html.Span(status_label),
                ]),
                alloc_block,
            ]),
        ],
    )


def _collab_member_chip(person_id, reports_label, is_lead, side):
    person = _ALL_PEOPLE.get(person_id)
    if not person:
        return None

    initials = "".join(p[0] for p in person["name"].split()[:2])

    if person.get("photo"):
        avatar = html.Img(
            src=person["photo"],
            className="collab-avatar-img",
            alt=person["name"],
        )
    else:
        avatar = html.Div(initials, className=f"collab-avatar-initials {side}")

    side_color = "#282727" if side == "tc" else "#d63346"

    return html.Div(
        className=f"collab-chip {'collab-chip-lead' if is_lead else 'collab-chip-sub'}",
        style={"borderLeftColor": side_color if is_lead else "transparent"},
        children=[
            html.Div(className="collab-chip-avatar", children=[avatar]),
            html.Div(className="collab-chip-info", children=[
                html.Div(person["name"], className="collab-chip-name"),
                html.Div(person["role"], className="collab-chip-role"),
                html.Div(reports_label, className="collab-chip-reports"),
            ]),
            html.Img(
                src="/assets/img/team_icon_mark.svg" if side == "tc" else "/assets/img/gilead_logo.svg",
                className=f"collab-side-logo {side}",
                alt="TC" if side == "tc" else "Gilead",
            ),
        ],
    )


def _collab_group_card(grp):
    tc_chips = []
    for m in grp["tc"]:
        chip = _collab_member_chip(m["id"], m["reports"], m["is_lead"], "tc")
        if chip:
            tc_chips.append(chip)

    gilead_chips = []
    for m in grp["gilead"]:
        chip = _collab_member_chip(m["id"], m["reports"], m["is_lead"], "gilead")
        if chip:
            gilead_chips.append(chip)

    return html.Div(
        className="collab-group",
        children=[
            html.Div(
                className="collab-group-header",
                style={"borderLeftColor": grp["color"]},
                children=[
                    html.Span(grp["label"], className="collab-group-title"),
                ],
            ),
            html.Div(
                className="collab-columns",
                children=[
                    html.Div(
                        className="collab-column collab-col-tc",
                        children=[
                            html.Div("Team Consulting", className="collab-col-label collab-col-label-tc"),
                            html.Div(tc_chips, className="collab-chips"),
                        ],
                    ),
                    html.Div(className="collab-divider", children=[
                        html.Div(className="collab-divider-line"),
                        html.Div("↔", className="collab-divider-icon"),
                        html.Div(className="collab-divider-line"),
                    ]),
                    html.Div(
                        className="collab-column collab-col-gilead",
                        children=[
                            html.Div("Gilead Sciences", className="collab-col-label collab-col-label-gilead"),
                            html.Div(gilead_chips, className="collab-chips"),
                        ],
                    ),
                ],
            ),
            html.Div(grp["connection"], className="collab-connection-note"),
        ],
    )


def layout():
    return html.Div([
        page_header(
            "Project Sycamore · Team",
            "Team",
            "Everyone working on the programme — Team Consulting and Gilead Sciences.",
        ),
        html.Div(className="team-view-toggle", children=[
            html.Button("By Team", id="team-view-btn-team", className="team-view-btn active",
                        n_clicks=0),
            html.Button("Collaboration", id="team-view-btn-disc", className="team-view-btn",
                        n_clicks=0),
        ]),
        dcc.Store(id="team-view-store", data="team"),
        html.Div(id="team-content"),
    ])


@callback(
    Output("team-view-store", "data"),
    Output("team-view-btn-team", "className"),
    Output("team-view-btn-disc", "className"),
    Input("team-view-btn-team", "n_clicks"),
    Input("team-view-btn-disc", "n_clicks"),
    prevent_initial_call=True,
)
def switch_team_view(_t, _d):
    if ctx.triggered_id == "team-view-btn-team":
        return "team", "team-view-btn active", "team-view-btn"
    return "discipline", "team-view-btn", "team-view-btn active"


@callback(
    Output("team-content", "children"),
    Input("team-view-store", "data"),
    Input("view-mode-store", "data"),
)
def render_team_content(view, mode):
    is_team_mode = mode == "team"

    if view == "discipline":
        groups = [_collab_group_card(grp) for grp in _COLLAB_GROUPS]
        return html.Div([
            html.P(
                "Showing who works with whom across Team Consulting and Gilead Sciences, "
                "grouped by work area with reporting lines indicated.",
                className="muted small",
                style={"marginBottom": "20px"},
            ),
            *groups,
        ])

    # By-team view (default)
    tc_cards = html.Div(
        className="team-cards-grid",
        children=[_person_card(p, side="tc", show_allocation=is_team_mode)
                  for p in TEAM_PEOPLE],
    )
    gilead_cards = html.Div(
        className="team-cards-grid",
        children=[_person_card(p, side="gilead", show_allocation=not is_team_mode)
                  for p in CLIENT_PEOPLE],
    )

    tc_section = card(
        "Team Consulting",
        html.Div([
            html.P(
                "Project delivery team." + (
                    " Allocation percentages visible to Team Consulting only."
                    if is_team_mode else ""),
                className="muted small",
                style={"marginBottom": "16px"},
            ),
            tc_cards,
        ]),
    )
    gilead_section = card(
        "Gilead Sciences",
        html.Div([
            html.P(
                "Client stakeholders engaged on the programme.",
                className="muted small",
                style={"marginBottom": "16px"},
            ),
            gilead_cards,
        ]),
    )

    return html.Div([
        tc_section,
        html.Div(gilead_section, style={"marginTop": "24px"}),
    ])
