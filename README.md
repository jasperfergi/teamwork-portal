# Teamwork Portal — Project Nefertari demonstration

A demonstration dashboard for Team Consulting, showing what a shared,
transparent collaboration space with a client (Kameo Therapeutics)
could look like for a medical device programme. Built with
[Dash](https://dash.plotly.com/) so you get full control of the look
and feel rather than a generic component library.

## Running it in VS Code

1. Open this folder in VS Code (`File > Open Folder…`).
2. Open a terminal (`` Ctrl+` ``) and create a virtual environment
   (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # on Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open the URL shown in the terminal — normally
   **http://127.0.0.1:8050** — in your browser.

`debug=True` is on in `app.py`, so the app will auto-reload whenever
you save a file change, which is convenient while you're tweaking
content or styling.

## What's in here

```
app.py                  Entry point: shell layout, mode toggle, side nav, AI chat widget
data/
  synthetic_data.py      All Project Nefertari / Kameo content — edit this to change the story
  tokens.py              Colour palette, fonts, sector list
components/
  shell.py               Top bar, side nav, cards, badges, AI overview panel
  chat.py                Floating AI chat widget + canned responses
  charts.py              Plotly figure builders (Gantt, budget, milestones, allocation)
pages/
  overview.py            "/" — minimal home dashboard
  project_management.py  "/project-management" — timeline, decisions, files, people
  finance.py              "/finance" — budget, burn, change orders, invoices
  engineering.py          "/engineering" — DV test execution detail
  quality.py              "/quality" — risk register, DV protocol, DHF
assets/
  style.css              All visual styling (Dash auto-loads anything in /assets)
  img/team_logo.png       Team Consulting logo, extracted from your brief
```

## The two things worth clicking on first

1. **The mode toggle**, top right — switches between "Team Consulting"
   and "Kameo (Client)" view. Most content is shared (that's the
   point), but a few things are genuinely internal-only and
   disappear in client mode:
   - The AI overview text on the homepage (same facts, written for
     the audience)
   - The "Internal forecast note" on the Finance page
   - The risk register's "Working note" on the Quality page
   - The "Internal note" on each decision card on the Project
     Management page

   Each of these is tagged with a small grey **Internal only** pill
   so it's obvious in Team mode which things wouldn't be shown to
   Kameo.

2. **The AI chat widget**, bottom right — a stand-in for a live
   model call. It answers a handful of canned questions (try "what
   are we waiting on?" or "why was the needle shield decision made?")
   by pattern-matching against the same synthetic data driving the
   rest of the dashboard. Swapping this for a real LLM call later
   would mean replacing `canned_response()` in `components/chat.py`
   with an actual API call — the UI plumbing is already in place.

## Editing the story

Everything about Project Nefertari — people, tasks, decisions,
budget, files — lives in `data/synthetic_data.py`. If you want to
change a number, add a person, or write a new decision, that's the
only file you need to touch; every page reads from it.

One thing worth knowing if you do edit the budget numbers: the
`monthly_burn` list is built to sum exactly to `fees_spent` and
`me_spent` further up in the same file. If you change one, the other
will look inconsistent on the Finance page unless you update both.

## Known limitations (this is a demo, not a real product)

- All file/SharePoint links are synthetic — they point at fake URLs
  and won't load anything if clicked.
- The AI overview and chatbot are pre-written, not live model calls.
- There's no real authentication — the mode toggle is just a UI
  state, not an actual permissions system.
- Data lives in Python dictionaries in memory; nothing persists
  between runs or is shared between browser tabs.
