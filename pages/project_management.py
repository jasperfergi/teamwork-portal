"""
Project Management page — tabbed view covering the programme timeline,
action log, risk register, costs & POs, and team availability.
"""

import dash
from dash import html, dcc, Input, Output, callback

from components.shell import page_header, card, status_badge
from components.charts import gantt_figure
from data.synthetic_data import (
    TASKS, FILES, PRESENTATIONS, TEAM_PEOPLE, CLIENT_PEOPLE, PROJECT,
    RISKS, ACTIONS, PURCHASE_ORDERS, COST_BREAKDOWN,
)

dash.register_page(__name__, path="/project-management", name="Project Management")

_TODAY = PROJECT["today"]


def layout():
    return html.Div([
        page_header(
            "Project Sycamore · Project Management",
            "Project Management",
            "Programme timeline, actions, risk register, costs, and team availability.",
        ),

        # Tab bar
        html.Div(className="pm-tabs", children=[
            html.Button("Programme",    id="pmtab-btn-programme", className="pm-tab active", n_clicks=0),
            html.Button("Actions",      id="pmtab-btn-actions",   className="pm-tab",        n_clicks=0),
            html.Button("Risk Register",id="pmtab-btn-risk",      className="pm-tab",        n_clicks=0),
            html.Button("Costs & POs",  id="pmtab-btn-costs",     className="pm-tab",        n_clicks=0),
            html.Button("Resources",    id="pmtab-btn-resources",  className="pm-tab",        n_clicks=0),
        ]),

        html.Div(id="pm-tab-content", style={"marginTop": "16px"}),
    ])


# ── Tab switching (clientside) ─────────────────────────────────────────────────

dash.get_app().clientside_callback(
    """
    function(p, a, r, c, res) {
        var labels = ['programme','actions','risk','costs','resources'];
        var triggered = window.dash_clientside.callback_context.triggered[0].prop_id;
        var active = 'programme';
        labels.forEach(function(l){ if(triggered.includes(l)) active = l; });
        labels.forEach(function(l){
            var btn = document.getElementById('pmtab-btn-' + l);
            if(btn) btn.className = 'pm-tab' + (l === active ? ' active' : '');
        });
        return active;
    }
    """,
    Output("pm-tab-store", "data"),
    Input("pmtab-btn-programme", "n_clicks"),
    Input("pmtab-btn-actions",   "n_clicks"),
    Input("pmtab-btn-risk",      "n_clicks"),
    Input("pmtab-btn-costs",     "n_clicks"),
    Input("pmtab-btn-resources", "n_clicks"),
    prevent_initial_call=True,
)


# ── Tab content ───────────────────────────────────────────────────────────────

@callback(
    Output("pm-tab-content", "children"),
    Input("pm-tab-store", "data"),
    Input("view-mode-store", "data"),
)
def render_tab(tab, _mode):
    tab = tab or "programme"
    if tab == "programme":
        return _programme_tab(_mode)
    if tab == "actions":
        return _actions_tab()
    if tab == "risk":
        return _risk_tab()
    if tab == "costs":
        return _costs_tab()
    if tab == "resources":
        return _resources_tab()
    return _programme_tab()


def _programme_tab(mode=None):
    pm_files = [f for f in FILES if f["sector"] == "Project Management"] or FILES[:4]
    file_rows = [
        html.Tr([
            html.Td(html.A(f["name"], href=f["url"], target="_blank", className="file-link")),
            html.Td(f["last_edited_by"]),
            html.Td(f["last_edited"].strftime("%d %b %Y")),
            html.Td(status_badge(f["status"])),
        ])
        for f in pm_files
    ]
    files_table = html.Table(className="simple-table", children=[
        html.Thead(html.Tr([html.Th("File"), html.Th("Edited by"), html.Th("Date"), html.Th("Status")])),
        html.Tbody(file_rows),
    ])

    pres_rows = [
        html.Tr([
            html.Td(html.A(p["name"], href=p["url"], target="_blank", className="file-link")),
            html.Td(p["date"].strftime("%d %b %Y")),
            html.Td(html.A("Transcript →", href=p["transcript_url"], target="_blank")),
        ])
        for p in sorted(PRESENTATIONS, key=lambda x: x["date"], reverse=True)
    ]
    pres_table = html.Table(className="simple-table", children=[
        html.Thead(html.Tr([html.Th("Presentation"), html.Th("Date"), html.Th("")])),
        html.Tbody(pres_rows),
    ])

    return html.Div([
        card("Full programme timeline", dcc.Graph(
            figure=gantt_figure(TASKS, today=_TODAY, mode=mode),
            config={"displayModeBar": False},
        )),
        html.Div(className="card-grid grid-2", style={"marginTop": "16px"}, children=[
            card("Files", files_table),
            card("Presentations & transcripts", pres_table),
        ]),
    ])


def _actions_tab():
    priority_cls = {"High": "action-pri-high", "Medium": "action-pri-med", "Low": "action-pri-low"}
    status_cls   = {"Open": "action-status-open", "In Progress": "action-status-prog", "Closed": "action-status-done"}

    rows = []
    for a in ACTIONS:
        rows.append(html.Tr(className="action-row", children=[
            html.Td(html.Span(a["id"], className="action-id")),
            html.Td(a["description"], className="action-desc"),
            html.Td(a["owner"]),
            html.Td(a["due_date"].strftime("%d %b %Y")),
            html.Td(html.Span(a["priority"], className=f"action-badge {priority_cls.get(a['priority'], '')}")),
            html.Td(html.Span(a["status"],   className=f"action-badge {status_cls.get(a['status'], '')}")),
            html.Td(a["source"], className="action-source"),
        ]))

    table = html.Table(className="simple-table action-table", children=[
        html.Thead(html.Tr([
            html.Th("ID"), html.Th("Action"), html.Th("Owner"),
            html.Th("Due"), html.Th("Priority"), html.Th("Status"), html.Th("Source"),
        ])),
        html.Tbody(rows),
    ])

    open_count = sum(1 for a in ACTIONS if a["status"] in ("Open", "In Progress"))
    return card(f"Action log — {open_count} open", table)


def _risk_tab():
    def _dots(n, total, cls):
        return html.Div(className="risk-dots", children=[
            html.Span(className=f"risk-dot filled {cls}" if i < n else "risk-dot")
            for i in range(total)
        ])

    def _score_chip(score):
        if score >= 15:
            return html.Span(str(score), className="risk-score-chip high")
        if score >= 8:
            return html.Span(str(score), className="risk-score-chip medium")
        return html.Span(str(score), className="risk-score-chip low")

    open_risks   = [r for r in RISKS if r["status"] == "Open"]
    closed_risks = [r for r in RISKS if r["status"] == "Closed"]

    def _risk_row(r):
        return html.Tr([
            html.Td(html.Span(r["id"], className="risk-id")),
            html.Td(r["title"], className="risk-title"),
            html.Td(html.Span(r["category"], className="risk-category-chip")),
            html.Td(_dots(r["severity"],   5, "sev")),
            html.Td(_dots(r["likelihood"], 5, "lik")),
            html.Td(_score_chip(r["score"])),
            html.Td(r["owner"]),
            html.Td(r["comment"], className="risk-comment"),
        ])

    open_table = html.Table(className="simple-table risk-table", children=[
        html.Thead(html.Tr([
            html.Th("ID"), html.Th("Risk"), html.Th("Category"),
            html.Th("Severity /5"), html.Th("Likelihood /5"), html.Th("Score /25"),
            html.Th("Owner"), html.Th("Comment"),
        ])),
        html.Tbody([_risk_row(r) for r in open_risks]),
    ])

    sections = [card(f"Open risks ({len(open_risks)})", open_table)]

    if closed_risks:
        closed_table = html.Table(className="simple-table risk-table", children=[
            html.Thead(html.Tr([
                html.Th("ID"), html.Th("Risk"), html.Th("Category"),
                html.Th("Severity /5"), html.Th("Likelihood /5"), html.Th("Score /25"),
                html.Th("Owner"), html.Th("Comment"),
            ])),
            html.Tbody([_risk_row(r) for r in closed_risks]),
        ])
        sections.append(html.Div(style={"marginTop": "16px"}, children=[
            card(f"Closed risks ({len(closed_risks)})", closed_table),
        ]))

    return html.Div(sections)


def _costs_tab():
    # Costing sheet — breakdown by type then discipline
    def _cost_row(label, budget, spent, forecast):
        variance = forecast - budget
        var_cls = "cost-var-over" if variance > 0 else "cost-var-under"
        var_str = f"+£{variance:,.0f}" if variance >= 0 else f"−£{abs(variance):,.0f}"
        return html.Tr([
            html.Td(label),
            html.Td(f"£{budget:,.0f}"),
            html.Td(f"£{spent:,.0f}"),
            html.Td(f"{round(100*spent/budget)}%"),
            html.Td(f"£{forecast:,.0f}"),
            html.Td(html.Span(var_str, className=var_cls)),
        ])

    type_rows = [_cost_row(t["type"], t["budget"], t["spent"], t["forecast"])
                 for t in COST_BREAKDOWN["by_type"]]
    disc_rows = [_cost_row(d["discipline"], d["budget"], d["spent"], d["forecast"])
                 for d in COST_BREAKDOWN["by_discipline"]]

    costing_card = card("Costing sheet", html.Div([
        html.Div("By cost type", className="cost-section-header"),
        html.Table(className="simple-table cost-table", children=[
            html.Thead(html.Tr([
                html.Th("Category"), html.Th("Budget"), html.Th("Spent"),
                html.Th("% used"), html.Th("Forecast"), html.Th("Variance"),
            ])),
            html.Tbody(type_rows),
        ]),
        html.Div("By discipline", className="cost-section-header", style={"marginTop": "16px"}),
        html.Table(className="simple-table cost-table", children=[
            html.Thead(html.Tr([
                html.Th("Discipline"), html.Th("Budget"), html.Th("Spent"),
                html.Th("% used"), html.Th("Forecast"), html.Th("Variance"),
            ])),
            html.Tbody(disc_rows),
        ]),
        html.Div(className="contingency-row", children=[
            html.Span("Contingency", className="contingency-label"),
            html.Span(
                f"£{COST_BREAKDOWN['contingency_used']:,.0f} used of "
                f"£{COST_BREAKDOWN['contingency_budget']:,.0f} "
                f"({round(100*COST_BREAKDOWN['contingency_used']/COST_BREAKDOWN['contingency_budget'])}%)",
                className="contingency-value",
            ),
        ]),
    ]))

    # PO table
    status_cls = {"Closed": "po-status-closed", "Open": "po-status-open", "Pending": "po-status-pending"}
    po_rows = [
        html.Tr([
            html.Td(html.Span(po["po_number"], className="po-number")),
            html.Td(po["description"], className="po-desc"),
            html.Td(po["vendor"]),
            html.Td(po["raised_by"]),
            html.Td(po["currency"]),
            html.Td(f"{po['currency']} {po['amount']:,.0f}"),
            html.Td(html.Span(po["status"], className=f"action-badge {status_cls.get(po['status'], '')}")),
            html.Td(html.Span(po["co_ref"] or "—", className="po-co-ref") if po.get("co_ref") else "—"),
        ])
        for po in PURCHASE_ORDERS
    ]
    po_card = card("Purchase orders", html.Table(
        className="simple-table po-table",
        children=[
            html.Thead(html.Tr([
                html.Th("PO Number"), html.Th("Description"), html.Th("Vendor"),
                html.Th("Raised by"), html.Th("Currency"), html.Th("Amount"),
                html.Th("Status"), html.Th("CO Ref"),
            ])),
            html.Tbody(po_rows),
        ],
    ))

    return html.Div([
        costing_card,
        html.Div(style={"marginTop": "16px"}, children=[po_card]),
    ])


def _resources_tab():
    def _person_row(p, side="tc"):
        pct = p["allocation_pct"]
        has_photo = p.get("photo") and side == "tc"
        if has_photo:
            avatar = html.Img(src=p["photo"], className="avail-photo")
        else:
            ini = "".join(n[0] for n in p["name"].split()[:2])
            avatar = html.Div(ini, className="avail-initials")

        if p["status"] == "rolling_off":
            bar_cls = "avail-bar-amber"
        elif p["status"] == "rolling_on":
            bar_cls = "avail-bar-blue"
        else:
            bar_cls = "avail-bar-main"

        return html.Div(className="avail-row", children=[
            avatar,
            html.Div(className="avail-info", children=[
                html.Div(p["name"], className="avail-name"),
                html.Div(p["role"], className="avail-role"),
            ]),
            html.Div(className="avail-bar-wrap", children=[
                html.Div(className="avail-bar-track", children=[
                    html.Div(className=f"avail-bar-fill {bar_cls}", style={"width": f"{pct}%"}),
                ]),
                html.Span(f"{pct}%", className="avail-bar-pct"),
            ]),
        ])

    tc_rows   = [_person_row(p, "tc")     for p in sorted(TEAM_PEOPLE,   key=lambda x: -x["allocation_pct"])]
    gilead_rows = [_person_row(p, "gilead") for p in sorted(CLIENT_PEOPLE, key=lambda x: -x["allocation_pct"])]

    return html.Div(className="card-grid grid-2", children=[
        card("Team Consulting availability", html.Div(tc_rows,    className="avail-list")),
        card("Gilead availability",          html.Div(gilead_rows, className="avail-list")),
    ])


