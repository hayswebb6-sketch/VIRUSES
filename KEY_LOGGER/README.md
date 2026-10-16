# KEY_LOGGER

Purpose
This folder contains a key-logging proof-of-concept intended strictly for controlled, local research in a disposable VM.

Files of interest
- KEY_LOGGER.py — client: listens for keyboard events and accumulates typed characters. The client attempts to connect to a websocket endpoint (currently: wss://key-logger-transmitter.onrender.com) and send captured data.
- server.py — example websocket relay: accepts client connections, appends incoming messages to messages.txt, and can broadcast messages to other connected clients.
- build/, dist/ — packaging/build artifacts (dist/ may contain compiled output if built).
- KEY_LOGGER.spec — packaging spec kept for reference.

What it does (high level, non-actionable)
- Captures keyboard events and builds a text buffer of typed input (letters, spaces, enters, backspace handling).
- The client (KEY_LOGGER.py) periodically sends the captured buffer over a websocket to a remote host.
- The included server (server.py) listens for websocket connections, writes incoming messages to messages.txt, and forwards messages to other connected clients.

Security, privacy & safety risks
- Captures sensitive input (passwords, personal data) and transmits it — extreme privacy risk.
- The server stores captured messages to disk in plain text (messages.txt), exposing sensitive data if the server filesystem is accessible.
- Running the code on shared, networked, or production machines may violate privacy rules, ethics, or laws.
- Network transmission to external hosts increases risk even in a VM — prefer an offline, isolated environment for testing.

It currently does not work (server.py is not reciving inputs) but if anyone wants to fix or point out why it might not be happening and suggest a fix, you can do that(In a matter of fact, you should)
