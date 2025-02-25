from dotenv import load_dotenv
from langchain.agents import tool

load_dotenv()

def get_text_length(text: str) -> int:
    """Returns the length of the text by characters"""
    print(f"get_text_length called with: {text=}")
    text = text.strip("'\n").strip("'")
    return len(text)


if __name__ == "__main__":
    print("Hello ReAct LangChain!")

    tools = [get_text_length]

    template="""
    Answer teh following questions as best you can.
    You have access to the following tools:
    {tools}

    Use the following format:
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought: {agent_scratchpad}
    """

    agent = create_react_agent(tools, template)
    
    