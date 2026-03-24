from dotenv import load_dotenv
import os

load_dotenv()



NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "Badal123"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")