# mygames
Collection of small Python/pygame example games used for learning and experimentation.

This repository contains several standalone game examples (procedural pygame scripts) you can run, study, and modify.

**Games included:**
- `Cannon_Shot/` — simple cannon vs. falling asteroids (`Cannon_Shot_game`).
- `Hang_Man/` — Hangman implementation (`Hang_Man_Code`, uses `Hang_man_Word.txt`).
- `pacman/` — a small Pac-Man style demo (`mygame.py`).
- `rocket_game/` — rocket game demo (`game.py`).
- `tic-tac-toe/` — Tic-Tac-Toe examples (`Tic-Tak-Toe.py` and `Pygame/Faster_Tic_Tack_Toe.py`).

**Quick start (requirements)**
- **Python:** 3.8+ recommended.
- **Dependencies:** `pygame` (install with pip).

Install pygame in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pygame
```

**Run a game**
- From the repository root you can run a game with `python3 <path>` — for example:

```bash
python3 Cannon_Shot/Cannon_Shot_game
python3 pacman/mygame.py
python3 rocket_game/game.py
python3 tic-tac-toe/Tic-Tak-Toe.py
```

Note: some files in this repo are plain Python scripts without a `.py` extension (for example `Cannon_Shot/Cannon_Shot_game`). Use `python3 <file>` to run them or add a `.py` extension if you prefer.

**Project notes & common patterns**
- Most games use `pygame` and are single-file procedural scripts (global state, main loop, simple classes for sprites such as `Asteroid`/`Laser` in `Cannon_Shot`).
- Asset loading is relative to the game folder (e.g. `Cannon.png`, `asteroid.png` in `Cannon_Shot/`). If you get `FileNotFoundError`, check the current working directory when launching.
- Controls and behaviours are implemented directly in the main loop (keyboard handling, collision checks). Example: `Cannon_Shot` uses `SPACE` to fire, `LEFT/RIGHT` to aim, `R` to reset and `Q` to quit.

**Troubleshooting**
- If the display doesn't open on a headless server (CI or remote container), run under Xvfb or on a local machine with a display.
- If images fail to load, ensure you run the script from the repo root or change working directory to the game's folder before running.
- Typical fixes are renaming files to include `.py` or ensuring the correct working directory.

**Contributing / Editing**
- These examples are intentionally simple — prefer small, focused changes.
- When modifying a game, run it locally and keep asset paths relative to the game folder.
- If adding dependencies, include them in a `requirements.txt` at repo root.

If you'd like, I can:
- add a `requirements.txt` and a small launcher script to pick and run games,
- or standardize filenames to use `.py` consistently.

Please tell me which change you'd like next.
