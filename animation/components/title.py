from textual.widgets import Static
from pyfiglet import figlet_format


class TitleWidget(Static):
    """Widget for displaying the title using figlet."""

    def on_mount(self) -> None:
        title = figlet_format("ANIMATION", font="big")
        self.update(title)
