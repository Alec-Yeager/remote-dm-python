import socket
import logging

logger = logging.getLogger(__name__)


class TestClient:

    HOST = "127.0.0.1"
    PORT = 42542

    def __init__(self) -> None:
        pass

    def launch(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((self.HOST, self.PORT))
            s.sendall(b"Hello from the client.")
            data = s.recv(1024)
            logger.info(f"Client Recieved: {data!r}")
            s.sendall(b"I don't think I will.")
            while True:
                s.sendall(b"teehee")

                logger.info(f"Client Recieved: {data!r}")
