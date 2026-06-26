"""
My Dashboard — personal view for Jasper Ferguson (T05).
"""

import dash
from dash import html

from components.shell import page_header, card
from data.synthetic_data import TEAM_PEOPLE

dash.register_page(__name__, path="/dashboard", name="My Dashboard")

_ME = next(p for p in TEAM_PEOPLE if p["id"] == "T05")

_SCHEDULE = [
    {"time": "09:30", "event": "DV Programme Standup", "type": "meeting", "who": "Full team · Conference Room B"},
    {"time": "11:00", "event": "Spring Force Tolerance Tests", "type": "task",    "who": "Lab 3 · with Emily Morley"},
    {"time": "14:00", "event": "1:1 with Tom Grant",          "type": "meeting", "who": "Tom Grant · his office"},
    {"time": "16:00", "event": "HF Protocol Review",          "type": "meeting", "who": "Sofia Alvarez · remote"},
]

_ACTIONS = [
    {"priority": "high",  "text": "DVP Rev C with Gilead QA for 10 days — 5-day review target exceeded",      "tag": "Gilead pending"},
    {"priority": "today", "text": "Spring force tolerance test report due for sign-off — run scheduled 11:00", "tag": "Due today"},
    {"priority": "info",  "text": "CO-04 shelf-life extension needs Gilead finance approval by end of June",   "tag": "Action needed"},
]

_FILES = [
    {"name": "Spring Force Test Protocol v3.2",  "type": "PDF",     "updated": "Yesterday",  "status": "In review"},
    {"name": "DV Pilot Test Report v2.1",        "type": "PDF",     "updated": "21 Jun",     "status": "Draft"},
    {"name": "Component Spec — Drive Spring",    "type": "Drawing", "updated": "18 Jun",     "status": "Draft"},
    {"name": "Risk Register v8",                 "type": "Excel",   "updated": "20 Jun",     "status": "Final"},
]

_ACTIVITY = [
    {"who": "Mei Lin Tan",   "action": "queried acceptance criteria on DVP Rev C",           "when": "Today, 08:47",    "photo": None},
    {"who": "Tom Grant",     "action": "updated spring force test protocol to v3.2",         "when": "Yesterday, 17:23","photo": "/assets/img/tom_grant.jpg"},
    {"who": "Emily Morley",  "action": "completed 50,000-cycle spring fatigue test run",     "when": "21 Jun, 14:30",   "photo": "/assets/img/emily_morley.jpg"},
    {"who": "Louis DeCleyn", "action": "submitted risk register v8 for Gilead QA review",   "when": "20 Jun, 11:05",   "photo": "/assets/img/louis_decleyn.jpg"},
    {"who": "John Burke",    "action": "circulated CO-04 shelf-life extension change order", "when": "19 Jun, 09:30",   "photo": "/assets/img/john_burke.jpg"},
]


def layout():
    return html.Div([
        # Greeting banner
        html.Div(className="dash-greeting-banner", children=[
            html.Div(className="dash-greeting-left", children=[
                html.Img(src=_ME["photo"], className="dash-user-photo"),
                html.Div([
                    html.Div("Good morning, Jasper", className="dash-greeting-text"),
                    html.Div(f"{_ME['role']} · Project Sycamore", className="dash-greeting-sub"),
                ]),
            ]),
            html.Div("Monday, 23 June 2026", className="dash-greeting-date"),
        ]),

        # Quick stats
        html.Div(className="dash-stats-row", children=[
            _stat("3",       "Action items",  "/project-management"),
            _stat("4",       "Active files",  "/files"),
            _stat("100%",    "Allocated",     "/project-management"),
            _stat("87 days", "To DV exit",    "/decisions"),
        ]),

        # Four-card grid — each card is a direct grid child so rows align
        html.Div(className="dash-grid", children=[
            card(
                "What I need to know",
                html.Div([_action(a) for a in _ACTIONS]),
                title_right=html.A("View action log →", href="/project-management", className="dash-card-link"),
            ),
            card("Today's schedule — 23 June", html.Div([_sched_row(s) for s in _SCHEDULE])),
            card(
                "Active files",
                html.Div([_file_row(f) for f in _FILES]),
                title_right=html.A("View all →", href="/files", className="dash-card-link"),
            ),
            card("Recent activity", html.Div([_activity_row(a) for a in _ACTIVITY])),
        ]),
    ])


def _stat(value, label, href=None):
    content = html.Div(className="dash-stat", children=[
        html.Div(value, className="dash-stat-value"),
        html.Div(label, className="dash-stat-label"),
    ])
    if href:
        return html.A(href=href, className="dash-stat-link", children=content)
    return content


def _action(item):
    cls = {"high": "dash-action-high", "today": "dash-action-today", "info": "dash-action-info"}.get(item["priority"], "dash-action-info")
    return html.Div(className=f"dash-action-item {cls}", children=[
        html.Div(item["text"], className="dash-action-text"),
        html.Span(item["tag"], className="dash-action-tag"),
    ])


def _file_row(f):
    return html.Div(className="dash-file-row", children=[
        html.Div(className="dash-file-info", children=[
            html.Div(f["name"], className="dash-file-name"),
            html.Div(f"Updated {f['updated']}", className="dash-file-meta"),
        ]),
        html.Span(f["status"], className="dash-file-status"),
    ])


def _sched_row(s):
    dot_cls = "dash-sched-meeting" if s["type"] == "meeting" else "dash-sched-task"
    return html.Div(className="dash-sched-row", children=[
        html.Div(s["time"], className="dash-sched-time"),
        html.Div(className=f"dash-sched-dot {dot_cls}"),
        html.Div([
            html.Div(s["event"], className="dash-sched-event"),
            html.Div(s["who"],   className="dash-sched-who"),
        ]),
    ])


def _activity_row(a):
    initials = "".join(p[0] for p in a["who"].split()[:2])
    if a.get("photo"):
        avatar = html.Img(src=a["photo"], className="dash-activity-avatar")
    else:
        avatar = html.Div(initials, className="dash-activity-avatar dash-activity-initials")
    return html.Div(className="dash-activity-row", children=[
        avatar,
        html.Div([
            html.Span(a["who"],    className="dash-activity-who"),
            html.Span(f" {a['action']}", className="dash-activity-text"),
            html.Div(a["when"],   className="dash-activity-when"),
        ]),
    ])
