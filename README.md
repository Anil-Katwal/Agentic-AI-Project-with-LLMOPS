# 🌍 AI Trip Planner

An intelligent travel planning application powered by AI that provides comprehensive trip itineraries with real-time data integration.

## Features

- **Real-time Weather Information**: Get current weather and forecasts for your destination
- **Place Search**: Find attractions, restaurants, activities, and transportation options
- **Expense Calculator**: Calculate trip costs and daily budgets
- **Currency Conversion**: Convert between different currencies
- **Comprehensive Itineraries**: Detailed day-by-day travel plans
- **Multiple AI Providers**: Support for Groq and OpenAI models

## Prerequisites

- Python 3.10 or higher
- API keys for the following services:
  - Groq API (or OpenAI API)
  - OpenWeatherMap API
  - Google Places API
  - Exchange Rate API
  - Tavily Search API

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_Trip_Planner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with your API keys:
```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
GPLACES_API_KEY=your_google_places_api_key
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Running the Application

You can run both the backend and frontend simultaneously:

```bash
python run_all.py
```

Or run them separately:

**Backend (FastAPI):**
```bash
uvicorn main:app --reload --port 8000
```

**Frontend (Streamlit):**
```bash
streamlit run streamlit_app.py
```

### Using the API

The application provides a REST API endpoint:

- **POST** `/query` - Submit travel planning questions
  - Body: `{"question": "Plan a trip to Paris for 5 days"}`

### Example Usage

1. Open the Streamlit interface at `http://localhost:8501`
2. Enter your travel query (e.g., "Plan a trip to Tokyo for 7 days")
3. The AI will generate a comprehensive travel plan including:
   - Day-by-day itinerary
   - Hotel recommendations with costs
   - Attractions and activities
   - Restaurant suggestions
   - Transportation options
   - Weather information
   - Cost breakdown

## Project Structure

```
AI_Trip_Planner/
├── agent/                 # Agent workflow and graph building
├── tools/                 # LangChain tools for various services
├── utils/                 # Utility functions and services
├── config/               # Configuration files
├── prompt_library/       # System prompts
├── exception/            # Exception handling
├── logger/               # Logging utilities
├── main.py              # FastAPI backend
├── streamlit_app.py     # Streamlit frontend
└── run_all.py           # Script to run both services
```

## Configuration

The application uses `config/config.yaml` for model configurations:

```yaml
llm:
  openai:
    provider: "openai"
    model_name: "gpt-4"
  groq:
    provider: "groq"
    model_name: "deepseek-r1-distill-llama-70b"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue in the repository.