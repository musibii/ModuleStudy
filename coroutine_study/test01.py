# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test01.py
# __time__  : 2020/6/19 11:01 上午
import _io
import asyncio
import aiofiles


async def new_file(file_name):
    async with aiofiles.open(file_name, mode="r") as f:
        contents = await f.read()
        print(contents)


# class NewFile(_io.TextIOWrapper):
#     def __await__(self):
#         yield

# async def read_content(file_name):


# async def read_content(file_name):
#     async with open("__init__.py") as f:
#         print(type(f))
# content = await f.read()
# print(content)

print(type(open))
loop = asyncio.get_event_loop()
loop.run_until_complete(read_content("__init__.py"))
