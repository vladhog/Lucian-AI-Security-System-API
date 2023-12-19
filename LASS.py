import random
import string

import requests
import aiohttp
from aiohttp import FormData

api_url = "https://vladhog.ru/lass/api"


def check_nsfw(file):
    characters = string.ascii_letters
    id = "".join([random.choice(characters) for i in range(8)])
    requests.post(f"{api_url}/detection/nsfw", files={'file': file}, headers={"id": id})
    return requests.get(f"{api_url}/detection/nsfw", headers={"id": id}).json()
    # {'drawings': int, 'hentai': int, 'neutral': int, 'porn': int, 'sexy': int} all numbers are percentages

async def check_nsfw_async(file):
    data = FormData()
    data.add_field('file', file)
    characters = string.ascii_letters
    id = "".join([random.choice(characters) for i in range(8)])
    async with aiohttp.ClientSession(headers={"id": id}) as session:
        await session.post(f"{api_url}/detection/nsfw", data=data)
        async with session.get(f"{api_url}/detection/nsfw") as a:
            return await a.json()
            # {'drawings': int, 'hentai': int, 'neutral': int, 'porn': int, 'sexy': int} all numbers are percentages
