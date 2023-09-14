# Rick and Morty API Project
## Description
The Rick and Morty API Game is a Python-based interactive game where players can engage with characters from the popular TV series, Rick and Morty. Leveraging the Rick and Morty API, this game provides a fun and immersive experience by allowing players to guess whether a character is dead or alive in the series. To help users make their guesses, information about the characters (e.g. first episode appearance, origin location, species, type, and links to reference photos) are provided. 

## Table of Contents
- Features
- Installation
- Usage
- Code Overview

## Features
1. **Character Status Guessing**: Players are presented with information about a character and must guess whether that character is dead or alive
2. **Interactive Gameplay**: Players receive immediate feedback on their guesses, fostering an engaging gameplay experience
3. **Rick and Morty API Integration**: Utilizes the Rick and Morty API to dynamically fetch character details and images

## Installation
To run these games locally, use the following command: `git clone https://github.com/jrkave/Rick-and-Morty-API-Game.git`

## Versions and Gameplay
- **Version 1 (main.py)**: In this version, the user chooses a random number between 1 and 725 to select a character. This number is used to fetch data about a specific character and ensures that the user cannot repeat characters they've already made guesses on. They receive immediate feedback on their answers and a counter keeps track of the amount of correct responses. The user may continue playing until issuing a 'quit' command.
- **Version 2 (game.py)**: This version of the game is similar to _main.py_ but has a few key differences. Instead of having the user enter a random number to select a character, this program auto-generates five characters for the user determine their status. After guessing the five statuses, the game ends and the user is presented with answers to the questions they answered incorrectly. They are also able to choose whether or not to play again.
