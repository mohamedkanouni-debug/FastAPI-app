from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class StoryJobBase(BaseModel):
    theme : str
    

class StoryJobResponse(BaseModel):
    job_id : str
    status : str
    created_at : datetime
    story_id : Optional[int] = None
    completed_at : Optional[datetime] = None
    error : Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class StoryJobCreate(StoryJobBase):
    pass
