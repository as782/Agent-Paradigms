from core.Agents.ReAct.agent import ReActAgent  
from tools.google_search import search
from tools.base import ToolExecutor
from core.Agents.base import HelloAgentsLLM
from dotenv import load_dotenv
load_dotenv()
tool_executor = ToolExecutor()
tool_executor.registerTool("google_search", "使用谷歌搜索", search)
llm = HelloAgentsLLM()

ReAct_agent = ReActAgent(llm_client=llm, tool_executor=tool_executor,max_steps=5)


if __name__ == '__main__':
    print('=== ReAct 范式 Agent 测试 ===')
    ReAct_agent.run("华为最新手机")