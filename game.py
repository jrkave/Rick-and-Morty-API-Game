import requests
import json
import random

def game_instructions():
    print("Welcome to Dead or Alive: Rick and Morty Version.")
    print("In this game, you will be given 10 random characters from Rick and Morty with some information about each one, such as their species, type, origin location, and the episode in which they were first seen in.")
    print("The objective of this game is to correctly guess if a character is dead or alive.")
    print("If you do not remember the character and would like a reference photo, you will have the option to request one.")
    print("Each correct guess is worth 1 point. Incorrect guesses are awarded no points.")
    print("Your score (out of 10) will be calculated at the end. Good luck!")
    print()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def characters_alive_or_dead(api_link):
    # Empty list to contain character data of all pages
    total_results = []
    # Grabs search results of first page
    response = requests.get(api_link)
    char_data = response.json()
    # Add data from first page to total results
    total_results = total_results + char_data['results']
    # Parse through all pages of data in API to update total_results with all character data
    while char_data['info']['next'] is not None:
        response = requests.get(char_data['info']['next'])
        char_data = response.json()
        total_results = total_results + char_data['results']
    return total_results

def errors(dict):
    my_dict = dict
    # my_dict has two items {a:b and {c:d}}
    for key, value in my_dict.items():
        print(f"{key} is {value.lower()}.")

if __name__ == "__main__":

    alive_characters_link = "https://rickandmortyapi.com/api/character/?status=alive"
    dead_characters_link = "https://rickandmortyapi.com/api/character/?status=dead"
    list_alive = characters_alive_or_dead(alive_characters_link)
    list_dead = characters_alive_or_dead(dead_characters_link)
    list_all = list_alive + list_dead
    # Gets amount of characters in list: 726
    num_of_characters = (len(list_all))
    random.seed()
    # Shuffles list to randomize
    random.shuffle(list_all)
    #jprint(list_all[0])
    #jprint(list_alive)
    #jprint(list_dead)

    # # Prints game instructions and initializes variables
    game_instructions()
    user_input = ''

    # While loop to continue game until 'q' or 'quit' are entered
    while user_input != 'q' or user_input != 'quit':

        points = 0
        num_iterations = 0
        dict_errors = {}
        
        while num_iterations < 5:
            # Gets a random number to determine which character is chosen; list_all contains 726 characters
            choice = random.randint(0, 725)
            num_iterations += 1

            # Stores parsed data from API in variables
            character = list_all[choice]['name']
            character_image = list_all[choice]['image']
            status = list_all[choice]['status']
            origin = list_all[choice]['origin']['name']
            type = list_all[choice]['type'].lower()
            species = list_all[choice]['species'].lower()
            # Gets episode name, season, and number that the character is first seen in
            episode = list_all[choice]['episode']
            response = requests.get(episode[0])
            episode_name = response.json()['name']
            season_and_episode = response.json()['episode']

            # Prints character information for players
            print(f"Your character from Rick and Morty is {character}.")
            print(f"{character} is first seen in {episode_name} in {season_and_episode}.")
            if origin != "unknown":
                print(f'Their origin location is {origin}.')
            if len(species) > 0:
                print(f'Their species is {species}.')
            if len(type) > 0:
                print(f'The type of this character is {type}.')

            # Provides user with option to see a picture of character, if needed
            valid = True
            while valid:
                get_image = input("Do you need a refresher on what they look like? Y for yes, N for no\n")
                if get_image == 'N':
                    valid = False
                    continue
                elif get_image == 'Y':
                    print("Use the link to see the character:", character_image)
                    valid = False
                else:
                    print("That is not a valid response! Enter Y for yes, N for no\n")

            # Prompts user to state whether character is alive or dead and keeps track of score
            alive_or_dead = input("Is this character alive or dead?\n").lower()
            if alive_or_dead == "dead" and status == "Dead":
                points +=1
            elif alive_or_dead == "alive" and status == "Alive":
                points +=1
            else:
                dict_errors[character] = status
            
        # Score breakdown
        if points == 0:
            print("Who is Rick, anyway? Your score was 0!")
            print(f"Here are the correct responses to the questions you missed:")
            errors(dict_errors)
        if 1 <= points <= 2:
            print(f"Could be worse, right? Your score was {points}.")
            print(f"Here are the correct responses to the questions you missed:")
            errors(dict_errors)
        if 3 <= points <= 4:
            print(f"Impressive indeed! Your score was {points}!")
            print(f"Here are the correct responses to the questions you missed:")
            errors(dict_errors)
        if points == 5:
            print("Woah! You're a Rick and Morty afficianado! You got all answers correct!")

    # Keep going?
        user_input = input("Press q or type 'quit' to quit. Press any other key to play another game.\n")
        if user_input == 'quit' or user_input == 'q':
            print("Thanks for playing!")
            break






