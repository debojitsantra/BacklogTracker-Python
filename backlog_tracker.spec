# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for Backlog Tracker v1.1.0
# Run with: pyinstaller backlog_tracker.spec

import sys
from pathlib import Path

# ── Locate customtkinter & darkdetect data dirs ──────────────────────────────
import customtkinter, darkdetect
CTK_DIR  = Path(customtkinter.__file__).parent
DARK_DIR = Path(darkdetect.__file__).parent

block_cipher = None

a = Analysis(
    ['backlog_tracker.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        # CustomTkinter theme assets (required at runtime)
        (str(CTK_DIR), 'customtkinter'),
        # darkdetect helper data
        (str(DARK_DIR), 'darkdetect'),
        # App icon
        ('icon.ico', '.'),
        # Our own packages
        ('theme.py',   '.'),
        ('version.py', '.'),
        ('utils',      'utils'),
        ('components', 'components'),
        # Example JSON files (optional, nice to ship)
        ('examplefull.json',      '.'),
        ('exampleonlycourse.json', '.'),
    ],
    hiddenimports=[
        'customtkinter',
        'darkdetect',
        'PIL',
        'PIL.Image',
        'PIL.ImageDraw',
        'PIL.ImageTk',
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BacklogTracker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # no terminal window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',        # Windows/Linux taskbar icon
)

if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='BacklogTracker.app',
        icon='icon.ico',
        bundle_identifier=None,
    )
