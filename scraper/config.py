from os import getenv
from dotenv import load_dotenv

load_dotenv()

GITHUB_URL = getenv("GITHUB_URL")
OUTPUT_PATH = getenv("OUTPUT_PATH")