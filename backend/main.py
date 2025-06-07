from fastapi import FastAPI
import yaml
import logging
from contextlib import asynccontextmanager


# Set up the root logger
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)
logger = logging.getLogger(__name__)  # Create a logger for this module

# Testing logger initialization
logger.info("Logger initialized successfully")

# Setting up dummy config variable
content = {}


# unloading page contents from yml file
def load_page_content():
    """
    Load the 'main' page content from a YAML file.
    """
    try:
        with open("page_content.yml", "r") as file:
            config = yaml.safe_load(file)
            # config is a list of dicts, find the one with 'main' key
            for item in config:
                if "main" in item:
                    return item["main"]
            logger.error("'main' section not found in page_content.yml.")
            return {}
    except FileNotFoundError:
        logger.error("page_content.yml not found.")
        return {}
    except yaml.YAMLError as e:
        logger.error(f"Error loading YAML file: {e}")
        return {}


content = load_page_content()

# Display loaded content for debugging
logger.info("Loaded page content: %s", content)


# Add an async context manager for lifecycle management for the FastAPI app
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.
    This can be used for startup and shutdown events.
    """
    logger.info("Starting up the FastAPI application...")
    global content
    content = load_page_content()
    logger.info("Page content loaded for FastAPI application: %s", content)
    yield  # This allows the application to run


# This is the main entry point for the FastAPI application.
api = FastAPI(lifespan=lifespan)


@api.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message and page content.
    """
    return {
        "title": content.get("title", "Welcome to the API!"),
        "description": content.get("description", "This is the default description."),
        "background_image_folder": content.get("background_image_folder", "images/"),
    }
