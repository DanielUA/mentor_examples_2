import asyncio

async def test():
    print("hello")


# def main():
#     async_func_list = [test(), test(), test()]
#     for el in async_func_list:
#         asyncio.run(el)
async def main():
    async_func_list = [test(), test(), test()]
    asyncio.gather(*async_func_list)

if __name__ == "__main__":
    asyncio.run(main())