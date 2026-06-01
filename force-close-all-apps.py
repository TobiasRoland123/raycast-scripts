#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Force Close All Apps
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 💀

# Documentation:
# @raycast.description Force closes all open applications except Raycast
# @raycast.author Tobias Roland Uyet

import subprocess
import time

EXCLUDED_APPS = {
    "Raycast",
}

try:
    # Get all visible app processes
    result = subprocess.run(
        [
            "osascript",
            "-e",
            'tell application "System Events" to get name of (application processes whose background only is false)'
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    running_apps = [app.strip() for app in result.stdout.split(",") if app.strip()]

    # Try graceful quit first
    for app in running_apps:
        if app in EXCLUDED_APPS:
            continue

        print(f"Quitting {app}...")
        subprocess.run(
            ["osascript", "-e", f'tell application "{app}" to quit'],
            capture_output=True,
        )

    # Give apps a moment to shut down cleanly
    time.sleep(3)

    # Force kill anything still running
    for app in running_apps:
        if app in EXCLUDED_APPS:
            continue

        print(f"Force killing {app}...")
        subprocess.run(
            ["pkill", "-9", "-x", app],
            capture_output=True,
        )

    print("Done.")

except Exception as e:
    print(f"Error: {e}")