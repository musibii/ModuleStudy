# -*- coding: utf-8 -*-
# __file__  : study_01.py
# __time__  : 2020/8/10 9:54 AM

import asyncio
import janus

loop = asyncio.get_event_loop()


def threaded(sync_q):
    for i in range(100):
        sync_q.put(i)
    sync_q.join()


async def async_coro(async_q):
    for i in range(100):
        val = await async_q.get()
        assert val == i
        async_q.task_done()


async def main():
    queue = janus.Queue()
    fut = loop.run_in_executor(None, threaded, queue.sync_q)
    await async_coro(queue.async_q)
    await fut
    queue.close()
    await queue.wait_closed()


try:
    loop.run_until_complete(main())
finally:
    loop.close()
