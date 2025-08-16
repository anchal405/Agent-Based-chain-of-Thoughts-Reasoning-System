from crewai import Crew
from tasks import create_tasks
from agents import problem_decomposer_agent, information_retriever_agent, reasoning_agent, answer_composer_agent


#create a crew

query = input("Enter your question: ")
tasks = create_tasks(query)
agents = [task.agent for task in tasks]

crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=True
)



response = crew.kickoff()
print(response)
