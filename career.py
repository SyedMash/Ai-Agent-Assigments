import asyncio
from setup import model
from agents import Agent, Runner, function_tool, set_tracing_disabled

set_tracing_disabled(disabled=True)

career_agent = Agent(
    name="Career Agent",
    instructions="Your are a career agent. Help user about his career opportunities",
    model=model
)

skill_agent = Agent(
    name="Skill Agent",
    instructions="You are a skills agent. Help user about skills he can learn",
    model=model
)

job_agent = Agent(
    name="Job Agent",
    instructions="You are a job agent. Help user about getting a job",
    model=model
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You are a routing agent. Handoffs to given agents prior to user's query",
    model=model,
    handoffs=[career_agent, skill_agent, job_agent]
)


async def main():
    user_input = input("Enter your query: ")
    result = await Runner.run(starting_agent=triage_agent, input=user_input)
    print(result.final_output)


if __name__ == '__main__':
    asyncio.run(main())
