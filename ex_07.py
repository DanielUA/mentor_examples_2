import asyncio
import aiofile
import re

async def read_file(file):
    tel_numbers = []
    phone_number_pattern = r'\b\d{3}-\d{3}-\d{3}-\d\b'
    
    async with aiofile.async_open(file, "r") as afp:
        async for lines in afp:
            res = re.findall(phone_number_pattern, lines)
            if res:
                tel_numbers.extend(res)           
    print(tel_numbers)

asyncio.run(read_file("text.txt"))