import asyncio
import aiofile

async def read_file_async(file):
    async with aiofile.AIOFile(file, "r") as afp:
        lines = await afp.read()
    for line in lines.splitlines():
        print(line)

if __name__ == "__main__":
    asyncio.run(read_file_async("text.txt"))