<div align="center">

<img src="https://img.shields.io/badge/AI-Study_Planner-10B981?style=for-the-badge&logo=python&logoColor=white" alt="AI Study Planner"/>

# AI Study Planner

<p align="center">
  <img src="https://img.shields.io/badge/LangChain-Chain-374151?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/FastAPI-Server-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI"/>
</p>

**An intelligent study assistant that generates comprehensive learning materials for any topic using AI-powered content generation.**

</div>

---

## Features

- **Topic Explanation** - Detailed markdown-formatted explanations of any subject
- **Simplified Summaries** - Beginner-friendly bullet-point breakdowns
- **Interesting Facts** - Engaging contextual facts to enhance learning
- **Practice Questions** - Auto-generated Q&A for self-assessment
- **Modern UI** - Clean, responsive web interface

## Architecture

```
Ai_Study_Planner/
├── main.py              # FastAPI application & LangChain pipelines
├── static/              # Frontend assets (HTML/CSS/JS)
├── requirements.txt     # Python dependencies
└── .env                 # API keys (not committed)
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| AI Engine | LangChain + OpenAI GPT-4o-mini |
| Parser | StrOutputParser |
| Frontend | Vanilla HTML/CSS/JS |
| Server | Uvicorn |

## Setup

```bash
# Clone and navigate
cd 08-Projects/Ai_Study_Planner

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the application
python main.py
```

Navigate to `http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve frontend |
| `POST` | `/api/study-plan` | Generate study materials for a topic |

### POST `/api/study-plan`

```json
{
  "topic": "Machine Learning"
}
```

**Response:**
```json
{
  "explanation": "...",
  "simplified": "...",
  "fact": "...",
  "questions": "..."
}
```

## How It Works

```
User Input (Topic)
       │
       ▼
┌──────────────────┐
│  Explain Chain   │──▶ Detailed Explanation
└──────────────────┘
       │
       ▼
┌──────────────────┐
│ Simplify Chain   │──▶ Beginner Summary
└──────────────────┘
       │
       ▼
┌──────────────────┐
│   Fact Chain     │──▶ Interesting Fact
└──────────────────┘
       │
       ▼
┌──────────────────┐
│ Question Chain   │──▶ Practice Q&A
└──────────────────┘
```

---

<div align="center">
<img src="https://img.shields.io/badge/Status-Active-10B981?style=for-the-badge" alt="Status"/>
</div>
