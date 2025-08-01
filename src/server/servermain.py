import logging
from testserver import TestServer

logger = logging.getLogger(__name__)


def main():
    server = TestServer()
    server.launch()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
