import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

if __name__ == "__main__":

    # Empty list to contain character data of all pages
    total_results = []
    # Grabs search results of first page
    response = requests.get("https://rickandmortyapi.com/api/character")
    char_data = response.json()
    # Add data from first page to total results
    total_results = total_results + char_data['results']

    # Parse through all pages of data in API to update total_results with all character data
    while char_data['info']['next'] is not None:
        response = requests.get(char_data['info']['next'])
        char_data = response.json()
        total_results = total_results + char_data['results']

    # Game instructions, initializing variables
    user_input = ''
    points = 0
    print("Welcome to Dead or Alive: Rick and Morty Version.")
    print("In this game, you will choose a character from Rick and Morty.")
    print("Then, you will decide if that character is alive, dead, or unknown.")
    print("If you need a picture to reference the character, you will have the option to request an image of them.")
    print("Each correct guess is worth 1 point. Incorrect guesses are awarded no points. Good luck!")
    print()

    # While loop to continue game until 'q' or 'quit' are entered
    while user_input != 'q' or user_input != 'quit':

        # Asks users for a number to determine which character they get
        valid = True
        while valid:
            choice = int(input("Choose a number between 0 and 825.\n"))
            if (0 <= choice <= 825):
                valid = False
            else:
                print("Invalid number. Choose a number between 0 and 825.")

        # Stores parsed data from API in variables
        character = total_results[choice]['name']
        character_image = total_results[choice]['image']
        status = total_results[choice]['status']
        origin = total_results[choice]['origin']['name']
        type = total_results[choice]['type'].lower()
        species = total_results[choice]['species'].lower()
        episode = total_results[choice]['episode']
        response = requests.get(episode[0])
        episode_name = response.json()['name']
        

        print(f"Your character from Rick and Morty is {character}.")
        print(f"{character} is first seen in {episode_name}.")
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
                print("Good memory! Moving on...")
                valid = False
            elif get_image == 'Y':
                print("Click the link to see the character:", character_image)
                valid = False
            else:
                print("That is not a valid response! Enter Y for yes, N for no\n")

        # Prompts user to state whether character is alive, dead, or unknown, and keeps track of score
        alive_or_dead = input("Is this character alive, dead, or unknown?\n")
        if (alive_or_dead == "Dead" or alive_or_dead == "dead") and status == "Dead":
            points +=1
            print(f'Correct! Your score is now {points}.')
        elif (alive_or_dead == "Alive" or alive_or_dead == "alive") and status == "Alive":
            points +=1
            print(f'Correct! Your score is now {points}.')
        elif (alive_or_dead == "Unknown" or alive_or_dead == "unknown") and status == "unknown":
            points +=1
            print(f'Correct! Your score is now {points}')
        else:
            print(f"Sorry, that's not correct. The correct answer was '{status}.'")

        # Keep going?
        user_input = input("Press q or type 'quit' to quit. Press any other key to keep going.\n")
        if user_input == 'quit' or user_input == 'q':
            if points == 1:
                print("Thanks for playing! You earned a total of 1 point.")
                break
            else:
                print(f"Thanks for playing! You earned a total of {points} points.")
                break







