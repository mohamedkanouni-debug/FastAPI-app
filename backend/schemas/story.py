from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class StoryOptionsSchema(BaseModel):
    text : str
    node_id : Optional[int] = None


class StoryNodeBase(BaseModel):
    content : str
    is_ending : bool = False
    is_winning : bool = False


class CompleteStoryNodeResponse(StoryNodeBase):
    id : int
    options : List[StoryOptionsSchema]
    model_config = ConfigDict(from_attributes=True)


class StoryBase(BaseModel):
    title : str
    session_id : Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class CreateStoryRequest(StoryBase):
    theme : str


class CompleteStoryResponse(StoryBase):
    id : int
    created_at : datetime
    root_node : CompleteStoryNodeResponse
    all_nodes : Dict[ int , CompleteStoryNodeResponse] 
    model_config = ConfigDict(from_attributes=True)
