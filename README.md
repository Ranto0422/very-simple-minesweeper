# Very Simple Minesweeper

A small Minesweeper-style game with a Tkinter GUI. Choose how many bombs to hide on a 5x5 board, then uncover tiles for points until you find a bomb. Made for a lab exercise.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue)

| | |
|---|---|
| **Stack** | Python 3, Tkinter (standard library) |
| **Concepts** | Event-driven GUI, grid layout, random bomb placement with `random.sample`, input validation |

## How to play

1. Enter the number of bombs (1 to 24) and press **Start**.
2. Click tiles. Each safe tile is worth 10 points.
3. Hit a bomb and the whole board is revealed with your final score.

## Running it

```bash
python minesweeper.py
```

No extra packages needed. On some Linux distributions install Tkinter first (`sudo apt install python3-tk`).

## Project structure

```
very-simple-minesweeper/
├── minesweeper.py    the game
├── assets/           tile, bomb and button images
└── archive/          earlier attempts (first draft and an alternate layout)
```
