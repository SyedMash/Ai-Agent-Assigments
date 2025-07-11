This repository contains 3 projects, game.py, career.py and travel.py
<h1>Game.py</h1>
Runs a text-based fantasy adventure game using multiple AI agents that collaborate to:

Narrate an evolving story based on player choices.

Handle combat using dice rolls.

Manage inventory, items, and loot.

Coordinate all phases smoothly using a Game Master agent.

Built with:

✅ OpenAI Agent SDK

✅ Runner for multi-agent conversation flow

✅ Custom tools for randomness (roll_dice, generate_event)

<h2>Game Flow</h2>
1️⃣ Player input:
You type a command or choice (e.g. explore forest, fight the orc, open chest).

2️⃣ Game Master routes:
The GameMasterAgent decides which specialized agent should handle the request.

3️⃣ Specialist agents:

If it’s a story choice → NarratorAgent

If it’s combat → MonsterAgent (uses roll_dice)

If it’s about loot/inventory → ItemAgent

4️⃣ Tools in action:
Agents can call tools to roll dice or create random story events as needed.

5️⃣ Loop continues:
Player keeps typing actions until they type exit to end the game.

<h1>Career.py</h1>
This program runs a simple multi-agent AI assistant that helps users with:

Career guidance (Career Agent)

Learning new skills (Skill Agent)

Getting a job (Job Agent)

It uses:

✅ OpenAI Agent SDK

✅ A Triage Agent that decides which specialized agent should handle the user’s query.

<h2>Flow</h2>

1️⃣ User Input:
You type a question or request (e.g. “How do I switch careers to tech?”).

2️⃣ Triage Agent:
Reads your query and decides whether it’s about:

General career advice → Career Agent

Skill suggestions → Skill Agent

Job search help → Job Agent

3️⃣ Specialized Agent:
The chosen agent responds with advice or suggestions.

4️⃣ Output:
You get the final answer in your console.

<h1>Travel.py</h1>
This project is a multi-agent travel assistant.
It helps users:

Pick a travel destination

Book flights and hotels (using mock tools)

Discover local attractions, food, and places to visit

It’s built with:

✅ OpenAI Agent SDK

✅ A Runner to coordinate the conversation

✅ Multiple specialized agents: destination, booking, and explore

✅ Two function tools: get_flights and suggest_hotel (mocked)

<h2>Flow</h2>
1️⃣ User Input:
You type a travel question or request (e.g. “I want to fly from Karachi to Chicago”).

2️⃣ Triage Agent:
Decides which agent should handle it:

If it’s about where to go → Destination Agent

If it’s about booking → Booking Agent

If it’s about things to do → Explore Agent

3️⃣ Specialized Agent:
The agent may:

Ask follow-up questions

Use get_flights or suggest_hotel tools to provide details

4️⃣ Response:
You get an answer in the console.
Type exit to quit anytime.

