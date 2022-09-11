from aiohttp import ClientSession
import asyncio

api_key = "537e8ef776632fed2b8283a26724d428"


async def hcaptcha_solver() -> None:
    async with ClientSession() as session:
        async with session.post(f"http://rucaptcha.com/in.php?key{api_key}&method=hcaptcha")