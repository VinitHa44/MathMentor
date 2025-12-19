"""
Custom Styles for Math Mentor Streamlit App
"""

import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styling to the Streamlit app - Dark Mode"""
    st.markdown("""
    <style>
    /* Global Styles - Dark Mode */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main {
        padding: 0 2rem;
        background-color: #0e1117;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    h1 {
        color: #667eea;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: #8b9dc3;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    
    h3 {
        color: #a8b7d1;
        margin-top: 1.5rem;
    }
    
    /* Text colors */
    p, li, span, div {
        color: #fafafa;
    }
    
    /* Buttons */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        padding: 0.5rem 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #5568d3 0%, #65408b 100%);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1a1d24;
        padding: 0.5rem;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        background-color: #262730;
        border: 1px solid #3a3f4b;
        color: #fafafa;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #2d3139;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
    }
    
    /* File Uploader */
    .stFileUploader {
        background: #1a1d24;
        border: 2px dashed #4a5568;
        border-radius: 10px;
        padding: 1rem;
        transition: all 0.3s;
    }
    
    .stFileUploader:hover {
        border-color: #667eea;
        background: #1f2433;
    }
    
    /* Text Input & Text Area */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #262730;
        border-radius: 8px;
        border: 2px solid #3a3f4b;
        color: #fafafa;
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3);
        background-color: #2d3139;
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background-color: #262730;
        border-radius: 8px;
        border: 2px solid #3a3f4b;
        color: #fafafa;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #1a1d24;
        border-radius: 8px;
        border: 1px solid #3a3f4b;
        color: #fafafa;
        font-weight: 600;
        padding: 0.75rem 1rem;
        transition: all 0.3s;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #262730;
        border-color: #667eea;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 1rem;
        font-weight: 600;
        color: #a8b7d1;
    }
    
    /* Alert Boxes */
    .stAlert {
        border-radius: 10px;
        border: none;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Success */
    .stSuccess {
        background: linear-gradient(135deg, #1a3a2a 0%, #2d5a3f 100%);
        color: #7cffb2;
    }
    
    /* Info */
    .stInfo {
        background: linear-gradient(135deg, #1a2a3a 0%, #2d3f5a 100%);
        color: #7cd4ff;
    }
    
    /* Warning */
    .stWarning {
        background: linear-gradient(135deg, #3a3a1a 0%, #5a5a2d 100%);
        color: #ffeb7c;
    }
    
    /* Error */
    .stError {
        background: linear-gradient(135deg, #3a1a1a 0%, #5a2d2d 100%);
        color: #ff7c7c;
    }
    
    /* Multiselect */
    .stMultiSelect > div > div {
        background-color: #262730;
        border-radius: 8px;
        border: 2px solid #3a3f4b;
        color: #fafafa;
    }
    
    /* Radio Buttons */
    .stRadio > div {
        background: #1a1d24;
        padding: 1rem;
        border-radius: 8px;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Code Blocks */
    .stCodeBlock {
        background: #1a1d24;
        border-radius: 8px;
        border: 1px solid #3a3f4b;
    }
    
    /* JSON Display */
    .stJson {
        background: #1a1d24;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #3a3f4b;
        color: #fafafa;
    }
    
    /* Columns */
    [data-testid="column"] {
        padding: 0 0.5rem;
    }
    
    /* Image */
    .stImage {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    /* Audio */
    .stAudio {
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #218838 0%, #1aa179 100%);
    }
    
    /* Custom Card */
    .custom-card {
        background: #262730;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
        margin: 1rem 0;
        transition: all 0.3s;
        border: 1px solid #3a3f4b;
    }
    
    .custom-card:hover {
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
        transform: translateY(-4px);
        border-color: #667eea;
    }
    
    /* Animations */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animated {
        animation: slideIn 0.5s ease-out;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1d24;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5568d3 0%, #65408b 100%);
    }
    
    /* Footer */
    footer {
        visibility: hidden;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom Tooltip */
    .tooltip {
        position: relative;
        display: inline-block;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #262730;
        color: #fafafa;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    
    /* Loading Animation */
    @keyframes pulse {
        0% {
            transform: scale(1);
            opacity: 1;
        }
        50% {
            transform: scale(1.05);
            opacity: 0.8;
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }
    
    /* Badge */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    .badge-success {
        background: #1a3a2a;
        color: #7cffb2;
    }
    
    .badge-warning {
        background: #3a3a1a;
        color: #ffeb7c;
    }
    
    .badge-danger {
        background: #3a1a1a;
        color: #ff7c7c;
    }
    
    .badge-info {
        background: #1a2a3a;
        color: #7cd4ff;
    }
    
    .badge-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main {
            padding: 0 1rem;
        }
        
        h1 {
            font-size: 1.75rem;
        }
        
        h2 {
            font-size: 1.5rem;
        }
        
        [data-testid="column"] {
            padding: 0 0.25rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def get_color_palette():
    """Return the app's color palette - Dark Mode"""
    return {
        'primary': '#667eea',
        'secondary': '#764ba2',
        'success': '#7cffb2',
        'warning': '#ffeb7c',
        'danger': '#ff7c7c',
        'info': '#7cd4ff',
        'light': '#262730',
        'dark': '#0e1117',
        'background': '#0e1117',
        'text_primary': '#fafafa',
        'text_secondary': '#a8b7d1',
        'border': '#3a3f4b'
    }


def get_emoji_mapping():
    """Return emoji mappings for various UI elements"""
    return {
        'topics': {
            'Algebra': '📐',
            'Probability': '🎲',
            'Calculus': '📈',
            'Linear Algebra': '🔢'
        },
        'status': {
            'completed': '✅',
            'running': '⏳',
            'failed': '❌',
            'pending': '🕐'
        },
        'feedback': {
            'correct': '✅',
            'incorrect': '❌',
            'clarification': '🤔',
            'corrected': '🔄'
        },
        'confidence': {
            'high': '🟢',
            'medium': '🟡',
            'low': '🔴'
        },
        'input_modes': {
            'image': '📷',
            'audio': '🎤',
            'text': '⌨️'
        }
    }
