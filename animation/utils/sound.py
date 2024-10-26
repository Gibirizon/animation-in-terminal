import logging
import os
import pathlib

import pygame

logger = logging.getLogger(__name__)


def init_sound() -> None:
    """Initialize pygame mixer for sound playback."""
    try:
        pygame.mixer.init()
        logger.info("Sound system initialized")
    except Exception as e:
        logger.error(f"Failed to initialize sound system: {e}")


def cleanup_sound() -> None:
    """Clean up pygame mixer."""
    try:
        pygame.mixer.quit()
        logger.info("Sound system cleaned up")
    except Exception as e:
        logger.error(f"Error during sound cleanup: {e}")


def play_sound() -> None:
    """Play a sound effect for frame changes."""
    try:
        current_dir = pathlib.Path(__file__).parent
        sound_file = current_dir.parent / "resources" / "sounds" / "step.wav"

        if os.path.exists(sound_file):
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
    except Exception as e:
        logger.error(f"Error playing sound: {e}")
