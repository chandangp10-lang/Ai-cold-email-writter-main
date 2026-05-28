import streamlit as st
import json
import os
import http.client
import base64
from dotenv import load_dotenv
load_dotenv("deep.env")

st.set_page_config(page_title="AI Cold Email Writer", page_icon="", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Epilogue:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Epilogue', sans-serif;
    background-color: #1a0010;
    color: #ffe0f0;
}
.stApp {
    background: radial-gradient(ellipse at top, #2d0a1e 0%, #1a0010 60%, #0d000a 100%) !important;
}

/* ── Hero ── */
.hero {
    padding: 1rem 1rem 0.5rem;
    text-align: center;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #ff69b4, #ff1493, #ffb6d9);
    -webkit-
    -webkit-text-fill-color: transparent;
    
    animation: fadeInDown 0.8s ease forwards;
}
.hero-sub {
    color: #d47fa6;
    font-size: 1rem;
    margin-top: 0.3rem;
    animation: fadeIn 1.4s ease forwards;
}
.hero-img {
    animation: float 4s ease-in-out infinite;
    display: block;
    margin: 0 auto;
}

/* ── Animations ── */
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes float {
    0%, 100% { transform: translateY(0px);   filter: drop-shadow(0 8px 24px rgba(255,105,180,0.4)); }
    50%       { transform: translateY(-10px); filter: drop-shadow(0 16px 32px rgba(255,20,147,0.5)); }
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes sparkle {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.4; transform: scale(0.8); }
}

/* ── Inputs ── */
.stTextArea textarea, .stTextInput input {
    background: #2d0a1e !important;
    border: 1.5px solid #7a1a4a !important;
    border-radius: 10px !important;
    color: #ffe0f0 !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: #ff69b4 !important;
    box-shadow: 0 0 0 3px rgba(255,105,180,0.2) !important;
}
.stTextArea label, .stTextInput label {
    color: #d47fa6 !important;
    font-weight: 500 !important;
}
.stSelectbox label { color: #d47fa6 !important; }
.stSelectbox > div > div {
    background: #2d0a1e !important;
    border: 1.5px solid #7a1a4a !important;
    color: #ffe0f0 !important;
    border-radius: 10px !important;
}

/* ── Button ── */
.stButton > button {
    background: linear-gradient(135deg, #7a1a4a, #ff1493, #ff69b4) !important;
    color: white !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 12px !important;
    width: 100% !important;
    padding: 0.8rem !important;
    font-size: 1rem !important;
    letter-spacing: 0.03em !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 24px rgba(255,20,147,0.4) !important;
}

/* ── Result card ── */
.result-card {
    background: linear-gradient(135deg, #2d0a1e, #1f0515);
    border: 1.5px solid #7a1a4a;
    border-radius: 16px;
    padding: 1.8rem;
    margin-top: 1rem;
    animation: slideUp 0.6s ease forwards;
    box-shadow: 0 4px 24px rgba(255,20,147,0.15);
}

/* ── Divider ── */
hr { border-color: #4a1030 !important; }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    color: #7a1a4a;
    font-size: 0.82rem;
}
.footer span { color: #ff69b4; }

/* ── Floating sparkles ── */
.sparkle1 { position: fixed; top: 10%; left: 5%;  font-size: 1.2rem; animation: sparkle 2s infinite; color: #ff69b4; }
.sparkle2 { position: fixed; top: 20%; right: 5%; font-size: 0.9rem; animation: sparkle 2.5s infinite 0.5s; color: #ffb6d9; }
.sparkle3 { position: fixed; top: 70%; left: 3%;  font-size: 1rem;   animation: sparkle 3s infinite 1s; color: #ff1493; }
.sparkle4 { position: fixed; top: 80%; right: 4%; font-size: 0.8rem; animation: sparkle 2.2s infinite 0.3s; color: #ff69b4; }

#MainMenu, footer, header { visibility: hidden; }
</style>

<!-- Floating sparkles -->
<div class="sparkle1">✦</div>
<div class="sparkle2">✦</div>
<div class="sparkle3">✦</div>
<div class="sparkle4">✦</div>
""", unsafe_allow_html=True)

# ── Logo ──
def get_logo_base64():
    try:
        with open("logo.svg", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo_b64 = get_logo_base64()
logo_html = f'<img src="data:image/svg+xml;base64,{logo_b64}" width="380" class="hero-img"/>' if logo_b64 else "💌"

st.markdown(f"""
<div class="hero">
    {logo_html}
    <h1 class="hero-title">Cold Email Writer</h1>
    <p class="hero-sub">✨ Generate a personalized job email instantly using AI ✨</p>
</div>
""", unsafe_allow_html=True)

st.divider()

email_type = st.selectbox(" Choose Email Type", [
    " Job Application (Resume + JD)",
    " Cold Outreach to Hiring Manager",
    " Follow-Up After Interview"
])

st.markdown("---")

c1, c2 = st.columns(2)
with c1:
    your_name    = st.text_input("Your Name *", placeholder="e.g. Deepthi")
    company_name = st.text_input("Company Name *", placeholder="e.g. Google")
with c2:
    your_role      = st.text_input("Role You're Targeting *", placeholder="e.g. AI Prompt Engineer")
    hiring_manager = st.text_input("Hiring Manager Name (optional)", placeholder="e.g. Sankar")
    tone           = st.selectbox("Email Tone ", ["Formal", "Friendly", "Bold"])

st.markdown("---")

resume_text = job_desc = interview_date = interview_role = extra_context = ""

if "Job Application" in email_type:
    c3, c4 = st.columns(2)
    with c3:
        resume_text = st.text_area("Your Resume Summary *", placeholder="Your skills, internship, projects...", height=180)
    with c4:
        job_desc = st.text_area("Job Description *", placeholder="Paste job requirements here...", height=180)
elif "Cold Outreach" in email_type:
    c3, c4 = st.columns(2)
    with c3:
        resume_text = st.text_area("Your Background *", placeholder="Your skills, internship, projects...", height=180)
    with c4:
        extra_context = st.text_area("Why this company? (optional)", placeholder="Any specific reason...", height=180)
elif "Follow-Up" in email_type:
    c3, c4 = st.columns(2)
    with c3:
        interview_date = st.text_input("Interview Date", placeholder="e.g. 24th Feb 2026")
        interview_role = st.text_input("Position Interviewed For", placeholder="e.g. AI Engineer")
    with c4:
        extra_context = st.text_area("Key highlights from interview", placeholder="Topics discussed...", height=140)

st.markdown("---")
generate_btn = st.button(" Generate My Email", use_container_width=True)

def generate_with_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
    if not api_key:
        raise Exception("GROQ_API_KEY not found!")

    payload = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 800,
        "temperature": 0.7
    })

    conn = http.client.HTTPSConnection("api.groq.com")
    conn.request("POST", "/openai/v1/chat/completions", payload, {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    })
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    if response.status != 200:
        raise Exception(f"Groq error {response.status}: {data}")
    return json.loads(data)["choices"][0]["message"]["content"]

def build_prompt(email_type, name, role, company, manager, tone, resume, jd, interview_date, interview_role, extra):
    manager_line = f"Hiring manager: {manager}." if manager else "No hiring manager name, use generic salutation."
    if "Job Application" in email_type:
        context = f"Job Application | Applicant: {name} | Role: {role} | Company: {company} | {manager_line} | Resume: {resume} | JD: {jd}"
    elif "Cold Outreach" in email_type:
        context = f"Cold Outreach | Applicant: {name} | Role: {role} | Company: {company} | {manager_line} | Background: {resume} | Why: {extra}"
    else:
        context = f"Post-Interview Follow-Up | Applicant: {name} | Role: {interview_role or role} | Company: {company} | {manager_line} | Date: {interview_date} | Discussion: {extra}"

    tone_guide = {
        "Formal": "Professional, structured, respectful.",
        "Friendly": "Warm, conversational, personable.",
        "Bold": "Confident, punchy, attention-grabbing."
    }

    return f"""You are an expert career coach. Write a single {tone} email for:
{context}
Tone: {tone_guide[tone]}

Return ONLY this JSON (no extra text, no markdown backticks):
{{"subject": "your subject line here", "body": "your full email body here"}}

Rules: 150-200 words. Compelling subject line. Clear call to action. Sound human not robotic."""

if generate_btn:
    missing = []
    if not your_name.strip():    missing.append("Your Name")
    if not your_role.strip():    missing.append("Role You're Targeting")
    if not company_name.strip(): missing.append("Company Name")

    if missing:
        st.error(f"Please fill in: {', '.join(missing)}")
    else:
        with st.spinner("✨ Writing your email..."):
            try:
                prompt = build_prompt(email_type, your_name, your_role, company_name,
                                      hiring_manager, tone, resume_text, job_desc,
                                      interview_date, interview_role, extra_context)
                raw = generate_with_groq(prompt)
                raw = raw.strip()
                if "```" in raw:
                    raw = raw.split("```")[1]
                    if raw.startswith("json"): raw = raw[4:]
                result = json.loads(raw.strip())

                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.success("💌 Your email is ready!")
                st.markdown(f"** Subject:** `{result.get('subject', '')}`")
                st.divider()
                st.write(result.get("body", ""))
                st.divider()
                st.text_area(" Copy your email", value=result.get("body", ""), height=200, key="copy_email")
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {str(e)}")

# ── Footer ──
st.markdown("""
<div class="footer">
    Built with  by <span>Deepthi</span> · Powered by Groq LLaMA 3.3 · Made with Python & Streamlit
</div>
""", unsafe_allow_html=True)
