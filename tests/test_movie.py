import unittest
from movie import Movie


class TestMovie(unittest.TestCase):
    def test_init(self):
        movie_json = {
            "title": "The Shawshank Redemption",
            "id": 278,
            "release_date": "1994-09-23",
            "vote_average": 8.704,
            "box_office": 28341469,
            "budget": 25000000,
            "runtime": 142,
            "director": "Frank Darabont",
            "cast": [
                "Tim Robbins",
                "Morgan Freeman",
                "Bob Gunton",
                "William Sadler",
                "Clancy Brown",
                "Gil Bellows",
                "James Whitmore",
                "Mark Rolston",
                "Jeffrey DeMunn",
                "Larry Brandenburg",
                "Neil Giuntoli",
                "Brian Libby",
                "David Proval",
                "Joseph Ragno",
                "Jude Ciccolella",
                "Paul McCrane",
                "Renee Blaine",
                "Scott Mann",
                "John Horton",
                "Gordon Greene",
                "Alfonso Freeman",
                "V.J. Foster",
                "John E. Summers",
                "Frank Medrano",
                "Mack Miles",
                "Alan R. Kessler",
                "Morgan Lund",
                "Cornell Wallace",
                "Gary Lee Davis",
                "Neil Summers",
                "Ned Bellamy",
                "Joe Pecoraro",
                "Harold E. Cope Jr.",
                "Brian Delate",
                "Don McManus",
                "Donald Zinn",
                "Dorothy Silver",
                "Robert Haley",
                "Dana Snyder",
                "John D. Craig",
                "Ken Magee",
                "Eugene C. DePasquale",
                "Bill Bolender",
                "Ron Newell",
                "John R. Woodward",
                "Chuck Brauchler",
                "Dion Anderson",
                "Claire Slemmer",
                "James Kisicki",
                "Rohn Thomas",
                "Charlie Kearns",
                "Rob Reider",
                "Brian Brophy",
                "Paul Kennedy",
                "James Babson",
                "Dennis Baker",
                "Fred Culbertson",
                "Alonzo F. Jones",
                "Sergio Kato",
                "Gary A. Jones"
            ],
            "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
            "rating": 0
        }

        test_movie = Movie(movie_json)
        self.assertEqual(test_movie.title, "The Shawshank Redemption")
        self.assertEqual(test_movie.id, 278)
        self.assertEqual(test_movie.release_date, "1994-09-23")
        self.assertEqual(test_movie.runtime, 142)
        self.assertAlmostEquals(test_movie.vote_average, 8.704)
        self.assertEqual(test_movie.box_office, 28341469)
        self.assertEqual(test_movie.budget, 25000000)
        self.assertEqual(test_movie.director, "Frank Darabont")
        self.assertEqual("Tim Robbins" in test_movie.cast, True)
        self.assertEqual("Pepe Pecas" in test_movie.cast, False)
        self.assertEqual(str(test_movie), "The Shawshank Redemption by Frank Darabont (1994).")

    def test_profit(self):
        movie_json = {
            "title": "The Shawshank Redemption",
            "id": 278,
            "release_date": "1994-09-23",
            "vote_average": 8.704,
            "box_office": 28341469,
            "budget": 25000000,
            "runtime": 142,
            "director": "Frank Darabont",
            "cast": [
                "Tim Robbins",
                "Morgan Freeman",
                "Bob Gunton",
                "William Sadler",
                "Clancy Brown",
                "Gil Bellows",
                "James Whitmore",
                "Mark Rolston",
                "Jeffrey DeMunn",
                "Larry Brandenburg",
                "Neil Giuntoli",
                "Brian Libby",
                "David Proval",
                "Joseph Ragno",
                "Jude Ciccolella",
                "Paul McCrane",
                "Renee Blaine",
                "Scott Mann",
                "John Horton",
                "Gordon Greene",
                "Alfonso Freeman",
                "V.J. Foster",
                "John E. Summers",
                "Frank Medrano",
                "Mack Miles",
                "Alan R. Kessler",
                "Morgan Lund",
                "Cornell Wallace",
                "Gary Lee Davis",
                "Neil Summers",
                "Ned Bellamy",
                "Joe Pecoraro",
                "Harold E. Cope Jr.",
                "Brian Delate",
                "Don McManus",
                "Donald Zinn",
                "Dorothy Silver",
                "Robert Haley",
                "Dana Snyder",
                "John D. Craig",
                "Ken Magee",
                "Eugene C. DePasquale",
                "Bill Bolender",
                "Ron Newell",
                "John R. Woodward",
                "Chuck Brauchler",
                "Dion Anderson",
                "Claire Slemmer",
                "James Kisicki",
                "Rohn Thomas",
                "Charlie Kearns",
                "Rob Reider",
                "Brian Brophy",
                "Paul Kennedy",
                "James Babson",
                "Dennis Baker",
                "Fred Culbertson",
                "Alonzo F. Jones",
                "Sergio Kato",
                "Gary A. Jones"
            ],
            "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
            "rating": 0
        }

        test_movie = Movie(movie_json)
        self.assertAlmostEquals(test_movie.get_profit(), 3.341469)

    def test_days_since_release(self):
        movie_json = {
            "title": "The Shawshank Redemption",
            "id": 278,
            "release_date": "1994-09-23",
            "vote_average": 8.704,
            "box_office": 28341469,
            "budget": 25000000,
            "runtime": 142,
            "director": "Frank Darabont",
            "cast": [
                "Tim Robbins",
                "Morgan Freeman",
                "Bob Gunton",
                "William Sadler",
                "Clancy Brown",
                "Gil Bellows",
                "James Whitmore",
                "Mark Rolston",
                "Jeffrey DeMunn",
                "Larry Brandenburg",
                "Neil Giuntoli",
                "Brian Libby",
                "David Proval",
                "Joseph Ragno",
                "Jude Ciccolella",
                "Paul McCrane",
                "Renee Blaine",
                "Scott Mann",
                "John Horton",
                "Gordon Greene",
                "Alfonso Freeman",
                "V.J. Foster",
                "John E. Summers",
                "Frank Medrano",
                "Mack Miles",
                "Alan R. Kessler",
                "Morgan Lund",
                "Cornell Wallace",
                "Gary Lee Davis",
                "Neil Summers",
                "Ned Bellamy",
                "Joe Pecoraro",
                "Harold E. Cope Jr.",
                "Brian Delate",
                "Don McManus",
                "Donald Zinn",
                "Dorothy Silver",
                "Robert Haley",
                "Dana Snyder",
                "John D. Craig",
                "Ken Magee",
                "Eugene C. DePasquale",
                "Bill Bolender",
                "Ron Newell",
                "John R. Woodward",
                "Chuck Brauchler",
                "Dion Anderson",
                "Claire Slemmer",
                "James Kisicki",
                "Rohn Thomas",
                "Charlie Kearns",
                "Rob Reider",
                "Brian Brophy",
                "Paul Kennedy",
                "James Babson",
                "Dennis Baker",
                "Fred Culbertson",
                "Alonzo F. Jones",
                "Sergio Kato",
                "Gary A. Jones"
            ],
            "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
            "rating": 0
        }

        test_movie = Movie(movie_json)
        self.assertEqual(test_movie.days_since_release(), 10755)

    def test_str_method(self):
        movie_json = {
            "title": "The Shawshank Redemption",
            "id": 278,
            "release_date": "1994-09-23",
            "vote_average": 8.704,
            "box_office": 28341469,
            "budget": 25000000,
            "runtime": 142,
            "director": "Frank Darabont",
            "cast": [
                "Tim Robbins",
                "Morgan Freeman",
                "Bob Gunton",
                "William Sadler",
                "Clancy Brown",
                "Gil Bellows",
                "James Whitmore",
                "Mark Rolston",
                "Jeffrey DeMunn",
                "Larry Brandenburg",
                "Neil Giuntoli",
                "Brian Libby",
                "David Proval",
                "Joseph Ragno",
                "Jude Ciccolella",
                "Paul McCrane",
                "Renee Blaine",
                "Scott Mann",
                "John Horton",
                "Gordon Greene",
                "Alfonso Freeman",
                "V.J. Foster",
                "John E. Summers",
                "Frank Medrano",
                "Mack Miles",
                "Alan R. Kessler",
                "Morgan Lund",
                "Cornell Wallace",
                "Gary Lee Davis",
                "Neil Summers",
                "Ned Bellamy",
                "Joe Pecoraro",
                "Harold E. Cope Jr.",
                "Brian Delate",
                "Don McManus",
                "Donald Zinn",
                "Dorothy Silver",
                "Robert Haley",
                "Dana Snyder",
                "John D. Craig",
                "Ken Magee",
                "Eugene C. DePasquale",
                "Bill Bolender",
                "Ron Newell",
                "John R. Woodward",
                "Chuck Brauchler",
                "Dion Anderson",
                "Claire Slemmer",
                "James Kisicki",
                "Rohn Thomas",
                "Charlie Kearns",
                "Rob Reider",
                "Brian Brophy",
                "Paul Kennedy",
                "James Babson",
                "Dennis Baker",
                "Fred Culbertson",
                "Alonzo F. Jones",
                "Sergio Kato",
                "Gary A. Jones"
            ],
            "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
            "rating": 0
        }
        movie = Movie(movie_json)
        self.assertEqual(str(movie), "The Shawshank Redemption by Frank Darabont (1994).")
