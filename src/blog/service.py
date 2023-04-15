from uuid import uuid4

import aiofiles
from fastapi import UploadFile, HTTPException


async def save_photo(
        title: str,
        file: UploadFile,
):
    file_name = f'../media/poster_book/{uuid4()}.jpg'
    if file.content_type.split('/')[0] == 'image':
        await write_image(file_name, file)
    else:
        raise HTTPException(status_code=418, detail="it's isn't image")
    return file_name


async def write_image(file_name, file):
    async with aiofiles.open(file_name, 'wb') as file_image:
        data = await file.read()
        await file_image.write(data)
