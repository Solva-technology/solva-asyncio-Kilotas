import asyncio


async def delayed_echo(text, delay):
    await asyncio.sleep(delay)
    return text


async def echo_all():
    tasks = [delayed_echo("hello", 1), delayed_echo("world", 2), delayed_echo("!", 0.5)]
    return await asyncio.gather(*tasks)
