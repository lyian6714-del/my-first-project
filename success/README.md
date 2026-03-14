# Snake Game

A classic Snake game implemented in Python using Pygame. All text and interface elements are in English.

## Game Features

- Classic snake gameplay
- Score tracking system
- Pause/Resume functionality
- Game over detection
- Clean grid-based graphics
- Responsive controls

## Requirements

- Python 3.6 or higher
- Pygame library

## Installation

1. **Install Python** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Install Pygame**
   Open Command Prompt or PowerShell and run:
   ```bash
   pip install pygame
   ```

## How to Run

1. **Navigate to the game directory**
   ```bash
   cd c:\Users\yasan\Desktop\success
   ```

2. **Run the game**
   ```bash
   python snake_game.py
   ```

## Game Controls

| Key | Action |
|-----|--------|
| ↑ (Up Arrow) | Move Up |
| ↓ (Down Arrow) | Move Down |
| ← (Left Arrow) | Move Left |
| → (Right Arrow) | Move Right |
| P | Pause/Resume Game |
| R | Restart Game |
| ESC | Quit Game |

## Game Rules

1. **Objective**: Control the snake to eat the red food
2. **Scoring**: Each food eaten adds 10 points to your score
3. **Growth**: The snake grows longer each time it eats food
4. **Game Over**: The game ends when:
   - The snake hits the wall
   - The snake collides with its own body

## Game Interface

- **Green squares**: Snake body
- **Red square**: Food
- **Score display**: Top-left corner
- **Controls guide**: Top-right corner

## Tips

- Plan your moves ahead to avoid trapping yourself
- The snake moves faster as it grows longer
- Use the pause feature (P key) to take breaks
- Try to keep the snake away from the walls

## Troubleshooting

**Problem**: "pygame module not found"
**Solution**: Run `pip install pygame` in your terminal

**Problem**: Game window is too small/large
**Solution**: You can modify `WINDOW_WIDTH` and `WINDOW_HEIGHT` constants in the code

**Problem**: Game is too fast/slow
**Solution**: Adjust the `FPS` constant in the code (default is 10)

## Technical Details

- **Resolution**: 800x600 pixels
- **Grid Size**: 20x20 pixels per cell
- **Frame Rate**: 10 FPS
- **Initial Snake Length**: 3 segments

## License

This is a free, open-source game for educational purposes.

Enjoy the game!
