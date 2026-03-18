import streamlit as st
import pandas as pd
from utils import get_users_with_filters, get_all_users, delete_user, update_user, export_data_to_csv

st.set_page_config(page_title="View Data", page_icon="📊", layout="wide")

# Check authentication
if not st.session_state.get("authenticated"):
    st.warning("Please login first!")
    st.switch_page("pages/01_Login.py")

st.title("📊 View & Filter Data")
st.markdown("---")

# Fetch all data
@st.cache_data(ttl=60)
def fetch_data():
    return get_all_users()

if st.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

# Get data
df = fetch_data()

if df.empty:
    st.warning("No data available. Please add users first!")
else:
    # Create filter section
    st.subheader("Filters")
    
    col1, col2, col3, col4 = st.columns(4)
    
    filters = {}
    
    with col1:
        tournament_filter = st.multiselect(
            "Tournament",
            options=df["tournament"].unique() if "tournament" in df.columns else [],
            key="tournament_filter"
        )
        if tournament_filter:
            filters["tournament"] = tournament_filter
    
    with col2:
        category_filter = st.multiselect(
            "Category",
            options=df["category"].unique() if "category" in df.columns else [],
            key="category_filter"
        )
        if category_filter:
            filters["category"] = category_filter
    
    with col3:
        status_filter = st.multiselect(
            "Match Status",
            options=df["match_status"].unique() if "match_status" in df.columns else [],
            key="status_filter"
        )
        if status_filter:
            filters["match_status"] = status_filter
    
    with col4:
        search_name = st.text_input("Search by Name", key="search_name")
    
    # Apply filters
    filtered_df = df.copy()
    
    if filters:
        for column, values in filters.items():
            if column in filtered_df.columns:
                filtered_df = filtered_df[filtered_df[column].isin(values)]
    
    if search_name:
        filtered_df = filtered_df[
            (filtered_df["first_name"].str.contains(search_name, case=False, na=False)) |
            (filtered_df["last_name"].str.contains(search_name, case=False, na=False))
        ]
    
    # Display statistics
    st.subheader("Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", len(filtered_df))
    with col2:
        st.metric("Tournaments", df["tournament"].nunique() if "tournament" in df.columns else 0)
    with col3:
        st.metric("Categories", df["category"].nunique() if "category" in df.columns else 0)
    with col4:
        st.metric("Mobile Numbers", df["mobile"].nunique() if "mobile" in df.columns else 0)
    
    st.divider()
    
    # Display table
    st.subheader(f"Data ({len(filtered_df)} records)")
    
    # Reorder columns for better display
    column_order = [col for col in [
        "id", "first_name", "last_name", "email", "mobile", "tournament", 
        "category", "match_status", "number", "sabha_reference_name", "spl_no", "image"
    ] if col in filtered_df.columns]
    
    display_df = filtered_df[column_order]
    
    # Display with pagination
    items_per_page = st.selectbox("Items per page", [10, 25, 50, 100], index=0)
    
    total_pages = (len(filtered_df) - 1) // items_per_page + 1 if len(filtered_df) > 0 else 1
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        page = st.number_input("Page", min_value=1, max_value=total_pages, value=1)
    
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    st.dataframe(
        display_df.iloc[start_idx:end_idx],
        use_container_width=True,
        height=400
    )
    
    st.caption(f"Showing {start_idx + 1} to {min(end_idx, len(filtered_df))} of {len(filtered_df)} records")
    
    # Export options
    st.divider()
    st.subheader("Export")
    
    col1, col2 = st.columns(2)
    
    with col1:
        csv_data = display_df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv_data,
            file_name="participants_data.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col2:
        # Excel export (requires openpyxl)
        try:
            excel_data = export_data_to_csv(display_df)
            st.download_button(
                label="📥 Download as Excel",
                data=excel_data,
                file_name="participants_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        except:
            pass
