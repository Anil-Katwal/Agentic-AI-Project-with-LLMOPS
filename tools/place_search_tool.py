import os
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.tavily_api_key = os.environ.get("TAVILY_API_KEY")
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            return "Attraction search is unavailable because no Google Places or Tavily API key is set."
        
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            return "Restaurant search is unavailable because no Google Places or Tavily API key is set."
        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            return "Activity search is unavailable because no Google Places or Tavily API key is set."
        
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            return "Transportation search is unavailable because no Google Places or Tavily API key is set."
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]