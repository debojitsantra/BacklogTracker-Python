<p align="center">
  <img src="assets/banner.png" width="100%" alt="Backlog Tracker Banner" />
</p>

<p align="center">
  <img src="assets/icon_300.png"  width=72 alt="Backlog Tracker Icon" />
</p>

<h1 align="center">Backlog Tracker</h1>

<p align="center">A lightweight cross-platform desktop application that helps students calculate, track, and systematically clear academic backlogs.</p>

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

Android Version Code Here: [Android](https://github.com/debojitsantra/BacklogTracker-Android/)

Download the latest release for your platform:

| Platform | Download |
|----------|----------|
| Windows  | [BacklogTracker_Setup.exe](https://github.com/debojitsantra/BacklogTracker/releases/) |
| Linux    | [BacklogTracker_Linux.tar.gz](https://github.com/debojitsantra/BacklogTracker/releases/) |
| macOS    | [BacklogTracker_macOS.zip](https://github.com/debojitsantra/BacklogTracker/releases/) *(untested)* |
| Android | [BacklogTracker-{tag}.apk](https://github.com/debojitsantra/BacklogTracker-Android/releases)|
| Web Version *(unstable)*| [backlogtracker.debojitworkers.qzz.io](https://backlogtracker.debojitworkers.qzz.io/)|

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

---

## Author

[github.com/debojitsantra](https://github.com/debojitsantra)


## You can help me by Donating
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/debojitsantra) 
[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/debojitsantra/donate)
<a href="https://chai4.me/debojitsantra" target="_blank" title="Support debojitsantra on Chai4Me" style="display:inline-flex;flex-direction:column;align-items:center;justify-content:center;background:#ffffff;padding:8px 32px;border-radius:16px;text-decoration:none;border:1px solid #e5e7eb;box-shadow:0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);transition:transform 0.2s;"><img src="https://chai4.me/icons/wordmark.png" alt="Chai4Me" style="height:32px;object-fit:contain;"/></a>
