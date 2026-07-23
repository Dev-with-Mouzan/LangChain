<div align="center">

<img src="https://img.shields.io/badge/Research-Agent-AI_Assistant-3B82F6?style=for-the-badge&logo=robot&logoColor=white" alt="Research Agent"/>

# Research Agent

<p align="center">
  <img src="https://img.shields.io/badge/LangChain-Agents-374151?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenRouter-Qwen_3-FF6B35?style=flat-square" alt="OpenRouter"/>
  <img src="https://img.shields.io/badge/Streaming-Real--Time-10B981?style=flat-square" alt="Streaming"/>
</p>

**A multi-tool research agent with web search, URL reading, Wikipedia lookup, calculator, and time utilities — powered by streaming responses.**

</div>

---

## Features

- **Multi-Tool Architecture** - 6 integrated tools for comprehensive research
- **Streaming Responses** - Real-time output via SSE
- **Web Search** - Fetch live information from the internet
- **URL Reader** - Extract content from any webpage
- **Wikipedia Search** - Access encyclopedic knowledge
- **Calculator** - Perform mathematical operations
- **Time Tool** - Get current date/time information
- **Modern Frontend** - Responsive web interface

## Architecture

```
Research_Agent/
├── main.py                  # FastAPI app & static files
├── api/
│   └── router.py           # API route definitions
├── Core/
│   ├── llm.py              # OpenRouter Qwen 3-8B config
│   └── get_response.py     # Response streaming logic
├── agent_tool/
│   ├── web_search_tool.py  # Internet search
│   ├── url_reader_tool.py  # URL content extraction
│   ├── wiki_search_tool.py # Wikipedia lookup
│   ├── calculator.py       # Math operations
│   ├── time_tool.py        # Current time
│   └── arvic_tool.py       # Additional tooling
├── models/
│   └── input_model.py      # Pydantic input schema
└── Frontend/               # Web interface assets
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| AI Engine | LangChain Agents |
| LLM | Qwen 3-8B (via OpenRouter) |
| Streaming | SSE (Server-Sent Events) |
| Frontend | HTML/CSS/JS |

## Setup

```bash
# Clone and navigate
cd 08-Projects/Research_Agent

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn langchain-openai langchain-core python-dotenv

# Configure environment
echo "OPENROUTER_API_KEY=your_key_here" > Core/.env

# Run the application
python main.py
```

Navigate to `http://0.0.0.0:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve frontend |
| `GET` | `/api/health` | Health check |
| `GET` | `/api/version` | Version info |
| `POST` | `/api/get_response` | Stream research response |

### POST `/api/get_response`

```json
{
  "question": "What are the latest developments in quantum computing?"
}
```

**Response:** Streamed text content via SSE

## Agent Tool Ecosystem

```
                    ┌─────────────────┐
                    │  User Question  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Qwen 3-8B    │
                    │  (OpenRouter)   │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │  Web Search  │ │ URL Reader   │ │   Wiki       │
    └──────────────┘ └──────────────┘ └──────────────┘
            │                │                │
            ▼                ▼                ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │  Calculator  │ │  Time Tool   │ │  ARVIC Tool  │
    └──────────────┘ └──────────────┘ └──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Streaming      │
                    │  Response       │
                    └─────────────────┘
```

---

<div align="center">
<img src="https://img.shields.io/badge/Status-Active-10B981?style=for-the-badge" alt="Status"/>
</div>
