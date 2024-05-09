import asyncio
import aiohttp
import aiofile
import cairosvg
from PIL import Image    

def get_file_extension(content_type):
    match content_type:
        case 'image/svg+xml':
            return 'svg'
        case _:
            return 'png'

async def get_image_url(width, height, *options):
    options = ''.join(options) # [1, 2, 3] -> '123'
    url = f'https://placekeanu.com/{width}/{height}/{options}'
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            extension = get_file_extension(response.content_type)
            file_name = f'test.{extension}'
            async with aiofile.async_open(file_name, 'wb') as file:
                result = await response.read()
                await file.write(result)
            return file_name

if __name__ == '__main__':
    width = input('Width: ')
    height = input('Height: ')
    filename = asyncio.run(get_image_url(width, height, 'y', 'g'))
    cairosvg.svg2png(url="test.svg", write_to="test.png")
    img = Image.open("test.png")
    img.show()