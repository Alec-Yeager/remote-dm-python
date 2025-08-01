import socket
import logging

logger = logging.getLogger(__name__)


# Class just to test basic connectivity.
class TestServer:

    HOST = "127.0.0.1"
    PORT = 42542

    def __init__(self):
        pass

    def launch(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            while True:
                try:
                    conn, addr = s.accept()
                    print(f"{addr} connected to server.")
                    with conn:
                        try:
                            self.handleClient(conn)
                        except Exception as e:
                            logger.warning(f"Failed to handle client: {e}")
                            s.close()
                            self.launch()
                except KeyboardInterrupt:
                    logger.info("Shutting down server.")
                    break
                except Exception as e:
                    logger.error(f"Unexpected error {e} crashed the server.")
                    break

    def handleClient(self, conn: socket.socket):
        while True:
            data = conn.recv(1024)
            logger.info(f"Server Recieved: {data!r}")
            conn.sendall(b"Begone")
