import streamlit as st
import home, loan_core_ml, loan_chatbot, about_me
from styles import app_styles

# Set page configuration with custom settings
st.set_page_config(
    page_title="BANK Dashboard",  # More descriptive title
    page_icon="🏦",              # Bank emoji for visual appeal
    layout="wide",               # Wide layout for better visualization
    initial_sidebar_state="expanded",  # Sidebar starts expanded
)

# Apply custom styles
app_styles()

# Sidebar Header
st.sidebar.title("Navigation 🧭")
st.sidebar.markdown("---")  # Add a divider for aesthetics

# Sidebar Navigation Options
app_mode = st.sidebar.radio(
    "Choose a section:",
    ["🏠 Home", "📊 Prediction (Traditional)", "🤖 Chatbot (GEN-AI)", "👤 About Me"],
)

# Route to pages based on sidebar selection
if app_mode == "🏠 Home":
    home.show()
elif app_mode == "📊 Prediction (Traditional)":
    loan_core_ml.show()
elif app_mode == "🤖 Chatbot (GEN-AI)":
    loan_chatbot.show()
elif app_mode == "👤 About Me":
    about_me.show()

# Footer Section (optional, for professionalism)
st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ using Streamlit | © 2025 BANK Dashboard")
