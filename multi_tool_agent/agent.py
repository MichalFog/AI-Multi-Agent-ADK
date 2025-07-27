import datetime
import asyncio
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner  # ← תיקון חשוב: מייבאים מ־google.adk, לא מ־asyncio!

# ---------- TOOLS ----------

def get_weather(city: str) -> dict:
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

def get_current_time(city: str) -> dict:
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

# ---------- AGENTS ----------

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"
AGENT_MODEL = MODEL_GEMINI_2_0_FLASH

weather_agent = Agent(
    name="weather_agent_v1",
    model=AGENT_MODEL,
    description="Provides weather information for specific cities.",
    instruction="You are a helpful weather assistant. "
                "When the user asks for the weather in a specific city, "
                "use the 'get_weather' tool to find the information. "
                "If the tool returns an error, inform the user politely. "
                "If the tool is successful, present the weather report clearly.",
    tools=[get_weather],
)

root_agent = Agent(
    name="weather_time_agent",
    model=AGENT_MODEL,
    description="Agent to answer questions about the time and weather in a city.",
    instruction="You are a helpful agent who can answer user questions about the time and weather in a city.",
    tools=[get_weather, get_current_time],
)

print(f"Agent '{weather_agent.name}' created using model '{AGENT_MODEL}'.")

# ---------- MAIN ASYNC FUNCTION ----------

async def main():
    # Session service
    session_service = InMemorySessionService()

    # Session constants
    APP_NAME = "weather_tutorial_app"
    USER_ID = "user_1"
    SESSION_ID = "session_001"

    # Create session
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")

    runner = Runner(
        agent=weather_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    print(f"Runner created for agent '{runner.agent.name}'.")

    # Ask a question
asyncio.run(main())
