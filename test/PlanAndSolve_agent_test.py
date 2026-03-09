from core.Agents.PlanAndSolve.agent import PlanAndSolveAgent  
from core.Agents.base import HelloAgentsLLM
from dotenv import load_dotenv
load_dotenv()
 
llm = HelloAgentsLLM()

plan_and_solve_agent = PlanAndSolveAgent(llm_client=llm)


if __name__ == '__main__':
    print('=== PlanAndSolve 范式 Agent 测试 ===')
    plan_and_solve_agent.run("一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？")