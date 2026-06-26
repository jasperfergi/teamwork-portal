"""
Teamwork Portal — Project Sycamore (Gilead) · Team Consulting

Run with:
    python app.py
then open the URL printed in the terminal from any device on the same network.

host='0.0.0.0' makes the server reachable from phones, tablets, and other
laptops on the same network — find your machine's local IP (e.g. 192.168.1.x)
and navigate to http://<your-ip>:8050 on any device.
"""

from dash import Dash, dcc, html, Input, Output, State, page_container, ctx, no_update, ALL

from components.shell import topbar, sidenav, _TC_PROJECTS, _GILEAD_PROJECTS
from components.chat import chat_fab, chat_panel, canned_response
from data.synthetic_data import PROJECT

app = Dash(
    __name__,
    use_pages=True,
    pages_folder="pages",
    title="Teamwork Portal · Project Sycamore",
    suppress_callback_exceptions=True,
)

# Message stores — separate per side (in-session only)
_internal_msg_store = dcc.Store(id="internal-msg-store", data=[], storage_type="memory")
_gilead_msg_store = dcc.Store(id="gilead-msg-store", data=[], storage_type="memory")
# Comments store (in-session only)
_comments_store = dcc.Store(id="comments-store", data={}, storage_type="memory")
# AI panel expanded state
_ai_expanded_store = dcc.Store(id="ai-expanded-store", data=False, storage_type="memory")

app.layout = html.Div(
    id="app-root",
    children=[
        dcc.Location(id="url"),
        dcc.Store(id="view-mode-store", data="team", storage_type="memory"),
        _internal_msg_store,
        _gilead_msg_store,
        _comments_store,
        _ai_expanded_store,
        dcc.Store(id="pm-tab-store", data="programme", storage_type="memory"),
        topbar(PROJECT["name"], PROJECT["phase"]),
        html.Div(id="sidenav-container"),
        html.Div(page_container, className="main-content"),
        chat_fab(),
        chat_panel(),
        html.Div(id="body-class-sync", style={"display": "none"}),
    ],
)

# ---------------------------------------------------------------------------
# Mode toggle — two-button pill, active button fills with brand colour
# ---------------------------------------------------------------------------

@app.callback(
    Output("view-mode-store", "data"),
    Output("mode-btn-team", "className"),
    Output("mode-btn-client", "className"),
    Input("mode-btn-team", "n_clicks"),
    Input("mode-btn-client", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_mode(_team, _client):
    if ctx.triggered_id == "mode-btn-team":
        return "team", "active team", ""
    return "client", "", "active client"


@app.callback(
    Output("project-switcher", "children"),
    Output("project-switcher", "value"),
    Input("view-mode-store", "data"),
)
def update_project_switcher(mode):
    projects = _TC_PROJECTS if mode == "team" else _GILEAD_PROJECTS
    options = [html.Option(p, value=p) for p in projects]
    return options, projects[0]


app.clientside_callback(
    """
    function(mode) {
        if (mode === "client") {
            document.body.classList.add("client-mode");
        } else {
            document.body.classList.remove("client-mode");
        }
        return "";
    }
    """,
    Output("body-class-sync", "children"),
    Input("view-mode-store", "data"),
)

# ---------------------------------------------------------------------------
# Side nav: highlight active link on route change
# ---------------------------------------------------------------------------

_PATH_TO_KEY = {
    "/dashboard": "dashboard",
    "/": "overview",
    "/project-management": "pm",
    "/finance": "finance",
    "/engineering": "engineering",
    "/files": "files",
    "/team": "team",
    "/decisions": "decisions",
    "/chat": "chat",
}


@app.callback(
    Output("sidenav-container", "children"),
    Input("url", "pathname"),
)
def render_sidenav(pathname):
    active_key = _PATH_TO_KEY.get(pathname, "overview")
    return sidenav(active_key)


# ---------------------------------------------------------------------------
# Transparency panel toggle (team mode only)
# ---------------------------------------------------------------------------

@app.callback(
    Output("transparency-panel", "style"),
    Input("transparency-toggle-btn", "n_clicks"),
    State("transparency-panel", "style"),
    prevent_initial_call=True,
)
def toggle_transparency_panel(n, current_style):
    is_hidden = (current_style or {}).get("display") == "none"
    return {"display": "block"} if is_hidden else {"display": "none"}


@app.callback(
    Output("transparency-panel-wrapper", "style"),
    Input("view-mode-store", "data"),
)
def show_transparency_in_team_mode(mode):
    return {"display": "flex", "position": "relative"} if mode == "team" else {"display": "none"}


# ---------------------------------------------------------------------------
# AI overview expand / collapse (pattern-match callback)
# ---------------------------------------------------------------------------

@app.callback(
    Output({"type": "ai-detail", "index": ALL}, "style"),
    Output({"type": "ai-expand-btn", "index": ALL}, "children"),
    Input({"type": "ai-expand-btn", "index": ALL}, "n_clicks"),
    State({"type": "ai-detail", "index": ALL}, "style"),
    prevent_initial_call=True,
)
def toggle_ai_detail(n_clicks_list, styles):
    out_styles = []
    out_labels = []
    for n, style in zip(n_clicks_list, styles):
        is_hidden = (style or {}).get("display") == "none"
        if is_hidden:
            out_styles.append({"display": "block"})
            out_labels.append("Hide full analysis ▴")
        else:
            out_styles.append({"display": "none"})
            out_labels.append("Show full analysis ▾")
    return out_styles, out_labels


# ---------------------------------------------------------------------------
# AI chat widget
# ---------------------------------------------------------------------------

@app.callback(
    Output("chat-panel", "style"),
    Input("chat-fab-btn", "n_clicks"),
    Input("chat-close-btn", "n_clicks"),
    State("chat-panel", "style"),
    prevent_initial_call=True,
)
def toggle_chat(fab_clicks, close_clicks, current_style):
    if ctx.triggered_id == "chat-close-btn":
        return {"display": "none"}
    is_hidden = (current_style or {}).get("display") == "none"
    return {"display": "flex"} if is_hidden else {"display": "none"}


@app.callback(
    Output("chat-panel-body", "children"),
    Output("chat-input", "value"),
    Input("chat-send-btn", "n_clicks"),
    Input("chat-input", "n_submit"),
    State("chat-input", "value"),
    State("chat-panel-body", "children"),
    prevent_initial_call=True,
)
def send_chat_message(send_clicks, n_submit, question, current_children):
    if not question or not question.strip():
        return no_update, no_update
    current_children = current_children or []
    answer = canned_response(question)
    new_children = current_children + [
        html.Div(question, className="chat-bubble user"),
        html.Div(answer, className="chat-bubble"),
    ]
    return new_children, ""


app.clientside_callback(
    """
    function(ai_clicks, team_clicks) {
        var triggeredId = window.dash_clientside.callback_context.triggered[0].prop_id;
        var aiContent   = document.getElementById('chat-tab-content-ai');
        var teamContent = document.getElementById('chat-tab-content-team');
        var aiBtn       = document.getElementById('chat-tab-btn-ai');
        var teamBtn     = document.getElementById('chat-tab-btn-team');
        if (!aiContent || !teamContent) return '';
        if (triggeredId.includes('chat-tab-btn-team')) {
            aiContent.style.display   = 'none';
            teamContent.style.display = 'flex';
            aiBtn.classList.remove('active');
            teamBtn.classList.add('active');
        } else {
            aiContent.style.display   = 'flex';
            teamContent.style.display = 'none';
            aiBtn.classList.add('active');
            teamBtn.classList.remove('active');
        }
        return '';
    }
    """,
    Output("chat-tab-dummy", "children"),
    Input("chat-tab-btn-ai",   "n_clicks"),
    Input("chat-tab-btn-team", "n_clicks"),
    prevent_initial_call=True,
)


if __name__ == "__main__":
    import os, socket
    port = int(os.environ.get("PORT", 8050))
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = "your-local-ip"
    print(f"\n  Teamwork Portal running at:")
    print(f"  Local:   http://127.0.0.1:{port}")
    print(f"  Network: http://{local_ip}:{port}\n")
    app.run(debug=False, host="0.0.0.0", port=port)
