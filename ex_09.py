import asyncio
import aiohttp
import pprint
import json

URL = "https://openlibrary.org/search/authors.json?q="

async def get_author_key(name):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}+{name}") as response:
            res = json.loads(await response.text())
            return res['docs'][0]['key']
            # pprint.pprint(await response.text)

async def info_about_autor(name):
    key = await get_author_key(name)
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://openlibrary.org/authors/{key}.json") as response:
            res = json.loads(await response.text())
            for key, value in res.items():
                print(f"{key} >>> {value}")


if __name__ == "__main__":
    name = str(input("enter author name: "))
    asyncio.run(info_about_autor(name))

