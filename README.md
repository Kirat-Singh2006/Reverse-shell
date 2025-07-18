# Reverse-shell
 Basic Reverse Shell (Client-Server)

Wrench is a simple client-server reverse shell written in Python. The server sends commands to a connected client, which executes them and returns the output. It also supports simple messaging with a "say" prefix.

⚠️ FOR EDUCATIONAL AND AUTHORIZED USE ONLY
Do not use this on any system you do not own or have explicit permission to access.
🧰 Project Structure

    client.py – The reverse shell client that connects to the server.

    server.py – The control server that sends commands and receives responses.

⚙️ Features

✅ Remote command execution
✅ One-line messaging (say <message>)
✅ Basic console-based interface
✅ ASCII art startup banner
✅ Graceful disconnect with exit command
🔧 Requirements

    Python 3.x

    No external libraries needed (uses socket and subprocess)
