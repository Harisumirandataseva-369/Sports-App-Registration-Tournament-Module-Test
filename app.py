import streamlit as st
from utils import sign_out_user

# Page configuration
st.set_page_config(
    page_title="Sports Tournament Registration",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user = None

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton button {
        width: 100%;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 Sports Tournament Registration System")

# Sidebar
with st.sidebar:
    st.markdown("### 🏆 Registration System")
    st.divider()
    
    if st.session_state.authenticated:
        st.success(f"✅ Logged in")
        st.caption(f"User: {st.session_state.user}")
        if st.button("🔓 Logout", use_container_width=True):
            sign_out_user()
            st.session_state.authenticated = False
            st.session_state.user = None
            st.rerun()
    else:
        st.info("🔒 Please login to continue")
    
    st.divider()

# Main content
if not st.session_state.authenticated:
    # Show login page
    st.markdown("### Welcome to the Registration Portal")
    st.info("👈 Please use the **Login** page from the sidebar to get started")
    
else:
    # Show dashboard
    st.markdown("### Dashboard")
    st.markdown("""
    Welcome to the Sports Tournament Registration System!
    
    **Quick Links:**
    - 👥 **Add Users** - Register individual participants or upload multiple users
    - 📊 **View Data** - Search and filter registered participants  
    - 📈 **Analytics** - View statistics and insights about registrations
    
    ---
    
    **Features:**
    - 🔐 Secure authentication via Supabase
    - 👤 Add users one by one or in bulk from CSV files
    - 🔍 Advanced filtering and search capabilities
    - 📊 Real-time analytics and visualizations
    - 📥 Export data to CSV format
    """)
