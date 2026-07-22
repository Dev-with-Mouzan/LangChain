<div align="center">

<img src="https://img.shields.io/badge/Prompt-Generator-AI_Prompt_Engineer-8B5CF6?style=for-the-badge&logo=openai&logoColor=white" alt="Prompt Generator"/>

# Prompt Generator

<p align="center">
  <img src="https://img.shields.io/badge/LangChain-Chains-374151?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenAI-LLM-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI"/>
</p>

**An AI-powered tool that transforms user requirements into professionally structured prompts using advanced prompt engineering techniques.**

</div>

---

## Features

- **Professional Prompt Generation** - Converts raw ideas into structured prompts
- **Role-Based Engineering** - Assigns AI roles, goals, and constraints
- **Customizable Tone** - Adjust output style (formal, casual, technical, etc.)
- **Structured Output** - Role, Goal, Context, Instructions, Constraints, Output Format
- **REST API** - Clean API endpoints for integration

## Architecture

```
Prompt_generator/
├── main.py                    # FastAPI app entry point
├── api/
│   └── route.py              # API route definitions
├── core/
│   ├── llm.py                # LLM model configuration
│   └── prompt.py             # LangChain prompt template & chain
├── models/
│   ├── request_model.py      # Pydantic request schema
│   └── response_model.py     # Pydantic response schema
└── frontend/                 # Web interface assets
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| AI Engine | LangChain + OpenAI |
| Parser | StrOutputParser |
| Validation | Pydantic |
| Server | Uvicorn |

## Setup

```bash
# Clone and navigate
cd 08-Projects/Prompt_generator

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn langchain-openai langchain-core python-dotenv

# Configure environment
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the application
python main.py
```

Navigate to `http://0.0.0.0:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/health` | Health check |
| `POST` | `/generate_prompt` | Generate a professional prompt |

### POST `/generate_prompt`

```json
{
  "user_input": "Create a chatbot for customer support",
  "tone": "professional"
}
```

**Response:**
```json
{
  "generated_prompt": "ROLE: You are a Senior Customer Support Specialist..."
}
```

## Prompt Structure

```
┌──────────────────────────────────────┐
│           USER INPUT                 │
│     "Create a chatbot for..."        │
└──────────────┬───────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│         AI PROMPT ENGINEER           │
│     (LangChain + OpenAI Chain)       │
├──────────────────────────────────────┤
│  ROLE:        Who the AI should be   │
│  GOAL:        What to accomplish     │
│  CONTEXT:     Background info        │
│  INSTRUCTIONS: Step-by-step guide    │
│  CONSTRAINTS: Rules to follow        │
│  OUTPUT FORMAT: Expected format      │
└──────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│       PROFESSIONAL PROMPT            │
│    (Ready to use with any LLM)       │
└──────────────────────────────────────┘
```

---

<div align="center">
<img src="https://img.shields.io/badge/Status-Active-10B981?style=for-the-badge" alt="Status"/>
</div>
