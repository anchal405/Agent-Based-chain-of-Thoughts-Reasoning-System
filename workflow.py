from langgraph.graph import StateGraph,START,END
from nodes import run_crew,evaluate_response,finalize_response,retry_crew
from state import GraphState
import sys

graph = StateGraph(GraphState)

graph.add_node("run_crew",run_crew)
graph.add_node("evaluate_response",evaluate_response)
graph.add_node("finalize_response",finalize_response)

graph.add_edge(START, "run_crew")
graph.add_edge("run_crew","evaluate_response")
graph.add_conditional_edges("evaluate_response",retry_crew,{"finalize_response":"finalize_response","run_crew":"run_crew"})
graph.add_edge("finalize_response",END)

app = graph.compile()



def stream_graph_updates(user_input: str):
    initial_state = GraphState(query=user_input,message=[{"role": "user", "content": user_input}],response="",is_correct=False,feedback="",retries=0)
    for event in app.stream(initial_state):
        for value in event.values():
            if "response" in value:
                print("Assistant:", value["response"])
            else:
                print("debug:",value)


while True:
    try:
        user_input = input("User: ")
        if not user_input:
            print("Error: no input")
            continue
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        print("Error:",sys.exc_info())






