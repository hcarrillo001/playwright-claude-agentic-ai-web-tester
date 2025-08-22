# playwright-claude-agentic-ai-web-tester
Using Playwrights MCP to automated Web Testing. 


💡 Vision & Future Potential
While the current steps are simple and processing may take some time, this proof of concept shows promising potential:
Extract test steps directly from tools like Quality Center (QC/ALM) or 
something like Microsoft Azure Devops to read the test cases and have the automation run. 


🧪 Playwright MCP Demo
This simple demo shows how natural language instructions in English can be used to control a web browser. Using Claude (LLM) integrated with Playwright MCP, the system automates browser actions based on plain English commands. The code does not have any playwright webdriver code. This testing is completly done using plain english language (testdescription.txt). 

It leverages the LangChain Playwright tool to translate language inputs into executable browser steps.
https://python.langchain.com/docs/integrations/tools/playwright/

📺 Demo Video: https://youtu.be/o-djtIUneg8

⚙️ How It Works
You provide instructions in plain English.

Claude interprets the commands.

LangChain + Playwright MCP carry out browser actions automatically.

💡 Vision & Future Potential
While the current steps are simple and processing may take some time, this proof of concept shows promising potential:

Run multiple agents simultaneously for parallel test execution.



Enable scalable web test automation using natural language.


Important Libraries 

| Library                      | Description                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| **`mcp`**                    | Interface to the Mission Control Platform for managing parameters, sessions, and telemetry. |
| **`langchain_mcp_adapters`** | MCP-compatible tools and agents for use with LangChain.                                     |
| **`langgraph`**              | Enables graph-based, reactive agent flows.                                                  |
| **`langchain_anthropic`**    | Integration for Claude language models.                                                     |
| **`dotenv`**                 | Loads sensitive config (API keys, MCP params) from a `.env` file.                           |
| **`asyncio`**                | Enables asynchronous execution of agent operations.                                         |
| **`os`**                     | Used to access environment variables.                                                       |


⚙️ Setup

 Node.js (v16 or higher)

Python 3.x

🔹 1. Claude Desktop Setup 

    Download and install from Anthropic.
    
    Launch the app.
    
    Go to Settings → Developer Settings and ensure it's ready for local development.

🔹 2. Account Setup
    
    Anthropic
    
    Create an account: Anthropic Console
    
    Generate your API Key (you’ll need to add a credit card).
    
    Add this key as an environment variable in your Python project (ANTHROPIC_API_KEY).

Playwright

🔹 3. Configure Playwright MCP Server
Option A – Use a config.json file:

    {
      "mcpServers": {
        "playwright": {
          "command": "npx",
          "args": [
            "@playwright/mcp@latest"
          ]
        }
      }
    }

🔹 4.  Python Code runs the Agent using the Playwright MCP


🔧 Technologies Used
Claude (LLM by Anthropic)

Playwright

LangChain/LangGraph

