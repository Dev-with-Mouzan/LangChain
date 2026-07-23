<div align="center">

<img src="https://img.shields.io/badge/Smart--AI--Explainer-Role_Based_Learning-EC4899?style=for-the-badge&logo=lightbulb&logoColor=white" alt="Smart AI Explainer"/>

# Smart AI Explainer

<p align="center">
  <img src="https://img.shields.io/badge/LangChain-Chat-374151?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/FastAPI-Server-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI"/>
</p>

**A conversational AI explainer that teaches concepts through different expert perspectives with structured What/How/Why responses.**

</div>

---

## Features

- **Role-Based Explanations** - Learn from different expert perspectives (teacher, scientist, engineer, etc.)
- **Structured Output** - JSON-formatted responses with What/How/Why breakdown
- **Session Memory** - Maintains conversation context per session
- **Interactive Chat** - Multi-turn conversation interface
- **Beginner-Friendly** - Simplified explanations for complex topics

## Architecture

```
Smart_Ai_Explaner/
├── main.py              # FastAPI app & LangChain chat
├── frontend/
│   ├── index.html       # Web interface
│   ├── styles.css       # Styling
│   └── script.js        # Client-side logic
├── requirements.txt     # Python dependencies
└── .env                # API keys (not committed)
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| AI Engine | LangChain + OpenAI GPT-4o-mini |
| Chat Memory | In-memory session storage |
| Output Format | Structured JSON |
| Frontend | Vanilla HTML/CSS/JS |

## Setup

```bash
# Clone and navigate
cd 08-Projects/Smart_Ai_Explaner

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the application
python main.py
```

Navigate to `http://0.0.0.0:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve frontend |
| `GET` | `/styles.css` | Serve CSS |
| `GET` | `/script.js` | Serve JavaScript |
| `POST` | `/explain` | Generate role-based explanation |

### POST `/explain`

```json
{
  "query": "What is quantum computing?",
  "role": "quantum physicist",
  "session_id": "user-123"
}
```

**Response:**
```json
{
  "response": {
    "what": "Quantum computing is...",
    "how": "It works by...",
    "why": "It matters because..."
  }
}
```

## How It Works

```
┌─────────────────────────────────────────────────────┐
│                  USER INPUT                         │
│  Topic: "Neural Networks"                           │
│  Role: "Data Scientist"                             │
│  Session: "abc-123"                                 │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│           ROLE-BASED PROMPT TEMPLATE                │
│  "You are a {role}. Explain {input} for a beginner"│
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│              SESSION MEMORY                         │
│         (Conversation History Context)              │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│              GPT-4o-mini Response                   │
│         (Structured JSON Output)                    │
├─────────────────────────────────────────────────────┤
│  {                                                  │
│    "what": "Neural networks are...",                │
│    "how": "They work by...",                        │
│    "why": "They're important because..."            │
│  }                                                  │
└─────────────────────────────────────────────────────┘
```

## Available Roles

| Role | Perspective |
|------|-------------|
| Teacher | Simplified, step-by-step explanations |
| Scientist | Research-focused, theoretical depth |
| Engineer | Practical, implementation-focused |
| Student | Beginner-friendly, analogy-based |
| Executive | Business impact, high-level overview |

---

<div align="center">
<img src="https://img.shields.io/badge/Status-Active-10B981?style=for-the-badge" alt="Status"/>
</div>
