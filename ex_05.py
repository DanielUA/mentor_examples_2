import asyncio
import aiofile


async def read_file(file):
    res = ""
    async with aiofile.async_open(file, "r") as afp:
        async for lines in afp:
            for line in lines:
                if line.isnumeric():
                    res += line
    print(res)

asyncio.run(read_file("text.txt"))