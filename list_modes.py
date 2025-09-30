import win32api
import win32con

def list_display_modes(display_number=1):
    device = win32api.EnumDisplayDevices(None, display_number)
    i = 0
    modes = []
    while True:
        try:
            mode = win32api.EnumDisplaySettings(device.DeviceName, i)
            modes.append((mode.PelsWidth, mode.PelsHeight, mode.DisplayFrequency, mode.BitsPerPel))
            i += 1
        except Exception:
            break
    return modes

if __name__ == "__main__":
    modes = list_display_modes(1)  # Display 2
    modes = [m for m in modes if m[0] == 1920 and m[1] == 1080]  # filter to native resolution
    print("Supported modes at 1920x1080 for Display 2:")
    for m in modes:
        print(m)
