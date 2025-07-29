import pytest

from tasks import echo_all


@pytest.mark.asyncio
async def test_echo_all():
    result = await echo_all()
    assert result == ["hello", "world", "!"]
