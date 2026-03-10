from datetime import datetime

from clickhouse_connect.driver import AsyncClient
from fastapi import APIRouter, Depends

from app.clickhouse.database import get_clickhouse_client
from app.clickhouse.schema import Event

clickhouse_router = APIRouter(prefix="/clickhouse")

@clickhouse_router.post("/events")
async def track_event(event: Event, ch_client: AsyncClient = Depends(get_clickhouse_client)):
    await ch_client.query(
        "INSERT INTO events (event_time, user_id, event_type) VALUES",
        [(event.event_time or datetime.now(), event.user_id, event.event_type.value)]
    )


@clickhouse_router.get("/events/count")
async def get_events_count(ch_client: AsyncClient = Depends(get_clickhouse_client)):
    result = await ch_client.query("SELECT COUNT() FROM events")
    count = result.result_rows[0][0]
    return {"total_events": count}
