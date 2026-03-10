import asyncio

# async def my_coroutine():
#     await asyncio.sleep(1)
#     return "done"

# def main():
#     cor = asyncio.run(my_coroutine())
#     print(cor) 

async def task_one():
    await asyncio.sleep(2)
    print("Task One Complete")

async def task_two():
    await asyncio.sleep(1)
    print("Task Two Complete")

async def main():
    t1 = asyncio.create_task(task_one())
    t2 = asyncio.create_task(task_two())

    print("Both tasks started...")
    await t1
    await t2
    print("All tasks done!")

if __name__ == "__main__":
    asyncio.run(main())
