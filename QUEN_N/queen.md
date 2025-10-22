# N-Queens Problem (Backtracking Solution)

## Description
This project solves the classic **N-Queens Problem**, where the goal is to place `N` queens on an `N x N` chessboard so that no two queens threaten each other.  
It uses a **backtracking algorithm** to explore valid configurations and display all possible solutions.

## Features
- Solves for any board size `N` entered by the user  
- Displays all valid board configurations  
- Shows total number of possible solutions  
- Efficient backtracking approach  

## How It Works
1. The chessboard is represented as a 2D array.  
2. Queens are placed row by row in safe positions.  
3. The algorithm checks:
   - Columns
   - Left diagonals
   - Right diagonals  
4. When a conflict occurs, the algorithm backtracks to try a new position.  

## Requirements
- Python 3.x

## Usage
```bash
python nqueens.py
