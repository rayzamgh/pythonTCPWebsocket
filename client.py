import asyncio
import websockets
import time
import hashlib


async def hello():
    uri = "ws://f3439234.ngrok.io"
    uri = "ws://localhost:65427"
    
    print("pepegeg")

    async with websockets.connect(uri) as websocket:
        print("testSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAMBURUSSU")
        name = input("What's your name? ")

        print(f"> {name}")
        greeting = "Hello" + name

        await websocket.send(greeting)
        time.sleep(5)
        print(f"< {greeting}")

        # await websocket.send("!submission")
        # # print(f"> {name}")

        # greeting = await websocket.recv()
        # fileA = open("teste.zip",'wb')
        # fileA.write(greeting)
        # fileA.close()
        # time.sleep(5)
        
        # pong_waiter = await websocket.ping()
        # time.sleep(5)
        # print(f"< {pong_waiter}")
        
        # # print(f"> {name}")

        # greeting = await websocket.recv()
        # time.sleep(5)
        # print(f"< {greeting}")
        
asyncio.get_event_loop().run_until_complete(hello())
