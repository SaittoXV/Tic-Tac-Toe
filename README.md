Here you go — a clean, ready‑to‑use **README.md** file based entirely on your provided text, with no extra analysis or changes.

***

# Tic‑Tac‑Toe (Python Project)

This project is a simple console‑based Tic‑Tac‑Toe game where the computer plays against the user. The game has been intentionally simplified to focus on core programming concepts without advanced AI.

***

## 🎮 Game Scenario

The program simulates a game of Tic‑Tac‑Toe with the following rules:

*   The **computer** uses **'X'**.
*   The **user** uses **'O'**.
*   The **computer always makes the first move**, placing an **'X' in the center** of the board.
*   The board squares are numbered **1 through 9**, row by row.
*   The user enters their move by typing the number of the chosen square.
*   A move is valid only if:
    *   It is an integer.
    *   It is between **1 and 9**.
    *   The square is **not already occupied**.
*   After each move, the program checks the game state:
    *   The game continues.
    *   The game ends in a tie.
    *   The user wins.
    *   The computer wins.
*   The computer chooses its moves **randomly** (no artificial intelligence).

***

## 🗂 Board Structure

The game board is stored as a **list of three lists**, each containing **three elements**:

```python
board[row][column]
```

*   Each element may be:
    *   `'O'`
    *   `'X'`
    *   A number representing a free square

The board must visually match the format shown in the example session.

***

## 🖼 Example Game Session

    +-------+-------+-------+
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   4   |   X   |   6   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    +-------+-------+-------+
    Enter your move: 1
    ...
    You won!

(Full session included in original description.)

***

## ✅ Requirements

Your implementation must include:

*   The board stored as a **3×3 nested list**.
*   The board displayed **exactly** like the example.
*   Full support for all required game functions.
*   A random computer move using `randrange()`:

```python
from random import randrange

for i in range(10):
    print(randrange(8))
```

***

## 🛠 Random Number Generation

The computer’s random move selection uses:

```python
from random import randrange
```

`randrange()` picks a random integer within the specified range, and can be used to choose an available board position.

***