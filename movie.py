from datetime import datetime


class Movie:
    def __init__(self, movie_json):
        """
        :param movie_json: a python dictionary representing the movie
        """
        self.id = movie_json['id']
        self.title = movie_json['title']
        self.release_date = movie_json['release_date']
        self.vote_average = movie_json['vote_average']
        self.runtime = movie_json['runtime']
        self.box_office = movie_json['box_office']
        self.budget = movie_json['budget']
        self.cast = movie_json['cast']
        self.director = movie_json['director']
        if 'rating' in movie_json:
            self.rating = movie_json['rating']
        else:
            self.rating = 0

    def get_profit(self):
        """
        :return: profit in millions
        """
        return (self.box_office - self.budget)/1000000

    def days_since_release(self):
        """
        :return: days since the release of the movie (integer)
        """
        given_date = self.release_date
        given_datetime = datetime.strptime(given_date, '%Y-%m-%d')
        current_datetime = datetime.now()
        days_passed = (current_datetime - given_datetime).days
        return days_passed

    def get_movie_year(self):
        """
        :return: the year the movie was released (integer)
        """
        return int(self.release_date[:4])

    def __str__(self):
        return f"{self.title} by {self.director} ({self.get_movie_year()})."

