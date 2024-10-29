import logging
from pathlib import Path
from typing import List

from rich.console import RenderableType
from rich_pixels import Pixels
from textual.reactive import reactive
from textual.timer import Timer
from textual.widgets import Static

from animation.utils.sound import play_sound

logger = logging.getLogger(__name__)


class Frame(Static):
    """Widget that displays and manages the animation frames."""

    current_frame = reactive(0)

    def __init__(self, frames_dir: str) -> None:
        super().__init__()
        self.frames_dir = frames_dir
        self.frames: List[RenderableType] = []
        self.is_playing = True
        self.timer: Timer | None = None
        self.load_frames()

    def load_frames(self) -> None:
        try:
            frame_files = sorted(Path(self.frames_dir).glob("*.png"))
            self.frames = [Pixels.from_image_path(frame) for frame in frame_files]
            logger.info(f"Loaded {len(self.frames)} frames from {self.frames_dir}")
        except Exception as e:
            logger.error(f"Error loading frames: {e}")
            self.frames = []

    def on_mount(self) -> None:
        if self.frames:
            self.timer = self.set_interval(1 / 10, self.next_frame)
            logger.info("Animation started")

    def render(self) -> RenderableType:
        return self.frames[self.current_frame]

    def next_frame(self) -> None:
        if not self.frames or not self.is_playing:
            return

        # Changing reactive attribute triggers re-render
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        play_sound()

    def toggle_play_pause(self) -> None:
        self.is_playing = not self.is_playing
        status = "resumed" if self.is_playing else "paused"
        logger.info(f"Animation {status}")
