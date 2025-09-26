📌 Description

This project is a Daily Finance Tracker (v21) built with Python + Flask.
It is designed to record daily income and expenses, generate automatic backups, and visualize spending patterns with charts and tag clouds. The tracker stores data in Excel, CSV, and SQLite DB simultaneously, ensuring redundancy and easy export.

🔑 Key Features

Multi-format storage:

SQLite database for structured queries.

Excel (.xlsx) file for easy editing.

CSV for lightweight data handling.

Backup system:

Automatic file backups with rotation (retains last 20 per type).

Data entry:

Pocket money, extra income, additional income.

Food & drinks, other spending.

Auto-calculated totals, balance, and income rollovers.

Notes with auto-tagging (#food, #travel, #savings, etc.).

Charts & Analytics:

Daily chart (always generated).

Monthly chart every 30 entries.

Yearly chart every 365 entries.

Word cloud of tags and notes.

Analytics dashboard with averages, best/worst balance days, tag statistics, and monthly summaries.

Web Dashboard (Flask):

Add new entries with a form.

View last 30 entries.

Download CSV, Excel, and DB files.

Browse and view generated charts.

Search entries by keyword.

Analytics page for deeper insights.

Robustness:

Auto-migration of Excel schema (v19+).

Auto-rebuild of CSV if corrupted or missing columns.

Safe DB migrations with ALTER TABLE.
