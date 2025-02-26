"""
Name: callbacks.py
Description: This file contains the callback handler for the agent. This helps visualize the agent's thought process by printing formatted messages at each step.
Date: 2025-02-27
Author: Ann Hagan
"""

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult

class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"\n\n🤔 Prompt to LLM: {prompts[0]}")
        
    def on_llm_end(self, response: LLMResult, **kwargs):
        print(f"💭 Response from LLM: {response.generations[0][0].text}")
        
    def on_tool_start(self, serialized, input_str, **kwargs):
        print(f"🛠️ Calling tool: {input_str}")
        
    def on_tool_end(self, output, **kwargs):
        print(f"🔨 Tool output: {output}")
        
    def on_agent_action(self, action: AgentAction, **kwargs):
        print(f"🎯 Agent Action: {action.tool} - {action.tool_input}")
        
    def on_agent_finish(self, finish: AgentFinish, **kwargs):
        print(f"🏁 Agent Finish: {finish.return_values}") 