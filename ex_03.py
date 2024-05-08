import asyncio
import aiofile

# async def read_file_async(file):
#     async with aiofile.AIOFile(file, "r") as afp:
#         lines = await afp.read()
#         last_line = lines.splitlines()[-1]
#         return last_line
    

# async def record_to_file_async(file, res):
#     async with aiofile.AIOFile(file, "w") as afp:
#         await afp.write(res)

# if __name__ == "__main__":
#     res = asyncio.run(read_file_async("text.txt"))
#     asyncio.run(record_to_file_async("text_output.txt", res))

async def read_record_file(file):
    lines = []
    async with aiofile.async_open(file, "r") as afp:
        async for line in afp:
            lines.append(line.strip())
    
    async with aiofile.async_open("output_text_2.txt", "w") as afp:
        await afp.write("\n".join(lines))    

async def main():
    file = "text.txt"
    await read_record_file(file)

if __name__ == "__main__":
    asyncio.run(main())