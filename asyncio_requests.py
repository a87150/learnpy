import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, requests.get, 'http://www.baidu.com')
    future2 = loop.run_in_executor(None, requests.get, 'http://www.baidu.jp')
    print('async')
    response1 = await future1
    response2 = await future2
    print(response1.text)
    print(response2.text)

loop = asyncio.get_event_loop()
tasks = [main(), main()]
loop.run_until_complete(asyncio.wait(tasks))