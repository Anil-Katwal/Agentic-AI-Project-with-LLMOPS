from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from starlette.responses import JSONResponse
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os

# Load .env variables
load_dotenv()

from agent.agentic_workflow import GraphBuilder  # This must NOT expect model_provider='groq' unless handled

app = FastAPI(title="Trip Planner", description="An intelligent travel planning application by Katwal Travel Agency")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class QueryRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML page"""
    try:
        # Try to serve the static HTML file
        return FileResponse("static/index.html")
    except FileNotFoundError:
        # Fallback: return a simple HTML page
        return HTMLResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title> Trip Planner by Katwal's Travel Agency</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
                .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; text-align: center; }
                .content { margin-top: 30px; }
                textarea { width: 100%; height: 120px; padding: 15px; border: 2px solid #e1e5e9; border-radius: 10px; margin: 10px 0; }
                button { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 15px 30px; border-radius: 10px; cursor: pointer; }
                .result { margin-top: 20px; padding: 20px; background: #f8f9fa; border-radius: 10px; display: none; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🌍 Trip Planner with details</h1>
                <p>Plan your perfect trip preparing by Katwal travel agency</p>
            </div>
            <div class="content">
                <h3>Describe your trip:</h3>
                <textarea id="query" placeholder="Example: Plan a trip to Paris for 5 days with a budget of $2000"></textarea>
                <br>
                <button onclick="planTrip()">🚀 Plan My Trip</button>
                <div id="result" class="result"></div>
            </div>
            <script>
                async function planTrip() {
                    const query = document.getElementById('query').value.trim();
                    if (!query) {
                        alert('Please enter a trip description');
                        return;
                    }
                    
                    const result = document.getElementById('result');
                    result.style.display = 'block';
                    result.innerHTML = 'AI is planning your trip...';
                    
                    try {
                        const response = await fetch('/query', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({question: query})
                        });
                        const data = await response.json();
                        result.innerHTML = data.answer.replace(/\\n/g, '<br>');
                    } catch (error) {
                        result.innerHTML = 'Error: ' + error.message;
                    }
                }
            </script>
        </body>
        </html>
        """)

@app.get("/health")
async def health_check():
    """Health check endpoint for Render deployment"""
    return {"status": "healthy", "message": "AI Trip Planner is running"}

@app.get("/api")
async def api_info():
    """API information endpoint"""
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

        # Do NOT pass model_provider unless GraphBuilder accepts it
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
