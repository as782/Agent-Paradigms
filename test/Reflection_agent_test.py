from core.Agents.Reflection.agent import ReflectionAgent  
from core.Agents.base import HelloAgentsLLM
from dotenv import load_dotenv
load_dotenv()
 
llm = HelloAgentsLLM()

reflection_agent = ReflectionAgent(llm_client=llm)


if __name__ == '__main__':
    print('=== reflection 范式 Agent 测试 ===')
    reflection_agent.run("编写一个Python函数，找出1到n之间所有的素数 (prime numbers)。")