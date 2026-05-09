from fastapi import FastAPI
from agents.planner_agent import PlannerAgent
from memory.memory import Memory

app = FastAPI(title="Personal Finance Advisor", description="Agentic AI for financial insights")

memory = Memory()
planner = PlannerAgent(memory)

@app.post("/chat")
async def chat(user_input: str):
    response = planner.process(user_input)
    return {"response": response}

@app.get("/")
async def root():
    return {"message": "Welcome to Personal Finance Advisor API"}