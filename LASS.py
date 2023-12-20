import random
import string

import requests
import aiohttp
from aiohttp import FormData

api_url = "https://vladhog.ru/lass/api"


def check_nsfw(file):
    return requests.get(f"{api_url}/detection/nsfw", files={'file': file}).json()
    # {'drawings': 1.5, 'hentai': 87.8, 'neutral': 1.5, 'porn': 7.7, 'sexy': 1.5} all numbers are p


async def check_nsfw_async(file):
    data = FormData()
    data.add_field('file', file)
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{api_url}/detection/nsfw", data=data) as a:
            return await a.json()
