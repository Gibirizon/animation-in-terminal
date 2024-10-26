import logging

from textual.logging import TextualHandler

from animation.app import AnimationApp

LOG_FILE = "animation.log"
logger = logging.getLogger(__name__)


def configure_logger():
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_date_format = "%Y-%m-%d %H:%M:%S"
    log_th = TextualHandler()
    log_fh = logging.FileHandler(LOG_FILE)
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=log_date_format,
        handlers=[log_th, log_fh],
    )


def main():
    configure_logger()
    app = AnimationApp()
    app.run()


if __name__ == "__main__":
    main()
