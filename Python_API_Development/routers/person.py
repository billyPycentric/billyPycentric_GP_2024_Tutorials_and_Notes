from fastapi import APIRouter , status , Response
from starlette.routing import Router
from typing import Optional
from fastapi import status , Response
from pydantic import BaseModel
from schemas import Person

router=APIRouter(
    tags=["Persons"]    
)


@router.post("/persons",status_code=status.HTTP_202_ACCEPTED)
async def add_person(person_body : Person, response : Response):
    ##response.status_code = status.HTTP_411_LENGTH_REQUIRED
    print(person_body)
    print(dict(person_body)["failed_marriages"])
    print(type(person_body))
    print(f"And No i failed Marriages is a {person_body.failed_marriages}")
    return {"new_user" : f" {person_body.name} new person has been added"}