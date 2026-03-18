import streamlit as st
import pandas as pd
from utils import add_user, add_bulk_users, parse_csv_to_dict
from datetime import datetime

st.set_page_config(page_title="Add Users", page_icon="👥", layout="wide")

# Check authentication
if not st.session_state.get("authenticated"):
    st.warning("Please login first!")
    st.switch_page("pages/01_Login.py")

st.title("👥 Add Users")
st.markdown("---")

# Create tabs for single and bulk upload
tab1, tab2 = st.tabs(["Add Single User", "Bulk Upload"])

with tab1:
    st.subheader("Register a Single Participant")
    
    with st.form("single_user_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name *")
            email = st.text_input("Email *")
            mobile = st.text_input("Mobile Number *")
            category = st.selectbox("Category", 
                ["Select", "Junior", "Senior", "Professional", "Amateur"])
            
        with col2:
            last_name = st.text_input("Last Name *")
            number = st.text_input("Number")
            match_status = st.selectbox("Match Status", 
                ["Select", "Registered", "Pending", "Confirmed", "Cancelled"])
            spl_no = st.text_input("SPL No")
        
        tournament = st.selectbox("Tournament *", 
            ["Select", "Cricket", "Badminton", "Table Tennis", "Football"])
        sabha_reference_name = st.text_input("Sabha Reference Name")
        image_url = st.text_input("Image URL")
        
        submit_button = st.form_submit_button("Register User", use_container_width=True)
        
        if submit_button:
            # Validate required fields
            if not all([first_name, email, mobile, tournament, category, match_status]):
                st.error("Please fill in all required fields (marked with *)")
            else:
                user_data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "mobile": mobile,
                    "number": number if number else None,
                    "category": category,
                    "match_status": match_status,
                    "tournament": tournament,
                    "sabha_reference_name": sabha_reference_name,
                    "spl_no": spl_no if spl_no else None,
                    "image": image_url if image_url else None
                }
                
                with st.spinner("Adding user..."):
                    result = add_user(user_data)
                    if result["success"]:
                        st.success(f"✅ {first_name} {last_name} registered successfully!")
                        st.balloons()
                    else:
                        st.error(f"Failed to add user: {result['error']}")

with tab2:
    st.subheader("Bulk Upload Participants")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Upload a CSV file with the following columns:**
        - first_name (required)
        - last_name
        - email (required)
        - mobile (required)
        - number
        - category (required)
        - match_status (required)
        - tournament (required)
        - sabha_reference_name
        - spl_no
        - image
        """)
    
    with col2:
        # Download sample template
        sample_data = {
            "first_name": ["John"],
            "last_name": ["Doe"],
            "email": ["john@example.com"],
            "mobile": ["9876543210"],
            "number": ["1"],
            "category": ["Senior"],
            "match_status": ["Registered"],
            "tournament": ["Cricket"],
            "sabha_reference_name": ["Sabha A"],
            "spl_no": ["SPL001"],
            "image": ["https://example.com/image.jpg"]
        }
        sample_df = pd.DataFrame(sample_data)
        csv = sample_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Template",
            data=csv,
            file_name="template.csv",
            mime="text/csv"
        )
    
    st.divider()
    
    uploaded_file = st.file_uploader("Choose CSV file", type="csv")
    
    if uploaded_file is not None:
        # Preview the file
        df = pd.read_csv(uploaded_file)
        st.subheader("Preview")
        st.dataframe(df, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Records", len(df))
        
        if st.button("✅ Upload All Records", use_container_width=True):
            # Parse and validate
            users_data = parse_csv_to_dict(uploaded_file)
            
            if users_data:
                with st.spinner(f"Uploading {len(users_data)} records..."):
                    result = add_bulk_users(users_data)
                    if result["success"]:
                        st.success(f"✅ Successfully uploaded {result['count']} records!")
                        st.balloons()
                    else:
                        st.error(f"Upload failed: {result['error']}")
            else:
                st.error("No valid data to upload")
