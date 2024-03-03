import random
import string

import requests
import aiohttp
from aiohttp import FormData

api_url = "https://lass.vladhog.ru/api"


def check_nsfw(file: BinaryIO) -> dict:
    return requests.get(f"{api_url}/detection/nsfw", files={'file': file}).json()
    # {'drawings': 1.5, 'hentai': 87.8, 'neutral': 1.5, 'porn': 7.7, 'sexy': 1.5} all numbers are percentages


async def check_nsfw_async(file: BinaryIO) -> dict:
    data = FormData()
    data.add_field('file', file)
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{api_url}/detection/nsfw", data=data) as a:
            return await a.json()
            # {'response': safe, malware or blocked (blocked means site have anti bot protection or like that)}

def check_url_content(url: str) -> dict:
    return requests.get(f"{api_url}/detection/linkcheck/content", headers={"url": url}).json()
    # {'response': safe, malware or blocked (blocked means site have anti bot protection or like that)}


async def check_url_content_async(url: str) -> dict:
    async with aiohttp.ClientSession(headers={"url": url}) as session:
        async with session.get(f"{api_url}/detection/linkcheck/content") as a:
            return await a.json()
            # {'response': safe, malware or blocked (blocked means site have anti bot protection or like that)}
