# Filler

**Filler** is a two-player terminal-based strategy game written in Python.

Players take turns choosing a color to expand their territory on a randomly generated grid. Starting from opposite corners, the goal is to fill more of the board than your opponent. The game emphasizes adjacency-based flood fill logic and is played entirely in the console with color-coded cells.

## How It Works

- The board is a 7x8 grid filled with randomly colored cells.
- Player 1 starts at the bottom-left corner; Player 2 starts at the top-right.
- Each turn, players choose a new color (1–6) to expand their region.
- The game ends when the board is fully claimed.

## Features

- Color-coded ASCII grid rendering in the terminal
- Custom flood fill logic without recursion
- Simple scoring and real-time board updates
- Clears and redraws the board each turn for better UX

## Getting Started

Run the game using:

```bash
python main.py
```

You'll play as both Player 1 and Player 2 via the terminal.

## Notes

- Works best in a terminal that supports ANSI color codes
- No third-party libraries required
