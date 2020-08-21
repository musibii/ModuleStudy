# -*- coding: utf-8 -*-
# __file__  : __init__.py.py
# __time__  : 2020/7/13 2:11 PM

import asyncio


async def nested():
    return 42


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task
    return task


# print(asyncio.run(main(), debug=True).result())
loop = asyncio.get_event_loop()
print(loop.run_until_complete(main()))
