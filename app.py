import streamlit as st
import hashlib
import os

def load_css_file(file_path="styles/default.css"):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

st.set_page_config(
    page_title="Grocery ML App", 
    page_icon="🛒", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple login system
def login():
    st.markdown("""
    <div style='text-align: center; padding: 50px 20px;'>
        <h1 style='color: #0099b5; font-size: 3em;'>🛒 Apex Sales Intelligence</h1>
        <p style='font-size: 1.2em; color: #2c3e50;'>Smart Analytics for Grocery Stores</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        with st.container():
            st.markdown("<div style='padding: 30px; background: rgba(255,255,255,0.95); border-radius: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.1);'>", unsafe_allow_html=True)
            
            st.subheader("🔐 Login to Dashboard")
            username = st.text_input("👤 Username", placeholder="Enter your username")
            password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")

            def hash_pw(pw):
                return hashlib.sha256(pw.encode()).hexdigest()

            users = {
                "admin": hash_pw("1234"),
                "demo": hash_pw("demo"),
                "user": hash_pw("password")
            }

            if st.button("🚀 Login", use_container_width=True):
                if username in users and users[username] == hash_pw(password):
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.success("✅ Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
                    
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Login credentials info
            with st.expander("ℹ️ Demo Credentials"):
                st.write("**Username:** `admin` | **Password:** `1234`")
                st.write("**Username:** `demo` | **Password:** `demo`")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

# Main application after login
def main_app():
    # Sidebar navigation
    st.sidebar.markdown(f"""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #0099b5, #1e8e3e); border-radius: 10px; margin-bottom: 20px;'>
        <h3 style='color: white; margin: 0;'>🛒 Apex Sales</h3>
        <p style='color: white; margin: 0; font-size: 0.8em;'>Welcome, {st.session_state.get('username', 'User')}!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.sidebar.title("📊 Navigation")
    
    # Page selection
    page = st.sidebar.radio(
        "Go to:",
        ["🏠 Dashboard"],
        index=0
    )
    
    # Logout button
    if st.sidebar.button("🚪 Logout", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()
    
    # Display selected page
    if page == "🏠 Dashboard":
        show_dashboard()
    elif page == "📁 Upload Data":
        import page1
        page1.load_page()
    elif page == "🔧 Column Mapping":
        import page2
        page2.load_page()
    elif page == "📈 Sales Dashboard":
        import page3
        page3.load_page()
    elif page == "🤖 Sales Prediction":
        import page4
        page4.load_page()
    elif page == "👥 About Us":
        import page5
        page5.load_page()

def show_dashboard():
    st.title("🏠 Dashboard Overview")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #0099b5, #1e8e3e); padding: 30px; border-radius: 15px; color: white; text-align: center;'>
        <h2>Welcome to Apex Sales Intelligence! 👋</h2>
        <p>Your complete solution for grocery store analytics and sales forecasting</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📊 Data Ready", "Upload & Map", "Step 1-2")
    with col2:
        st.metric("📈 Analytics", "View Dashboard", "Step 3")
    with col3:
        st.metric("🤖 Predictions", "Sales Forecast", "Step 4")
    
    st.markdown("---")
    
    st.subheader("🚀 Quick Start Guide")
    
    steps = [
        {"icon": "📁", "title": "Upload Data", "desc": "Upload your CSV sales data file"},
        {"icon": "🔧", "title": "Map Columns", "desc": "Match your CSV columns to app fields"},
        {"icon": "📊", "title": "View Analytics", "desc": "Explore sales insights and trends"},
        {"icon": "🤖", "title": "Predict Sales", "desc": "Get AI-powered sales forecasts"}
    ]
    
    cols = st.columns(4)
    for i, step in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div style='text-align: center; padding: 20px; background: white; border-radius: 10px; border: 2px solid #0099b5;'>
                <h1>{step['icon']}</h1>
                <h4>{step['title']}</h4>
                <p>{step['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# Run the main app
main_app()
