"""
Synthetic project data for the Teamwork Portal demonstration.

Project Sycamore: a disposable autoinjector being developed for
Gilead (fictional client), currently preparing for Design Verification (DV).
All data below is fabricated for demonstration purposes but designed to be
plausible to medical device development professionals.
"""

from datetime import date

# ---------------------------------------------------------------------------
# Project metadata
# ---------------------------------------------------------------------------

PROJECT = {
    "name": "Project Sycamore",
    "client": "Gilead",
    "device": "Single-use autoinjector, 1.0 mL prefilled syringe platform",
    "phase": "Design Verification",
    "budget_total": 3_000_000,
    "start_date": date(2025, 1, 13),
    "target_dv_complete": date(2026, 9, 18),
    "target_submission": date(2027, 2, 1),
    "today": date(2026, 6, 22),
    "description": (
        "Sycamore is a single-use, spring-driven autoinjector developed for "
        "Gilead to deliver a 1.0 mL subcutaneous biologic for "
        "rheumatoid arthritis. The programme is currently in Design "
        "Verification, with formal DV testing underway against the finalised "
        "Design Output Specification following design freeze in Q1 2026."
    ),
}

# ---------------------------------------------------------------------------
# People — Team Consulting side and Gilead side
# ---------------------------------------------------------------------------

TEAM_PEOPLE = [
    {"id": "T01", "name": "John Burke", "role": "Managing Consultant", "discipline": "Project Management",
     "photo": "/assets/img/john_burke.jpg",
     "allocation_pct": 60, "status": "active", "on_since": date(2025, 1, 13), "off_date": None},
    {"id": "T02", "name": "Tom Grant", "role": "Senior Consultant", "discipline": "Engineering",
     "photo": "/assets/img/tom_grant.jpg",
     "allocation_pct": 80, "status": "active", "on_since": date(2025, 1, 13), "off_date": None},
    {"id": "T03", "name": "Emily Morley", "role": "Senior Device Testing Consultant", "discipline": "Engineering",
     "photo": "/assets/img/emily_morley.jpg",
     "allocation_pct": 100, "status": "active", "on_since": date(2025, 3, 3), "off_date": None},
    {"id": "T04", "name": "Louis DeCleyn", "role": "Graduate Industrial Designer", "discipline": "Quality",
     "photo": "/assets/img/louis_decleyn.jpg",
     "allocation_pct": 50, "status": "active", "on_since": date(2025, 1, 13), "off_date": None},
    {"id": "T05", "name": "Jasper Ferguson", "role": "Mechanical Engineering Intern", "discipline": "Engineering",
     "photo": "/assets/img/jasper_ferguson.jpg",
     "allocation_pct": 100, "status": "active", "on_since": date(2026, 4, 6), "off_date": None},
]

CLIENT_PEOPLE = [
    {"id": "G01", "name": "Anita Devereux", "role": "Programme Director", "discipline": "Project Management",
     "photo": "/assets/img/g_anita_devereux.svg",
     "allocation_pct": 40, "status": "active", "on_since": date(2025, 1, 13), "off_date": None},
    {"id": "G02", "name": "James Okonkwo", "role": "Device Development Lead", "discipline": "Engineering",
     "photo": "/assets/img/g_james_okonkwo.svg",
     "allocation_pct": 70, "status": "active", "on_since": date(2025, 1, 13), "off_date": None},
    {"id": "G03", "name": "Mei Lin Tan", "role": "QA Manager", "discipline": "Quality",
     "photo": "/assets/img/g_mei_lin_tan.svg",
     "allocation_pct": 50, "status": "active", "on_since": date(2025, 2, 10), "off_date": None},
    {"id": "G04", "name": "Robert FitzGerald", "role": "Regulatory Affairs Manager", "discipline": "Quality",
     "photo": "/assets/img/g_robert_fitzgerald.svg",
     "allocation_pct": 25, "status": "active", "on_since": date(2025, 9, 1), "off_date": None},
    {"id": "G05", "name": "Sofia Alvarez", "role": "Clinical & HF Liaison", "discipline": "Engineering",
     "photo": "/assets/img/g_sofia_alvarez.svg",
     "allocation_pct": 15, "status": "active", "on_since": date(2026, 1, 12), "off_date": None},
]

# ---------------------------------------------------------------------------
# Gantt / task data
# ---------------------------------------------------------------------------

TASKS = [
    {"id": "WP1.1", "name": "DVP & protocol approval", "sector": "Engineering",
     "owner_team": "client", "owner_name": "Mei Lin Tan",
     "start": date(2026, 4, 20), "end": date(2026, 6, 25),
     "pct_complete": 85, "status": "in_progress", "waiting_on": "client",
     "waiting_note": "Awaiting Gilead QA sign-off on DVP Rev C (submitted 12 Jun)."},
    {"id": "WP1.2", "name": "Spring force — DV test execution", "sector": "Engineering",
     "owner_team": "team", "owner_name": "Daniel Osei",
     "start": date(2026, 5, 18), "end": date(2026, 7, 10),
     "pct_complete": 55, "status": "in_progress", "waiting_on": None,
     "waiting_note": None},
    {"id": "WP1.3", "name": "Needle insertion depth — DV test", "sector": "Engineering",
     "owner_team": "team", "owner_name": "Daniel Osei",
     "start": date(2026, 6, 1), "end": date(2026, 7, 24),
     "pct_complete": 30, "status": "in_progress", "waiting_on": None,
     "waiting_note": None},
    {"id": "WP1.4", "name": "Dose accuracy — DV test execution", "sector": "Engineering",
     "owner_team": "team", "owner_name": "Priya Nadarajah",
     "start": date(2026, 6, 8), "end": date(2026, 8, 7),
     "pct_complete": 15, "status": "in_progress", "waiting_on": None,
     "waiting_note": None},
    {"id": "WP1.5", "name": "Shipping & transit simulation", "sector": "Engineering",
     "owner_team": "team", "owner_name": "Oliver Bancroft",
     "start": date(2026, 7, 1), "end": date(2026, 8, 21),
     "pct_complete": 0, "status": "not_started", "waiting_on": "team",
     "waiting_note": "Awaiting final shipper carton design freeze before rig build."},
    {"id": "WP1.6", "name": "Sterile barrier integrity testing", "sector": "Engineering",
     "owner_team": "team", "owner_name": "Sarah Quinn",
     "start": date(2026, 6, 15), "end": date(2026, 7, 31),
     "pct_complete": 10, "status": "in_progress", "waiting_on": "client",
     "waiting_note": "Awaiting sterilisation dose mapping report from Gilead's contract steriliser."},
    {"id": "WP1.7", "name": "Human factors validation protocol", "sector": "Engineering",
     "owner_team": "team", "owner_name": "Lucy Fenwick",
     "start": date(2026, 5, 4), "end": date(2026, 6, 19),
     "pct_complete": 95, "status": "in_progress", "waiting_on": "client",
     "waiting_note": "Awaiting Gilead clinical sign-off on participant inclusion criteria."},
    {"id": "WP1.8", "name": "Risk file (ISO 14971) — DV update", "sector": "Project Management",
     "owner_team": "team", "owner_name": "Sarah Quinn",
     "start": date(2026, 4, 1), "end": date(2026, 6, 30),
     "pct_complete": 70, "status": "in_progress", "waiting_on": None,
     "waiting_note": None},
    {"id": "WP1.9", "name": "DHF compilation — DV section", "sector": "Project Management",
     "owner_team": "team", "owner_name": "Marcus Webb",
     "start": date(2026, 6, 1), "end": date(2026, 9, 18),
     "pct_complete": 20, "status": "in_progress", "waiting_on": None,
     "waiting_note": None},
    {"id": "WP1.10", "name": "Budget re-forecast & change order", "sector": "Finance",
     "owner_team": "client", "owner_name": "Anita Devereux",
     "start": date(2026, 6, 10), "end": date(2026, 6, 26),
     "pct_complete": 40, "status": "in_progress", "waiting_on": "client",
     "waiting_note": "Awaiting Gilead finance approval of CO-04."},
    {"id": "WP1.11", "name": "DV test report compilation", "sector": "Engineering",
     "owner_team": "team", "owner_name": "Priya Nadarajah",
     "start": date(2026, 8, 10), "end": date(2026, 9, 11),
     "pct_complete": 0, "status": "not_started", "waiting_on": None,
     "waiting_note": None},
    {"id": "WP1.12", "name": "Design review 5 (DV exit gate)", "sector": "Project Management",
     "owner_team": "team", "owner_name": "Helen Marsh",
     "start": date(2026, 9, 14), "end": date(2026, 9, 18),
     "pct_complete": 0, "status": "not_started", "waiting_on": None,
     "waiting_note": None},
]

MILESTONES = [
    {"name": "Design freeze", "date": date(2026, 3, 6), "status": "complete"},
    {"name": "DV protocol approval", "date": date(2026, 6, 25), "status": "at_risk"},
    {"name": "Sterile barrier complete", "date": date(2026, 7, 31), "status": "on_track"},
    {"name": "HF validation study", "date": date(2026, 8, 14), "status": "on_track"},
    {"name": "DV execution complete", "date": date(2026, 8, 21), "status": "on_track"},
    {"name": "Design review 5", "date": date(2026, 9, 18), "status": "on_track"},
    {"name": "Regulatory submission", "date": date(2027, 2, 1), "status": "on_track"},
]

# ---------------------------------------------------------------------------
# Decisions log — used in decision tree page
# ---------------------------------------------------------------------------

DECISIONS = [
    {
        "id": "D-014",
        "title": "Retain stainless steel needle shield",
        "date": date(2026, 5, 22),
        "sector": "Engineering",
        "made_by": "Joint — Design Review 4",
        "signed_off_by": "Helen Marsh / Anita Devereux",
        "context": (
            "Polymer shield offered ~£0.04/unit cost saving at the forecast volume, but "
            "introduced a particulate risk in shield-removal force testing (3 of 30 samples "
            "exceeded the 15N upper specification limit)."
        ),
        "decision": (
            "Retain the stainless steel rigid needle shield (RNS) design carried forward from "
            "the feasibility build. Cost saving does not justify re-opening verification testing "
            "this close to DV start."
        ),
        "consequence": "No change to DV test plan. Tooling for polymer variant de-scoped from CO-03.",
        "internal_note": (
            "Gilead's procurement team raised this again informally in the May steering call — "
            "worth being ready to re-explain the failure data simply if it resurfaces, since the "
            "unit cost saving is the kind of number that travels up to their CFO without the "
            "test context attached."
        ),
        "children": ["D-013"],
    },
    {
        "id": "D-013",
        "title": "Shelf-life ageing study extended to 36 months",
        "date": date(2026, 6, 10),
        "sector": "Engineering",
        "made_by": "Gilead — Anita Devereux",
        "signed_off_by": "Anita Devereux",
        "context": (
            "Gilead's commercial team requested a 36-month shelf-life claim to align with "
            "competitor labelling, exceeding the 24-month claim in the original DVP."
        ),
        "decision": (
            "Extend real-time ageing study to 36 months; add accelerated ageing arm at 40°C/75% "
            "RH to support an interim claim while real-time data matures."
        ),
        "consequence": "Raised as Change Order CO-04, pending Gilead finance approval (see budget).",
        "internal_note": (
            "If CO-04 isn't approved by end of June, the accelerated ageing arm slips a full "
            "chamber-booking cycle (next slot isn't until September) — flag this deadline "
            "explicitly in the next steering update rather than letting it sit as a line item."
        ),
        "children": [],
    },
    {
        "id": "D-012",
        "title": "Spring pre-load tolerance tightened to ±3%",
        "date": date(2026, 4, 30),
        "sector": "Engineering",
        "made_by": "Team — Priya Nadarajah",
        "signed_off_by": "Priya Nadarajah / Helen Marsh",
        "context": (
            "Early DV pilot runs (n=10) showed dose accuracy variance trending toward the "
            "specification boundary at the original ±5% spring pre-load tolerance."
        ),
        "decision": (
            "Tighten incoming spring pre-load acceptance tolerance to ±3% and add a 100% "
            "incoming inspection step for the DV test article batch."
        ),
        "consequence": "No DV timeline impact; flagged as a recommendation for pilot-line incoming QC.",
        "internal_note": (
            "This is the change driving the 4% forecast variance noted on the Finance page — "
            "worth keeping an eye on whether the tighter tolerance becomes a supplier cost "
            "conversation at pilot-line volumes."
        ),
        "children": ["D-011"],
    },
    {
        "id": "D-011",
        "title": "Defer electronics dose-logging feature to V2",
        "date": date(2026, 2, 18),
        "sector": "Project Management",
        "made_by": "Joint — Design Review 3",
        "signed_off_by": "Helen Marsh / Anita Devereux",
        "context": (
            "Gilead explored adding Bluetooth dose-logging ahead of design freeze, which would "
            "have required a full re-verification cycle and pushed DV start by an estimated 4 months."
        ),
        "decision": (
            "Defer connected dose-logging to a V2 programme. Freeze V1 as a mechanical-only "
            "device to protect the DV timeline and original budget envelope."
        ),
        "consequence": "Design freeze held on schedule (6 Mar 2026). V2 scoping to begin post-submission.",
        "internal_note": (
            "Ben Crowther's July start is specifically to begin early V2 electronics scoping "
            "in parallel with V1 DV — don't let this slide into a generic 'future work' bucket, "
            "Gilead's commercial team is keen and we should stay ahead of a re-ask."
        ),
        "children": [],
    },
]

# ---------------------------------------------------------------------------
# Autoinjector parts (for CAD model in Engineering page)
# ---------------------------------------------------------------------------

AUTOINJECTOR_PARTS = [
    {
        "id": "P001", "name": "Needle Cap",
        "material": "Polypropylene (PP), Blue RAL 5009",
        "drawing": "SYC-DRG-001-C",
        "spec": "Removal force: 5–15 N; Pull-off axial ≤ 8 N",
        "file": "Sycamore_NeedleCap_DRG-001-C.pdf",
        "description": "Protective removable needle cap. Twist-and-pull mechanism. Must be removed before activation.",
    },
    {
        "id": "P002", "name": "Rigid Needle Shield (RNS)",
        "material": "316L Stainless Steel",
        "drawing": "SYC-DRG-002-D",
        "spec": "Shield removal force: 5–15 N; OD: 6.35 ± 0.05 mm",
        "file": "Sycamore_RNS_DRG-002-D.pdf",
        "description": "Sterile barrier rigid needle shield. Retained decision D-014 confirmed stainless steel over polymer.",
    },
    {
        "id": "P003", "name": "Outer Housing / Body",
        "material": "ABS/PC blend, Grey RAL 7035",
        "drawing": "SYC-DRG-003-F",
        "spec": "Wall thickness: 2.0 ± 0.1 mm; Length: 155 ± 0.5 mm",
        "file": "Sycamore_Housing_DRG-003-F.pdf",
        "description": "Main structural body housing the drug cartridge, drive spring, and plunger assembly.",
    },
    {
        "id": "P004", "name": "Drug Cartridge (1.0 mL PFS)",
        "material": "Borosilicate glass Type I",
        "drawing": "SYC-DRG-004-B",
        "spec": "Volume: 1.0 mL nominal; Break-loose: ≤ 8 N; Glide: ≤ 15 N",
        "file": "Sycamore_Cartridge_DRG-004-B.pdf",
        "description": "1.0 mL pre-filled syringe drug container. ISO 11040-4 compliant.",
    },
    {
        "id": "P005", "name": "Drive Spring",
        "material": "302 Stainless Steel wire",
        "drawing": "SYC-DRG-005-C",
        "spec": "Pre-load force: 18 ± 3% N; Free length: 92 mm; Rate: 0.46 N/mm",
        "file": "Sycamore_DriveSpring_DRG-005-C.pdf",
        "description": "Compression spring providing injection force. Tolerance tightened to ±3% per decision D-012.",
    },
    {
        "id": "P006", "name": "Plunger Rod",
        "material": "Polypropylene (PP)",
        "drawing": "SYC-DRG-006-B",
        "spec": "Length: 88 ± 0.2 mm; Drive force transmission: 100%",
        "file": "Sycamore_PlungerRod_DRG-006-B.pdf",
        "description": "Transmits spring force to the syringe plunger stopper to expel the drug dose.",
    },
    {
        "id": "P007", "name": "Activation Button",
        "material": "ABS, Blue RAL 5009",
        "drawing": "SYC-DRG-007-A",
        "spec": "Activation force: 10–25 N; Travel: 3.5 ± 0.5 mm",
        "file": "Sycamore_ActivationBtn_DRG-007-A.pdf",
        "description": "User-facing activation mechanism. Press to release drive spring and initiate injection.",
    },
    {
        "id": "P008", "name": "End Cap / Base",
        "material": "ABS/PC blend, Grey RAL 7035",
        "drawing": "SYC-DRG-008-B",
        "spec": "Snap-fit retention: ≥ 50 N pull-off; Threading torque: 0.8–1.2 Nm",
        "file": "Sycamore_EndCap_DRG-008-B.pdf",
        "description": "Base closure securing the drive mechanism. Provides grip surface for the user.",
    },
]

# ---------------------------------------------------------------------------
# Files (mock SharePoint-style references)
# ---------------------------------------------------------------------------

FILES = [
    {"id": "F001", "name": "Sycamore_DVP_RevC.docx", "sector": "Quality", "last_edited_by": "Mei Lin Tan",
     "last_edited": date(2026, 6, 12), "status": "Awaiting client approval",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Quality/Sycamore_DVP_RevC.docx"},
    {"id": "F002", "name": "Spring_Force_DV_TestRecord_001-030.xlsx", "sector": "Engineering", "last_edited_by": "Daniel Osei",
     "last_edited": date(2026, 6, 17), "status": "In progress",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Engineering/Spring_Force_DV_TestRecord.xlsx"},
    {"id": "F003", "name": "Sycamore_RiskFile_ISO14971_v9.xlsx", "sector": "Quality", "last_edited_by": "Sarah Quinn",
     "last_edited": date(2026, 6, 14), "status": "In progress",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Quality/Sycamore_RiskFile.xlsx"},
    {"id": "F004", "name": "CO-04_ShelfLife_Extension_Proposal.docx", "sector": "Project Management", "last_edited_by": "Grace Holloway",
     "last_edited": date(2026, 6, 15), "status": "Awaiting client approval",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/PM/CO-04_ShelfLife_Extension.docx"},
    {"id": "F005", "name": "HF_Validation_Study_Protocol_v4.docx", "sector": "Engineering", "last_edited_by": "Lucy Fenwick",
     "last_edited": date(2026, 6, 9), "status": "Awaiting client approval",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Engineering/HF_Validation_Protocol_v4.docx"},
    {"id": "F006", "name": "DesignReview4_Minutes_and_Actions.pptx", "sector": "Project Management", "last_edited_by": "Helen Marsh",
     "last_edited": date(2026, 5, 22), "status": "Final",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/PM/DesignReview4_Minutes.pptx"},
    {"id": "F007", "name": "Sycamore_DHF_DV_Section_draft.docx", "sector": "Quality", "last_edited_by": "Marcus Webb",
     "last_edited": date(2026, 6, 16), "status": "In progress",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Quality/Sycamore_DHF_DV_Section.docx"},
    {"id": "F008", "name": "Sterile_Barrier_DoseMapping_Request.pdf", "sector": "Quality", "last_edited_by": "Sarah Quinn",
     "last_edited": date(2026, 6, 11), "status": "Awaiting client approval",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Quality/Sterile_Barrier_DoseMapping.pdf"},
    {"id": "F009", "name": "Dose_Accuracy_DV_Protocol_v2.docx", "sector": "Engineering", "last_edited_by": "Priya Nadarajah",
     "last_edited": date(2026, 6, 8), "status": "Final",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Engineering/Dose_Accuracy_Protocol_v2.docx"},
    {"id": "F010", "name": "Sycamore_BudgetForecast_Q2-2026.xlsx", "sector": "Finance", "last_edited_by": "Grace Holloway",
     "last_edited": date(2026, 6, 19), "status": "In progress",
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Finance/Budget_Forecast_Q2.xlsx"},
]

PRESENTATIONS = [
    {"name": "Design Review 4 — DV Readiness", "date": date(2026, 5, 22),
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/DR4_DV_Readiness.pptx",
     "transcript_url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/DR4_Transcript.docx"},
    {"name": "Monthly Steering Update — May 2026", "date": date(2026, 5, 29),
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/Steering_May26.pptx",
     "transcript_url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/Steering_May26_Transcript.docx"},
    {"name": "CO-04 Shelf-Life Extension — Business Case", "date": date(2026, 6, 15),
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/CO04_BusinessCase.pptx",
     "transcript_url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/CO04_Transcript.docx"},
    {"name": "Monthly Steering Update — June 2026", "date": date(2026, 6, 22),
     "url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/Steering_Jun26.pptx",
     "transcript_url": "https://gilead-team.sharepoint.com/sites/Sycamore/Presentations/Steering_Jun26_Transcript.docx"},
]

# ---------------------------------------------------------------------------
# Budget
# ---------------------------------------------------------------------------

BUDGET = {
    "total": 3_000_000,
    "fees_budget": 2_400_000,
    "me_budget": 600_000,
    "fees_spent": 1_584_000,
    "me_spent": 367_000,
    "change_orders": [
        {"id": "CO-01", "title": "Additional drop-test rig build", "value": 28_000, "status": "Approved", "date": date(2025, 11, 4)},
        {"id": "CO-02", "title": "Extended human factors formative study", "value": 41_500, "status": "Approved", "date": date(2026, 1, 20)},
        {"id": "CO-03", "title": "Polymer needle shield tooling (de-scoped)", "value": 19_000, "status": "Withdrawn", "date": date(2026, 4, 2)},
        {"id": "CO-04", "title": "Shelf-life study extension (24mo → 36mo)", "value": 86_000, "status": "Pending approval", "date": date(2026, 6, 15)},
    ],
    "monthly_burn": [
        ("Jan 25", 52_000, 11_000),
        ("Feb 25", 55_000, 8_000),
        ("Mar 25", 58_000, 13_000),
        ("Apr 25", 60_000, 6_000),
        ("May 25", 64_000, 5_000),
        ("Jun 25", 62_000, 5_000),
        ("Jul 25", 66_000, 7_000),
        ("Aug 25", 63_000, 3_000),
        ("Sep 25", 68_000, 9_000),
        ("Oct 25", 71_000, 10_000),
        ("Nov 25", 73_000, 6_000),
        ("Dec 25", 58_000, 4_000),
        ("Jan 26", 142_000, 38_000),
        ("Feb 26", 138_000, 22_000),
        ("Mar 26", 151_000, 61_000),
        ("Apr 26", 146_000, 54_000),
        ("May 26", 159_000, 71_000),
        ("Jun 26", 98_000, 34_000),
    ],
    # Forecast: remaining months to DV complete
    "monthly_forecast": [
        ("Jul 26", 162_000, 78_000),
        ("Aug 26", 155_000, 42_000),
        ("Sep 26", 148_000, 22_000),
    ],
    "invoices": [
        {"number": "INV-2026-014", "period": "May 2026", "amount": 159_000, "status": "Paid", "date": date(2026, 6, 5)},
        {"number": "INV-2026-013", "period": "Apr 2026", "amount": 146_000, "status": "Paid", "date": date(2026, 5, 6)},
        {"number": "INV-2026-012", "period": "Mar 2026", "amount": 151_000, "status": "Paid", "date": date(2026, 4, 4)},
        {"number": "INV-2026-015", "period": "Jun 2026 (partial)", "amount": 98_000, "status": "Draft — not yet issued", "date": None},
    ],
}

# ---------------------------------------------------------------------------
# AI overview
# ---------------------------------------------------------------------------

AI_OVERVIEW = {
    "internal": {
        "summary": (
            "Sycamore is in Design Verification following design freeze on 6 March 2026. "
            "Engineering is mid-way through DV test execution. The critical path risk this "
            "week is DVP Rev C approval — 10 days with Gilead QA against a 5-day target. "
            "CO-04 (shelf-life extension, £86k) is pending Gilead finance approval; missing the "
            "30 Jun deadline pushes the accelerated ageing arm to September."
        ),
        "detail": (
            "PROJECT SYCAMORE — PROGRAMME OVERVIEW (22 Jun 2026)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

            "WHAT IS THIS PROJECT?\n"
            "Project Sycamore is a 17-month development programme to bring a single-use, "
            "spring-driven autoinjector to Design Verification for Gilead Sciences. "
            "The device delivers a 1.0 mL subcutaneous biologic for rheumatoid arthritis. "
            "Target regulatory submission is 1 Feb 2027. Budget: £3.0M (TC fees + M&E).\n\n"

            "WHO IS ON THE PROJECT?\n"
            "Team Consulting:\n"
            "  John Burke — Project Lead (60%). Programme delivery, client relationship, "
            "steering committee chair.\n"
            "  Tom Grant — Senior Mechanical Engineer (80%). Leads DV test execution and "
            "spring force programme. Principal technical authority on the device.\n"
            "  Emily Morley — Mechanical Engineer (100%). Day-to-day DV test delivery, "
            "dosing accuracy protocols, engineering files.\n"
            "  Louis DeCleyn — Quality Engineer (50%). DHF, risk file (ISO 14971), "
            "DVP management and QMS compliance. Key interface with Gilead QA.\n"
            "  Jasper Ferguson — Test Engineer (100%). New to the project Apr 2026. "
            "Running spring force and needle insertion test execution.\n"
            "  Lucy Fenwick — Human Factors Specialist (20%, rolling off 3 Jul). "
            "Leads HF validation protocol. Handover critical before departure.\n"
            "  Marcus Webb — Regulatory Affairs (30%). ISO 13485 / MDR strategy, DHF structure.\n"
            "  Grace Holloway — Finance & Commercial Lead (15%). Budget tracking, CO management, "
            "invoicing.\n"
            "  Ben Crowther — Electronics Engineer (joining 14 Jul). Early V2 scoping "
            "(connected dose-logging deferred from V1 per decision D-011).\n\n"
            "Gilead stakeholders:\n"
            "  Anita Devereux (Programme Director) — executive sponsor and final sign-off.\n"
            "  James Okonkwo (Device Development Lead) — technical counterpart.\n"
            "  Mei Lin Tan (QA Manager) — approves DVP, protocols, and DHF sections.\n"
            "  Robert FitzGerald (Regulatory Affairs) — regulatory strategy alignment.\n"
            "  Sofia Alvarez (Clinical & HF Liaison) — HF validation and clinical context.\n\n"

            "WHAT HAS BEEN DONE?\n"
            "  Jan 2025 – Feb 2026: Concept, design development, and Design Reviews 1–3.\n"
            "  Feb 2026: Decision D-011 — electronics dose-logging deferred to V2 to protect timeline.\n"
            "  3 Mar 2026: Design Output Specification approved (Helen Marsh / Anita Devereux).\n"
            "  6 Mar 2026: Design freeze confirmed. DVP Rev B issued.\n"
            "  Apr 2026: Decision D-012 — spring pre-load tolerance tightened to ±3% "
            "following DV pilot data showing dose accuracy trending toward spec boundary.\n"
            "  Apr 2026: Decision D-014 — stainless steel RNS confirmed (polymer failed drop test).\n"
            "  Apr–May 2026: DV test articles prepared; initial protocol approvals.\n"
            "  18 May 2026: WP1.2 (spring force) commenced. 55% complete, no failures.\n"
            "  22 May 2026: Design Review 4 (DV Readiness) completed.\n"
            "  12 Jun 2026: DVP Rev C submitted to Gilead QA (revision driven by D-012 change).\n"
            "  Jun 2026: Decision D-013 — shelf-life extended to 36 months (Gilead commercial "
            "request). Raised as CO-04, pending finance approval.\n\n"

            "WHAT IS IN PROGRESS NOW?\n"
            "  WP1.2 — Spring force DV testing: 55% complete. Jasper Ferguson leading. "
            "Samples 1–18 within spec. Tracking to 10 Jul completion.\n"
            "  WP1.3 — Needle insertion depth DV: 30% complete. No issues.\n"
            "  WP1.4 — Dose accuracy DV: 15% complete. Monitoring closely (spring tolerance change).\n"
            "  WP1.7 — HF validation protocol: 95% complete. BLOCKED on DVP Rev C sign-off.\n"
            "  DVP Rev C: 10 days with Gilead QA (target was 5 days). Unblocking WP1.7.\n"
            "  CO-04 (shelf-life extension): Awaiting Gilead finance approval. Deadline 30 Jun.\n\n"

            "WHAT IS COMING NEXT?\n"
            "  Jun 2026: CO-04 finance approval decision from Gilead (deadline: 30 Jun).\n"
            "  Jul 2026: DVP Rev C sign-off; HF study recruitment begins.\n"
            "  Jul 2026: Ben Crowther joins for V2 electronics scoping.\n"
            "  Jul 2026: Lucy Fenwick departs — HF protocol must be fully handed over by 3 Jul.\n"
            "  Aug 2026: HF validation study execution.\n"
            "  Sep 2026: DV exit gate (target 18 Sep). All test reports signed off.\n"
            "  Oct–Dec 2026: DHF compilation and regulatory submission prep.\n"
            "  Feb 2027: Target regulatory submission.\n\n"

            "IMMEDIATE PRIORITIES & CONCERNS\n"
            "  [CRITICAL] DVP Rev C approval is 5 days overdue. Escalate via John Burke "
            "to Anita Devereux if no response from Mei Lin by 25 Jun.\n"
            "  [URGENT] CO-04 budget decision: 30 Jun hard deadline. Next accelerated ageing "
            "chamber slot after that is September — a 3-month programme slip.\n"
            "  [WATCH] RISK-021 — Spring fatigue under worst-case patient grip force: open, "
            "in active DV testing (WP1.2). Cannot close until test report signed off.\n"
            "  [WATCH] RISK-027 — Sterile barrier seal integrity post-shipping vibration: open, "
            "in WP1.6. Thinnest-margin item on the plan. Do not commit publicly to the "
            "18 Sep exit gate until this mitigation data is in hand.\n"
            "  [RESOURCE] Lucy Fenwick departs 3 Jul. HF protocol handover is time-critical.\n\n"

            "BUDGET STATUS (as of May 2026)\n"
            "  Total budget: £3.0M | Spent: £1,951k (65%) | Remaining: £1,049k\n"
            "  Currently ~4% over phased plan (driven by spring tolerance tightening in D-012).\n"
            "  CO-04 (£86k) is not yet in the budget baseline — approval would add to remaining.\n"
            "  CO-01 (£28k drop-test rig) and CO-02 (£41.5k HF formative) approved and absorbed.\n"
            "  CO-03 (£19k polymer needle shield tooling) withdrawn — not in the cost.\n\n"

            "KEY DECISIONS MADE\n"
            "  D-014: Stainless steel RNS confirmed (Apr 2026)\n"
            "  D-013: Shelf-life extended to 36 months — CO-04 raised (Jun 2026)\n"
            "  D-012: Spring pre-load tolerance tightened to ±3% (Apr 2026)\n"
            "  D-011: Electronics dose-logging deferred to V2 (Feb 2026)\n"
            "  See Decisions page for full tree with rationale and sign-off records.\n\n"

            "USEFUL CONTEXT FOR NEW JOINERS\n"
            "  The device is a V1 mechanical-only autoinjector — no electronics in scope.\n"
            "  Ben Crowther's July start is specifically to begin V2 electronics scoping in "
            "parallel with V1 DV. Keep this separate from V1 scope conversations with Gilead.\n"
            "  The most sensitive internal item: do not commit publicly to 18 Sep exit date "
            "until RISK-027 sterile barrier data is in. The gate is real but the margin is thin."
        ),
    },
    "client": {
        "summary": (
            "Sycamore has completed design freeze and is in Design Verification. Core DV tests "
            "are running in parallel, tracking toward the 18 September 2026 DV exit gate. "
            "Two decisions are needed from Gilead this week: DVP Rev C approval and CO-04 "
            "budget sign-off (£86k shelf-life extension)."
        ),
        "detail": (
            "PROJECT SYCAMORE — GILEAD STATUS BRIEFING (22 Jun 2026)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

            "PROGRAMME CONTEXT\n"
            "Sycamore is delivering a single-use autoinjector for a 1.0 mL subcutaneous "
            "biologic. The programme entered Design Verification following design freeze on "
            "6 March 2026 and is targeting DV completion on 18 September 2026, with regulatory "
            "submission planned for 1 February 2027.\n\n"

            "WHO YOU ARE WORKING WITH\n"
            "  Team Consulting leads: John Burke (Programme Director), Tom Grant (Engineering Lead), "
            "Emily Morley (Test Execution), Louis DeCleyn (Quality), Jasper Ferguson (Testing).\n"
            "  Gilead leads: Anita Devereux (Programme Director), James Okonkwo (Device Development), "
            "Mei Lin Tan (QA Manager), Robert FitzGerald (Regulatory Affairs), "
            "Sofia Alvarez (Clinical & HF Liaison).\n\n"

            "MILESTONES ACHIEVED\n"
            "  6 March 2026: Design freeze. All design outputs locked.\n"
            "  22 May 2026: Design Review 4 (DV Readiness) — passed.\n"
            "  18 May 2026: DV test execution commenced.\n"
            "  Decisions D-011 through D-014 completed. Key: electronics deferred to V2 "
            "(D-011), stainless steel RNS confirmed (D-014).\n\n"

            "CURRENT PROGRAMME STATUS\n"
            "  Spring force testing (WP1.2): 55% complete. No failures. On plan.\n"
            "  Needle insertion testing (WP1.3): 30% complete. Progressing on plan.\n"
            "  Dose accuracy testing (WP1.4): 15% complete. Progressing on plan.\n"
            "  Human Factors validation protocol (WP1.7): 95% complete. "
            "Awaiting DVP Rev C approval to finalise.\n\n"

            "ACTIONS REQUIRED FROM GILEAD\n\n"
            "  1. DVP Rev C APPROVAL (urgent)\n"
            "     Submitted: 12 June 2026 | Awaiting: Mei Lin Tan / Gilead QA\n"
            "     Impact: Sign-off unblocks the HF validation study protocol (WP1.7). "
            "Delay past 25 Jun risks moving HF study recruitment into August, which "
            "compresses the margin to the 18 Sep DV exit gate.\n\n"
            "  2. CO-04 BUDGET APPROVAL — Shelf-life study extension (£86,000)\n"
            "     Deadline: 30 June 2026 | Contact: Anita Devereux\n"
            "     Background: Gilead commercial requested extension from 24-month to 36-month "
            "shelf-life claim (to align with competitor labelling). This requires an additional "
            "accelerated ageing arm at 40°C/75% RH.\n"
            "     Impact: If not approved by 30 Jun, the next available ageing chamber slot is "
            "September — a 3-month delay to the ageing programme.\n\n"

            "UPCOMING MILESTONES\n"
            "  30 Jun 2026: CO-04 budget decision deadline\n"
            "  Jul 2026: HF validation study recruitment begins (pending DVP sign-off)\n"
            "  Aug 2026: HF validation study execution\n"
            "  18 Sep 2026: DV exit gate — all DV test reports completed and signed\n"
            "  Oct–Dec 2026: Design History File compilation\n"
            "  1 Feb 2027: Regulatory submission\n\n"

            "BUDGET SUMMARY\n"
            "  Total contract value: £3.0M | Spent to date: £1,951k (65%)\n"
            "  All invoices to May 2026 are paid and up to date.\n"
            "  CO-04 (£86k) is pending your approval and not yet in the baseline.\n"
            "  Programme is tracking to budget, with June invoice to be issued shortly."
        ),
    },
}

# ---------------------------------------------------------------------------
# Comments (attached to tasks, files, or decisions)
# ---------------------------------------------------------------------------

COMMENTS = [
    {"id": "C001", "target_type": "task", "target_id": "WP1.1", "author": "Helen Marsh", "team": "team",
     "date": date(2026, 6, 16), "text": "Following up with Mei Lin today — this is now the long pole for the HF study start.",
     "resolved": False},
    {"id": "C002", "target_type": "task", "target_id": "WP1.1", "author": "Mei Lin Tan", "team": "client",
     "date": date(2026, 6, 17), "text": "Apologies for the delay, our internal QA review board meets Thursday. Will confirm Friday.",
     "resolved": False},
    {"id": "C003", "target_type": "decision", "target_id": "D-013", "author": "Grace Holloway", "team": "team",
     "date": date(2026, 6, 15), "text": "CO-04 raised and sent for approval. Flagging this will need a budget decision before invoicing in July.",
     "resolved": False},
    {"id": "C004", "target_type": "file", "target_id": "F002", "author": "Priya Nadarajah", "team": "team",
     "date": date(2026, 6, 17), "text": "Samples 1-18 complete and within spec. Continuing through the batch this week.",
     "resolved": True},
    {"id": "C005", "target_type": "file", "target_id": "F001", "author": "James Okonkwo", "team": "client",
     "date": date(2026, 6, 18), "text": "Circulating internally — expect sign-off by end of week per Mei Lin.",
     "resolved": False},
]

# ---------------------------------------------------------------------------
# Internal messages (Team Consulting only — never shown to Gilead)
# ---------------------------------------------------------------------------

INTERNAL_MESSAGES = [
    {"id": "M001", "author": "Helen Marsh", "date": date(2026, 6, 19),
     "text": "Heads up — Anita mentioned informally that Gilead's CFO is asking about the CO-03 de-scope saving again. "
             "Let's make sure Grace has the numbers ready before the steering call."},
    {"id": "M002", "author": "Priya Nadarajah", "date": date(2026, 6, 20),
     "text": "Spring batch looking good — if we keep this pace we'll be done early. Might be worth flagging "
             "to Helen so we can plan resources for WP1.4 overlap."},
    {"id": "M003", "author": "Grace Holloway", "date": date(2026, 6, 21),
     "text": "Finance update: we're ~4% over phased plan this month. I'll have an updated forecast by EOD. "
             "Not material yet but let's not let it drift further."},
    {"id": "M004", "author": "Helen Marsh", "date": date(2026, 6, 22),
     "text": "Reminder — Lucy's last day is 3 Jul. Make sure the HF protocol is fully handed over before then."},
]

# ---------------------------------------------------------------------------
# Gilead-side internal messages (only visible in client mode)
# ---------------------------------------------------------------------------

GILEAD_INTERNAL_MESSAGES = [
    {"id": "G-M001", "author": "Anita Devereux", "date": date(2026, 6, 18),
     "text": "Team Consulting have submitted DVP Rev C. Mei Lin — can you confirm your "
             "QA review timeline? John is following up and I want to give him a committed date."},
    {"id": "G-M002", "author": "Mei Lin Tan", "date": date(2026, 6, 19),
     "text": "Board meets Thursday. I'll have the DVP reviewed by end of Thursday and send "
             "comments or sign-off Friday morning. No major concerns from my initial read."},
    {"id": "G-M003", "author": "James Okonkwo", "date": date(2026, 6, 20),
     "text": "CO-04 shelf-life proposal looks reasonable. The 36-month claim is important for "
             "commercial — I'm supportive. Anita, can you confirm what finance needs from us "
             "before 30 Jun?"},
    {"id": "G-M004", "author": "Anita Devereux", "date": date(2026, 6, 21),
     "text": "Finance need a signed business case and the CO-04 proposal document. Grace's "
             "CO-04 document covers it. Sofia — are you comfortable with the HF study protocol "
             "structure? I want to approve the DVP before circling back on HF scope."},
    {"id": "G-M005", "author": "Sofia Alvarez", "date": date(2026, 6, 22),
     "text": "HF protocol v4 looks good from a clinical perspective. The simulated use study "
             "design aligns with FDA guidance. Happy to sign off once DVP is cleared."},
]

# ---------------------------------------------------------------------------
# Gilead-side decision tree (approvals Gilead gives to Team Consulting)
# ---------------------------------------------------------------------------

GILEAD_DECISIONS = [
    {
        "id": "GA-001",
        "title": "Design Output Specification approval",
        "date": date(2026, 3, 3),
        "sector": "Project Management",
        "made_by": "Anita Devereux",
        "signed_off_by": "Anita Devereux / James Okonkwo",
        "context": (
            "Team Consulting submitted the Design Output Specification (DOS v2.1) for Gilead "
            "approval ahead of the design freeze gate. The DOS locks all functional, dimensional, "
            "and performance requirements the device must meet."
        ),
        "decision": (
            "Gilead approved the Design Output Specification v2.1. Design freeze authorised "
            "to proceed on 6 March 2026."
        ),
        "consequence": (
            "Confirmed the complete design requirements baseline. All subsequent DV testing "
            "is executed against this approved specification."
        ),
        "signed_off_by_gilead": "Anita Devereux",
        "children": ["GA-002"],
    },
    {
        "id": "GA-002",
        "title": "Design freeze confirmation",
        "date": date(2026, 3, 6),
        "sector": "Project Management",
        "made_by": "Joint — Helen Marsh / Anita Devereux",
        "signed_off_by": "Anita Devereux",
        "context": (
            "Following DOS approval, Team Consulting confirmed no outstanding design changes "
            "and requested formal design freeze authorisation from Gilead."
        ),
        "decision": (
            "Gilead confirmed design freeze. V1 device configuration locked. "
            "DV test execution authorised to commence."
        ),
        "consequence": (
            "Design freeze in effect from 6 March 2026. Any design changes from this point "
            "require a formal change order process."
        ),
        "signed_off_by_gilead": "Anita Devereux",
        "children": ["GA-003"],
    },
    {
        "id": "GA-003",
        "title": "DVP Rev C approval — PENDING",
        "date": date(2026, 6, 12),
        "sector": "Engineering",
        "made_by": "Team Consulting — Louis DeCleyn",
        "signed_off_by": "Pending — Mei Lin Tan",
        "context": (
            "Team Consulting submitted Design Verification Plan Rev C on 12 June 2026. "
            "Rev C incorporates the spring pre-load tolerance change (D-012) and updated "
            "acceptance criteria for dose accuracy testing."
        ),
        "decision": (
            "PENDING — Gilead QA review in progress. Expected sign-off: 27 June 2026."
        ),
        "consequence": (
            "Sign-off unblocks the Human Factors validation study protocol (WP1.7). "
            "Delay past 25 Jun risks HF study recruitment slipping to August."
        ),
        "signed_off_by_gilead": "Pending",
        "children": ["GA-004"],
    },
    {
        "id": "GA-004",
        "title": "HF validation study protocol approval — BLOCKED",
        "date": date(2026, 6, 9),
        "sector": "Engineering",
        "made_by": "Lucy Fenwick / Team Consulting",
        "signed_off_by": "Pending — Sofia Alvarez / Mei Lin Tan",
        "context": (
            "HF Validation Study Protocol v4 submitted to Gilead for review. The protocol "
            "defines the simulated-use study for the final Human Factors validation study "
            "required for regulatory submission."
        ),
        "decision": (
            "BLOCKED — Cannot be signed off until DVP Rev C (GA-003) is approved by Gilead QA."
        ),
        "consequence": (
            "HF study recruitment cannot begin until both DVP and protocol are signed off. "
            "Note: Lucy Fenwick (HF Specialist) is departing Team Consulting on 3 July."
        ),
        "signed_off_by_gilead": "Pending",
        "children": [],
    },
    {
        "id": "GA-005",
        "title": "CO-04 budget authorisation — PENDING",
        "date": date(2026, 6, 15),
        "sector": "Finance",
        "made_by": "Grace Holloway / Team Consulting",
        "signed_off_by": "Pending — Anita Devereux",
        "context": (
            "Following Gilead commercial's request for a 36-month shelf-life claim, Team "
            "Consulting raised Change Order CO-04 (£86,000) to add a 36-month real-time "
            "ageing arm and an accelerated ageing study at 40°C/75% RH."
        ),
        "decision": (
            "PENDING — Gilead finance authorisation required by 30 June 2026."
        ),
        "consequence": (
            "If not authorised by 30 Jun, the next available ageing chamber slot is "
            "September 2026 — a 3-month delay to the accelerated ageing programme."
        ),
        "signed_off_by_gilead": "Pending",
        "children": [],
    },
    {
        "id": "GA-006",
        "title": "Regulatory strategy endorsement",
        "date": date(2025, 9, 15),
        "sector": "Project Management",
        "made_by": "Marcus Webb / Robert FitzGerald",
        "signed_off_by": "Robert FitzGerald",
        "context": (
            "Team Consulting and Gilead RA jointly agreed the regulatory submission strategy: "
            "CE marking under EU MDR 2017/745 as primary route, 510(k) for US as secondary. "
            "ISO 13485 and IEC 62366-1 (HF) as applicable standards."
        ),
        "decision": (
            "Regulatory strategy endorsed. EU MDR + FDA 510(k) dual-track confirmed. "
            "DHF structure aligned with both pathways."
        ),
        "consequence": (
            "DHF compilation in progress from Q3 2026 onward. Robert FitzGerald "
            "remains the Gilead point of contact for all regulatory submissions."
        ),
        "signed_off_by_gilead": "Robert FitzGerald",
        "children": [],
    },
]

# ---------------------------------------------------------------------------
# Risk register (full)
# ---------------------------------------------------------------------------

RISKS = [
    {"id": "RISK-001", "title": "DVP sign-off delay blocks HF study start",
     "category": "Schedule", "severity": 4, "likelihood": 4, "score": 16,
     "owner": "John Burke", "status": "Open",
     "comment": "DVP Rev C now 10 days with Gilead QA. Escalate to Anita Devereux if not resolved by 25 Jun."},
    {"id": "RISK-002", "title": "CO-04 budget approval missed — ageing arm slips to September",
     "category": "Commercial", "severity": 4, "likelihood": 3, "score": 12,
     "owner": "John Burke", "status": "Open",
     "comment": "Hard deadline 30 Jun. Next ageing chamber slot is September — 3-month programme impact."},
    {"id": "RISK-021", "title": "Spring fatigue failure under worst-case patient grip force",
     "category": "Technical", "severity": 5, "likelihood": 2, "score": 10,
     "owner": "Tom Grant", "status": "Open",
     "comment": "Mitigation: 75,000-cycle fatigue testing (WP1.2, 55% complete). Cannot close until DV report signed."},
    {"id": "RISK-027", "title": "Sterile barrier seal integrity failure post-shipping vibration",
     "category": "Technical", "severity": 5, "likelihood": 2, "score": 10,
     "owner": "Tom Grant", "status": "Open",
     "comment": "Thinnest margin item. Do not commit to 18 Sep gate publicly until WP1.6 data is in hand."},
    {"id": "RISK-003", "title": "Lucy Fenwick departure leaves HF protocol handover incomplete",
     "category": "Resource", "severity": 3, "likelihood": 3, "score": 9,
     "owner": "Helen Marsh", "status": "Open",
     "comment": "Lucy departs 3 Jul. Protocol 95% complete but handover to replacement lead must be confirmed."},
    {"id": "RISK-010", "title": "CRO dose mapping report delayed — blocks sterile barrier protocol",
     "category": "Technical", "severity": 3, "likelihood": 3, "score": 9,
     "owner": "Sarah Quinn", "status": "Open",
     "comment": "CRO confirmed 5 Jul target. Protocol sign-off and WP1.6 start both blocked until report received."},
    {"id": "RISK-005", "title": "Shipping simulation rig build delayed by carton design freeze slip",
     "category": "Schedule", "severity": 3, "likelihood": 3, "score": 9,
     "owner": "Oliver Bancroft", "status": "Open",
     "comment": "WP1.5 not started — blocked on secondary packaging carton design freeze from Gilead commercial."},
    {"id": "RISK-004", "title": "Dose accuracy trends toward lower spec limit at ±3% spring tolerance",
     "category": "Technical", "severity": 4, "likelihood": 2, "score": 8,
     "owner": "Emily Morley", "status": "Open",
     "comment": "D-012 tightened tolerance to reduce risk. WP1.4 only 15% complete — monitor closely."},
    {"id": "RISK-007", "title": "EU MDR Annex XIV gap in DHF clinical evaluation structure",
     "category": "Regulatory", "severity": 4, "likelihood": 2, "score": 8,
     "owner": "Marcus Webb", "status": "Open",
     "comment": "DHF clinical evaluation section needs MDR alignment review with Robert FitzGerald."},
    {"id": "RISK-008", "title": "Budget variance exceeds 5% if CO-04 and inspection overhead both run",
     "category": "Commercial", "severity": 3, "likelihood": 2, "score": 6,
     "owner": "Grace Holloway", "status": "Open",
     "comment": "Currently ~4% over phased plan. CO-04 approval ring-fenced separately. Monitoring monthly."},
    {"id": "RISK-009", "title": "HF study participant recruitment insufficient or delayed",
     "category": "Clinical", "severity": 3, "likelihood": 2, "score": 6,
     "owner": "Lucy Fenwick", "status": "Open",
     "comment": "CRO shortlisted. Recruitment blocked until both DVP Rev C and HF protocol are signed off."},
    {"id": "RISK-006", "title": "Schott single-source cartridge supply disruption",
     "category": "Supply Chain", "severity": 4, "likelihood": 1, "score": 4,
     "owner": "Louis DeCleyn", "status": "Open",
     "comment": "Schott locked per D-008. Supply agreement has 6-month notice — low probability, high impact."},
    {"id": "RISK-011", "title": "IEC 62366-1 summative study insufficient to meet FDA guidance",
     "category": "Regulatory", "severity": 3, "likelihood": 1, "score": 3,
     "owner": "Lucy Fenwick", "status": "Open",
     "comment": "FDA 510(k) is secondary route. Robert FitzGerald monitoring FDA guidance updates."},
    {"id": "RISK-012", "title": "Spring tooling dimensional drift after D-012 tolerance change",
     "category": "Technical", "severity": 2, "likelihood": 2, "score": 4,
     "owner": "Tom Grant", "status": "Closed",
     "comment": "Incoming inspection protocol updated. Two-week qualification run completed — no drift observed."},
]

# ---------------------------------------------------------------------------
# Action log
# ---------------------------------------------------------------------------

ACTIONS = [
    {"id": "A001", "description": "Chase DVP Rev C sign-off — escalate to Anita Devereux if no response by 25 Jun",
     "owner": "John Burke", "due_date": date(2026, 6, 25), "priority": "High", "status": "Open",
     "source": "Programme Standup · 22 Jun 2026"},
    {"id": "A002", "description": "Obtain CO-04 Gilead finance approval before 30 Jun hard deadline",
     "owner": "John Burke", "due_date": date(2026, 6, 30), "priority": "High", "status": "Open",
     "source": "Steering Committee · 22 Jun 2026"},
    {"id": "A003", "description": "Prepare signed CO-04 business case document for Gilead finance submission",
     "owner": "Grace Holloway", "due_date": date(2026, 6, 26), "priority": "High", "status": "In Progress",
     "source": "Internal · 21 Jun 2026"},
    {"id": "A004", "description": "Complete HF protocol v4 handover before Lucy Fenwick departs (3 Jul)",
     "owner": "Lucy Fenwick", "due_date": date(2026, 7, 3), "priority": "High", "status": "In Progress",
     "source": "Resource planning · 19 Jun 2026"},
    {"id": "A005", "description": "Send Q2 2026 budget forecast update to Gilead ahead of steering call",
     "owner": "Grace Holloway", "due_date": date(2026, 6, 27), "priority": "Medium", "status": "In Progress",
     "source": "Internal · 21 Jun 2026"},
    {"id": "A006", "description": "Confirm CRO scope and report date for sterile barrier dose mapping",
     "owner": "Sarah Quinn", "due_date": date(2026, 6, 28), "priority": "Medium", "status": "Open",
     "source": "WP1.6 Review · 20 Jun 2026"},
    {"id": "A007", "description": "Complete spring force test batch samples 19–30 and issue interim report",
     "owner": "Tom Grant", "due_date": date(2026, 7, 10), "priority": "Medium", "status": "In Progress",
     "source": "DV Standup · 22 Jun 2026"},
    {"id": "A008", "description": "Review DHF DV section structure against EU MDR Annex XIV requirements",
     "owner": "Marcus Webb", "due_date": date(2026, 7, 15), "priority": "Low", "status": "Open",
     "source": "Regulatory review · 18 Jun 2026"},
]

# ---------------------------------------------------------------------------
# Purchase orders
# ---------------------------------------------------------------------------

PURCHASE_ORDERS = [
    {"po_number": "PO-2025-044", "description": "Drop test rig — custom pneumatic fixture build",
     "vendor": "Precision Test Rigs Ltd", "raised_by": "Tom Grant",
     "currency": "GBP", "amount": 28_000, "status": "Closed",
     "date": date(2025, 11, 4), "co_ref": "CO-01"},
    {"po_number": "PO-2026-001", "description": "Extended human factors formative study — CRO fee",
     "vendor": "Human Interface Research Ltd", "raised_by": "Lucy Fenwick",
     "currency": "GBP", "amount": 41_500, "status": "Closed",
     "date": date(2026, 1, 20), "co_ref": "CO-02"},
    {"po_number": "PO-2026-002", "description": "Schott 1 mL long cartridge — DV test articles batch 1 (500 units)",
     "vendor": "Schott AG", "raised_by": "Tom Grant",
     "currency": "EUR", "amount": 15_200, "status": "Closed",
     "date": date(2026, 3, 15), "co_ref": None},
    {"po_number": "PO-2026-003", "description": "SHL Molly platform components — DV test article assembly (250 units)",
     "vendor": "SHL Medical AG", "raised_by": "Tom Grant",
     "currency": "CHF", "amount": 32_000, "status": "Open",
     "date": date(2026, 4, 22), "co_ref": None},
    {"po_number": "PO-2026-004", "description": "Sterilisation dose mapping — EO sterilisation CRO",
     "vendor": "Sterility Sciences Ltd", "raised_by": "Sarah Quinn",
     "currency": "GBP", "amount": 8_700, "status": "Open",
     "date": date(2026, 6, 8), "co_ref": None},
    {"po_number": "PO-2026-005", "description": "Accelerated ageing chambers — CO-04 shelf-life extension",
     "vendor": "Climatic Test Systems Ltd", "raised_by": "Grace Holloway",
     "currency": "GBP", "amount": 86_000, "status": "Pending",
     "date": date(2026, 6, 15), "co_ref": "CO-04"},
]

# ---------------------------------------------------------------------------
# Issue tracker (cross-linked to files / documents)
# ---------------------------------------------------------------------------

ISSUES = [
    {"id": "ISS-001", "title": "DVP Rev B acceptance criteria for dose accuracy not updated per D-012",
     "type": "Document", "priority": "High", "assigned_to": "Louis DeCleyn",
     "raised_date": date(2026, 6, 10), "status": "Resolved",
     "description": "Rev B rejected by Gilead QA — WP7 criteria missing D-012 spring tolerance change. Fixed in Rev C."},
    {"id": "ISS-002", "title": "Spring force test report template missing acceptance criterion reference",
     "type": "Document", "priority": "Medium", "assigned_to": "Emily Morley",
     "raised_date": date(2026, 6, 18), "status": "Open",
     "description": "WP1.2 report template does not reference D-012 tolerance table. Must update before interim report is issued."},
    {"id": "ISS-003", "title": "DHF DV section WP index mismatches DVP Rev C numbering",
     "type": "Quality", "priority": "Medium", "assigned_to": "Louis DeCleyn",
     "raised_date": date(2026, 6, 20), "status": "In Progress",
     "description": "WP numbering in DHF index diverges from DVP Rev C. Both must align before next Gilead DHF submission."},
    {"id": "ISS-004", "title": "Budget forecast spreadsheet double-counts June partial invoice",
     "type": "Finance", "priority": "Low", "assigned_to": "Grace Holloway",
     "raised_date": date(2026, 6, 21), "status": "Resolved",
     "description": "June partial invoice was counted twice in forecast model. Corrected in v3.2 of the forecast spreadsheet."},
    {"id": "ISS-005", "title": "Sterile barrier protocol v0.3 missing CRO escalation contact",
     "type": "Quality", "priority": "Low", "assigned_to": "Sarah Quinn",
     "raised_date": date(2026, 6, 22), "status": "Open",
     "description": "Protocol does not name the CRO contact for dose mapping escalation. Update required before Gilead review."},
]

# ---------------------------------------------------------------------------
# Cost breakdown (by discipline and type) — for costing sheet
# ---------------------------------------------------------------------------

COST_BREAKDOWN = {
    "by_discipline": [
        {"discipline": "Engineering",          "budget": 1_400_000, "spent": 984_000,  "forecast": 1_382_000},
        {"discipline": "Quality & Regulatory", "budget": 480_000,   "spent": 312_000,  "forecast": 498_000},
        {"discipline": "Project Management",   "budget": 360_000,   "spent": 244_000,  "forecast": 358_000},
        {"discipline": "Finance & Commercial", "budget": 160_000,   "spent": 108_000,  "forecast": 162_000},
    ],
    "by_type": [
        {"type": "Fees",                   "budget": 2_400_000, "spent": 1_584_000, "forecast": 2_400_000},
        {"type": "Materials & Equipment",  "budget": 600_000,   "spent": 367_000,   "forecast": 598_000},
    ],
    "contingency_budget": 150_000,
    "contingency_used":    22_500,
}

RISK_REGISTER_SUMMARY = {
    "open_risks": 14,
    "high_severity_open": 2,
    "closed_since_freeze": 9,
    "internal_note": (
        "Two high-severity risks remain open: spring fatigue under worst-case patient "
        "grip force (RISK-021) and sterile barrier seal integrity post-shipping vibration "
        "(RISK-027). Both have mitigations in active DV testing (WP1.2 and WP1.6 "
        "respectively) but neither can be formally closed until test reports are signed "
        "off. Recommend not committing to the 18 Sep DV exit gate publicly with Gilead "
        "until RISK-027 mitigation data is in — sterile barrier testing is currently the "
        "thinnest-margin item on the plan."
    ),
}

# ---------------------------------------------------------------------------
# Helper accessors
# ---------------------------------------------------------------------------

def all_people():
    return TEAM_PEOPLE + CLIENT_PEOPLE


def tasks_for_sector(sector):
    return [t for t in TASKS if t["sector"] == sector]


def waiting_on_summary():
    return [t for t in TASKS if t.get("waiting_on")]


def comments_for(target_type, target_id):
    return [c for c in COMMENTS if c["target_type"] == target_type and c["target_id"] == target_id]
