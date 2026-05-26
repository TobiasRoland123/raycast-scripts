#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title KMD start apps
# @raycast.mode compact

# Optional parameters:
# @raycast.icon images/kmd-logo.svg

# Documentation:
# @raycast.description Opens a list of applications
# @raycast.author Tobias Roland Uyet

import subprocess

apps = [
    "Microsoft Outlook",
    "Arc",
    "WebStorm",
    "Slack",
    "Warp",
    "Notion",
    "Codex",
    "ChatGPT",
    "Microsoft Teams",
    "Docker Desktop",
    "Cisco Secure Client",
]

for app in apps:
    print(f"Opening {app}...")
    try:
        subprocess.Popen(["open", "-a", app])
    except Exception as e:
        print(f"Failed to open {app}: {e}")
