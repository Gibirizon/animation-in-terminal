[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)
[![pl](https://img.shields.io/badge/lang-pl-white.svg)](./README-PL.md)

# Terminal Animation Player

## Table of Contents

- [Project Description](#project-description)
- [Project Preview](#project-preview)
- [Installation](#installation)
  - [Windows](#windows)
  - [Linux](#linux)
- [User Guide](#user-guide)
- [Main Features](#main-features)
- [Troubleshooting](#troubleshooting)

## Project Description

Terminal Animation Player is a console application created in Python that enables displaying animations directly in the terminal. The program uses the Textual library to create an interactive console user interface, along with sound support through the Pygame library. Animations are displayed as sequences of PNG images (64x64 pixels) with a central "ANIMATION" title created using ASCII art.

## Project Preview

![video](./docs/screenshots/video.gif)

### Kitty terminal

![kitty_terminal](./docs/screenshots/kitty_terminal.png)

### Windows terminal

![windows_terminal](./docs/screenshots/windows_terminal.png)

## Installation

### System Requirements

- Python 3.8 or newer
- Pip (Python package manager)

### Windows

1. Install Python:

   - Download and install Python 3.8 or newer from [python.org](https://python.org)
   - During installation, check "Add Python to environment variables"

2. Open Command Prompt (cmd) as administrator

3. Clone the repository and navigate to the project directory:

```cmd
git clone <repository-url>
cd animation-in-terminal
```

4. Create and activate virtual environment:

```cmd
python -m venv venv
venv\Scripts\activate
```

5. Install the application:

   Option 1 - Install required packages:

```cmd
pip install -r requirements.txt
```

Option 2 - Install as an editable package:

```cmd
pip install -e .
```

### Linux

1. Install Python (if not installed):

- _Debian based distributions_ (use appropriate package manager and packages for other distributions)

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv git
```

2. Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd animation-in-terminal
```

3. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the application:

   Option 1 - Install required packages:

```bash
pip install -r requirements.txt
```

Option 2 - Install as an editable package:

```bash
pip install -e .
```

## User Guide

### Running the Application

After installation, you can run the animation player in one of the following ways:

1. If you installed using requirements.txt:

```bash
python main.py
# or
python -m src.animation.app
```

2. If you installed as a package (pip install -e .):

```bash
animate
```

### Controls:

- `space` - Pause/Resume animation
- `ctrl+q` - Exit program

## Main Features

- Terminal animation display:
  - Support for 64x64 PNG images
  - Smooth playback at 10 FPS
- Sound support:
  - Sound effects on frame change
  - Automatic audio system management
- Logging system:
  - Log saving to animation.log file
  - Application state monitoring
  - Error and event logging

## Troubleshooting

1. Sound issues:
   - Check if step.wav file is in the correct directory (assets/sounds)
   - Verify that system audio is working correctly
2. Display issues:
   - Check if terminal supports 256 color mode
   - Ensure terminal size is sufficient
3. Startup errors:
   - Verify all dependencies are installed
   - Check file paths are correct
