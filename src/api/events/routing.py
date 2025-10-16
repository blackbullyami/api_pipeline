from fastapi import APIRouter
from .schemas import ( 
 EventSchema,
 EventListSchema,
 createEventSchmea,
 UpdateEventSchema
 ) # here . is used for the import to specify the import is happening from the same folder 
router= APIRouter()
# get /
#This routing file is desidgend to define different routes to our api
@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results":[{"id":1},{"id":2},{"id":3}],
        "count":3,
        "description":"My Hollow purple"
        
    }
# To send the data we use POST method or we can say  creating the data
#Create_viewz
@router.post("/")
def create_events(payload:createEventSchmea) -> EventSchema:
    data=payload.model_dump() # what happening here is payload -> dict -> pydantic
    return {"id":123,**data}


# get/api/events/int
@router.get("/{event_id}")
def get_events(event_id:int) -> EventSchema:
    return {
        "id":event_id

    }


@router.put("/{event_id}")
def Update_events(event_id:int ,payload:UpdateEventSchema) -> EventSchema:
    data=payload.model_dump()
    return {
        "id":event_id,**data,

    }





