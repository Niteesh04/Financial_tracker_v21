# 📌 Daily Finance Tracker (v21)

A **Daily Finance Tracker** built with **Python + Flask**.  
It records daily income and expenses, generates automatic backups, and visualizes
spending patterns with charts and tag clouds.  
Data is stored in **Excel, CSV, and SQLite DB** simultaneously, ensuring redundancy
and easy export.

---

## 🔑 Key Features

### 📂 Multi-format Storage
→ SQLite database for structured queries.  
→ Excel (`.xlsx`) file for easy editing.  
→ CSV for lightweight data handling.  

### 🗂️ Backup System
→ Automatic file backups with rotation (retains last **20** per type).  

### ✍️ Data Entry
→ Pocket money, extra income, additional income.  
→ Food & drinks, other spending.  
→ Auto-calculated totals, balance, and income rollovers.  
→ Notes with auto-tagging (`#food`, `#travel`, `#savings`, etc.).  

### 📊 Charts & Analytics
→ Daily chart (always generated).  
→ Monthly chart every **30 entries**.  
→ Yearly chart every **365 entries**.  
→ Word cloud of tags and notes.  
→ Analytics dashboard with averages, best/worst balance days,  
   tag statistics, and monthly summaries.  

### 🌐 Web Dashboard (Flask)
→ Add new entries with a form.  
→ View last **30 entries**.  
→ Download CSV, Excel, and DB files.  
→ Browse and view generated charts.  
→ Search entries by keyword.  
→ Analytics page for deeper insights.  

### 🛠️ Robustness
→ Auto-migration of Excel schema (v19+).  
→ Auto-rebuild of CSV if corrupted or missing columns.  
→ Safe DB migrations with `ALTER TABLE`.  

---

## 🚀 Tech Stack
- **Backend:** Python, Flask  
- **Database:** SQLite  
- **Storage:** Excel (.xlsx), CSV  
- **Visualization:** Matplotlib, WordCloud  

---

## 📸 Screenshots (Optional)
*(Add screenshots of your dashboard, charts, or word cloud here for better
presentation)*

---

## ⚡ Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/daily-finance-tracker.git
cd daily-finance-tracker
