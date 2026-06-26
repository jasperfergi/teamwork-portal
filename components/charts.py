"""
Plotly figure builders. All figures use consistent fonts, colours, and
margins so they look uniform across pages.

Gantt fix: Plotly horizontal bars with a date x-axis require the bar
width (x) in milliseconds. We convert days → ms via * 86_400_000.
"""

import plotly.graph_objects as go
from data.tokens import ACCENT, AMBER, GREY, LINE, INK, FONT_STACK, FORECAST

MS_PER_DAY = 86_400_000

BASE_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family=FONT_STACK, color=INK, size=12.5),
    margin=dict(l=10, r=10, t=10, b=10),
)


def gantt_figure(tasks, today=None, mode=None):
    """Horizontal bar Gantt chart. x values are in ms for date-axis bars."""
    if not tasks:
        fig = go.Figure()
        fig.update_layout(**BASE_LAYOUT, height=100)
        return fig

    tasks_sorted = sorted(tasks, key=lambda t: t["start"])
    # Category order reversed so first task appears at top
    category_order = [t["name"] for t in tasks_sorted][::-1]

    _base_color = "#BE1E2D" if mode == "client" else "#1A3F6B"

    fig = go.Figure()

    for t in tasks_sorted:
        color = _base_color

        duration_ms = (t["end"] - t["start"]).days * MS_PER_DAY

        fig.add_trace(go.Bar(
            x=[duration_ms],
            y=[t["name"]],
            base=[t["start"].isoformat()],
            orientation="h",
            marker=dict(color=color, opacity=0.85, line=dict(width=0)),
            customdata=[[t["pct_complete"], t["owner_name"],
                         t["start"].strftime("%d %b"), t["end"].strftime("%d %b %Y")]],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Owner: %{customdata[1]}<br>"
                "%{customdata[2]} → %{customdata[3]}<br>"
                "%{customdata[0]}% complete"
                "<extra></extra>"
            ),
            showlegend=False,
        ))

    n = len(tasks_sorted)
    row_height = 44
    fig.update_layout(**BASE_LAYOUT)
    fig.update_layout(height=n * row_height + 60, bargap=0.3)
    fig.update_yaxes(
        categoryorder="array",
        categoryarray=category_order,
        showgrid=False,
        tickfont=dict(size=12),
        ticksuffix="  ",
    )
    fig.update_xaxes(
        type="date",
        showgrid=True,
        gridcolor=LINE,
        tickfont=dict(size=11),
        tickformat="%b %Y",
        tickangle=0,
    )
    fig.update_layout(margin=dict(l=10, r=20, t=16, b=40))

    if today is not None:
        fig.add_vline(
            x=today.isoformat(),
            line=dict(color="#BE1E2D", width=1.5, dash="solid"),
        )

    return fig


def budget_burn_figure(monthly_burn, monthly_forecast=None, accent=ACCENT):
    """Stacked bar of fees + M&E actual spend, with optional forecast bars."""
    months_actual = [m[0] for m in monthly_burn]
    fees_actual = [m[1] for m in monthly_burn]
    me_actual = [m[2] for m in monthly_burn]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months_actual, y=fees_actual, name="Fees (actual)",
        marker_color=accent, marker_opacity=0.9,
    ))
    fig.add_trace(go.Bar(
        x=months_actual, y=me_actual, name="M&E (actual)",
        marker_color="#9FB3C2", marker_opacity=0.9,
    ))

    if monthly_forecast:
        months_fc = [m[0] for m in monthly_forecast]
        fees_fc = [m[1] for m in monthly_forecast]
        me_fc = [m[2] for m in monthly_forecast]
        fig.add_trace(go.Bar(
            x=months_fc, y=fees_fc, name="Fees (forecast)",
            marker_color=FORECAST, marker_opacity=0.7,
            marker_pattern_shape="/",
        ))
        fig.add_trace(go.Bar(
            x=months_fc, y=me_fc, name="M&E (forecast)",
            marker_color="#C4AACC", marker_opacity=0.7,
            marker_pattern_shape="/",
        ))

    fig.update_layout(**BASE_LAYOUT)
    fig.update_layout(
        barmode="stack",
        height=320,
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="left", x=0, font=dict(size=11),
        ),
        margin=dict(l=10, r=10, t=44, b=60),
    )
    fig.update_yaxes(showgrid=True, gridcolor=LINE, tickprefix="£", tickfont=dict(size=11))
    fig.update_xaxes(showgrid=False, tickfont=dict(size=10), tickangle=-45)
    return fig


def budget_donut_figure(spent, remaining, accent=ACCENT):
    pct = round(100 * spent / (spent + remaining))
    fig = go.Figure(data=[go.Pie(
        labels=["Spent", "Remaining"],
        values=[spent, remaining],
        hole=0.70,
        marker=dict(colors=[accent, "#EDEBE6"]),
        textinfo="none",
        sort=False,
        hovertemplate="%{label}: £%{value:,.0f}<extra></extra>",
    )])
    fig.update_layout(**BASE_LAYOUT)
    fig.update_layout(height=180, showlegend=False, margin=dict(l=0, r=0, t=0, b=0))
    fig.add_annotation(
        text=f"<b>{pct}%</b><br><span style='font-size:11px;color:{GREY}'>spent</span>",
        showarrow=False, font=dict(size=20, color=INK),
    )
    return fig


def milestone_timeline_figure(milestones, today):
    from data.tokens import STATUS_COLORS

    milestones_sorted = sorted(milestones, key=lambda m: m["date"])
    dates = [m["date"] for m in milestones_sorted]
    names = [m["name"] for m in milestones_sorted]
    colors = [STATUS_COLORS.get(m["status"], GREY) for m in milestones_sorted]
    n = len(milestones_sorted)

    # Place markers on staggered y-rows so labels never overlap.
    # Use 4 rows cycling top-to-bottom with increasing offsets.
    row_offsets = [0.55, 0.20, -0.20, -0.55]
    y_pos = [row_offsets[i % len(row_offsets)] for i in range(n)]

    fig = go.Figure()

    # Baseline
    fig.add_trace(go.Scatter(
        x=[min(dates), max(dates)], y=[0, 0], mode="lines",
        line=dict(color=LINE, width=1.5), showlegend=False, hoverinfo="skip",
    ))

    # Vertical stems from baseline to marker
    for i, (d, y) in enumerate(zip(dates, y_pos)):
        fig.add_shape(
            type="line",
            x0=d.isoformat(), x1=d.isoformat(),
            y0=0, y1=y * 0.85,
            line=dict(color=colors[i], width=1, dash="dot"),
        )

    # Markers
    fig.add_trace(go.Scatter(
        x=dates, y=y_pos,
        mode="markers+text",
        marker=dict(size=11, color=colors, line=dict(width=2, color="white")),
        text=names,
        textposition=["top center" if y >= 0 else "bottom center" for y in y_pos],
        textfont=dict(size=10, color=GREY),
        customdata=[[m["date"].strftime("%d %b %Y"), m["status"]] for m in milestones_sorted],
        hovertemplate="<b>%{text}</b><br>%{customdata[0]}<br>%{customdata[1]}<extra></extra>",
        showlegend=False,
        cliponaxis=False,
    ))

    fig.add_vline(x=today.isoformat(), line=dict(color=INK, width=1.5, dash="dot"))
    fig.add_annotation(
        x=today.isoformat(), y=0.96, text="Today",
        showarrow=False, font=dict(size=10, color=INK), yref="paper",
    )

    fig.update_layout(**BASE_LAYOUT)
    fig.update_yaxes(visible=False, range=[-0.95, 0.95])
    fig.update_xaxes(showgrid=False, tickfont=dict(size=11), tickformat="%b %Y")
    fig.update_layout(height=260, margin=dict(l=10, r=10, t=20, b=30))
    return fig


def allocation_bar_figure(people, accent=ACCENT):
    people_sorted = sorted(people, key=lambda p: -p["allocation_pct"])
    names = [p["name"] for p in people_sorted][::-1]
    pct = [p["allocation_pct"] for p in people_sorted][::-1]
    roles = [p["role"] for p in people_sorted][::-1]
    colors = []
    for p in people_sorted[::-1]:
        if p["status"] == "rolling_off":
            colors.append(AMBER)
        elif p["status"] == "rolling_on":
            colors.append("#9FB3C2")
        else:
            colors.append(accent)

    fig = go.Figure(go.Bar(
        x=pct, y=names, orientation="h",
        marker=dict(color=colors, opacity=0.85),
        customdata=roles,
        hovertemplate="%{y} — %{customdata}<br>%{x}% allocated<extra></extra>",
    ))
    fig.update_layout(**BASE_LAYOUT)
    fig.update_xaxes(
        range=[0, 110], showgrid=True, gridcolor=LINE,
        ticksuffix="%", tickfont=dict(size=11),
    )
    fig.update_yaxes(showgrid=False, tickfont=dict(size=11.5))
    fig.update_layout(height=max(180, 34 * len(people_sorted) + 40),
                      margin=dict(l=10, r=20, t=10, b=30))
    return fig
