# Powered Chatbot using Gemini API
# This code uses the Gemini API to create a chatbot that can answer questions.
from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import chainlit as cl

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="My Chatbot Danish",
    instructions ="An agent that uses Gemini API to answer questions."
)


# Chainlit integration
@cl.on_message
async def handle_message(message: cl.Message):
    run_result = await Runner.run(agent, input=message.content, run_config=config)
    final_response = run_result.final_output
    await cl.Message(content=final_response).send()
# print(response)