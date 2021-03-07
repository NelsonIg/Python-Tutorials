import asyncio
import json
import time

import aiohttp


async def worker(name, n, session):
    print(f'worker-{name}')
    url = f"http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count={n}"
    response = await session.request(method='GET', url=url)
    value = await response.json()
    return value


async def main():
    async with aiohttp.ClientSession() as session:
        response = await worker('bob', 3, session)
        sums = await asyncio.gather(*( worker(f'{i}', n, session) for i, n in enumerate(range(1, 5))))
        print('sums:', sums)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'executed in {elapsed:.2f} seconds')