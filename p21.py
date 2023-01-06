import asyncio
from aiogram import Bot, Dispatcher, types, executor


async def send_sec1() -> None:
    n = 0
    while(True):
        await asyncio.sleep(1)
        n +=1
        if n%3 != 0:
            print(f"Прошло {n} секунд")


async def send_sec3() -> None:
    n = 0
    while(True):
        await asyncio.sleep(3)
        n +=3
        print(f"Прошло {n} seconds")





async def ttt() -> None:
    x2 = asyncio.create_task(send_sec3())
    x1 = asyncio.create_task(send_sec1())

    await x2
    await x1


ttt()





if __name__ == "__main__":
    asyncio.run(ttt())