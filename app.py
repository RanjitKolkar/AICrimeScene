import streamlit as st

st.set_page_config(
    page_title="Workshop on AI in Crime Scene Investigation",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Force consistent theme across all browsers/devices ---
st.markdown("""
    <style>
    html, body, [class*="st-"], .stApp {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #003366 !important;
    }
    .stAlert {
        background-color: #e6f0ff !important;
        color: #003366 !important;
        border: 1px solid #99c2ff !important;
        border-radius: 8px;
        padding: 10px;
    }
    div[data-baseweb="tab"] {
        background-color: #f0f6ff !important;
        color: #003366 !important;
        border-radius: 6px 6px 0 0 !important;
        padding: 8px 16px !important;
        font-weight: 600;
    }
    div[data-baseweb="tab"][aria-selected="true"] {
        background-color: #003366 !important;
        color: #ffffff !important;
    }
    .stButton button {
        background-color: #1E90FF !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        color: #003366;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# ============ HEADER ============
with st.container():
    col1, col2 = st.columns([2, 5])
    with col1:
        st.image("nfsu emblem logo.png", use_container_width=True)
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <h3>National Forensic Sciences University, Goa Campus</h3>
            <h3>Workshop on</h3>
            <h2>Use of Artificial Intelligence in Crime Scene Investigation</h2>
            <p style="font-size:16px;">
                📅 <b>Tuesday, 27 January 2026</b> |
                ⏳ <b>One Day</b> |
                🏫 <b>Offline Mode</b>
            </p>
        </div>
        """, unsafe_allow_html=True)


st.markdown("---")

# ============ ABOUT ============
st.subheader("📌 About the Workshop")
st.write("""
This **one-day workshop** aims to introduce participants to the role of **Artificial Intelligence in crime scene investigation and cybercrime analysis**. The programme focuses on conceptual understanding, real-world case studies, and hands-on exposure to AI tools relevant to law enforcement and forensic professionals. This one-day workshop is designed to familiarize participants with the application of Artificial Intelligence in crime scene investigation and cybercrime analysis. The programme emphasizes a balanced approach combining conceptаoretical foundations, real-world case studies, and hands-on interaction with AI-based tools, enabling law enforcement and forensic professionals to effectively understand and apply AI-driven techniques in investigative practices.""")

# ============ OBJECTIVES ============
st.subheader("🎯 Objectives of the Workshop")
st.markdown("""
1. Introduce AI concepts relevant to crime scene investigation and cybercrime  
2. Demonstrate AI-based applications and case studies in policing  
3. Provide hands-on exposure to selected AI tools for crime analysis  
4. Discuss ethical, legal, and operational challenges of AI in law enforcement  
""")

# ============ TARGET AUDIENCE ============
st.subheader("👥 Target Audience")
st.markdown("""
- Faculty Members  
- Researchers and Research Scholars  
- Law Enforcement Officials  
- Government Professionals  
- Students interested in AI and Forensic Investigation  
""")

# ============ SCHEDULE ============
st.subheader("📅 Programme Schedule (27 January 2026)")

st.markdown("""
| Time | Session | Resource Person |
|------|--------|----------------|
| 09:30 – 10:00 AM | Registration & Welcome Tea | — |
| 10:00 – 10:30 AM | Inaugural Session |  Prof. (Dr.) Naveen Kumar Chaudhary, Director, NFSU Goa  |
| 10:30 – 11:15 AM | Introduction to AI and Cyber Crime | Dr. Ranjit Kolkar, Assistant Professor, NFSU Goa |
| 11:15 – 11:30 AM | Tea Break |
| 11:30 – 01:00 PM | AI Applications & Case Studies in Cyber Crime and Policing | Dr. Jovi D’Silva, Assistant Professor, NFSU Goa |
| 01:00 – 02:00 PM | Lunch Break |
| 02:00 – 03:15 PM | Hands-on AI Tools for Cybercrime Analysis | Dr. Ranjit Kolkar/Dr. Jovi D’Silva, Assistant Professor, NFSU Goa |
| 03:15 – 03:30 PM | Tea Break  |
| 03:30 – 04:30 PM | Panel Discussion: Ethics & Challenges in AI for Law Enforcement | Academia, Law Enforcement & Industry |
| 04:30 – 05:00 PM | Valedictory & Certificate Distribution | — |
""")

# ============ EXPECTED OUTCOMES ============
st.subheader("✅ Expected Outcomes")
st.markdown("""
- Improved understanding of AI-driven crime investigation  
- Exposure to practical AI tools used in cybercrime analysis  
- Awareness of ethical and legal considerations in AI adoption  
""")

# ============ REGISTRATION ============
st.subheader("💰 Registration Details")
st.markdown("""
- **NFSU Students/Faculties:** FREE 
- **Other College Students:** 500 /-
- **Other( Academician/ Industry Professional/ Government Officials):** 1000 /-

""")

st.info("👉 Note: Accommodation is not provided by NFSU Goa. Participants will be assisted in identifying nearby accommodation if required.")

st.markdown("""
<a href="https://forms.gle/Mce8Kd5rJoDPdXCR8" target="_blank">
<button style="background-color:#1E90FF;color:white;padding:12px 24px;border:none;border-radius:8px;font-size:16px;">
📌 Register Here
</button>
</a>
""", unsafe_allow_html=True)

# ============ ORGANIZING COMMITTEE ============
st.subheader("👥 Organizing Committee")
st.markdown("""
<div class="highlight-box">
<b>Chief Patron:</b> Dr. J. M. Vyas, Hon'ble Vice-Chancellor, NFSU <br>
<b>Chair:</b> Prof. (Dr.) Naveen Kumar Chaudhary, Director, NFSU Goa  <br>
<b>Co-Chair:</b> Dr. Lokesh Chouhan, Dean Academics, NFSU Goa  <br>
<b>Coordinator / Convener:</b> Dr. Ranjit Kolkar<br>
<b>Co-Coordinators:</b> Dr. Jovi D’Silva<br>
""", unsafe_allow_html=True)




# ============ FOOTER ============
st.markdown("---")
st.markdown('<div class="footer">Contact <br><b><href>ranjit.kolkar@nfsu.ac.in</href></b>  Mobile:<b>8618879217</b>,<br><b><href>jovi.dsilva@nfsu.ac.in</href></b>  Mobile:<b>77740 97231</b></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">📍 Organized by <b>National Forensic Sciences University, Goa Campus</b></div>', unsafe_allow_html=True)
