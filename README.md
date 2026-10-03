# Suits You Sir

A tiny Windows background app that plays a random sound whenever an application is opened.

Inspired by the legendary **"Ooh, suits you, sir!"** sounds from *The Fast Show*.

---

## 📋Features

* 🎵 Plays a random sound when an application starts
* 🔒 Only plays one sound at a time
* 🖥️ Runs silently in the background
* 🔔 Lives in the Windows system tray
* 🚫 Large list of Windows and system processes that are ignored
* 📝 Logs detected application launches
* 🎲 Randomly selects from all available sounds
* 📦 Can be built into a standalone `.exe` with PyInstaller
* 🚀 Can be added to Windows startup

---

## 🤔How It Works

Suits You Sir monitors Windows processes using [`psutil`](https://github.com/giampaolo/psutil).

When a new process appears, it checks whether the process is in the ignored-process list.

If it isn't ignored:

1. The application name is written to `SuitsYouSir.log`
2. A random sound is selected
3. If no other sound is currently playing, it is played

If a sound is already playing, the new sound is skipped rather than interrupting the current one.

This means launching several applications at once won't result in a horrible pile-up of sounds.

---

## 💡Contributing

Contributions are welcome!

The easiest way to contribute is by adding more sounds.

### 🎙️Adding a Sound

Just drop a `.wav`, `.mp3`, or `.ogg` file into:

```text
Sounds\
```

That's it.

The application automatically detects the file and includes it in the random sound selection.

No code changes or configuration are required.

For example:

```text
Sounds\
├── suits_you_sir.mp3
├── nice_one.wav
├── very_nice.ogg
└── another_sound.mp3
```

### 🎤Audio Contributions

For *The Fast Show* sounds, the original audio remains the property of its respective rights holders.

You can also contribute by:

* Adding useful processes to the ignore list
* Fixing bugs
* Improving process detection
* Improving the tray interface
* Improving the build process
* Suggesting new features
* Improving documentation
* Creating additional sound packs

---

## 🔊Sounds

Suits You Sir supports:

```text
.wav
.mp3
.ogg
```

There is no special naming convention. You can call the files whatever you want.

A sound is selected randomly whenever a non-ignored application starts.

### Included Sounds

The sound effects included with this project are sourced from **The Fast Show PC Game**.

They are included as part of this fan-made project and are not original recordings created by Suits You Sir.

---

## 🧾Application Log

Detected application launches are recorded in:

```text
SuitsYouSir.log
```

Example:

```text
[03/10/2026 13:32:30] discord.exe
[03/10/2026 13:32:30] Modrinth App.exe
[03/10/2026 13:22:17] WhatsApp.Root.exe
```

The log **only records applications being opened**.

It does **not** record:

* Applications closing
* Sounds being played
* Ignored processes

---

## ⌨️Running From Source

### 📋Requirements

* Windows
* Python 3

Python packages:

```text
psutil
pygame
pystray
Pillow
```

Install them with:

```powershell
python3 -m pip install psutil pygame pystray Pillow
```

### 🏃‍♂️‍➡️Running

Run:

```powershell
python3 main.py
```

The application doesn't open a normal window.

It runs in the background and places an icon in the Windows system tray.

Right-click the tray icon and select **Quit** to close it.

---

## 🏃‍♂️‍➡️Running the `.exe`

The compiled application is completely windowless, so no console window appears.

It runs in the background and can be accessed through the Windows system tray.

If you want Suits You Sir running automatically, you can add a shortcut to the Windows Startup folder.

```text
SuitsYouSir.exe
       │
       ├── Runs in background
       ├── Watches for new processes
       ├── Ignores system/helper processes
       ├── Logs application launches
       └── Plays a random sound
```

---

## 🧱Building

A PowerShell build script is included:

```text
build.ps1
```

Run it from the project directory:

```powershell
.\build.ps1
```

The build script:

1. Removes previous build files
2. Builds the application with PyInstaller
3. Creates a windowless executable
4. Cleans temporary PyInstaller files
5. Creates a distributable ZIP

The final files are:

```text
SuitsYouSir.exe
SuitsYouSir.zip
```

### 🛠️Manual Build

You can also build it manually:

```powershell
python3 -m PyInstaller --onefile --windowed --name "SuitsYouSir" --add-data "Sounds;Sounds" main.py
```

---

## 🏗️Project Structure

```text
SuitsYouSir/
├── Sounds/
│   ├── sound1.mp3
│   ├── sound2.mp3
│   └── ...
├── main.py
├── build.ps1
├── README.md
└── SuitsYouSir.log
```

After building, additional files may temporarily appear:

```text
build/
dist/
SuitsYouSir.spec
```

The build script automatically removes these when the build finishes.

---

## 🖥️Technology

Suits You Sir is built using:

* **Python** — Application logic
* **psutil** — Windows process monitoring
* **pygame** — Audio playback
* **pystray** — System tray integration
* **Pillow** — Tray icon generation
* **PyInstaller** — Standalone executable builds

---

## 🐜Bug Reports

If you find a bug, please include:

* Windows version
* Python version, if running from source
* The error message, if there is one
* What you were doing when the problem occurred
* Whether you were running `main.py` or the compiled `.exe`

If the problem is related to a particular application launching, include the application's executable name if possible.

---

## 🤔Future Ideas

Possible future features include:

* 🔊 More sound packs
* ⚙️ Configurable ignored processes
* 🎚️ Volume control
* 🎲 Sound categories
* ⏱️ Cooldowns between sounds
* 🔀 Custom sound-selection rules
* 📋 A viewable application log
* 🚀 Automatic Windows startup configuration
* 🎨 Custom tray icons
* 🔔 Optional Windows notifications

---

## ❓Why?

Because opening stuff is boring.

Opening stuff and immediately hearing:

> "Ooh, suits you, sir!"

is considerably less boring.

---

## 🫡Credits & Attribution

**Suits You Sir** is an unofficial fan-made project inspired by *The Fast Show*.

The audio assets included with this project originate from **The Fast Show PC Game** and were not created by this project.

*The Fast Show* was originally broadcast by the **BBC**. The programme, characters, audio, trademarks, and associated intellectual property belong to their respective rights holders.

This project is **not affiliated with, endorsed by, or sponsored by** the BBC, *The Fast Show*, or the creators and rights holders of the original game.

The included audio assets remain the property of their respective rights holders.

---

## ❗Disclaimer

This project is made for fun and is not intended to claim ownership of any third-party material.

The project does not claim ownership of:

* *The Fast Show*
* The Fast Show PC Game
* Characters
* Audio recordings
* Trademarks
* Logos
* Other third-party intellectual property

If distributing a version containing third-party audio, make sure you have the appropriate rights or permission to distribute those files.

---

## 📜Licensing

The **source code** for this project may be used and modified freely.

The included *The Fast Show* audio assets are **not covered by the source-code license** and remain the property of their respective rights holders.

Third-party assets should be treated according to their respective ownership and licensing terms.
