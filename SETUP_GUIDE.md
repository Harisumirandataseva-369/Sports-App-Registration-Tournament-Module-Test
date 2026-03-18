# 🏆 Sports Tournament Registration System - Setup Guide

A comprehensive Streamlit application for managing sports tournament registrations with Supabase backend integration.

## Features

- **🔐 Secure Authentication**: User login and registration via Supabase Auth
- **👥 User Management**: 
  - Add individual users with detailed information
  - Bulk upload participants via CSV file
- **📊 Data Management**:
  - View all registered participants
  - Advanced filtering by tournament, category, and status
  - Search by participant name
  - Export data to CSV
- **📈 Analytics Dashboard**:
  - Real-time statistics and metrics
  - Tournament distribution charts
  - Category breakdown visualizations
  - Match status analysis

## Project Structure

```
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration and constants
├── utils.py                    # Utility functions for Supabase operations
├── requirements.txt            # Python dependencies
└── pages/
    ├── 01_Login.py            # Authentication page
    ├── 02_Add_Users.py        # User registration and bulk upload
    ├── 03_View_Data.py        # Data viewing and filtering
    └── 04_Analytics.py        # Analytics and visualizations
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Supabase account and project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Supabase

1. Go to [supabase.com](https://supabase.com) and create a new project
2. Navigate to **Settings → API**
3. Copy your **Project URL** and **Anon Public Key**
4. Create a `.env` file:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your_anon_key
   ```

### Step 3: Create the Database Table

In Supabase SQL Editor, run:

```sql
CREATE TABLE MainTable (
  id BIGSERIAL PRIMARY KEY,
  created_at TIMESTAMP DEFAULT NOW(),
  first_name TEXT NOT NULL,
  last_name TEXT,
  email TEXT UNIQUE NOT NULL,
  mobile TEXT NOT NULL,
  number TEXT,
  category TEXT,
  match_status TEXT,
  tournament TEXT NOT NULL,
  sabha_reference_name TEXT,
  spl_no TEXT,
  image TEXT
);

CREATE INDEX idx_email ON MainTable(email);
CREATE INDEX idx_mobile ON MainTable(mobile);
```

## Running the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

## CSV Format for Bulk Upload

```csv
first_name,last_name,email,mobile,number,category,match_status,tournament,sabha_reference_name,spl_no,image
John,Doe,john@example.com,9876543210,1,Senior,Registered,Cricket,Sabha A,SPL001,https://example.com/image.jpg
```

**Required fields:** first_name, email, mobile, category, match_status, tournament

## Troubleshooting

- **Connection Issues**: Verify `.env` file has correct SUPABASE_URL and SUPABASE_KEY
- **Authentication Errors**: Ensure Email/Password provider is enabled in Supabase
- **CSV Upload Issues**: Check that column names match (case-insensitive)
- **Performance**: Click "Refresh" button to clear data cache

---

**Happy Tournament Management! 🎉**
