# Asteroids Game

A recreation of the classic Asteroids arcade game built with Python and Pygame. Shoot through waves of asteroids that split into smaller pieces, and survive as long as you can.

![Asteroid's game screenshot](/game/pygame.png)

## Features

- Player ship with rotation and thrust movement in all directions
- Asteroids that split into two faster, smaller pieces when shot
- Projectile shooting with a cooldown timer
- Collision detection between ship, asteroids, and shots
- Continuous asteroid spawning from random screen edges
- Frame-rate independent movement using delta time

## How the Game Works

The player controls a triangular ship in the centre of the screen. Asteroids spawn from the edges and drift inward. Shooting a large asteroid splits it into two smaller, faster ones. The game ends when the ship collides with any asteroid.

**Controls**

|   Key   |     Action      |
|---------|-----------------|
|   `W`   | Thrust forward  |
|   `S`   | Thrust backward |
|   `A`   | Rotate left     |
|   `D`   | Rotate right    |
| `Space` | Shoot           |

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- [Pygame](https://www.pygame.org/) (installed automatically via `uv sync`)

## Getting Started

```bash
git clone https://github.com/lillysilly3/asteroid-game.git
cd asteroid-game
uv sync
uv run python main.py
```

## Project Structure

```
asteroid-game/
├── game/
│   ├── player.py         # Ship movement, rotation, and shooting
│   ├── asteroid.py       # Asteroid behaviour and splitting logic
│   ├── asteroidfield.py  # Spawning system
│   ├── shot.py           # Projectile mechanics
│   ├── circleshape.py    # Base class with shared collision detection
│   ├── constants.py      # Game configuration values
│   └── logger.py         # Game state and event logging
├── main.py               # Entry point and game loop
├── pyproject.toml
└── uv.lock
```

## What I Explored

- **Pygame fundamentals** — Game loop, event handling, sprite groups, and display rendering
- **OOP with inheritance** — Shared `CircleShape` base class for collision logic across all game objects
- **Delta time** — Frame-rate independent movement so the game runs consistently at any speed
- **Sprite group pattern** — Separating `updatable` and `drawable` groups for a clean game loop
- **Game physics** — Velocity vectors, rotation, and asteroid splitting mechanics
- **Package structure** — Organising a multi-file Python project into a proper package

## Future Ideas

- Score counter and high score tracking
- Health system with respawning
- Sound effects and background music
- Increasing difficulty over time
- Main menu and game over screen

## Acknowledgments

This project was built as part of the [Boot.dev](https://boot.dev) curriculum.
