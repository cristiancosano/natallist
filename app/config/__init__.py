from .environment import initialize_environment
from .database import register_database
from .routes import register_routes


def initialize_config(app):
    initialize_environment()  # Must be the first called function!
    register_database(app)
    register_routes(app)
