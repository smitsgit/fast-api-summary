from typing import Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary.id


async def get_all():
    return await TextSummary.all().values()


async def get_one(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    else:
        return None
