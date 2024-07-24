import unittest
import tmdb_functions
import json
from movie_collection import MovieCollection


class TestImdbFunctions(unittest.TestCase):
    def test_get_movie_info(self):
        with self.assertRaises(TypeError):
            tmdb_functions.get_movie_info('hello')

        with open("best_rated_list.json", "r") as file:
            best_rated_list = json.load(file)
            shawshank_dict = best_rated_list[0]
            self.assertEqual(tmdb_functions.get_movie_info(278), shawshank_dict)

    def test_best_rated_list(self):
        movie_list = tmdb_functions.best_rated_list(6)
        self.assertEqual(len(movie_list), 6)
        self.assertEqual(movie_list[0]["title"], "The Shawshank Redemption")
        self.assertEqual(movie_list[0]["director"], "Frank Darabont")
        self.assertEqual(movie_list[0]["box_office"], 28341469)
        self.assertEqual(movie_list[1]["title"], "The Godfather")

        movie_list = tmdb_functions.best_rated_list(1)
        self.assertEqual(len(movie_list), 1)
        self.assertEqual(movie_list[0]["title"], "The Shawshank Redemption")

        with self.assertRaises(ValueError):
            tmdb_functions.best_rated_list(0)

        movie_list = tmdb_functions.best_rated_list(25)
        self.assertEqual(len(movie_list), 25)
        self.assertEqual(movie_list[24]["title"], "Psycho")

        with open("best_rated_list.json", "r") as json_file:
            json_object = json.load(json_file)
            movie_collection = MovieCollection(json_object)
            self.assertEqual(len(movie_collection.movie_list) + len(movie_collection.excluded_movies), 100)
            self.assertEqual(movie_collection.movie_list[3].title, "Schindler's List")

    def test_popular_list(self):
        movie_list = tmdb_functions.popular_list(6)
        self.assertEqual(len(movie_list), 6)
        self.assertEqual(movie_list[0]["title"], "No Way Up")
        self.assertEqual(movie_list[0]["director"], "Claudio Fäh")

        movie_list = tmdb_functions.popular_list(1)
        self.assertEqual(len(movie_list), 1)
        self.assertEqual(movie_list[0]["title"], "No Way Up")

        with self.assertRaises(ValueError):
            tmdb_functions.popular_list(0)

    def test_user_rated_list(self):
        acct_id = 21033804
        movie_list = tmdb_functions.user_rated_list(acct_id)
        self.assertEqual(len(movie_list), 104)
        self.assertEqual(movie_list[0]['title'], "Top Gun: Maverick")
        self.assertEqual(movie_list[0]["rating"], 7)
        self.assertEqual(movie_list[1]['title'], "Up")
        self.assertEqual(movie_list[1]["rating"], 8)

    def test_get_movies_from_tmdb_list(self):
        list_id = 8292727
        movie_list = tmdb_functions.get_movies_from_tmdb_list(list_id)
        self.assertEqual(len(movie_list), 5)
        self.assertEqual(movie_list[0]['title'], "V for Vendetta")
        self.assertEqual(movie_list[2]['director'], "Pete Docter")

    def test_movie_prediction(self):
        with open("oscar_rated.json", "r") as json_file:
            json_object = json.load(json_file)
            movie_collection = MovieCollection(json_object)
            movie_prediction = tmdb_functions.movie_prediction(movie_collection)
            print(movie_prediction)
            self.assertFalse(movie_prediction.title in movie_collection.get_movie_titles())
