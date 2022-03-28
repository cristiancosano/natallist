import os
from dotenv import load_dotenv
from pathlib import Path


def initialize_environment():
    env_path = Path(__file__).parent.parent.joinpath('.env')
    load_dotenv(env_path)
