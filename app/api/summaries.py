from typing import List

from fastapi import APIRouter, HTTPException
from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.get("/", response_model=List[SummarySchema])
async def get_all_summaries():
    data = await crud.get_all()
    print(data)
    return data


@router.get("/{id}", response_model=SummarySchema)
async def get_single_summary(id: int):
    summary = await crud.get_one(id=id)
    if not summary:
        raise HTTPException(400, detail="Summary not found")
    return await crud.get_one(id)


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def add_summary(payload: SummaryPayloadSchema):
    summary_id = await crud.post(payload)
    return {'id': summary_id, 'url': payload.url}
