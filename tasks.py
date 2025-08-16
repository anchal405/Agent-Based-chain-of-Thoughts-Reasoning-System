from crewai import Task
from agents import problem_decomposer_agent, information_retriever_agent, reasoning_agent, answer_composer_agent




def create_tasks(query):
    

# problem decomposer task

    problem_decomposer_task = Task(
        description=f"Decompose the problem/query into smaller sub-problems/sub-queries for the user query: {query}",
        expected_output="A list of smaller sub-problems/sub-queries",
        agent=problem_decomposer_agent,
        verbose=True,
    )



    #information retriever for the sub-problems

    information_retriever_task = Task(
        description=f"search for facts or knowledge that might be critical to solve the sub-problems/sub-queries for the user query: {query} may be from the web or from the knowledge base or your own knowledge if no tools are available",
        expected_output="A list of facts or knowledge that might be critical to solve the sub-problems/sub-queries",
        agent=information_retriever_agent,
        depends_on=[problem_decomposer_task],
        verbose=True
    )


    #reasoning task for the sub-problems

    reasoning_task = Task(
        description=f"Reason about the sub-problems/sub-queries by logically combining and build logical connections between the facts and the information retrieved,to derive logical conclusion for the user query: {query}",
        expected_output="A list of reasoning for the sub-problems/sub-queries",
        agent=reasoning_agent,
        depends_on=[information_retriever_task],
        verbose=True
    )



    #answer composer task for the final answer
    answer_composer_task = Task(
        description=f"Compose the final answer to the problem/query in a concise and informative manner for the user query: {query}",
        expected_output="A final answer to the problem/query",
        agent=answer_composer_agent,
        depends_on=[reasoning_task],
        verbose=True
    )

    return [problem_decomposer_task, information_retriever_task, reasoning_task, answer_composer_task]