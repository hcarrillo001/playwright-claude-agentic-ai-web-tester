from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import asyncio
import os




def main():
    file_name = "testdescription.txt"
    test_description = read_from_file(file_name)
    asyncio.run(chat_with_agent(test_description))


def read_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")





async def chat_with_agent(test_description):
    load_dotenv()
    #model = ChatAnthropic(model_name="claude-3-5-sonnet-20240620")
    model = ChatAnthropic(model_name="claude-3-5-haiku-20241022")

    #llm = ChatGoogleGenerativeAI(model="gemini-pro")

    # tools used is bright data mcp, specify the commands to load mcp client within python script with our agent, similar to what was done in the claude desktop app
    server_params = StdioServerParameters(
        command="npx",
        env={
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY")
        },
        # make sure to update the full absolute path to your math_server.py file
        args=["@playwright/mcp@latest"],
    )
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model,tools)


            #start conversation history
            #encourages agent to use multiple of the tools
            messages = [
                {
                    "role": "system",
                    "content": "You can use multiple tools in sequence to answer complex questions. Think step by step. After each answer determine if its PASS or FAIL or UNDETERMINED and print it as a seperate response"
                }
            ]


            user_input= "Testing Description: " + test_description

            #add user history (adding more context)
            messages.append({"role": "user", "content": user_input})

            #call the agent
            agent_response = await agent.ainvoke({"messages": messages})

            #extract agents reply and add to history
            ai_message = agent_response["messages"][-1].content
            print(f"Agent: {ai_message}")
            return ai_message




if __name__ == '__main__':
    main()