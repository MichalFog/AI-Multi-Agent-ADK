# 🌐 Multi-Tool Agent using Google's ADK

This project is a Python-based agent built with Google's Agent Development Kit (ADK).  
It demonstrates how to create a local agent with multiple tools such as checking the weather and getting the current time in a city.

---

## 🚀 Features

- ✅ Built using [`google-adk`](https://pypi.org/project/google-adk/)
- 🔧 Includes two tools:
  - `get_weather`: Provides weather information for New York (mocked).
  - `get_current_time`: Returns current time in New York.
- 💻 Runs locally with `adk web` for an interactive browser UI
- 🎙️ Supports microphone input (with Gemini Live API)
- 🔐 Uses `.env` for secure API key management

---

## 📁 Project Structure

```
multi_tool_agent/
├── __init__.py
├── agent.py
├── .env
```

---

## 🛠️ Quickstart

### 1. Clone & Set up Environment

```bash
git clone https://github.com/MichalFog/multi-tool-agent-adk.git
cd multi-tool-agent-adk

# Create and activate virtual environment
python -m venv .venv
# On macOS/Linux
source .venv/bin/activate
# On Windows CMD
.venv\Scripts\activate.bat
# On Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
pip install google-adk
```

### 3. Configure Environment Variables

Create a `.env` file in the `multi_tool_agent/` directory:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

Replace `PASTE_YOUR_ACTUAL_API_KEY_HERE` with your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## 🧪 Run the Agent

Navigate to the parent folder (one level above `multi_tool_agent`) and launch the web UI:

```bash
adk web
```

Open the URL in your browser (e.g. http://localhost:8000), and select your agent: `multi_tool_agent`.

---

## 💬 Example Prompts to Try

- What is the weather in New York?
- What is the time in New York?
- What is the weather in Paris?
- What is the time in Paris?

---

## 🛣️ Next Steps

- Add more tools (e.g. location, calendar, news)
- Add memory and session state
- Switch to Gemini Live model for voice input
- Deploy as API server using `adk api_server`

---

## 📜 License
