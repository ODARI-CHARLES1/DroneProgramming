# PySimVerse Drone Controller

A drone programming project built on **PySimVerse**, providing templates and utilities for controlling simulated drones. Includes keyboard-based RC control, video streaming, movement scripts, and mission examples.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installing PySimVerse](#installing-pysimverse)
- [Project Setup](#project-setup)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Basic Movement](#basic-movement)
  - [Keyboard Control with Video Stream](#keyboard-control-with-video-stream)
  - [Custom Mission](#custom-mission)
- [Controls Reference](#controls-reference)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---


## Prerequisites

- Python 3.8 or higher
- Windows / macOS / Linux
- pip package manager

---

## Installing PySimVerse

PySimVerse is the core simulation Environment used by this project.

  [Pysimverse](https://pysimverse.com/)

### Option 1: Install requiremnts

```bash
pip install -r requirements.txt
```

### Option 2: Install from Source

1. Clone or download the repository:
   - GitHub: https://github.com/pysimverse/pysimverse
2. Navigate to the project directory and install:

```bash
git clone https://github.com/pysimverse/pysimverse
cd pysimverse
pip install -e .
```

### Option 3: Download a Release Wheel

1. Visit the [Releases page](https://github.com/pysimverse/pysimverse/releases)
2. Download the `.whl` file matching your Python version and platform
3. Install it:

```bash
pip install pysimverse-<version>-<platform>.whl
```

### Verify Installation

```bash
python -c "import pysimverse; print(pysimverse.__version__)"
```

---

## Project Setup

1. Clone this repository:

```bash
git clone https://github.com/ODARI-CHARLES1/DroneProgramming.git
cd DroneProgramming
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

- Windows (PowerShell):
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

4. Run an example script:

```bash
python src/movements.py
```

---

## Project Structure

```
DroneProgramming/
├── .gitignore
├── Readme.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── mission1_garage.py
│   ├── movements.py
│   └── pygame_fm.py
└── Templates/
    ├── keyboard_control.py
    ├── drone_video_stream.py
    ├── rc_controller.py
    └── __pycache__/
```

### Key Files

| File                                | Description                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------ |
| `src/movements.py`                | Demonstrates basic drone movements (forward, backward, left, right, up, down). |
| `src/mission1_garage.py`          | A simple take-off, move, and land mission sequence.                            |
| `Templates/keyboard_control.py`   | Reads keyboard input using PyGame and returns velocity commands.               |
| `Templates/drone_video_stream.py` | Full example combining keyboard control with live video streaming via OpenCV.  |
| `Templates/rc_controller.py`      | Template for RC-style controller integration.                                  |

---

## Usage

### Basic Movement

```python
from pysimverse import Drone

drone = Drone()

drone.connect()
drone.take_off()

drone.move_forward(250)
drone.move_right(250)
drone.move_up(100)

drone.land()
drone.disconnect()
```

### Keyboard Control with Video Stream

```bash
python Templates/drone_video_stream.py
```

Press the following keys to control the drone:

- **W / S** — Forward / Backward
- **A / D** — Left / Right
- **↑ / ↓** — Up / Down
- **← / →** — Yaw Left / Yaw Right
- **Q** — Quit and land

### Custom Mission

Create a new file in `src/` and import the `Drone` class from `pysimverse`. Follow the pattern in `mission1_garage.py` to chain movement commands between `take_off()` and `land()`.

---

## Controls Reference

| Input                | Action                |
| -------------------- | --------------------- |
| `W`                | Move forward          |
| `S`                | Move backward         |
| `A`                | Move left             |
| `D`                | Move right            |
| `↑` (Arrow Up)    | Increase altitude     |
| `↓` (Arrow Down)  | Decrease altitude     |
| `←` (Arrow Left)  | Yaw left              |
| `→` (Arrow Right) | Yaw right             |
| `Q`                | Emergency quit / land |

---

## Troubleshooting

| Issue                                                 | Solution                                                                                              |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'pysimverse'` | Ensure PySimVerse is installed:`pip install pysimverse`                                             |
| Video window freezes                                  | Make sure OpenCV is installed (`pip install opencv-python`) and your display drivers are up to date |
| Drone does not respond to keys                        | Check that the PyGame window is focused before pressing keys                                          |
| Port conflict on stream                               | Ensure no other application is using the default video stream port                                    |

---

## License

This project is provided as-is for educational and experimental purposes.
