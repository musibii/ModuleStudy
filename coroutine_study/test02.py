# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test02.py
# __time__  : 2020/6/19 11:36 上午
import asyncio


class aoiFiles:
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._obj.close()
        self._obj = None

    def __await__(self):
        self.f = iter(self.f)
        yield self.f.readline()

    def open(self, file_name):
        self.f = open(file_name, "r")

    async def __anext__(self):
        self.f = iter(self.f)
        resp = await self.f.readline()
        return resp

    async def __aenter__(self):
        self._obj = await self._coro
        return self._obj

    # async def __aexit__(self, exc_type, exc, tb):
    #     self._obj.close()
    #     self._obj = None

    # def __aexit__(self):
    #     yield


async def new_read_file(file_name):
    async with aoiFiles().open(file_name) as f:
        cont = await f.readline()
        print(cont)


if __name__ == "__main__":
    print(dir(aoiFiles))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(new_read_file("__init__.py"))
