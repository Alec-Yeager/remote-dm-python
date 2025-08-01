import logging
from testclient import TestClient

logger = logging.getLogger(__name__)


def main():
    client = TestClient()
    client.launch()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
