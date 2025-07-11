from agents import OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_AI_API_KEY = os.getenv("GEMINI_AI_API_KEY")

external_client = AsyncOpenAI(
    api_key=GEMINI_AI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
