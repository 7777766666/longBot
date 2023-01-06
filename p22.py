import asyncio



async def send_time (sec: int) -> None:
    while True:
        await asyncio.sleep(sec)

        print(f"Прошло {sec} second")

# print(send_time(2), send_time(5), sep="\n")
async def mem1() -> None:

    x1 = asyncio.create_task(send_time(2))  #различные объекты корутины
    x2 = asyncio.create_task(send_time(5))  #различные объекты корутины

    await x1
    await x2

mem1()


if __name__ == "__main__":
    asyncio.run(mem1())
