from crewai import Agent
from llm import get_gemini_llm
from crewai_tools import SerperDevTool,WebsiteSearchTool

from dotenv import load_dotenv
load_dotenv()



llm=get_gemini_llm()


#problem Decomposer agent

problem_decomposer_agent = Agent(
    role="Problem Decomposer",
    goal="Decompose the problem into smaller sub-problems",
    backstory="You are a problem decomposer agent. You are responsible for decomposing the problem into smaller sub-problems.",
    llm=llm,
    verbose=True
)

#Information  retriever agent

information_retriever_agent = Agent(
    role="Information Retriever",
    goal="Retrieve information from the web",
    backstory="You are a information retriever agent. You are responsible for gathering background knowledge facts that might be critical to solve the problem use the avialble tools only when you need to.",
    llm=llm,
    tools=[SerperDevTool()],
    verbose=True
)




#Reasoning agent

reasoning_agent = Agent(
    role="Reasoning",
    goal="Reason about the problem and the information retrieved",
    backstory="You are a reasoning agent. You are responsible for reasoning about the problem by logically commbining the facts and the information retrieved for addressing the problem.",
    llm=llm,
    verbose=True
)


#Answer composer agent
answer_composer_agent = Agent(
    role="Answer Composer",
    goal="Compose the answer to the problem",
    backstory="You are a answer composer agent. You are responsible for the final answer to the problem in a concise and informative manner.",
    llm=llm,
    verbose=True
)
