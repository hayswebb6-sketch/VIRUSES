import asyncio
import websockets
import os

clients=set()
async def handler(websocket):
    clients.add(websocket)
    ip = websocket.remote_address[0] if websocket.remote_address else "unknown"
    try:
        async for text in websocket:
            with open("messages.txt", "a", encoding="utf-8") as f:
                f.write(f"Ip: {ip} | Text:{text}\n")
            for client in clients.copy():
                if client!=websocket:
                    await client.send(text)
    finally:
        clients.discard(websocket)
async def main():
    async with websockets.serve(handler, "0.0.0.0", int(os.environ.get("PORT", 10000))):
        await asyncio.Future()
if __name__=="__main__":
    asyncio.run(main())