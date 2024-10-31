import logging
from pathlib import Path

from textual.app import App
from textual.logging import TextualHandler

from animation.components.screen import AnimationScreen
from animation.utils.sound import cleanup_sound, init_sound

LOG_FILE = "animation.log"
logger = logging.getLogger(__name__)


class AnimationApp(App):
    """Main application class."""

    def __init__(self):
        super().__init__()

    def on_mount(self) -> None:
        init_sound()
        logger.info("Application started")
        self.push_screen(AnimationScreen(self.get_frames_path()))

    def get_frames_path(self) -> str:
        # Get the project root directory (where pyproject.toml is)
        project_root = Path(__file__).parent
        # Navigate to resources/images
        frames_path = project_root / "assets" / "frames"
        logger.info(f"Image path: {frames_path}")
        return str(frames_path)

    def on_unmount(self) -> None:
        cleanup_sound()
        logger.info("Application closed")


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
