import asyncio
from setup import model
from agents import Agent, Runner, function_tool, set_tracing_disabled

set_tracing_disabled(disabled=True)

import asyncio


# Function tools
@function_tool
def get_flights(origin: str, destination: str) -> str:
    return f"Here are the flight details from {origin} to {destination}."


@function_tool
def suggest_hotel(destination: str) -> str:
    return f"Here are the hotel details for {destination}."


# Agents
destination_agent = Agent(
    name="Destination Agent",
    instructions="You are a destination agent. Ask the user where they want to travel or help them choose a destination.",
    model=model
)

booking_agent = Agent(
    name="Booking Agent",
    instructions=(
        "You are a booking agent. When the user asks for a flight, ask them for origin and destination if not provided. "
        "If the user provides them, use the tool `get_flights(origin, destination)` to return flight details. "
        "For hotels, use `suggest_hotel(destination)` when asked."
    ),
    model=model,
    tools=[get_flights, suggest_hotel]
)

explore_agent = Agent(
    name="Explore Agent",
    instructions="You are an explore agent. Recommend attractions, local food, and interesting places to visit at the user's chosen destination.",
    model=model
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You are a routing agent. Based on the user's request, hand off the conversation to the most relevant agent: booking, explore, or destination.",
    model=model,
    handoffs=[booking_agent, explore_agent, destination_agent]
)


async def main():
    history = []
    print("Welcome! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        history.append({"role": "user", "content": user_input})

        result = await Runner.run(starting_agent=triage_agent, input=history)

        response = result.final_output
        history.append({"role": "assistant", "content": response})
        print(f"Assistant: {response}")


asyncio.run(main())
