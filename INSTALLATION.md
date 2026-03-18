# Installation & Setup Guide

## Quick Start (Windows)

1. **Extract the project** to your desired location

2. **Double-click `run.bat`** to start the application
   - This will automatically:
     - Create Python virtual environment
     - Install all dependencies
     - Launch the Streamlit app

3. **Configure `.env` file**:
   - Copy `.env.example` to `.env`
   - Add your Supabase credentials

4. **Create database table** in Supabase (see Setup Instructions below)

---

## Detailed Setup Instructions

### 1. Install Python

- Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
- During installation, check **"Add Python to PATH"**
- Verify installation:
  ```bash
  python --version
  ```

### 2. Create Project Directory

```bash
cd Documents
git clone <your-repo-link>
# or extract the ZIP file
```

### 3. Setup Supabase

#### Create Project
1. Go to [supabase.com](https://supabase.com)
2. Click "New Project"
3. Fill in project details and create
4. Wait for project to initialize (2-3 minutes)

#### Get API Credentials
1. Navigate to **Settings → API**
2. Copy **Project URL** (starts with https://)
3. Copy **Anon (Public)** key
4. Paste into `.env` file:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=eyJhbGc...
   ```

#### Create Database Table
1. Go to **SQL Editor**
2. Click "New Query"
3. Paste this SQL and execute:

```sql
-- Create main table
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

-- Create indexes for performance
CREATE INDEX idx_email ON MainTable(email);
CREATE INDEX idx_mobile ON MainTable(mobile);
CREATE INDEX idx_category ON MainTable(category);
CREATE INDEX idx_tournament ON MainTable(tournament);
CREATE INDEX idx_status ON MainTable(match_status);
```

#### Enable Authentication
1. Go to **Authentication → Providers**
2. Make sure **Email/Password** is enabled
3. Go to **URL Configuration**
4. Set your domain (for local development, set to `http://localhost:3000`)

### 4. Install Dependencies

```bash
# Navigate to project directory
cd Sports-App-Registration-Tournament-Module-Test

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 5. Run Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
# Make sure virtual environment is activated
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Then install:
pip install -r requirements.txt
```

### Issue: ".env file not found" or credentials not loading

**Solution:**
1. Create `.env` file in project root:
   ```bash
   copy .env.example .env  # Windows
   cp .env.example .env    # macOS/Linux
   ```
2. Edit `.env` with your Supabase credentials
3. Restart the app

### Issue: "Invalid Supabase credentials" error

**Solution:**
1. Verify `.env` file exists in project root directory
2. Check credentials are correct:
   - `SUPABASE_URL` - should start with `https://`
   - `SUPABASE_KEY` - should be 100+ characters
3. Ensure Supabase project is running
4. Test connection in Supabase dashboard

### Issue: "Email already exists" when registering

**Solution:**
- This email is already registered. Use a different email or login with existing credentials

### Issue: CSV upload fails

**Solution:**
1. Check column names match (case-insensitive):
   - All required: `first_name`, `email`, `mobile`, `category`, `match_status`, `tournament`
   - Optional: all others
2. Ensure all rows have required fields
3. Check email addresses are unique
4. Verify file encoding is UTF-8

### Issue: Data not showing in View Data page

**Solution:**
1. Click **"Refresh Data"** button to clear cache
2. Check if users were actually added (check Add Users page)
3. Verify database table `MainTable` exists in Supabase
4. Check Supabase table has data

### Issue: Application runs slow with many records

**Solution:**
1. Click **"Refresh"** button to clear cache
2. Filter data to smaller date ranges
3. In Supabase, ensure all indexes are created
4. Consider adding more indexes for filtered columns

### Issue: "Port 8501 already in use"

**Solution:**
```bash
# Windows: Find process using port 8501
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# macOS/Linux: Find and kill process
lsof -i :8501
kill -9 <PID>

# Or use different port
streamlit run app.py --server.port 8502
```

### Issue: Login page shows but buttons don't work

**Solution:**
1. Check browser console for errors (F12)
2. Verify Supabase credentials in `.env`
3. Ensure Email/Password provider is enabled in Supabase
4. Clear browser cache and reload

---

## System Requirements

- **OS**: Windows 7+, macOS 10.12+, Linux (Ubuntu 14.04+)
- **Python**: 3.8 or higher
- **RAM**: 512 MB minimum (1 GB recommended)
- **Disk Space**: 500 MB free
- **Internet**: Required (for Supabase connection)

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Supabase Auth
- **Data Analysis**: Pandas
- **Visualizations**: Plotly

## Performance Tips

1. **Use filters** - Narrow down data instead of loading everything
2. **Enable caching** - App caches data for 60 seconds
3. **Export to CSV** - For large reports, export and open in Excel
4. **Clean up old data** - Archive past tournament data
5. **Add indexes** - In Supabase, add indexes to frequently filtered columns

## Security Tips

1. **Never share `.env` file** - Contains sensitive credentials
2. **Use strong passwords** - For Supabase account and user accounts
3. **Enable Row Level Security (RLS)** - In production deployment
4. **Regular backups** - Export data regularly
5. **Keep packages updated** - Run `pip install --upgrade -r requirements.txt`

## Getting Help

1. Check the Troubleshooting section above
2. Review Streamlit documentation: https://docs.streamlit.io
3. Check Supabase docs: https://supabase.com/docs
4. Check browser console: Press F12 in browser
5. Review logs: Check terminal output for error messages

## Next Steps

1. ✅ Complete the setup above
2. ✅ Create a test account
3. ✅ Add a test user manually
4. ✅ Test bulk upload with sample CSV
5. ✅ Verify analytics dashboard works
6. ✅ Export data to CSV

---

**Happy Tournament Management! 🎉**
