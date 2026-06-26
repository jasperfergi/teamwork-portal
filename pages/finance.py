"""
Finance page — budget, burn rate, EVM analysis, change orders, POs, and invoicing.
"""

import dash
from dash import html, dcc, Input, Output, callback

from components.shell import page_header, card, stat_block, status_badge, internal_only_tag
from components.charts import budget_burn_figure, budget_donut_figure
from data.synthetic_data import BUDGET, PURCHASE_ORDERS

dash.register_page(__name__, path="/finance", name="Finance")

# ---------------------------------------------------------------------------
# Earned Value Management metrics (as of 25 Jun 2026)
# ---------------------------------------------------------------------------
_BAC = 3_000_000     # Budget at Completion
_PV  = 1_875_000     # Planned Value — phased budget to date
_AC  = 1_951_000     # Actual Cost to date
_EV  = 1_895_000     # Earned Value — work physically accomplished

_CPI  = round(_EV / _AC,  3)              # 0.971
_SPI  = round(_EV / _PV,  3)              # 1.011
_CV   = _EV - _AC                         # -56,000
_SV   = _EV - _PV                         # +20,000
_EAC  = round(_BAC / _CPI)                # 3,089,000
_ETC  = _EAC - _AC                        # 1,138,000
_VAC  = _BAC - _EAC                       # -89,000
_TCPI = round((_BAC - _EV) / (_BAC - _AC), 3)  # 1.054


def layout():
    spent     = BUDGET["fees_spent"] + BUDGET["me_spent"]
    remaining = BUDGET["total"] - spent
    forecast_total = sum(m[1] + m[2] for m in BUDGET["monthly_forecast"])

    return html.Div([
        page_header(
            "Project Sycamore · Finance",
            "Finance",
            "Budget, earned value analysis, burn rate, change orders, POs, and invoicing.",
        ),

        # EVM Analysis — top of page
        html.Div(id="finance-evm", style={"marginTop": "20px"}),

        html.Div(className="card-grid grid-4", style={"marginTop": "20px"}, children=[
            card("Total budget", stat_block(
                "Contracted", f"£{BUDGET['total']:,.0f}",
                f"£{BUDGET['fees_budget']:,.0f} fees · £{BUDGET['me_budget']:,.0f} M&E",
            )),
            card("Spent to date", dcc.Graph(
                figure=budget_donut_figure(spent, remaining),
                config={"displayModeBar": False},
            )),
            card("Remaining", stat_block(
                "Available", f"£{remaining:,.0f}",
                f"{round(100 * remaining / BUDGET['total'])}% of budget",
            )),
            card("Forecast to complete", stat_block(
                "Remaining months", f"£{forecast_total:,.0f}",
                "Jul – Sep 2026 (3 months)",
            )),
        ]),

        html.Div(style={"marginTop": "20px"}, children=[
            card("Monthly burn — actual vs. forecast", dcc.Graph(
                figure=budget_burn_figure(
                    BUDGET["monthly_burn"],
                    monthly_forecast=BUDGET["monthly_forecast"],
                ),
                config={"displayModeBar": False},
            )),
        ]),

        html.Div(id="finance-internal-note", style={"marginTop": "20px"}),

        html.Div(className="card-grid grid-2", style={"marginTop": "20px"}, children=[
            card("Change orders", html.Div(id="finance-change-orders")),
            card("Invoices",      html.Div(id="finance-invoices")),
        ]),

        html.Div(style={"marginTop": "20px"}, children=[
            card("Purchase orders", html.Div(id="finance-pos")),
        ]),
    ])


@callback(Output("finance-evm", "children"), Input("view-mode-store", "data"))
def update_evm(_mode):
    def _metric(label, value, sub=None, highlight=False):
        return html.Div(className="evm-metric", children=[
            html.Div(label, className="evm-label"),
            html.Div(value, className=f"evm-value{'  evm-value--flag' if highlight else ''}"),
            html.Div(sub, className="evm-sub") if sub else None,
        ])

    cv_str  = f"−£{abs(_CV):,.0f}"  if _CV  < 0 else f"+£{_CV:,.0f}"
    sv_str  = f"+£{_SV:,.0f}"       if _SV  >= 0 else f"−£{abs(_SV):,.0f}"
    vac_str = f"−£{abs(_VAC):,.0f}" if _VAC < 0 else f"+£{_VAC:,.0f}"

    metrics = html.Div(className="evm-grid", children=[
        _metric("BAC",  f"£{_BAC:,.0f}",  "Budget at Completion"),
        _metric("PV",   f"£{_PV:,.0f}",   "Planned Value"),
        _metric("EV",   f"£{_EV:,.0f}",   "Earned Value"),
        _metric("AC",   f"£{_AC:,.0f}",   "Actual Cost"),
        _metric("CV",   cv_str,            "Cost Variance",              highlight=(_CV < 0)),
        _metric("SV",   sv_str,            "Schedule Variance"),
        _metric("EAC",  f"£{_EAC:,.0f}",  "Estimate at Completion",     highlight=(_EAC > _BAC)),
        _metric("ETC",  f"£{_ETC:,.0f}",  "Estimate to Complete"),
    ])

    narrative = html.Div(className="evm-narrative", children=[
        html.Div("Programme analysis", className="evm-narrative-title"),
        html.P(
            f"The programme is running approximately {round((1 - _CPI) * 100, 1)}% hot on cost "
            f"over the past six weeks (CPI {_CPI:.3f}), driven primarily by the additional "
            f"incoming-inspection step introduced under decision D-012 (spring force tolerance "
            f"tightened to ±3%). Despite this, schedule performance is marginally ahead of plan "
            f"(SPI {_SPI:.3f}), reflecting the parallel DV test execution strategy which has "
            f"pulled forward several work packages.",
            className="evm-narrative-text",
        ),
        html.P(
            f"The trend-based EAC of £{_EAC:,.0f} represents an adverse variance of "
            f"£{abs(_VAC):,.0f} (VAC) against the BAC of £{_BAC:,.0f}. However, the "
            f"inspection overhead is expected to diminish as the spring test batch (WP1.2) "
            f"completes in July, and the schedule advancement creates headroom to recover cost "
            f"efficiency in Q3. The TCPI of {_TCPI:.3f} indicates the remaining work needs to "
            f"be delivered at approximately {round((_TCPI - 1) * 100, 1)}% greater efficiency "
            f"than current to return to BAC — considered achievable given the reducing overhead.",
            className="evm-narrative-text",
        ),
        html.P(
            "Note: CO-04 (£86k shelf-life extension) is not yet in the BAC baseline. "
            "If approved, BAC increases to £3,086,000 and the adverse VAC reduces to "
            "approximately £3,000 — effectively budget-neutral.",
            className="evm-narrative-note",
        ),
    ])

    return card("Earned Value Analysis", html.Div([metrics, narrative]),
                title_right=internal_only_tag())


@callback(Output("finance-internal-note", "children"), Input("view-mode-store", "data"))
def update_internal_note(mode):
    if mode == "client":
        return None
    return card(
        "Internal forecast note",
        html.Div([
            html.P(
                "Current burn rate is ~4% ahead of the phased budget for this stage, driven "
                "by the additional incoming-inspection step under D-012. The July–September "
                "forecast assumes CO-04 is approved and the shelf-life ageing arm starts on "
                "schedule. If CO-04 slips, the M&E forecast for Jul drops by ~£35k but "
                "rebounds in September when the chamber slot becomes available.",
                style={"fontSize": "13.5px", "color": "#4A4A48", "lineHeight": "1.6", "margin": 0},
            ),
        ]),
        title_right=internal_only_tag(),
    )


@callback(Output("finance-change-orders", "children"), Input("view-mode-store", "data"))
def update_change_orders(_mode):
    rows = [
        html.Tr([
            html.Td(co["id"], style={"fontFamily": "monospace", "fontSize": "12px", "fontWeight": "600"}),
            html.Td(co["title"]),
            html.Td(f"£{co['value']:,.0f}"),
            html.Td(co["date"].strftime("%d %b %Y")),
            html.Td(status_badge(co["status"])),
        ])
        for co in BUDGET["change_orders"]
    ]
    return html.Table(className="simple-table", children=[
        html.Thead(html.Tr([
            html.Th("ID"), html.Th("Title"), html.Th("Value"),
            html.Th("Date"), html.Th("Status"),
        ])),
        html.Tbody(rows),
    ])


@callback(Output("finance-invoices", "children"), Input("view-mode-store", "data"))
def update_invoices(_mode):
    rows = [
        html.Tr([
            html.Td(inv["number"], style={"fontFamily": "monospace", "fontSize": "12px", "fontWeight": "600"}),
            html.Td(inv["period"]),
            html.Td(f"£{inv['amount']:,.0f}"),
            html.Td(inv["date"].strftime("%d %b %Y") if inv["date"] else "—"),
            html.Td(status_badge(inv["status"])),
        ])
        for inv in BUDGET["invoices"]
    ]
    return html.Table(className="simple-table", children=[
        html.Thead(html.Tr([
            html.Th("Invoice"), html.Th("Period"), html.Th("Amount"),
            html.Th("Date"), html.Th("Status"),
        ])),
        html.Tbody(rows),
    ])


@callback(Output("finance-pos", "children"), Input("view-mode-store", "data"))
def update_pos(_mode):
    status_cls = {
        "Closed":  "action-badge po-status-closed",
        "Open":    "action-badge po-status-open",
        "Pending": "action-badge po-status-pending",
    }
    rows = [
        html.Tr([
            html.Td(html.Span(po["po_number"], className="po-number")),
            html.Td(po["description"], className="po-desc"),
            html.Td(po["vendor"]),
            html.Td(po["raised_by"]),
            html.Td(po["currency"]),
            html.Td(f"{po['currency']} {po['amount']:,.0f}"),
            html.Td(html.Span(po["status"], className=status_cls.get(po["status"], "action-badge"))),
            html.Td(po.get("co_ref") or "—"),
        ])
        for po in PURCHASE_ORDERS
    ]
    return html.Table(className="simple-table po-table", children=[
        html.Thead(html.Tr([
            html.Th("PO Number"), html.Th("Description"), html.Th("Vendor"),
            html.Th("Raised by"), html.Th("Currency"), html.Th("Amount"),
            html.Th("Status"), html.Th("CO Ref"),
        ])),
        html.Tbody(rows),
    ])
