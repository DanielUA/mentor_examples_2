import asyncio
import aiofile

async def read_file_async(file):
    async with aiofile.AIOFile(file, "r") as afp:
        lines = await afp.read()
        last_line = lines.splitlines()[-1]
        return last_line
    

async def record_to_file_async(file, res):
    async with aiofile.AIOFile(file, "w") as afp:
        await afp.write(res)

if __name__ == "__main__":
    res = asyncio.run(read_file_async("text.txt"))
    asyncio.run(record_to_file_async("text_output.txt", res))

