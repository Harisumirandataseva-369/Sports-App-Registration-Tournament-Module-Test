import streamlit as st
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY, TABLE_NAME
import pandas as pd
from typing import Optional, List, Dict
import io

@st.cache_resource
def init_supabase() -> Client:
    """Initialize Supabase client"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase_client() -> Client:
    """Get Supabase client from cache"""
    return init_supabase()

def authenticate_user(email: str, password: str) -> Dict:
    """Authenticate user with Supabase"""
    try:
        supabase = get_supabase_client()
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return {"success": True, "user": response.user}
    except Exception as e:
        return {"success": False, "error": str(e)}

def sign_up_user(email: str, password: str) -> Dict:
    """Sign up new user"""
    try:
        supabase = get_supabase_client()
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        return {"success": True, "user": response.user}
    except Exception as e:
        return {"success": False, "error": str(e)}

def sign_out_user():
    """Sign out user"""
    try:
        supabase = get_supabase_client()
        supabase.auth.sign_out()
        return True
    except:
        return False

def add_user(user_data: Dict) -> Dict:
    """Add single user to database"""
    try:
        supabase = get_supabase_client()
        response = supabase.table(TABLE_NAME).insert(user_data).execute()
        return {"success": True, "data": response.data}
    except Exception as e:
        return {"success": False, "error": str(e)}

def add_bulk_users(users_data: List[Dict]) -> Dict:
    """Add multiple users to database"""
    try:
        supabase = get_supabase_client()
        response = supabase.table(TABLE_NAME).insert(users_data).execute()
        return {"success": True, "count": len(response.data), "data": response.data}
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_all_users() -> pd.DataFrame:
    """Fetch all users from database"""
    try:
        supabase = get_supabase_client()
        response = supabase.table(TABLE_NAME).select("*").execute()
        df = pd.DataFrame(response.data)
        return df
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return pd.DataFrame()

def get_users_with_filters(filters: Dict) -> pd.DataFrame:
    """Fetch users with filters applied"""
    try:
        supabase = get_supabase_client()
        query = supabase.table(TABLE_NAME).select("*")
        
        for column, value in filters.items():
            if value and value != "All":
                query = query.eq(column, value)
        
        response = query.execute()
        df = pd.DataFrame(response.data)
        return df
    except Exception as e:
        st.error(f"Error fetching filtered data: {str(e)}")
        return pd.DataFrame()

def delete_user(user_id: int) -> Dict:
    """Delete user by ID"""
    try:
        supabase = get_supabase_client()
        response = supabase.table(TABLE_NAME).delete().eq("id", user_id).execute()
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def update_user(user_id: int, user_data: Dict) -> Dict:
    """Update user information"""
    try:
        supabase = get_supabase_client()
        response = supabase.table(TABLE_NAME).update(user_data).eq("id", user_id).execute()
        return {"success": True, "data": response.data}
    except Exception as e:
        return {"success": False, "error": str(e)}

def parse_csv_to_dict(csv_file) -> List[Dict]:
    """Parse uploaded CSV file to list of dictionaries"""
    try:
        df = pd.read_csv(csv_file)
        # Convert column names to lowercase and replace spaces with underscores
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        return df.to_dict('records')
    except Exception as e:
        st.error(f"Error parsing CSV: {str(e)}")
        return []

def export_data_to_csv(df: pd.DataFrame) -> bytes:
    """Convert DataFrame to CSV bytes"""
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue().encode()
