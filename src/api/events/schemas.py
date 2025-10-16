from typing import List,Optional
from pydantic import BaseModel,Field

class EventSchema(BaseModel):
    id:int
    page:Optional[str]=""#This is to set the optional data default value to show
    description:Optional[str]=Field(default="Nigga")

class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int

class createEventSchmea(BaseModel):
    page:str

class UpdateEventSchema(BaseModel):
    description:str

