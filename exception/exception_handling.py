"""
Custom exception classes for the AI Trip Planner application.
"""

class TripPlannerException(Exception):
    """Base exception class for the Trip Planner application."""
    pass


class APIKeyMissingException(TripPlannerException):
    """Raised when a required API key is missing."""
    pass


class ModelLoadException(TripPlannerException):
    """Raised when there's an error loading the AI model."""
    pass


class WeatherAPIException(TripPlannerException):
    """Raised when there's an error with weather API calls."""
    pass


class PlaceSearchException(TripPlannerException):
    """Raised when there's an error with place search API calls."""
    pass


class CurrencyConversionException(TripPlannerException):
    """Raised when there's an error with currency conversion API calls."""
    pass


class GraphBuildException(TripPlannerException):
    """Raised when there's an error building the agent graph."""
    pass


class ConfigurationException(TripPlannerException):
    """Raised when there's an error with configuration loading."""
    pass
