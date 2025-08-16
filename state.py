from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages    
from langchain_core.messages import BaseMessage







class GraphState(TypedDict):
    message: Annotated[list[BaseMessage],add_messages]
    query: str
    response: str
    is_correct: bool
    feedback: str
    retries: int


 