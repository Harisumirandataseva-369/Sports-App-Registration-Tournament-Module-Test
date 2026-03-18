# Deployment Guide for Streamlit Cloud

## Step 1: Prepare Your Repository

1. Push your code to GitHub:
```bash
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
git push origin main
```

2. Ensure `.env` file is in `.gitignore` ✅ (it already is)

## Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repository
4. Select `main` branch
5. Select `app.py` as main file
6. Click "Deploy"

## Step 3: Add Secrets

1. Once deployed, go to your app's settings (click 3 dots)
2. Click "Settings" → "Secrets"
3. Paste your secrets in TOML format:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your_anon_key_here"
```

4. Click "Save"

## Files Included for Deployment

- `.gitignore` - Excludes .env and sensitive files ✅
- `requirements.txt` - All dependencies ✅
- `.streamlit/config.toml` - Streamlit settings ✅
- `.streamlit/secrets.toml` - Secrets template ✅

## Troubleshooting Deployment Issues

### Issue: "ModuleNotFoundError"
**Solution:** Check that all imports in requirements.txt are correct. Run locally:
```bash
pip install -r requirements.txt
```

### Issue: "Secrets not loading"
**Solution:** Ensure secrets are added in Streamlit Cloud dashboard (Settings → Secrets), not in code

### Issue: "Supabase connection error"
**Solution:** Verify SUPABASE_URL and SUPABASE_KEY in Secrets match your actual values

### Issue: "Port already in use"
**Solution:** Not an issue on Streamlit Cloud - it handles port management

## Streamlit Cloud Features

- Free tier available
- Auto-deploys on GitHub push
- Free SSL certificate
- Community support
- Docker container runs your app

## Performance Tips for Cloud

1. **Use caching** - All caching is already implemented ✅
2. **Optimize data loading** - Pagination is already implemented ✅
3. **Filter large datasets** - Filters are already available ✅
4. **Regular maintenance** - Archive old data periodically

## Post-Deployment

After successful deployment:
- Test all login flows
- Test user addition (single & bulk)
- Test data filtering
- Test analytics charts
- Export test data

Your app URL will be: `https://[your-username]-[repo-name].streamlit.app`

---

**Deployment Complete! 🎉**
