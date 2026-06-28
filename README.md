# Backlog Tracker Python


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
| Windows  | [BacklogTracker_Setup.exe](https://github.com/debojitsantra/BacklogTracker-Python/releases/) |
| Linux    | [BacklogTracker_Linux.tar.gz](https://github.com/debojitsantra/BacklogTracker-Python/releases/) |
| macOS    | [BacklogTracker_macOS.zip](https://github.com/debojitsantra/BacklogTracker-Python/releases/) *(untested)* |

All releases: [github.com/debojitsantra/BacklogTracker/releases](https://github.com/debojitsantra/BacklogTracker-Python/releases/)

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
