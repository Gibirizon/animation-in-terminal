import logging
import pathlib

from textual.app import App

from animation.components.screen import AnimationScreen
from animation.utils.sound import cleanup_sound, init_sound

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
        # Get the directory where the current file (models.py) is located
        current_dir = pathlib.Path(__file__).parent
        # Navigate to resources/images
        frames_path = current_dir / "resources" / "frames"
        logger.info(f"Image path: {frames_path}")
        return str(frames_path)

    def on_unmount(self) -> None:
        cleanup_sound()
        logger.info("Application closed")
