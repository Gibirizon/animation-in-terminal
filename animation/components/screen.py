import logging
from typing import cast

from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Footer, Header

from animation.components.frame import Frame
from animation.components.title import TitleWidget

logger = logging.getLogger(__name__)


class AnimationScreen(Screen):
    """Main screen containing the animation and title."""

    CSS_PATH = "screen.tcss"
    BINDINGS = [
        ("space", "toggle_play_pause", "Play/Pause"),
        ("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self, frames_dir: str):
        super().__init__()
        self.frames_dir = frames_dir

    def compose(self) -> ComposeResult:
        yield Header()
        yield TitleWidget()
        yield Container(Frame(self.frames_dir), id="frame-container")
        yield Footer()

    def action_toggle_play_pause(self) -> None:
        logger.info("Toggling play/pause")
        animation = cast(Frame, self.query_one("Frame"))
        animation.toggle_play_pause()

    def action_quit(self) -> None:
        self.app.exit()
