"""
Design tokens for the Teamwork Portal.

Visual identity derived from Team Consulting's brand: editorial,
restrained, sans-only on an off-white ground with charcoal text.
Slate-blue accent for interactive elements; amber for attention states.
"""

# Colour palette -------------------------------------------------------
INK = "#1A1A1A"
INK_SOFT = "#4A4A48"
GREY = "#6B6B6B"
PAPER = "#FAFAF8"
SURFACE = "#FFFFFF"
LINE = "#E5E3DE"
ACCENT = "#003057"          # Team Consulting navy
ACCENT_SOFT = "#E5EBF2"
TEAM_BAR = "#282727"        # Team Consulting off-black (brand bars)
CLIENT_ACCENT = "#d63346"   # Gilead red (brand)
GILEAD_BAR = "#d63346"      # Gilead brand bar colour
CLIENT_ACCENT_SOFT = "#FBECEE"
AMBER = "#C17817"
AMBER_SOFT = "#F8EBD8"
GOOD = "#3E6B4F"
GOOD_SOFT = "#E8EFE9"
FORECAST = "#8B6E9A"       # purple — forecast bars in budget chart

# Typography -------------------------------------------------------------
FONT_STACK = "-apple-system, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO_STACK = "'SF Mono', 'Roboto Mono', Consolas, monospace"

# Spacing scale (px) -----------------------------------------------------
SPACE = {"xs": 4, "sm": 8, "md": 16, "lg": 24, "xl": 40, "xxl": 64}

# Sector / page navigation -----------------------------------------------
SECTORS = [
    {"key": "dashboard",    "label": "My Dashboard",        "path": "/dashboard"},
    {"key": "overview",     "label": "Overview",            "path": "/"},
    {"key": "pm",           "label": "Project Management",  "path": "/project-management"},
    {"key": "finance",      "label": "Finance",             "path": "/finance"},
    {"key": "engineering",  "label": "Engineering",         "path": "/engineering"},
    {"key": "files",        "label": "Files",               "path": "/files"},
    {"key": "team",         "label": "Team",                "path": "/team"},
    {"key": "decisions",    "label": "Decisions",           "path": "/decisions"},
    {"key": "chat",         "label": "Chat",                "path": "/chat"},
]

STATUS_COLORS = {
    "on_track": GOOD, "complete": GOOD, "in_progress": ACCENT,
    "at_risk": AMBER, "not_started": GREY, "Approved": GOOD,
    "Pending approval": AMBER, "Withdrawn": GREY, "Paid": GOOD,
    "Draft — not yet issued": GREY, "Final": GOOD,
    "Awaiting client approval": AMBER, "In progress": ACCENT,
}
