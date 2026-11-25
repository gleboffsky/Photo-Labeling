# Photo Labeling

A PyQt5 desktop tool for sorting a folder of photos into labelled subfolders.
Photos are shown one at a time and a single key press assigns the current photo
to a category and moves the file into the matching folder. It was written as a
personal helper for hand-labelling image datasets.

## Features

- Preview of the current photo, optionally downscaled to keep browsing fast.
- 12 configurable category buttons, each bound to a hotkey
  (`Q W E R A S D F Z X C V`); `G` / `T` go to the next / previous photo.
- Photos are *moved* to `<output folder>/<category>/` and can be renamed to
  `<category>_<n>.<ext>`.
- Counters for processed photos and for photos still left in the folder.
- Settings are kept as JSON in `%USERPROFILE%\Documents\PhotoLabeling.txt`
  (source folder, output folder, resize on/off and resolution, rename mode and
  the list of category names) and can be edited from the **File** menu.

## Requirements

Python 3.8+, `PyQt5` and `opencv-python`. Tkinter (used for the folder pickers)
ships with the official Windows Python build.

## Run

```
pip install PyQt5 opencv-python
python functional.py
```

Then choose **File → Photo Folder** for the images to label and
**File → Exit Folder** for the destination root, and press a category key.

## Build a standalone executable

```
pyinstaller PhotoLabeling.exe.spec
```

## Files

- `functional.py` — the whole application: window, hotkeys, file sorting.
- `mainwindow.py` — Qt Designer generated UI definition.
- `resources.py`, `resources.qrc` — compiled Qt resources (window icon).
- `PhotoLabeling.exe.spec`, `functional.py.spec` — PyInstaller build specs.
- `PhotoLabeling.ico`, `PhotoLabeling.jpg` — icon and placeholder graphic.
