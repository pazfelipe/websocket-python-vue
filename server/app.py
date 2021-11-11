import asyncio
import websockets
import json

connected = set()


async def server(websocket, path):
    if not websocket in connected:
        connected.add(websocket)
    try:
        async for message in websocket:
            print(message)
            msg = json.loads(message)
            for con in connected:
                await con.send(f"{json.dumps(msg)}")

    finally:
        connected.remove(websocket)


async def main():
    async with websockets.serve(server, "localhost", 5000):
        await asyncio.Future()  # run forever


asyncio.run(main())
