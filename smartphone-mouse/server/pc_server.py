import socket
import pyautogui

HOST = '0.0.0.0'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                x, y = map(float, data.decode().split(','))
                # Swap x and y to use width as vertical
                pyautogui.moveTo(y, x)

if __name__ == "__main__":
    main()
