import random
import asyncio
from setup import model
from agents import Agent, Runner, set_tracing_disabled, function_tool


@function_tool
def roll_dice() -> int:
    return random.randint(1, 6)

@function_tool()
def generate_event() -> str:
    events = [
        "A hidden trap is triggered!",
        "A treasure chest appears.",
        "An old wizard offers help.",
        "A secret passage is revealed.",
        "A monster ambushes you!"
    ]
    return random.choice(events)


narrator_agent = Agent(
    name="Narrator Agent",
    instructions=(
        "You are the story narrator. Move the adventure forward based on the player's choices. "
        "When needed, you may call `generate_event` to surprise the player."
    ),
    model=model,
    tools=[generate_event]
)

monster_agent = Agent(
    name="Monster Agent",
    instructions=(
        "You manage combat encounters. "
        "Use `roll_dice` to calculate attack damage, defense, or chance to hit."
    ),
    model=model,
    tools=[roll_dice]
)

item_agent = Agent(
    name="Item Agent",
    instructions=(
        "You handle inventory and item rewards. "
        "When the player defeats an enemy or finds treasure, decide what they get."
    ),
    model=model
)

triage_agent = Agent(
    name="Game Master Agent",
    instructions=(
        "You are the game master. Read the player's input and decide which agent should handle it: "
        "narrator, monster, or item agent. For example, if the player enters a choice, hand off to narrator; "
        "if they choose to fight, hand off to monster; if they ask about loot, hand off to item agent."
    ),
    model=model,
    handoffs=[narrator_agent, monster_agent, item_agent]
)


async def main():
    history = []
    print("Welcome to the Fantasy Adventure Game! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("👋 Thanks for playing!")
            break

        history.append({"role": "user", "content": user_input})

        result = await Runner.run(starting_agent=triage_agent, input=history)

        response = result.final_output
        print(f"Assistant: {response}")

        history.append({"role": "assistant", "content": response})


asyncio.run(main())
