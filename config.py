import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE_NAME = "MainTable"

# Column definitions
COLUMNS = {
    "Match Status": "match_status",
    "Tournament": "tournament",
    "First Name": "first_name",
    "Last Name": "last_name",
    "Number": "number",
    "Email": "email",
    "Mobile": "mobile",
    "Sabha Reference Name": "sabha_reference_name",
    "SPL No": "spl_no",
    "Category": "category",
    "Image": "image"
}
