import asyncio


async def lol() -> None :
    await asyncio.sleep(2.000000001)
    print("lol")



async def super1() -> None:
    await asyncio.sleep(2.00000000000001)
    print("super")

# asyncio.run(super1())
# asyncio.run(lol())

async def mega():
    x1 = asyncio.create_task(lol())
    x2 = asyncio.create_task(super1())

    await x1
    await x2

asyncio.run(mega())