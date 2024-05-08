import asyncio

# Класс асинхронного итератора
class AsyncIterable:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
    
    # __aiter__ должен возвращать сам объект
    def __aiter__(self):
        return self
    
    # Асинхронный метод __anext__ для получения следующего элемента
    async def __anext__(self):
        if self.index >= len(self.iterable):
            raise StopAsyncIteration  # Окончание итерации
        element = self.iterable[self.index]
        self.index += 1
        await asyncio.sleep(0.1)  # Имитация асинхронной задержки
        return element

# Асинхронная главная функция
async def main():
    async_iterable = AsyncIterable([1, 2, 3, 4])  # Создание асинхронного итератора
    async for el in async_iterable:
        print(el)

# Запуск асинхронного кода
if __name__ == "__main__":
    asyncio.run(main())
