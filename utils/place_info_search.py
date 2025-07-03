import os
import json
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 

class GooglePlaceSearchTool:
    def __init__(self, api_key: str = None):
        if not api_key:
            api_key = os.environ.get("GPLACES_API_KEY")
        if api_key:
            self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
            self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
            self.enabled = True
        else:
            print("[Warning] Google Places API key not found. Google search will be disabled; only Tavily will be used.")
            self.enabled = False
    
    def google_search_attractions(self, place: str) -> str:
        if self.enabled:
            return self.places_tool.run(f"top attractive places in and around {place}")
        else:
            raise RuntimeError("Google Places is not enabled.")
    
    def google_search_restaurants(self, place: str) -> str:
        if self.enabled:
            return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
        else:
            raise RuntimeError("Google Places is not enabled.")
    
    def google_search_activity(self, place: str) -> str:
        if self.enabled:
            return self.places_tool.run(f"Activities in and around {place}")
        else:
            raise RuntimeError("Google Places is not enabled.")

    def google_search_transportation(self, place: str) -> str:
        if self.enabled:
            return self.places_tool.run(f"What are the different modes of transportations available in {place}")
        else:
            raise RuntimeError("Google Places is not enabled.")

class TavilyPlaceSearchTool:
    def __init__(self):
        self.tavily_search = TavilySearchAPIWrapper()

    def tavily_search_attractions(self, place: str) -> str:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        try:
            result = self.tavily_search.run(f"top attractive places in and around {place}")
            return result
        except Exception as e:
            return f"Could not search attractions for {place}: {str(e)}"
    
    def tavily_search_restaurants(self, place: str) -> str:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        try:
            result = self.tavily_search.run(f"what are the top 10 restaurants and eateries in and around {place}")
            return result
        except Exception as e:
            return f"Could not search restaurants for {place}: {str(e)}"
    
    def tavily_search_activity(self, place: str) -> str:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        try:
            result = self.tavily_search.run(f"activities in and around {place}")
            return result
        except Exception as e:
            return f"Could not search activities for {place}: {str(e)}"

    def tavily_search_transportation(self, place: str) -> str:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        try:
            result = self.tavily_search.run(f"What are the different modes of transportations available in {place}")
            return result
        except Exception as e:
            return f"Could not search transportation for {place}: {str(e)}"
    
