# Personal Finance Advisor Prototype

This is a prototype of an agentic AI-based personal finance advisor for a retail bank. It demonstrates multi-agent architecture with the following agents:

- **Planner Agent**: Coordinates the system, understands user queries, decides which agents to invoke, maintains execution flow, and generates final responses.

- **Spend Analysis Agent**: Analyzes customer transactions, categorizes expenses, calculates monthly spending trends, detects unusual patterns, and generates summarized insights.

- **Recommendation Agent**: Generates financial advice based on insights, suggests savings, budget optimization, and spending reductions.

- **Alerting Agent**: Identifies financial risks, detects overspending, triggers warnings, and notifies about unusual spikes.

## Architecture

The system uses a modular architecture with separate frontend and backend.

- **Backend**: FastAPI-based Python API using LangChain for agent tools and LangGraph for multi-agent orchestration.
- **Frontend**: React app (via Vite) for conversational chat interface.

Mock functions are used for AI capabilities, tool calling, and data fetching. LangChain's FakeLLM is used for demonstration without requiring real LLM APIs.

Basic memory is implemented via LangChain's ConversationBufferMemory.

## Running the Prototype

1. **Backend**:
   - Install Python dependencies: `pip install -r backend/requirements.txt`
   - Run: `uvicorn backend.app:app --reload` (runs on http://localhost:8000)

2. **Frontend**:
   - Install Node.js dependencies: `npm install` (in frontend/)
   - Run: `npm run dev` (runs on http://localhost:5173)

Open the frontend in your browser and start chatting with the advisor. Enter queries like "Analyze my spending".

## Project Structure

- `backend/`: FastAPI backend with agents, memory, and tools.
- `frontend/`: React frontend for chat interface.
- `README.md`: This file.

## Architectural Decisions

- **Separated Frontend/Backend**: Backend handles logic via FastAPI, frontend provides UI via React.
- **Modular Design**: Each agent is in its own file for clarity and maintainability.
- **Mock AI**: Since this is a prototype, LangChain's FakeLLM is used with LangGraph for orchestration to demonstrate agentic AI without requiring actual LLM integration.
- **Lightweight Libraries**: FastAPI for backend, Vite+React for frontend, LangChain/LangGraph for agent framework.
- **Basic Memory**: LangChain's ConversationBufferMemory for context.
- **Tool Calling**: Mock tools for data fetching and analysis.