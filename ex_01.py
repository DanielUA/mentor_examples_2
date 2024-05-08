import asyncio


async def rand_numb(num):
    for i in range(num):
        await asyncio.sleep(1)
        print(num - i)


if __name__ == "__main__":
    asyncio.run(rand_numb(10))