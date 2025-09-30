# DisplayPort Monitor Auto-Refresh

**Tired of Windows not detecting your second monitor after a reboot?**  
This tool automatically toggles your monitor’s refresh rate to force detection, eliminating the need to physically unplug and replug the monitor. Works especially well for DisplayPort monitors with hot-plug detection issues.

---

## Features

- Detects supported refresh rates at native resolution.
- Toggles between two refresh rates to wake up the monitor.
- Stores the last state so it knows which rate to toggle to next.
- Works as a standalone `.exe` with PyInstaller.
- Can be automated to run at Windows startup.

---

## Requirements

- Windows 10 or 11
- Python 3.x
- [`pywin32`](https://pypi.org/project/pywin32/)

Install dependencies:

```bash
pip install -r requirements.txt
