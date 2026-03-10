from clickhouse_connect import get_async_client
from clickhouse_connect.driver import AsyncClient

from app.settings import settings


async def get_clickhouse_client() -> AsyncClient:
    """
    Функция-зависимость для получения асинхронного клиента ClickHouse.
    """
    client = await get_async_client(
        host=settings.CLICKHOUSE_HOST,
        port=settings.CLICKHOUSE_PORT,
        username=settings.CLICKHOUSE_USER,
        password=settings.CLICKHOUSE_PASSWORD,
        database=settings.CLICKHOUSE_DB,
    )
    return client