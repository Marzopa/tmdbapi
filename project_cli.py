import tmdb_functions
from movie_collection import MovieCollection
import json
import datetime
import data_functions


def start():
    """
    :return: a movie collection to apply data functions to
    """
    print("TMdB API manipulation")
    while True:
        option = input("Enter F to load from a file, G to generate from TMdB API, or X to exit the program: ").lower()
        if option == "f":
            while True:
                filename = input("Enter name of file to load: ")
                try:
                    file = open(filename, "r")
                    json_object = json.load(file)
                    file.close()
                    movie_collection = MovieCollection(json_object)
                    return movie_collection
                except FileNotFoundError:
                    print("Invalid File")
        elif option == 'g':
            return generate_list_options()
        elif option == 'x':
            quit()
        else:
            print("Invalid input")


def get_valid_number():
    """
    makes sure user input is a valid number
    :return: the number of movies from list you want to request from API
    """
    number = input("Enter the number of movies you want from the list: ")
    while type(number) is not int or int(number) <= 0:
        try:
            number = int(number)
            if number <= 0:
                number = int(input("Number must be positive: "))
        except ValueError:
            number = input("Number is not an integer, try again: ")

    return number


def print_tmdb_commands():
    print("Available commands:")
    print("1. Get best rated TMdB movies (B)")
    print("2. Get most popular TMdB movies (P)")
    print("3. Get movies from TMdB list (L)")
    print("4. Get rated movies from TMdB account (R)")
    print("5. Get trending movies on TMdB (T)")
    print("Exit program (X)")


def generate_list_options():
    """
    provides options to generate different movie collections from API
    :return: a movie collection made from TMdB API
    """
    print("\nGenerate movies from TMdB")
    while True:
        option = input("Select a command, or type 'H' for a list of commands: ").lower()
        if option == "1" or option == "b":
            number = get_valid_number()
            print(f"Fetching first {number} best rated TMdB movies...")
            movie_collection = MovieCollection(tmdb_functions.best_rated_list(number))
            return movie_collection
        elif option == "2" or option == "p":
            number = get_valid_number()
            print(f"Fetching first {number} most popular TMdB movies right now...")
            movie_collection = MovieCollection(tmdb_functions.popular_list(number))
            return movie_collection
        elif option == "3" or option == "l":
            list_id = input("Please enter the TMdB list ID: ")
            print(f"Fetching movies from list {list_id}...")
            movie_collection = MovieCollection(tmdb_functions.get_movies_from_tmdb_list(list_id))
            return movie_collection
        elif option == "4" or option == "r":
            acct_id = 21033804
            print(f"Fetching rated movies by account {acct_id}...")
            movie_collection = MovieCollection(tmdb_functions.user_rated_list(acct_id))
            return movie_collection
        elif option == "5" or option == "t":
            number = get_valid_number()
            print(f"Fetching first {number} trending TMdB movies right now...")
            movie_collection = MovieCollection(tmdb_functions.trending_list(number))
            return movie_collection
        elif option == 'h':
            print_tmdb_commands()
        elif option == 'x':
            quit()
        else:
            print("Invalid option!")


def save_movie_collection(movie_collection):
    """
    :param movie_collection: a MovieCollection object
    """
    filename = "saved_collections/" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + "_movie_collection.json"
    print(f"Saving movie collection to {filename}...")
    collection_dict = movie_collection.__dict__
    out_list = []
    for movie in collection_dict['movie_list']:
        out_list.append(movie.__dict__)
    for movie in collection_dict['excluded_movies']:
        out_list.append(movie.__dict__)

    with open(filename, 'w') as outfile:
        json.dump(out_list, outfile, indent=4)


def print_data_commands():
    print("Available commands:")
    print("1. Plot user rating against TMdB rating (R)")
    print("2. Plot budget against TMdB rating (B)")
    print("3. Graph distribution of directors (D)")
    print("4. Graph distribution of actors (A)")
    print("5. Plot TMdD rating against profit (P)")
    print("6. Order movies from oldest to newest (N)")
    print("7. Plot runtime against age of the movie (T)")
    print("8. Graph distribution of movies by year (Y)")
    print("9. Get a recommended movie (M)")
    print("Return to main menu (X)")


def data_visualization_options(movie_collection):
    """
    provides option to visualize data from a movie collection
    :param movie_collection: a movie collection object
    """
    print("\nData visualization options")
    while True:
        option = input("Select a command, or type 'H' for a list of commands: ").lower()
        if option == "1" or option == "r":
            data_functions.user_rating_against_tmdb_rating(movie_collection)
        elif option == "2" or option == "b":
            data_functions.rating_against_budget(movie_collection)
        elif option == "3" or option == "d":
            data_functions.director_distribution(movie_collection)
        elif option == "4" or option == "a":
            data_functions.actor_distribution(movie_collection)
        elif option == "5" or option == "p":
            data_functions.rating_against_profit(movie_collection)
        elif option == "6" or option == "n":
            data_functions.order_movies_by_date(movie_collection)
        elif option == "7" or option == "t":
            data_functions.runtime_against_age(movie_collection)
        elif option == "8" or option == "y":
            data_functions.distribution_by_year(movie_collection)
        elif option == "9" or option == "m":
            print(f"You should watch {tmdb_functions.movie_prediction(movie_collection)}")
        elif option == 'h':
            print_data_commands()
        elif option == 'x':
            print()
            break
        else:
            print("Invalid option!")


def main():
    while True:
        movie_collection = start()
        save_file = input("Do you want to save this movie collection to a file? (Y/N): ").lower()
        if save_file == "y":
            save_movie_collection(movie_collection)
        data_visualization_options(movie_collection)


if __name__ == "__main__":
    main()
