import os
import platform

LOCATIONS = {
    "chrome": {
        "windows": "%LOCALAPPDATA%\\Google\\Chrome\\User Data",
        "darwin": "$HOME/Library/Application Support/Google/Chrome",  # macOS
        "linux": "$HOME/.config/google-chrome"
    },
    "chromium": {
        "windows": "%LOCALAPPDATA%\\Chromium\\User Data",
        "darwin": "$HOME/Library/Application Support/Chromium",  # macOS
        "linux": "$HOME/.config/chromium"
    },
    "brave": {
        "windows": "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data",
        "darwin": "$HOME/Library/Application Support/BraveSoftware/Brave-Browser",  # macOS
        "linux": "$HOME/.config/BraveSoftware/Brave-Browser"
    },
    "edge": {
        "windows": "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data",
        "darwin": "$HOME/Library/Application Support/Microsoft Edge",  # macOS
        "linux": "$HOME/.config/microsoft-edge"
    },
}


def get_browser_path(browser: str) -> str | None:
    system = platform.system().lower()
    if browser in LOCATIONS and system in LOCATIONS[browser]:
        return os.path.expandvars(LOCATIONS[browser][system])
