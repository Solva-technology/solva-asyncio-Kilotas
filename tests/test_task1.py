import pytest

from tasks import fetch_all


@pytest.mark.asyncio
async def test_fetch_all_statuses():
    urls = ["https://httpbin.org/status/200", "https://httpbin.org/status/404"]
    statuses = await fetch_all(urls)
    assert statuses == [200, 404]
