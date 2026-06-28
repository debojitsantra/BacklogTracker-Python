# Backlog Tracker Python
---

## Features

- **Smart Backlog Clearance Calculations**: Dynamically computes when you will clear your backlogs based on current target pacing.
- **Classes Per Day (CPD) Tracking**: Plan and adjust your target daily watches.
- **Sunday-Aware ETA Prediction**: Accurate completion dates that take into account whether new classes are released/skipped on Sundays.
- **Data Export & Import/Merge**:
  - Export your entire progress to a portable JSON backup file.
  - Import full backups, or import a course-only design layout (with automatic Setup Wizard validation and setup).
  - Built-in validation helper with immediate success/error visual feedback.
- **Keyboard Shortcuts**:
  - `Ctrl + S`: Sync/Save changes
  - `Ctrl + Z`: Undo last change
  - `Ctrl + ,`: Open Settings Modal
- **Undo Support**: Access a 20-step local change undo stack from the footer or via shortcut to revert mis-clicks.
- **Last Studied Badges**: Automatically tracks and displays the "Last studied" timestamp for every subject when you mark a class completed.
- **Settings Panel**: Tweak your appearance mode (Light/Dark) and show/hide motivational productivity prompts dynamically.
- **Time Simulator**: Fast-forward days, weeks, or months to preview the compound effects of neglecting core daily study targets.

---

## Screenshots
<p align="center">
  <img src="assets/1.png" width="100%" alt="Screenshot 1" />
  <img src="assets/2.png" width="100%" alt="Screenshot 2" />
</p>

---

## Installation



Download the latest release for your platform:

| Platform | Download |
|----------|----------|
| Windows  | [BacklogTracker_Setup.exe](https://github.com/debojitsantra/BacklogTracker/releases/) |
| Linux    | [BacklogTracker_Linux.tar.gz](https://github.com/debojitsantra/BacklogTracker/releases/) |
| macOS    | [BacklogTracker_macOS.zip](https://github.com/debojitsantra/BacklogTracker/releases/) *(untested)* |

All releases: [github.com/debojitsantra/BacklogTracker/releases](https://github.com/debojitsantra/BacklogTracker/releases/)


<a href="https://apps.microsoft.com/detail/9p112ngslvf0?referrer=appbadge&mode=full" target="_blank"  rel="noopener noreferrer">
	<img src="https://get.microsoft.com/images/en-us%20dark.svg" width="200"/>
</a>

### Linux — Emoji Support

If emojis appear as blank squares, install the Noto Color Emoji font:

```bash
sudo apt install fonts-noto-color-emoji -y
```

> Required on Ubuntu/Debian-based distros. Not needed on most modern distros that ship with it by default.

---

## Local Development

**Install dependencies**
```bash
pip install customtkinter pillow pyinstaller darkdetect
```

**Run locally**
```bash
python backlog_tracker.py
```

**Build executable**
```bash
pyinstaller backlog_tracker.spec --noconfirm
```

---

## Releases via CI/CD

To deploy and package using the automatic multi-platform CI/CD pipeline:
```bash
git tag v1.1.0
git push origin v1.1.0
```
