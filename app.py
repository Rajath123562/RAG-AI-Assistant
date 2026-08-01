"""
RAG AI Assistant — Local Retrieval-Augmented Generation app.

Uses Streamlit for the UI, Google GenAI SDK (google-genai) for LLM calls,
and python-dotenv for API-key management.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ──────────────────────────────────────────────
# 1. Configuration
# ──────────────────────────────────────────────
load_dotenv()  # loads .env in project root

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error(
        "🔑 **GEMINI_API_KEY not found.**  "
        "Create a `.env` file in this directory with:\n\n"
        "```\nGEMINI_API_KEY=your_api_key_here\n```"
    )
    st.stop()

# Initialise the Google GenAI client (new SDK style)
client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-2.0-flash"

# ──────────────────────────────────────────────
# 2. Page & Theme Setup
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="RAG AI Assistant",
    page_icon="🧠",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* subtle gradient header bar */
    header[data-testid="stHeader"] {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
    }
    /* sidebar styling */
    section[data-testid="stSidebar"] > div {
        background-color: #0e1117;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧠 RAG AI Assistant")
st.caption("Ask questions grounded in *your* knowledge base.")

# ──────────────────────────────────────────────
# 3. Sidebar — Knowledge Base
# ──────────────────────────────────────────────
DUMMY_CONTEXT = """\
=== Acme Corp — Internal Policy Handbook (2026 Edition) ===

1. Remote-Work Policy
   • All full-time employees may work remotely up to 3 days per week.
   • Requests for fully-remote arrangements require VP-level approval.
   • Core collaboration hours are 10 AM – 2 PM in the employee's local time zone.

2. Expense Reimbursement
   • Meal expenses during business travel are capped at $75/day.
   • Software subscriptions under $50/month may be self-approved.
   • Hardware purchases above $500 require manager sign-off via the internal portal.

3. Leave & Time-Off
   • Employees accrue 1.5 days of paid leave per month (18 days/year).
   • Unused leave can carry over up to a maximum of 10 days into the next calendar year.
   • Parental leave is 16 weeks for all new parents, regardless of gender.

4. Data & Security
   • All laptops must use full-disk encryption (FileVault / BitLocker).
   • Sharing credentials via email or messaging apps is strictly prohibited.
   • Employees must complete the annual cybersecurity training by March 31 each year.

5. Performance Reviews
   • Reviews are conducted semi-annually in January and July.
   • Self-assessments are due one week before the review meeting.
   • Promotion nominations open during the July review cycle only.
"""

st.sidebar.header("📚 Knowledge Base")
st.sidebar.markdown(
    "Paste or edit the context below. "
    "The assistant will **only** use this text to answer your questions."
)
context_text = st.sidebar.text_area(
    label="Context / Documents",
    value=DUMMY_CONTEXT,
    height=420,
    help="This text is injected into every prompt as the RAG context.",
)

st.sidebar.divider()
st.sidebar.markdown(
    f"**Model:** `{MODEL_ID}`  \n"
    "**Mode:** Context-only (RAG)"
)

# ──────────────────────────────────────────────
# 4. Session State — Chat History
# ──────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ──────────────────────────────────────────────
# 5. Chat Input & LLM Integration
# ──────────────────────────────────────────────
user_input = st.chat_input("Ask a question about the knowledge base…")

if user_input:
    # Display and persist the user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build the RAG prompt
    system_prompt = (
        "You are a helpful AI assistant. Your job is to answer the user's "
        "question using ONLY the context provided below. "
        "Do NOT use any prior knowledge. "
        "If the answer cannot be found in the context, respond exactly with: "
        '"I don\'t know based on the provided context."\n\n'
        "--- BEGIN CONTEXT ---\n"
        f"{context_text}\n"
        "--- END CONTEXT ---"
    )

    full_prompt = f"{system_prompt}\n\nUser question: {user_input}"

    # Call Gemini
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            try:
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=full_prompt,
                )
                answer = response.text
            except Exception as exc:
                answer = f"⚠️ Error calling Gemini API:\n\n```\n{exc}\n```"

        st.markdown(answer)

    # Persist the assistant reply
    st.session_state.messages.append({"role": "assistant", "content": answer})
