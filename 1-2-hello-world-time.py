import asyncio
import time

async def example(message):
    print(f"{time.ctime()} - start of :", message)
    await asyncio.sleep(1)
    print(f"{time.ctime()} - end of :", message)

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = example("First call")
    second_awaitable = example("Second all")
    
    # Wait for corountines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())

#Mon Nov  6 21:55:35 2023 - start of : First call
#Mon Nov  6 21:55:36 2023 - end of : First call
#Mon Nov  6 21:55:36 2023 - start of : Second all
#Mon Nov  6 21:55:37 2023 - end of : Second all