import streamlit as st

def app_styles():
    # Custom CSS for styling the sidebar
    st.markdown("""
        <style>
            /* Sidebar styling */
            [data-testid="stSidebar"] {
                background-color: #F8F9FA;  /* Light gray background */
                color: #343A40;  /* Dark gray text */
                padding: 20px;
                border-right: 1px solid #E9ECEF;
            }
            [data-testid="stSidebar"] h1 {
                color: #007BFF;  /* Bootstrap blue for header */
            }
            [data-testid="stSidebar"] label {
                font-size: 18px;  /* Larger font for labels */
                font-weight: bold;  /* Bold font for labels */
            }
            [data-testid="stSidebar"] .css-1jxswup {  /* Custom class for radio buttons */
                color: #6C757D;  /* Subtle gray text */
            }
            /* Sidebar hover effect for radio options */
            [data-testid="stSidebar"] .css-1jxswup:hover {
                color: #495057;  /* Darker gray on hover */
                cursor: pointer;
            }
            /* Sidebar border and shadow */
            [data-testid="stSidebar"] {
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)


def apply_styles():
    st.markdown("""
        <style>
        .stApp {
            background-color: #FFFFFF;  /* White background */
            color: #212529;  /* Black font */
        }

        .chat-container {
            background: linear-gradient(145deg, #F8F9FA, #E9ECEF);  /* Light gray gradient */
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 1rem;
        }

        .chat-message {
            background-color: #F1F3F5;  /* Slightly darker gray */
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            border: 1px solid #DEE2E6;
        }

        .risk-low {
            background: linear-gradient(145deg, #28A745, #218838);  /* Green tones */
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }

        .risk-high {
            background: linear-gradient(145deg, #DC3545, #C82333);  /* Red tones */
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }

        .stButton > button {
            background: linear-gradient(90deg, #007BFF, #0056B3);  /* Blue gradient */
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background: linear-gradient(90deg, #0056B3, #004085);
            transform: translateY(-2px);
        }

        .stTextInput > div > div > input {
            background-color: #F8F9FA;  /* Light gray */
            color: #212529;  /* Black text */
            border: 1px solid #CED4DA;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)


def core_ml_apply_styles():
    st.markdown("""
        <style>
        /* Main theme and container styles */
        .stApp {
            background-color: #FFFFFF;  /* White background */
            color: #212529;  /* Black text */
        }
        
        .main-container {
            background: linear-gradient(145deg, #F8F9FA, #E9ECEF);  /* Subtle light gradient */
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }
        
        /* Risk assessment indicators */
        .risk-low {
            background: linear-gradient(145deg, #28A745, #218838);  /* Green tones */
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(40, 167, 69, 0.2);
            text-align: center;
            font-size: 1.2rem;
            margin: 1rem 0;
        }
        
        .risk-high {
            background: linear-gradient(145deg, #DC3545, #C82333);  /* Red tones */
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(220, 53, 69, 0.2);
            text-align: center;
            font-size: 1.2rem;
            margin: 1rem 0;
        }
        
        /* Input field styling */
        .stNumberInput, .stSlider, .stSelectbox {
            background-color: #F8F9FA;  /* Light background */
            border-radius: 6px;
            padding: 0.5rem;
            margin: 0.5rem 0;
            border: 1px solid #CED4DA;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(90deg, #007BFF, #0056B3);  /* Blue gradient */
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton > button:hover {
            background: linear-gradient(90deg, #0056B3, #004085);
            transform: translateY(-2px);
        }
        
        /* Section headers */
        .section-header {
            background: linear-gradient(90deg, #6C757D, #343A40);  /* Darker gray header */
            padding: 1rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            font-weight: bold;
            color: white;
        }
        
        </style>
    """, unsafe_allow_html=True)
