import logging

from clickhouse_connect.driver import AsyncClient

from app.clickhouse.database import get_clickhouse_client

logger = logging.getLogger(__name__)

async def create_tables():
    client: AsyncClient = await get_clickhouse_client()

    # await client.query("DROP TABLE IF EXISTS events")

    await client.query("""
            CREATE TABLE IF NOT EXISTS events (
                event_time DateTime,
                user_id Int,
                event_type String
            ) ENGINE = MergeTree()
            ORDER BY (event_type, event_time)
        """)

    result = await client.query("select count(*) from events")

    logger.warning(f"{result=}")

    client.database = "events"
