import asyncio
import aiofile

async def read_file(file):
    async with aiofile.AIOFile(file, "r") as afp:
        data = await afp.read()
    return data

async def write_multi_files(data, file_paths):
    tasks = []
    for file_path in file_paths:
        tasks.append(write_to_file(data, file_path))
    await asyncio.gather(*tasks)

async def write_to_file(data, file_path):
    async with aiofile.AIOFile(file_path, "w") as afp:
        await afp.write(data) 

async def main():
    data_1 = await read_file("text.txt")
    output_files = ["res_1.txt", "res_2.txt", "res_3.txt"]
    await write_multi_files(data_1, output_files)

if __name__ == "__main__":
    asyncio.run(main())