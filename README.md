<div align="center">

# 🤖 Domain-Grounded RAG Engine with Gemini 2.0

### High-Precision Retrieval-Augmented Generation, Strict Context Boundary Guardrails, and Interactive Chat Interface

[![Model](https://img.shields.io/badge/Model-Gemini_2.0_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Hallucination Defense](https://img.shields.io/badge/Guardrails-Zero_Hallucination_Policy-success?style=for-the-badge)](https://github.com/Rajath123562/RAG-AI-Assistant)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br/>

<p align="center">
  <b>An enterprise-ready Retrieval-Augmented Generation (RAG) assistant designed for high-stakes domain compliance.</b><br/>
  Combines Google Gemini 2.0 Flash with explicit knowledge-boundary constraints to guarantee that generated outputs remain 100% faithful to supplied contextual documents with deterministic out-of-domain refusal.
</p>

</div>

---

## 📌 Core Capabilities

- **Zero-Hallucination Guardrail Policy:** The model enforces strict epistemic bounds. If an answer cannot be deduced strictly from the provided context corpus, it explicitly rejects speculation rather than hallucinating plausible falsehoods.
- **Dynamic Context Injection:** Ingests unstructured technical handbooks, enterprise compliance policies, proprietary schemas, or legal docs directly via the interactive sidebar.
- **Stateful Multi-Turn Context Retention:** Maintains conversational continuity across turns without leaking memory or violating document scope.
- **Graceful Fault & Rate-Limit Handling:** Native interception of API rate limits (HTTP 429) and invalid credential keys with actionable diagnostic banners.

---

## 🏗️ Information Flow & Architecture

```
  [ User Documents / Domain Corpus ]
                 |
                 v
  +-------------------------------+
  |   STREAMLIT INGESTION LAYER   |
  | Dynamic Text Ingestion Buffer |
  +-------------------------------+
                 |
                 v
  +-------------------------------------------------------------+
  |              SYSTEM PROMPT GUARDRAIL SYNTHESIZER            |
  |  - Epistemic Constraint: Reject out-of-context queries      |
  |  - Grounding Enforcement: Reference only explicit facts     |
  +-------------------------------------------------------------+
                 |
                 +--------------------------+
                 |                          |
                 v                          v
       [ User Query / Prompt ]     [ Chat History Buffer ]
                 \                          /
                  v                        v
  +-------------------------------------------------------------+
  |                   GOOGLE GEMINI 2.0 FLASH                   |
  |              High-Speed Structured Reasoning                |
  +-------------------------------------------------------------+
                                 |
                                 v
        [ Grounded Answer Output OR Epistemic Refusal ]
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.9+
- A Google Gemini API Key ([Get one for free at Google AI Studio](https://aistudio.google.com/apikey))

### 2. Clone & Install
```bash
git clone https://github.com/Rajath123562/RAG-AI-Assistant.git
cd RAG-AI-Assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Credentials
```bash
cp .env.example .env
```
Edit `.env` and insert your Gemini API Key:
```ini
GEMINI_API_KEY=AIzaSyYourActualKeyHere
```

### 4. Launch the Application
```bash
python -m streamlit run app.py
```
The interface will automatically open in your browser at `http://localhost:8501`.

---

## 📂 Repository Layout

```
├── app.py              # Application logic, UI layout, GenAI SDK client, state machine
├── requirements.txt    # streamlit, google-genai, python-dotenv
├── .env.example        # Environment configuration template
├── .gitignore          # Excludes .env, caches, and virtual environments
└── README.md           # Systems documentation
```

---

## 🛡️ Guardrail Performance Comparison

| Scenario | Standard Unconstrained LLM | Grounded RAG Engine |
| :--- | :--- | :--- |
| **Question found in Context** | Generates answer (often adds ungrounded external details) | **Extracts exact facts strictly within document boundary** |
| **Question missing from Context** | Hallucinates plausible but fake answer | **Explicitly states information is unavailable** |
| **Adversarial Jailbreak** | Vulnerable to prompt diversion | **Strict system prompt anchoring prevents context breach** |

---

## 📜 License
Distributed under the **MIT License**.
