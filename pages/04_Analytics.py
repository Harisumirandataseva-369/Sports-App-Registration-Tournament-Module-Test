import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import get_all_users

st.set_page_config(page_title="Analytics", page_icon="📈", layout="wide")

# Check authentication
if not st.session_state.get("authenticated"):
    st.warning("Please login first!")
    st.switch_page("pages/01_Login.py")

st.title("📈 Analytics Dashboard")
st.markdown("---")

# Fetch data
@st.cache_data(ttl=60)
def fetch_data():
    return get_all_users()

if st.button("🔄 Refresh"):
    st.cache_data.clear()
    st.rerun()

df = fetch_data()

if df.empty:
    st.warning("No data available. Please add users first!")
else:
    # Summary metrics
    st.subheader("Summary Metrics")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Participants", len(df))
    with col2:
        st.metric("Tournaments", df["tournament"].nunique() if "tournament" in df.columns else 0)
    with col3:
        st.metric("Categories", df["category"].nunique() if "category" in df.columns else 0)
    with col4:
        registered = len(df[df["match_status"] == "Registered"]) if "match_status" in df.columns else 0
        st.metric("Registered", registered)
    with col5:
        pending = len(df[df["match_status"] == "Pending"]) if "match_status" in df.columns else 0
        st.metric("Pending", pending)
    
    st.divider()
    
    # Charts
    col1, col2 = st.columns(2)
    
    # Tournament Distribution
    if "tournament" in df.columns:
        with col1:
            st.subheader("Participants by Tournament")
            tournament_counts = df["tournament"].value_counts()
            fig_tournament = px.pie(
                values=tournament_counts.values,
                names=tournament_counts.index,
                title="Distribution of Participants"
            )
            st.plotly_chart(fig_tournament, use_container_width=True)
    
    # Category Distribution
    if "category" in df.columns:
        with col2:
            st.subheader("Participants by Category")
            category_counts = df["category"].value_counts()
            fig_category = px.bar(
                x=category_counts.index,
                y=category_counts.values,
                labels={"x": "Category", "y": "Count"},
                title="Participants per Category"
            )
            st.plotly_chart(fig_category, use_container_width=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    # Match Status Distribution
    if "match_status" in df.columns:
        with col1:
            st.subheader("Participants by Status")
            status_counts = df["match_status"].value_counts()
            fig_status = px.bar(
                x=status_counts.index,
                y=status_counts.values,
                labels={"x": "Status", "y": "Count"},
                title="Participants by Match Status",
                color=status_counts.index,
                color_discrete_map={
                    "Registered": "#2ecc71",
                    "Pending": "#f39c12",
                    "Confirmed": "#3498db",
                    "Cancelled": "#e74c3c"
                }
            )
            st.plotly_chart(fig_status, use_container_width=True)
    
    # Tournament vs Category
    if "tournament" in df.columns and "category" in df.columns:
        with col2:
            st.subheader("Tournament vs Category Breakdown")
            cross_tab = pd.crosstab(df["tournament"], df["category"])
            fig_cross = px.imshow(
                cross_tab,
                labels=dict(x="Category", y="Tournament", color="Count"),
                title="Heatmap: Tournament & Category",
                color_continuous_scale="YlOrRd"
            )
            st.plotly_chart(fig_cross, use_container_width=True)
    
    st.divider()
    
    # Detailed breakdown
    st.subheader("Detailed Breakdown")
    
    tab1, tab2, tab3 = st.tabs(["By Tournament", "By Category", "By Status"])
    
    with tab1:
        if "tournament" in df.columns:
            tournament_breakdown = df.groupby("tournament").size().reset_index(name="Count")
            st.dataframe(tournament_breakdown, use_container_width=True)
    
    with tab2:
        if "category" in df.columns:
            category_breakdown = df.groupby("category").size().reset_index(name="Count")
            st.dataframe(category_breakdown, use_container_width=True)
    
    with tab3:
        if "match_status" in df.columns:
            status_breakdown = df.groupby("match_status").size().reset_index(name="Count")
            st.dataframe(status_breakdown, use_container_width=True)
    
    st.divider()
    
    # Advanced Analytics
    st.subheader("Advanced Analytics")
    
    if "tournament" in df.columns and "category" in df.columns:
        st.write("**Top Combinations (Tournament + Category)**")
        combinations = df.groupby(["tournament", "category"]).size().reset_index(name="Count").sort_values("Count", ascending=False)
        st.dataframe(combinations.head(10), use_container_width=True)
    
    # Email Distribution
    if "email" in df.columns:
        unique_emails = df["email"].nunique()
        st.metric("Unique Email Addresses", unique_emails)
    
    # Mobile Distribution
    if "mobile" in df.columns:
        unique_mobiles = df["mobile"].nunique()
        st.metric("Unique Mobile Numbers", unique_mobiles)
