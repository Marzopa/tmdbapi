import unittest
import json
from movie_collection import MovieCollection


class TestMovieCollection(unittest.TestCase):
    def test_most_expensive_movie(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:5])
            self.assertEqual(test_collection.most_expensive_movie().id, 278)
            test_collection = MovieCollection(json_object[1:5])
            self.assertEqual(test_collection.most_expensive_movie().id, 424)

    def test_least_expensive_movie(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:5])
            self.assertEqual(test_collection.least_expensive_movie().id, 238)
            test_collection = MovieCollection(json_object[2:6])
            self.assertEqual(test_collection.least_expensive_movie().id, 389)

    def test_get_revenues_in_millions(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:5])
            revenues = test_collection.get_revenues_in_millions()
            revenues2 = [28.341469, 245.066411, 102.600000, 321.365567, 274.925095]
            for i in range(len(revenues)):
                self.assertAlmostEqual(revenues2[i], revenues[i])

    def test_get_directors(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:6])
            director_dict = test_collection.get_directors(3)
            self.assertEqual(len(director_dict), 0)
            director_dict = test_collection.get_directors()
            self.assertEqual(len(director_dict), 5)
            self.assertEqual(director_dict["Francis Ford Coppola"], 2)
            self.assertEqual(director_dict["Hayao Miyazaki"], 1)
            director_dict = test_collection.get_directors(2)
            self.assertEqual(len(director_dict), 1)
            self.assertEqual(director_dict["Francis Ford Coppola"], 2)
            with self.assertRaises(KeyError):
                wrong = director_dict["Hayao Miyazaki"]

    def test_get_actors(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:5])
            actor_dict = test_collection.get_actors()
            self.assertEqual(actor_dict['Al Pacino'], 2)
            self.assertEqual(actor_dict['Morgan Freeman'], 1)
            with self.assertRaises(KeyError):
                wrong = actor_dict["Oscar Jimenez"]

    def test_str_method(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:25])
            self.assertEqual(str(test_collection), "A collection of 25 movies.")

    def test_order_movies_by_date(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:5])
            ordered_movies = test_collection.order_movies_by_date()
            self.assertEqual(ordered_movies[0].title, "12 Angry Men")
            self.assertEqual(ordered_movies[4].title, "The Shawshank Redemption")
            self.assertEqual(len(ordered_movies), 5)

            test_collection = MovieCollection(json_object[5:10])
            ordered_movies = test_collection.order_movies_by_date()
            for movie in ordered_movies:
                print(movie, end="\t")
            self.assertEqual(len(ordered_movies), 5)
            self.assertEqual(ordered_movies[0].title, "Dilwale Dulhania Le Jayenge")
            self.assertEqual(ordered_movies[1].title, "The Green Mile")
            self.assertEqual(ordered_movies[2].title, "Spirited Away")
            self.assertEqual(ordered_movies[3].title, "The Dark Knight")
            self.assertEqual(ordered_movies[4].title, "Parasite")

    def test_get_movies_by_year(self):
        with open("best_rated_list.json", "r") as file_json:
            json_object = json.load(file_json)
            test_collection = MovieCollection(json_object[:12])
            movies_by_year = test_collection.get_movies_by_year()
            self.assertEqual(movies_by_year[1994], 2)
            self.assertEqual(movies_by_year[2019], 1)
            self.assertEqual(len(movies_by_year), 11)
            print(movies_by_year)
