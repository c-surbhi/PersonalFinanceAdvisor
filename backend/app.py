from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.agents.planner_agent import PlannerAgent

app = FastAPI(title="Personal Finance Advisor", description="Agentic AI for financial insights")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_input: str

planner = PlannerAgent()

@app.post("/chat")
async def chat(request: ChatRequest):
    response = planner.process(request.user_input)
    return {"response": response}

@app.get("/")
async def root():
    return {"message": "Welcome to Personal Finance Advisor API"}