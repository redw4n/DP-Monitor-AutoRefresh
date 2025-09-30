import win32api
import win32con
import os

STATE_FILE = "refresh_state_display2.txt"
DISPLAY_INDEX = 1  # 0 = Primary, 1 = Second monitor

def get_display_device(display_number=DISPLAY_INDEX):
    return win32api.EnumDisplayDevices(None, display_number)

def set_refresh_rate(display_number=DISPLAY_INDEX, hz=75):
    device = get_display_device(display_number)
    settings = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
    settings.DisplayFrequency = hz
    result = win32api.ChangeDisplaySettingsEx(device.DeviceName, settings)
    if result == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f"✅ Changed Display {display_number+1} refresh rate to {hz}Hz")
        return True
    else:
        print(f"⚠️ Failed to change refresh rate (Error {result})")
        return False

def load_last_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                return int(float(f.read().strip()))
            except:
                return None
    return None

def save_state(hz):
    with open(STATE_FILE, "w") as f:
        f.write(str(hz))

def toggle_refresh(hz1=75, hz2=85):
    last = load_last_state()
    if last == hz1:
        success = set_refresh_rate(DISPLAY_INDEX, hz2)
        if success: save_state(hz2)
    else:
        success = set_refresh_rate(DISPLAY_INDEX, hz1)
        if success: save_state(hz1)

if __name__ == "__main__":
    toggle_refresh(hz1=75, hz2=85)
