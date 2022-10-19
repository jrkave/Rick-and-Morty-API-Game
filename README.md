# API Project: Rick and Morty Game
This project allows users to guess whether a character in Rick and Morty is alive or dead using data from an API.

# Game 1 (main.py)
The main.py file selects a character based on a random number from the user. Information about that character is printed for the viewer, such as the episode in which they first appeared, their origin location, species, type, and a link to a reference photo (if the user wants one). The user then determines whether the character is dead or alive and receives immediate feedback on their response. The amount of correct answers gets stored for the user to view, and they can continue playing until a 'quit' command is entered.

Note: having the user select a random number was mainly for fun / practice, but isn't really "necessary" in terms of choosing a random number.

# Game 2 (game.py)
The game in this file is largely similar to the one built in main.py. However, instead of having a user enter a random number to select a character, this program auto-generates five characters for the user to determine their status. This game scores the amount of correct guesses and prints it at the end, along with answers to the questions that the user missed.
