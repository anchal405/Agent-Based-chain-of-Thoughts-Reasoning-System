from crewai import Crew
from tasks import create_tasks
from state import GraphState
from llm import get_langchain_chat_llm
from pydantic import BaseModel,Field
from langchain_core.messages import AIMessage
class EvaluationResponse(BaseModel):
    is_correct: bool = Field(description="Whether the response is correct or not")
    feedback: str = Field(description="Feedback on the response")





#run crew
def run_crew(state:GraphState):
    query = state["query"]
    tasks = create_tasks(query)
    agents = [task.agent for task in tasks]
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )
    response = crew.kickoff()
    state["message"].append({"role":"assistant","content":response.raw})
    state["response"] = response.raw

    return state

#evaluate the crew response

def evaluate_response(state:GraphState):
    response = state["response"]
    query = state["query"]
    evaluation_prompt = f"""
    you are an expert in evaluating the answer of to a user query.
    The user query is: {query}
    The crew response is: {response}

    response should be in the following format:
    {{
        "is_correct": bool,
        "feedback": str
    }}
    """
    evaluation_llm = get_langchain_chat_llm().with_structured_output(EvaluationResponse)
    evaluation_response = evaluation_llm.invoke(evaluation_prompt)
    return {"is_correct":evaluation_response.is_correct,"feedback":evaluation_response.feedback}

# retry the crew
def retry_crew(state:GraphState):
    if state["is_correct"]:
        return "finalize_response"

    elif state["retries"] < 2:
        state["retries"] += 1
        return "run_crew"
    else:
        return "finalize_response"


# finalize    

def finalize_response(state:GraphState):
    is_correct = state["is_correct"]
    feedback = state["feedback"]
    response = state["response"]
    if is_correct:
        return {"response":f" The final response is: {response}","message": state["message"]+ [{"role":"assistant","content":f" The final response is: {response}"}]}
    else:
        return {"response":f"The response is incorrect. {feedback} \n The final response is: {response}","message": state["message"]+ [{"role":"assistant","content":f"The response is incorrect. {feedback} \n The final response is: {response}"}]}