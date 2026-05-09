# Asteroids Game

Based on the eponymous boot.dev course.

## Prerequisities:
 - Python 3.13+
 - [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Set-up:
1. Clone respository: `git clone https://github.com/SandorTeleki/asteroids-game.git`
2. Move to cloned respository with `cd asteroids-game`
3. Install dependencies with `uv sync`
4. Run game with: `uv run python main.py`

## Pontential future improvements:
* Add a scoring system (time survived + asteroids destroyed + maybe, power-ups gathered)
* Implement multiple lives and respawning
* Add an explosion effect for the asteroids
* Add acceleration to the player movement
* Make the objects wrap around the screen instead of disappearing
* Add a background image
* Create different weapon types
* Make the asteroids lumpy instead of perfectly round
* Make the ship have a triangular hit box instead of a circular one
* Add a shield power-up
* Add a speed power-up
* Add bombs that can be dropped
* Help menu