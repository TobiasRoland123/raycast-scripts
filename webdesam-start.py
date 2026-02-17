#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Webdesam start apps
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 💼

# Documentation:
# @raycast.description Opens a list of applications
# @raycast.author Tobias Roland Uyet

import subprocess

apps = [
    "chatGPT",
    "Codex",
    "Google Chrome",
    "webstorm",
    "warp",
    "Notion",
    "Docker"
]

for app in apps:
    print(f"Opening {app}...")
    try:
        subprocess.Popen(["open", "-a", app])
    except Exception as e:
        print(f"Failed to open {app}: {e}")
