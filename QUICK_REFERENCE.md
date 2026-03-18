# 🎯 Quick Reference Guide

## Application Navigation

```
🏆 Home (app.py)
├── 🔐 Login Page (01_Login.py)
│   ├── Login form
│   └── Sign up form
├── 👥 Add Users (02_Add_Users.py)
│   ├── Single user registration
│   └── Bulk CSV upload
├── 📊 View Data (03_View_Data.py)
│   ├── Filter & search
│   ├── Pagination
│   └── Export to CSV
└── 📈 Analytics (04_Analytics.py)
    ├── Key metrics
    ├── Charts & graphs
    └── Detailed breakdowns
```

## Common Tasks

### Add a Single User
1. Login to the application
2. Go to **"Add Users"** → **"Add Single User"**
3. Fill in required fields (marked with *)
4. Click **"Register User"**

### Bulk Upload Users
1. Go to **"Add Users"** → **"Bulk Upload"**
2. Click **"Download Template"** to get sample CSV
3. Fill with your data
4. Upload the file
5. Click **"Upload All Records"**

### View & Filter Data
1. Go to **"View Data"**
2. Use filters for Tournament, Category, Match Status
3. Use search box to find by name
4. Click **"Download as CSV"** to export

### Check Analytics
1. Go to **"Analytics"**
2. View summary metrics
3. Scroll for charts
4. Click charts to interact

## Database Columns

| Column | Type | Required | Example |
|--------|------|----------|---------|
| first_name | Text | ✅ | John |
| last_name | Text | ❌ | Doe |
| email | Text | ✅ | john@example.com |
| mobile | Text | ✅ | 9876543210 |
| tournament | Text | ✅ | Cricket |
| category | Text | ✅ | Senior |
| match_status | Text | ✅ | Registered |
| number | Text | ❌ | 1 |
| sabha_reference_name | Text | ❌ | Sabha A |
| spl_no | Text | ❌ | SPL001 |
| image | Text (URL) | ❌ | https://... |

## CSV Upload Rules

### ✅ Do's
- Include header row
- Required fields: first_name, email, mobile, tournament, category, match_status
- Save as UTF-8 encoding
- Email addresses must be unique
- Keep file size < 10MB

### ❌ Don'ts
- Include "id" column in CSV
- Leave required fields empty
- Use duplicate emails
- Special characters in names (use ASCII)
- Include quote marks in text

## Filter Options

### Tournament
- Cricket
- Badminton
- Table Tennis
- Football

### Category
- Junior
- Senior
- Professional
- Amateur

### Match Status
- Registered
- Pending
- Confirmed
- Cancelled

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Refresh page | F5 |
| Clear cache | Ctrl+Shift+Delete |
| Developer tools | F12 |
| Search on page | Ctrl+F |

## File Locations

```
Project Root/
├── app.py → Main entry point
├── config.py → Configuration
├── utils.py → Helper functions
├── .env → Credentials (NOT in repo)
├── .streamlit/ → Streamlit settings
└── pages/ → Application pages
```

## Environment Setup

```bash
# Copy template
copy .env.example .env

# Activate environment
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## Troubleshooting Quick Fixes

| Issue | Fix |
|-------|-----|
| Won't login | Check `.env` credentials |
| CSV upload fails | Check column names match |
| Port in use | Use `streamlit run app.py --server.port 8502` |
| Cache stale | Click "Refresh" button |
| Slow performance | Filter data or use pagination |

## Support Contacts

- **Streamlit Docs**: https://docs.streamlit.io
- **Supabase Docs**: https://supabase.com/docs
- **Python Docs**: https://docs.python.org

---

**Version 1.0  |  Updated: 2024**
