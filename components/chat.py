"""
Floating AI chatbot + Team Chat panel.
Two tabs: AI assistant (canned responses) and Team Chat (pre-populated thread).
"""

from dash import html, dcc

_TEAM_MSGS = [
    {"from": "John Burke",   "photo": "/assets/img/john_burke.jpg",   "time": "09:22", "msg": "DVP Rev C still with Mei Lin — I've pinged her and expecting a response today. Let's flag the status at standup."},
    {"from": "Tom Grant",    "photo": "/assets/img/tom_grant.jpg",    "time": "09:31", "msg": "Emily — great timing on the spring results. Jasper, can you cross-check the tolerance readings against D-012 targets after the 11:00 run?"},
    {"from": "Emily Morley", "photo": "/assets/img/emily_morley.jpg", "time": "09:35", "msg": "Yesterday's batch looks clean — all readings within ±2.8%. Report circulating before lunch."},
    {"from": "Louis DeCleyn","photo": "/assets/img/louis_decleyn.jpg","time": "09:48", "msg": "Risk file v8 is back from QA — two medium risks formally downgraded. Updating the tracker now."},
]


def _team_msg(m):
    return html.Div(className="team-msg-row", children=[
        html.Img(src=m["photo"], className="team-msg-av"),
        html.Div(className="team-msg-body", children=[
            html.Div(className="team-msg-meta", children=[
                html.Span(m["from"], className="team-msg-name"),
                html.Span(f"Today {m['time']}", className="team-msg-time"),
            ]),
            html.Div(m["msg"], className="team-msg-text"),
        ]),
    ])


def chat_fab():
    return html.Button("💬", id="chat-fab-btn", className="chat-fab", n_clicks=0)


def chat_panel():
    return html.Div(
        id="chat-panel",
        className="chat-panel",
        style={"display": "none"},
        children=[
            # Header row
            html.Div(
                className="chat-panel-header",
                children=[
                    html.Div(
                        className="chat-panel-title-row",
                        children=[
                            html.Span("*", className="chat-header-spark"),
                            html.Span("Project Sycamore"),
                        ],
                    ),
                    html.Button(
                        "x", id="chat-close-btn", n_clicks=0,
                        style={"border":"none","background":"none","cursor":"pointer",
                               "fontSize":"13px","color":"#6B6B6B"},
                    ),
                ],
            ),
            # Tab bar
            html.Div(className="chat-tabs", children=[
                html.Button("AI Assistant", id="chat-tab-btn-ai",   className="chat-tab-btn active", n_clicks=0),
                html.Button("Team Chat",    id="chat-tab-btn-team", className="chat-tab-btn",        n_clicks=0),
            ]),
            # ── AI tab ──
            html.Div(
                id="chat-tab-content-ai",
                className="chat-tab-content",
                children=[
                    html.Div(
                        id="chat-panel-body",
                        className="chat-panel-body",
                        style={"flex":"1","overflowY":"auto","padding":"12px"},
                        children=[
                            html.Div(
                                'Ask me about Sycamore\'s status, blockers, budget, or decisions'
                                ' — e.g. "what are we waiting on?" or "why was the needle shield kept?"',
                                className="chat-bubble",
                            ),
                        ],
                    ),
                    html.Div(
                        style={"padding":"10px 12px","borderTop":"1px solid #E5E3DE","display":"flex","gap":"6px"},
                        children=[
                            dcc.Input(
                                id="chat-input", type="text",
                                placeholder="Ask a question...", n_submit=0,
                                style={"flex":"1","border":"1px solid #E5E3DE","borderRadius":"6px",
                                       "padding":"7px 10px","fontSize":"13px","fontFamily":"inherit"},
                            ),
                            html.Button(
                                "Send", id="chat-send-btn", n_clicks=0,
                                style={"border":"none","background":"#1A1A1A","color":"#fff",
                                       "borderRadius":"6px","padding":"7px 14px",
                                       "fontSize":"12.5px","fontWeight":"600","cursor":"pointer"},
                            ),
                        ],
                    ),
                ],
            ),
            # ── Team tab ──
            html.Div(
                id="chat-tab-content-team",
                className="chat-tab-content",
                style={"display": "none"},
                children=[
                    html.Div(
                        style={"flex":"1","overflowY":"auto"},
                        children=[_team_msg(m) for m in _TEAM_MSGS],
                    ),
                    html.Div(
                        style={"padding":"10px 12px","borderTop":"1px solid #E5E3DE","display":"flex","gap":"6px"},
                        children=[
                            dcc.Input(
                                id="team-chat-input", type="text",
                                placeholder="Message the team...", n_submit=0,
                                style={"flex":"1","border":"1px solid #E5E3DE","borderRadius":"6px",
                                       "padding":"7px 10px","fontSize":"13px","fontFamily":"inherit"},
                            ),
                            html.Button(
                                "Send", id="team-chat-send-btn", n_clicks=0,
                                style={"border":"none","background":"#282727","color":"#fff",
                                       "borderRadius":"6px","padding":"7px 14px",
                                       "fontSize":"12.5px","fontWeight":"600","cursor":"pointer"},
                            ),
                        ],
                    ),
                ],
            ),
            # Dummy output for tab clientside callback
            html.Div(id="chat-tab-dummy", style={"display":"none"}),
        ],
    )


def canned_response(question: str) -> str:
    q = question.lower()
    if any(k in q for k in ["waiting", "blocked", "block", "outstanding"]):
        return (
            "Three items are currently waiting on Gilead: DVP Rev C approval (10 days with "
            "QA, against a 5-day target), the human factors study sign-off on participant "
            "inclusion criteria, and CO-04 budget approval for the shelf-life extension. "
            "One item is waiting on Team: the shipping simulation rig build, pending "
            "shipper carton design freeze."
        )
    if any(k in q for k in ["needle shield", "shield", "d-014", "stainless"]):
        return (
            "The team retained the stainless steel rigid needle shield over a polymer "
            "alternative. The polymer version saved ~4p per unit but 3 of 30 samples "
            "failed the removal-force test at 15N. Re-opening verification this close to "
            "DV start was not worth the saving. See Decision D-014."
        )
    if any(k in q for k in ["budget", "spend", "cost", "money", "finance", "forecast"]):
        return (
            "1.95m of the 3m budget is spent to date (1.58m fees, 0.37m M&E). "
            "We are ~4% over the phased plan. Forecast for the remaining three months "
            "(Jul-Sep 2026) is ~507k. CO-04 (86k shelf-life extension) is pending "
            "Gilead approval and not yet in committed spend."
        )
    if any(k in q for k in ["milestone", "deadline", "gate", "next", "schedule"]):
        return (
            "The next milestone is DVP protocol approval, due 25 June 2026 — currently "
            "at risk pending Gilead QA sign-off. The DV exit gate (Design Review 5) is "
            "targeted for 18 September 2026. Regulatory submission is scheduled 1 Feb 2027."
        )
    if any(k in q for k in ["who", "team", "people", "jasper", "tom", "emily"]):
        return (
            "The TC team on Sycamore: John Burke (Managing Consultant), Tom Grant (Senior "
            "Consultant, engineering lead), Emily Morley (device testing), Louis DeCleyn "
            "(quality/DHF), and Jasper Ferguson (engineering intern). Key Gilead contacts: "
            "Anita Devereux (Programme Director), James Okonkwo (device lead), Mei Lin Tan (QA)."
        )
    if any(k in q for k in ["shelf", "co-04", "ageing", "36 month"]):
        return (
            "CO-04 extends the shelf-life ageing study from 24 to 36 months, per Gilead's "
            "commercial team request. It costs 86k and needs Gilead finance approval before "
            "end of June — otherwise the next available chamber slot is September."
        )
    if any(k in q for k in ["spring", "d-012", "pre-load", "dose", "force"]):
        return (
            "Spring pre-load tolerance was tightened to +/-3% (decision D-012) after early "
            "DV pilot runs showed dose accuracy trending toward the specification limit at "
            "the original +/-5%. This is tracked as the driver of our 4% budget variance."
        )
    if any(k in q for k in ["decision", "log", "d-011", "electronics", "bluetooth", "v2"]):
        return (
            "10 programme decisions are logged. D-011 deferred Bluetooth dose-logging to V2. "
            "D-012 tightened spring tolerance. D-013 targets 36-month shelf life. D-014 "
            "confirmed the steel needle shield. Full decision tree is on the Decisions page."
        )
    if any(k in q for k in ["risk", "risk-027", "risk-021", "sterile", "barrier"]):
        return (
            "Two high-severity risks remain open: spring fatigue under worst-case grip "
            "force (RISK-021) and sterile barrier integrity post-shipping (RISK-027). "
            "Both have active mitigations in DV testing but cannot be formally closed "
            "until test reports are signed off."
        )
    if any(k in q for k in ["cad", "part", "autoinjector", "component"]):
        return (
            "The Sycamore autoinjector has 8 main components: Needle Cap, Rigid Needle "
            "Shield, Outer Housing, Drug Cartridge (1.0 mL PFS), Drive Spring, Plunger Rod, "
            "Activation Button, and End Cap. See the Engineering page for the interactive "
            "component diagram and spec sheets."
        )
    return (
        "I can help with project status, blockers, budget, milestones, decisions, "
        "team, or the autoinjector design — try asking about one of those."
    )
