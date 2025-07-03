from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import JSONResponse
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os

# Load .env variables
load_dotenv()

from agent.agentic_workflow import GraphBuilder  # This must NOT expect model_provider='groq' unless handled

app = FastAPI(title="AI Trip Planner", description="An intelligent travel planning application powered by AI")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
async def health_check():
    """Health check endpoint for Render deployment"""
    return {"status": "healthy", "message": "AI Trip Planner is running"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "AI Trip Planner API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "query": "/query"
        }
    }

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(f"Received question: {query.question}")

        # ✅ Do NOT pass model_provider unless GraphBuilder accepts it
        graph = GraphBuilder()  # Remove model_provider="groq" if it's not accepted

        react_app = graph()  # Build the reactive app

        # Optional: Save graph visualization
        try:
            png_graph = react_app.get_graph().draw_mermaid_png()
            with open("my_graph.png", "wb") as f:
                f.write(png_graph)
            print("Graph image saved as 'my_graph.png'")
        except Exception as graph_error:
            print(f"[Warning] Failed to generate graph: {graph_error}")

        # Prepare messages for the agent - create proper HumanMessage
        human_message = HumanMessage(content=query.question)
        messages = {"messages": [human_message]}
        output = react_app.invoke(messages)

        # Extract and return final message
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}

    except Exception as e:
        print(f"[Error] {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
