import asyncio
from aiogram import Bot, Dispatcher, types, executor


async def send_sec1() -> None:
    n = 0
    while(True):
        await asyncio.sleep(1)
        n +=1
        print(n)


async def send_sec3() -> None:
    n = 0
    while(True):
        await asyncio.sleep(3)
        n +=3
        print(n)





async def ttt() -> None:
    x1 = asyncio.create_task(send_sec1())
    x2 = asyncio.create_task(send_sec3())

    await x1
    await x2

ttt()





if __name__ == "__main__":
    asyncio.run(ttt())