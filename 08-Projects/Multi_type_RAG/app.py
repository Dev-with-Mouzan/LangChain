import streamlit as st
import os
import backend
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Multi Type RAG",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ══════════════════════════════════════════════════════════════════════════════
# DESIGN SYSTEM — Bold Neon Glassmorphism
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ═══ TOKENS ═══ */
:root {
    --bg:          #111111;
    --bg-raised:   #1a1a1a;
    --bg-glass:    rgba(26, 26, 26, 0.65);
    --bg-glass-hi: rgba(38, 38, 38, 0.7);
    --border:      rgba(255, 255, 255, 0.06);
    --border-med:  rgba(255, 255, 255, 0.1);
    --amber:       #F59E0B;
    --amber-light: #FBBF24;
    --amber-dim:   rgba(245, 158, 11, 0.15);
    --gold:        #D97706;
    --gold-dim:    rgba(217, 119, 6, 0.12);
    --cream:       #FDE68A;
    --cream-dim:   rgba(253, 230, 138, 0.1);
    --green:       #10B981;
    --green-dim:   rgba(16, 185, 129, 0.12);
    --red:         #EF4444;
    --text:        #f5f5f4;
    --text-2:      #a8a29e;
    --text-3:      #57534e;
    --glow-amber:  0 0 30px rgba(245, 158, 11, 0.3), 0 0 60px rgba(245, 158, 11, 0.1);
    --glow-gold:   0 0 30px rgba(217, 119, 6, 0.25), 0 0 60px rgba(217, 119, 6, 0.08);
    --glow-cream:  0 0 20px rgba(253, 230, 138, 0.15);
    --r:           14px;
    --r-lg:        20px;
    --r-pill:      9999px;
}

/* ═══ KEYFRAMES ═══ */
@keyframes orbFloat {
    0%, 100% { transform: translate(0, 0) scale(1); }
    25%      { transform: translate(30px, -40px) scale(1.05); }
    50%      { transform: translate(-20px, 20px) scale(0.95); }
    75%      { transform: translate(15px, 35px) scale(1.02); }
}

@keyframes orbFloat2 {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33%      { transform: translate(-40px, 30px) scale(1.08); }
    66%      { transform: translate(25px, -25px) scale(0.92); }
}

@keyframes racingBorder {
    0%   { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
}

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-16px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.9); }
    to   { opacity: 1; transform: scale(1); }
}

@keyframes slideLeft {
    from { opacity: 0; transform: translateX(-24px); }
    to   { opacity: 1; transform: translateX(0); }
}

@keyframes neonPulse {
    0%, 100% { box-shadow: 0 0 8px rgba(245, 158, 11, 0.3), 0 0 20px rgba(245, 158, 11, 0.1); }
    50%      { box-shadow: 0 0 16px rgba(245, 158, 11, 0.5), 0 0 40px rgba(245, 158, 11, 0.2); }
}

@keyframes neonPulseViolet {
    0%, 100% { box-shadow: 0 0 8px rgba(217, 119, 6, 0.3), 0 0 20px rgba(217, 119, 6, 0.1); }
    50%      { box-shadow: 0 0 16px rgba(217, 119, 6, 0.5), 0 0 40px rgba(217, 119, 6, 0.2); }
}

@keyframes dotBounce {
    0%, 60%, 100% { transform: translateY(0); opacity: 0.3; }
    30%            { transform: translateY(-10px); opacity: 1; }
}

@keyframes shimmer {
    0%   { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

@keyframes breathe {
    0%, 100% { opacity: 0.4; }
    50%      { opacity: 1; }
}

@keyframes lineExpand {
    from { width: 0; opacity: 0; }
    to   { width: 100%; opacity: 1; }
}

@keyframes spinGlow {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

@keyframes textGlow {
    0%, 100% { text-shadow: 0 0 20px rgba(245, 158, 11, 0.3); }
    50%      { text-shadow: 0 0 40px rgba(245, 158, 11, 0.6), 0 0 80px rgba(217, 119, 6, 0.3); }
}

/* ═══ BACKGROUND — Animated Gradient Orbs + Grid ═══ */
.stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Space Grotesk', -apple-system, sans-serif !important;
    overflow-x: hidden;
}

.stApp > .block-container {
    position: relative;
    z-index: 1;
}

/* Floating orbs */
.stApp::before {
    content: '';
    position: fixed;
    width: 600px; height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(245, 158, 11, 0.15) 0%, transparent 70%);
    top: -100px; left: -150px;
    animation: orbFloat 18s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
    filter: blur(60px);
}

.stApp::after {
    content: '';
    position: fixed;
    width: 500px; height: 500px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(217, 119, 6, 0.12) 0%, transparent 70%);
    bottom: -100px; right: -100px;
    animation: orbFloat2 22s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
    filter: blur(60px);
}

/* Grid pattern overlay */
.block-container::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
    z-index: 0;
}

/* Raise all Streamlit content */
[data-testid="stMarkdown"], [data-testid="stVerticalBlock"],
div[data-testid="stChatMessage"], .stButton, .stTextInput,
.stFileUploader, .stSpinner, .stSuccess, .stError, .stWarning,
div[data-testid="stChatInput"], div[data-testid="stExpander"] {
    position: relative;
    z-index: 2;
}

/* ═══ SIDEBAR ═══ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #08080c 0%, #0c0c10 50%, #09090b 100%) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}

[data-testid="stSidebar"] [data-testid="stMarkdown"] {
    animation: slideLeft 0.5s ease-out both;
}
[data-testid="stSidebar"] [data-testid="stMarkdown"]:nth-child(2) { animation-delay: 0.05s; }
[data-testid="stSidebar"] [data-testid="stMarkdown"]:nth-child(3) { animation-delay: 0.1s; }
[data-testid="stSidebar"] [data-testid="stMarkdown"]:nth-child(4) { animation-delay: 0.15s; }

/* Sidebar brand */
.sb-brand {
    display: flex; align-items: center; gap: 14px;
    padding: 4px 0 24px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 24px;
    animation: fadeInDown 0.6s ease-out both;
}

.sb-logo {
    width: 44px; height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--amber), var(--cream));
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; color: #000; font-weight: 700;
    box-shadow: var(--glow-amber);
    animation: neonPulse 3s ease-in-out infinite;
    flex-shrink: 0;
}

.sb-title {
    font-size: 1.15rem; font-weight: 700; color: var(--text);
    margin: 0; letter-spacing: -0.3px;
}

.sb-sub {
    font-size: 0.65rem; color: var(--text-3);
    text-transform: uppercase; letter-spacing: 1.5px; margin: 2px 0 0 0;
    font-family: 'JetBrains Mono', monospace;
}

/* Sidebar cards */
.sb-card {
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 16px;
    margin-bottom: 14px;
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
    animation: fadeInUp 0.5s ease-out both;
}

.sb-card:hover {
    border-color: var(--border-med);
    background: var(--bg-glass-hi);
    box-shadow: var(--glow-gold);
}

.sb-card:nth-child(1) { animation-delay: 0.1s; }
.sb-card:nth-child(2) { animation-delay: 0.2s; }

.sb-label {
    font-size: 0.6rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 1.5px;
    color: var(--amber);
    margin-bottom: 8px;
    font-family: 'JetBrains Mono', monospace;
    display: flex; align-items: center; gap: 8px;
}

.sb-label::before {
    content: ''; width: 8px; height: 8px;
    border-radius: 2px;
    background: var(--amber);
    box-shadow: 0 0 10px var(--amber);
    animation: breathe 2s ease-in-out infinite;
}

/* Status badge */
.idx-badge {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 6px 16px; border-radius: var(--r-pill);
    font-size: 0.7rem; font-weight: 500;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.3px;
    animation: fadeInUp 0.5s ease-out 0.2s both;
    margin-bottom: 20px;
}

.idx-badge.active {
    background: var(--green-dim);
    border: 1px solid rgba(16, 185, 129, 0.2);
    color: var(--green);
}

.idx-badge.none {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border);
    color: var(--text-3);
}

.idx-dot {
    width: 7px; height: 7px; border-radius: 50%;
    animation: breathe 2s ease-in-out infinite;
}

.idx-dot.on  { background: var(--green); box-shadow: 0 0 12px var(--green); }
.idx-dot.off { background: var(--text-3); }

/* ═══ HEADERS ═══ */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}

.hero {
    text-align: center;
    padding: 4px 0 20px;
    animation: fadeInDown 0.6s ease-out both;
}

.hero h1 {
    font-size: 2.6rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.5px;
    line-height: 1.2;
    background: linear-gradient(135deg, var(--amber) 0%, #fff 35%, var(--gold) 100%);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 5s ease infinite;
    margin: 0 auto 8px auto !important;
    display: block;
}

.hero-sub {
    font-size: 0.95rem;
    color: var(--text-2);
    font-weight: 400;
    letter-spacing: 0.2px;
    text-align: center;
    margin: 0 auto;
    display: block;
}

.hero-line {
    height: 1px;
    max-width: 360px;
    margin: 16px auto 20px auto;
    background: linear-gradient(90deg, transparent, var(--amber), var(--gold), transparent);
    animation: lineExpand 1s ease-out 0.3s both;
    opacity: 0.5;
}

/* ═══ CHAT MESSAGES — Glass Bubbles ═══ */
div[data-testid="stChatMessage"] {
    background: transparent !important;
    border: 1px solid transparent !important;
    border-radius: var(--r-lg) !important;
    margin-bottom: 14px !important;
    padding: 18px 22px !important;
    animation: fadeInUp 0.35s ease-out both;
    transition: all 0.3s ease !important;
}

div[data-testid="stChatMessage"]:hover {
    background: rgba(255, 255, 255, 0.015) !important;
}

/* Assistant — left cyan accent */
div[data-testid="stChatMessage"][data-testid-header="assistant"] {
    background: var(--bg-glass) !important;
    border: 1px solid var(--border) !important;
    border-left: 3px solid var(--amber) !important;
    border-radius: 6px var(--r-lg) var(--r-lg) 6px !important;
    backdrop-filter: blur(8px);
}

div[data-testid="stChatMessage"][data-testid-header="assistant"]:hover {
    border-color: rgba(245, 158, 11, 0.2) !important;
    box-shadow: inset 0 0 30px rgba(245, 158, 11, 0.03), 0 0 20px rgba(245, 158, 11, 0.05);
}

/* User — right violet accent */
div[data-testid="stChatMessage"][data-testid-header="user"] {
    background: rgba(217, 119, 6, 0.06) !important;
    border: 1px solid rgba(217, 119, 6, 0.12) !important;
    border-right: 3px solid var(--cream) !important;
    border-radius: var(--r-lg) 6px 6px var(--r-lg) !important;
}

div[data-testid="stChatMessage"][data-testid-header="user"]:hover {
    border-color: rgba(217, 119, 6, 0.2) !important;
    box-shadow: 0 0 20px rgba(217, 119, 6, 0.06);
}

/* ═══ SOURCE CARDS ═══ */
.src-card {
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-left: 3px solid var(--amber);
    border-radius: 4px var(--r) var(--r) 4px;
    padding: 16px 18px;
    font-size: 0.82rem; color: var(--text-2); line-height: 1.7;
    margin-top: 10px;
    backdrop-filter: blur(8px);
    transition: all 0.3s ease;
    animation: scaleIn 0.3s ease-out both;
}

.src-card:hover {
    border-left-color: var(--cream);
    box-shadow: var(--glow-gold);
}

.src-tag {
    font-size: 0.6rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 1.2px;
    color: var(--amber); margin-bottom: 10px;
    font-family: 'JetBrains Mono', monospace;
    display: flex; align-items: center; gap: 8px;
}

.src-tag::before {
    content: ''; width: 6px; height: 6px;
    background: var(--amber); border-radius: 2px;
    box-shadow: 0 0 8px var(--amber);
}

/* ═══ TYPING INDICATOR — Neon Ring ═══ */
.typing-wrap {
    display: inline-flex; align-items: center; gap: 14px;
    padding: 12px 22px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--r-pill);
    backdrop-filter: blur(12px);
    animation: fadeInUp 0.3s ease-out both;
}

.typing-ring {
    width: 22px; height: 22px;
    border-radius: 50%;
    border: 2px solid transparent;
    border-top-color: var(--amber);
    border-right-color: var(--cream);
    animation: spinGlow 1s linear infinite;
    box-shadow: 0 0 12px rgba(245, 158, 11, 0.3);
}

.typing-dots {
    display: flex; gap: 5px;
}

.typing-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--amber);
    animation: dotBounce 1.3s ease-in-out infinite;
    box-shadow: 0 0 6px var(--amber);
}

.typing-dot:nth-child(1) { animation-delay: 0s; background: var(--amber); }
.typing-dot:nth-child(2) { animation-delay: 0.15s; background: var(--cream); box-shadow: 0 0 6px var(--cream); }
.typing-dot:nth-child(3) { animation-delay: 0.3s; background: var(--gold); box-shadow: 0 0 6px var(--gold); }

.typing-text {
    font-size: 0.75rem; color: var(--text-3);
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.5px;
}

/* ═══ INPUT FIELDS ═══ */
.stTextInput input, .stTextArea textarea {
    background: var(--bg-raised) !important;
    border: 1px solid var(--border-med) !important;
    border-radius: var(--r) !important;
    color: var(--text) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    transition: all 0.3s ease !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--amber) !important;
    box-shadow: 0 0 0 3px var(--amber-dim), var(--glow-amber) !important;
}

.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: var(--text-3) !important;
}

/* ═══ CHAT INPUT — Floating Glass Bar ═══ */
div[data-testid="stChatInput"] {
    background: var(--bg-glass-hi) !important;
    border: 1px solid var(--border-med) !important;
    border-radius: var(--r-lg) !important;
    backdrop-filter: blur(20px) !important;
    padding: 4px 6px !important;
    animation: fadeInUp 0.5s ease-out 0.3s both;
    transition: all 0.4s ease !important;
}

div[data-testid="stChatInput"]:focus-within {
    border-color: var(--amber) !important;
    box-shadow: 0 0 0 4px var(--amber-dim), var(--glow-amber) !important;
}

div[data-testid="stChatInput"] textarea {
    background: transparent !important;
    border: none !important;
    color: var(--text) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

div[data-testid="stChatInput"] textarea:focus {
    box-shadow: none !important;
    border: none !important;
}

/* ═══ BUTTONS — Neon Glow ═══ */
.stButton > button {
    background: linear-gradient(135deg, var(--amber), var(--cream)) !important;
    color: #000 !important;
    border: none !important;
    border-radius: var(--r) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    padding: 11px 24px !important;
    width: 100% !important;
    letter-spacing: 0.3px;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute; top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.6s ease;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: var(--glow-amber), 0 8px 30px rgba(245, 158, 11, 0.2) !important;
}

.stButton > button:hover::before { left: 100%; }

.stButton > button:active {
    transform: translateY(-1px) !important;
}

/* ═══ FILE UPLOADER ═══ */
.stFileUploader {
    border: 1px dashed var(--border-med) !important;
    border-radius: var(--r) !important;
    background: rgba(245, 158, 11, 0.02) !important;
    transition: all 0.3s ease !important;
}

.stFileUploader:hover {
    border-color: var(--amber) !important;
    background: rgba(245, 158, 11, 0.04) !important;
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.05);
}

.stFileUploader section { background: transparent !important; border: none !important; }
.stFileUploader label { color: var(--text-2) !important; font-family: 'Space Grotesk', sans-serif !important; }

/* ═══ EXPANDERS ═══ */
div[data-testid="stExpander"] {
    background: var(--bg-glass) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--r) !important;
    backdrop-filter: blur(8px);
    transition: all 0.3s ease !important;
}

div[data-testid="stExpander"]:hover {
    border-color: rgba(245, 158, 11, 0.2) !important;
    box-shadow: 0 0 16px rgba(245, 158, 11, 0.05);
}

div[data-testid="stExpander"] summary {
    color: var(--amber) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 500 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.5px;
}

/* ═══ DIVIDER ═══ */
hr {
    border: none !important; height: 1px !important;
    background: linear-gradient(90deg, transparent, var(--border-med), transparent) !important;
    margin: 14px 0 !important;
}

/* ═══ SPINNER ═══ */
.stSpinner > div {
    border-color: var(--amber) transparent transparent transparent !important;
    filter: drop-shadow(0 0 6px var(--amber));
}

/* ═══ ALERTS ═══ */
.stSuccess {
    background: var(--green-dim) !important;
    border: 1px solid rgba(16, 185, 129, 0.2) !important;
    border-radius: var(--r) !important;
    color: var(--green) !important;
    animation: fadeInUp 0.3s ease-out both;
}

.stError {
    background: rgba(255, 64, 96, 0.08) !important;
    border: 1px solid rgba(255, 64, 96, 0.2) !important;
    border-radius: var(--r) !important;
    color: var(--red) !important;
    animation: fadeInUp 0.3s ease-out both;
}

.stWarning {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--r) !important;
    color: var(--text-2) !important;
}

/* ═══ SCROLLBAR ═══ */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(245, 158, 11, 0.15); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(245, 158, 11, 0.3); }

/* ═══ MISC ═══ */
#MainMenu, footer, header[data-testid="stHeader"] { display: none !important; }

::selection {
    background: rgba(245, 158, 11, 0.25);
    color: #fff;
}

[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h2 {
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    color: var(--text) !important;
}

/* ═══ WELCOME ═══ */
.welcome {
    text-align: center;
    padding: 40px 28px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: var(--r-lg);
    backdrop-filter: blur(16px);
    margin: 20px 0;
    animation: scaleIn 0.5s ease-out both;
    position: relative;
    overflow: hidden;
}

.welcome::before {
    content: '';
    position: absolute; top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: conic-gradient(from 0deg, transparent, rgba(245, 158, 11, 0.03), transparent, rgba(217, 119, 6, 0.03), transparent);
    animation: spinGlow 20s linear infinite;
    pointer-events: none;
}

.welcome h2 {
    font-size: 1.5rem !important; font-weight: 700 !important;
    color: var(--text) !important;
    margin-bottom: 8px !important;
    position: relative;
}

.welcome h2 span {
    background: linear-gradient(135deg, var(--amber), var(--cream));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}

.welcome p {
    color: var(--text-2); font-size: 0.92rem;
    max-width: 460px; margin: 0 auto 24px;
    line-height: 1.6; position: relative;
}

.feat-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 14px; position: relative;
}

.feat {
    padding: 20px 14px;
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid var(--border);
    border-radius: var(--r);
    text-align: center;
    transition: all 0.35s ease;
    animation: fadeInUp 0.5s ease-out both;
}

.feat:nth-child(1) { animation-delay: 0.15s; }
.feat:nth-child(2) { animation-delay: 0.25s; }
.feat:nth-child(3) { animation-delay: 0.35s; }

.feat:hover {
    border-color: rgba(245, 158, 11, 0.25);
    transform: translateY(-4px);
    box-shadow: var(--glow-amber);
    background: rgba(245, 158, 11, 0.04);
}

.feat-icon {
    font-size: 1.8rem; margin-bottom: 10px; display: block;
    filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.3));
}

.feat-title {
    font-size: 0.82rem; font-weight: 600; color: var(--text); margin-bottom: 4px;
}

.feat-desc {
    font-size: 0.7rem; color: var(--text-3); line-height: 1.4;
}

/* ═══ CLEAR BTN ═══ */
.clr-btn > button {
    background: rgba(255, 64, 96, 0.08) !important;
    color: var(--red) !important;
    border: 1px solid rgba(255, 64, 96, 0.15) !important;
    font-size: 0.75rem !important;
    padding: 6px 14px !important;
}

.clr-btn > button:hover {
    background: rgba(255, 64, 96, 0.15) !important;
    box-shadow: 0 0 20px rgba(255, 64, 96, 0.1) !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def index_exists():
    return os.path.exists("faiss_index") and os.path.isdir("faiss_index")

def index_size():
    if index_exists():
        total = sum(os.path.getsize(os.path.join("faiss_index", f)) for f in os.listdir("faiss_index"))
        return f"{total / 1024:.1f} KB"
    return None

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
        <div class="sb-brand">
            <div class="sb-logo">N</div>
            <div>
                <div class="sb-title">Multi Type RAG</div>
                <div class="sb-sub">Knowledge Engine</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if index_exists():
        sz = index_size()
        st.markdown(f'<div class="idx-badge active"><span class="idx-dot on"></span>INDEXED · {sz}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="idx-badge none"><span class="idx-dot off"></span>NO INDEX</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-card"><div class="sb-label">Document Upload</div></div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"], label_visibility="collapsed")
    if st.button("◆  Index PDF", key="idx_pdf"):
        if uploaded_file:
            with st.spinner("Processing..."):
                os.makedirs("Data", exist_ok=True)
                path = os.path.join("Data", uploaded_file.name)
                with open(path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                try:
                    docs = backend.ingest_pdf(path)
                    backend.add_to_index(docs)
                    st.success(f"Indexed: {uploaded_file.name}")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))
        else:
            st.warning("Select a PDF first.")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<div class="sb-card"><div class="sb-label">Web Ingestion</div></div>', unsafe_allow_html=True)
    url_input = st.text_input("URL", placeholder="https://docs.example.com...", label_visibility="collapsed")
    if st.button("◆  Ingest URL", key="idx_url"):
        if url_input:
            with st.spinner("Fetching..."):
                try:
                    docs = backend.ingest_url(url_input)
                    backend.add_to_index(docs)
                    st.success("URL indexed.")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))
        else:
            st.warning("Enter a URL.")

    st.markdown("<hr>", unsafe_allow_html=True)

    if index_exists():
        st.markdown('<div class="sb-label" style="margin-bottom:8px;">Management</div>', unsafe_allow_html=True)
        if st.button("Clear Index", key="clr"):
            try:
                backend.clear_index()
                st.success("Index cleared.")
                st.rerun()
            except Exception as e:
                st.error(str(e))

# ══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
    <div class="hero">
        <h1>Multi Type RAG</h1>
        <p class="hero-sub">Intelligent retrieval from your documents and the web — powered by advanced RAG.</p>
    </div>
    <div class="hero-line"></div>
""", unsafe_allow_html=True)

if index_exists():
    sz = index_size()
    st.markdown(f'<div style="text-align:center;"><div class="idx-badge active" style="display:inline-flex;"><span class="idx-dot on"></span>KNOWLEDGE BASE ONLINE · {sz}</div></div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="text-align:center;"><div class="idx-badge none" style="display:inline-flex;"><span class="idx-dot off"></span>UPLOAD A DOCUMENT OR INGEST A URL TO BEGIN</div></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CHAT
# ══════════════════════════════════════════════════════════════════════════════
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown("""
        <div class="welcome">
            <h2>Welcome to <span>Multi Type RAG</span></h2>
            <p>Your AI-powered knowledge assistant. Upload documents or ingest web content, then ask anything.</p>
            <div class="feat-grid">
                <div class="feat">
                    <span class="feat-icon">📄</span>
                    <div class="feat-title">PDF Analysis</div>
                    <div class="feat-desc">Upload & index PDFs for deep Q&A</div>
                </div>
                <div class="feat">
                    <span class="feat-icon">🌐</span>
                    <div class="feat-title">Web Ingestion</div>
                    <div class="feat-desc">Pull knowledge from any URL</div>
                </div>
                <div class="feat">
                    <span class="feat-icon">◆</span>
                    <div class="feat-title">Smart Retrieval</div>
                    <div class="feat-desc">Context-aware answers with citations</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            st.markdown("""
                <div class="typing-wrap">
                    <div class="typing-ring"></div>
                    <div class="typing-dots">
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                    </div>
                    <span class="typing-text">generating</span>
                </div>
            """, unsafe_allow_html=True)
            st.empty()
        st.markdown(msg["content"])
        if msg.get("context"):
            with st.expander("◆  Sources"):
                st.markdown(f'<div class="src-card"><div class="src-tag">Retrieved Context</div>{msg["context"]}</div>', unsafe_allow_html=True)

if prompt := st.chat_input("Ask anything about your data..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("""
            <div class="typing-wrap">
                <div class="typing-ring"></div>
                <div class="typing-dots">
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                </div>
                <span class="typing-text">retrieving & generating</span>
            </div>
        """, unsafe_allow_html=True)

        try:
            answer, context = backend.query_rag(prompt)
            placeholder.empty()
            st.markdown(answer)
            if context:
                with st.expander("◆  Sources"):
                    st.markdown(f'<div class="src-card"><div class="src-tag">Retrieved Context</div>{context}</div>', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": answer, "context": context})
        except Exception as e:
            placeholder.empty()
            st.error(f"Error: {e}")
