from movie import Movie


class MovieCollection:
    def __init__(self, movie_list):
        """
        :param movie_list: a python list of movie dictionaries
        """
        self.movie_list = []
        self.budgets = []
        self.revenues = []
        self.tmdb_ratings = []
        self.user_ratings = []
        self.profits = []
        self.runtimes = []
        self.excluded_movies = []
        for movie in movie_list:
            movie_object = Movie(movie)
            if movie_object.budget > 0 and movie_object.box_office > 0:
                # Some movies are registered with a budget or box_office of 0,
                # and we want to exclude them from the comparisons
                self.movie_list.append(movie_object)
                self.budgets.append(movie_object.budget)
                self.revenues.append(movie_object.box_office)
                self.tmdb_ratings.append(movie_object.vote_average)
                self.user_ratings.append(movie_object.rating)
                self.profits.append(movie_object.get_profit())
                self.runtimes.append(movie_object.runtime)
            else:
                self.excluded_movies.append(movie_object)

        if len(self.excluded_movies) != 0:
            print(f"Excluded {len(self.excluded_movies)} movies because they didn't have any budgets or box offices.")

        if len(movie_list) == 0:
            raise ValueError("No movies found!")

    def most_expensive_movie(self):
        """
        :return: a Movie object with the highest box office (excluding the excluded movies)
        """
        budget = 0
        expensive = None
        for movie in self.movie_list:
            if movie.budget > budget:
                expensive = movie
                budget = movie.budget
        return expensive

    def least_expensive_movie(self):
        """
        :return: a Movie object with the lowest box office (excluding the excluded movies)
        """
        budget = float('inf')
        expensive = None
        for movie in self.movie_list:
            if budget > movie.budget > 0:
                expensive = movie
                budget = movie.budget
        return expensive

    def most_profitable_movie(self):
        """
        :return: a Movie object with the highest profit (excluding the excluded movies)
        """
        profit = 0
        profitable = None
        for movie in self.movie_list:
            movie_profit = movie.get_profit()
            if movie_profit > profit:
                profitable = movie
                profit = movie_profit
        return profitable

    def least_profitable_movie(self):
        """
        :return: a Movie object with the lowest profit (excluding the excluded movies)
        """
        profit = float('inf')
        profitable = None
        for movie in self.movie_list:
            movie_profit = movie.get_profit()
            if profit > movie_profit:
                profitable = movie
                profit = movie_profit
        return profitable

    def best_rated_movie(self):
        """
        :return: a Movie object with the highest TMdB rating (excluding the excluded movies)
        """
        best_rating = 0
        best_movie = None
        for movie in self.movie_list:
            if movie.vote_average > best_rating:
                best_movie = movie
                best_rating = movie.vote_average
        return best_movie

    def worst_rated_movie(self):
        """
        :return: a Movie object with the lowest TMdB rating (excluding the excluded movies)
        """
        worst_rating = 11
        worst_movie = None
        for movie in self.movie_list:
            if movie.vote_average < worst_rating:
                worst_movie = movie
                worst_rating = movie.vote_average
        return worst_movie

    def best_rated_user_movie(self):
        """
        :return: a Movie object with the highest user rating (excluding the excluded movies)
        :raises ValueError: if there are no movies with user rating in collection (not generated using the appropriate
        TMdB command)
        """
        best_rating = 0
        best_movie = None
        for movie in self.movie_list:
            if movie.rating > best_rating:
                best_movie = movie
                best_rating = movie.rating
        if best_movie is None:
            raise ValueError("No movie with user rating in collection")
        else:
            return best_movie

    def worst_rated_user_movie(self):
        """
        :return: a Movie object with the least user rating (excluding the excluded movies)
        :raises ValueError: if there are no movies with user rating in collection (not generated using the appropriate
        TMdB command)
        """
        worst_rating = 11
        worst_movie = None
        for movie in self.movie_list:
            if 0 < movie.rating < worst_rating:
                worst_movie = movie
                worst_rating = movie.rating
        if worst_movie is None:
            raise ValueError("No movie with user rating in collection")
        else:
            return worst_movie

    def longest_movie(self):
        """
        :return: a Movie object with the longest runtime (including the excluded movies)
        """
        longest_runtime = 0
        longest_movie = None
        for movie in self.movie_list:
            if movie.runtime > longest_runtime:
                longest_movie = movie
                longest_runtime = movie.runtime
        for movie in self.excluded_movies:
            if movie.runtime > longest_runtime:
                longest_movie = movie
                longest_runtime = movie.runtime
        return longest_movie

    def shortest_movie(self):
        """
        :return: a Movie object with the shortest runtime (including the excluded movies)
        """
        shortest_runtime = float("inf")
        shortest_movie = None
        for movie in self.movie_list:
            if movie.runtime < shortest_runtime:
                shortest_movie = movie
                shortest_runtime = movie.runtime
        for movie in self.excluded_movies:
            if movie.runtime < shortest_runtime:
                shortest_movie = movie
                shortest_runtime = movie.runtime
        return shortest_movie

    def get_budgets_in_millions(self):
        """
        :return: a list of the budgets of the movies (excluding the excluded movies)
        """
        new_budgets = []
        for budget in self.budgets:
            new_budgets.append(budget/1000000)
        return new_budgets

    def get_revenues_in_millions(self):
        """
        :return: a list of the revenues of the movies (excludes excluded_movies)
        """
        new_revenues = []
        for revenue in self.revenues:
            new_revenues.append(revenue/1000000)
        return new_revenues

    def get_directors(self, threshold=0):
        """
        :param threshold: minimum value to consider director
        :return: a list of directors above threshold (including the excluded movies)
        """
        director_dict = {}
        for movie in self.movie_list:
            if movie.director in director_dict:
                director_dict[movie.director] += 1
            else:
                director_dict[movie.director] = 1

        for movie in self.excluded_movies:
            if movie.director in director_dict:
                director_dict[movie.director] += 1
            else:
                director_dict[movie.director] = 1

        final_dict = {}
        for director in director_dict:
            if director_dict[director] >= threshold:
                final_dict[director] = director_dict[director]

        return final_dict

    def get_actors(self, threshold=0):
        """
        :param threshold: minimum value to consider actor
        :return: a list of actors above threshold (including the excluded movies)
        """
        actor_dict = {}
        for movie in self.movie_list:
            for actor in movie.cast:
                if actor in actor_dict:
                    actor_dict[actor] += 1
                else:
                    actor_dict[actor] = 1

        for movie in self.excluded_movies:
            for actor in movie.cast:
                if actor in actor_dict:
                    actor_dict[actor] += 1
                else:
                    actor_dict[actor] = 1

        final_dict = {}
        for actor in actor_dict:
            if actor_dict[actor] >= threshold:
                final_dict[actor] = actor_dict[actor]

        return final_dict

    def get_ages_in_years(self):
        """
        :return: a list of ages in years of movies (including the excluded movies)
        """
        ages = []
        for movie in self.movie_list:
            age = movie.days_since_release()/365
            ages.append(age)
        for movie in self.excluded_movies:
            age = movie.days_since_release()/365
            ages.append(age)
        return ages

    def get_excluded_runtimes(self):
        """
        :return: a list of all runtimes (including the excluded movies)
        """
        runtimes = self.runtimes
        for movie in self.excluded_movies:
            runtimes.append(movie.runtime)
        return runtimes

    def order_movies_by_date(self):
        """
        :return: the ordered list of Movie objects (including the excluded movies)
        """
        ordered_list = [self.movie_list[0]]
        # will raise index error if movie_list[1] doesn't exist, that's why this if statement. and because of error
        # raised by the innit method we know collection cannot be empty
        if len(self.movie_list) == 1:
            return ordered_list

        for movie in self.movie_list[1:]:
            movie_days = movie.days_since_release()
            flag = True
            for i in range(len(ordered_list)):
                if ordered_list[i].days_since_release() <= movie_days:
                    ordered_list.insert(i, movie)
                    flag = False
                    break
            # checks if movie was added to list, and if it wasn't append it at the end
            if flag:
                ordered_list.append(movie)

        for movie in self.excluded_movies:
            movie_days = movie.days_since_release()
            flag = True
            for i in range(len(ordered_list)):
                if ordered_list[i].days_since_release() <= movie_days:
                    ordered_list.insert(i, movie)
                    flag = False
                    break
            # checks if movie was added to list, and if it wasn't append it at the end
            if flag:
                ordered_list.append(movie)

        return ordered_list

    def get_movies_by_year(self):
        """
        :return: a dictionary with keys being a year and values being number of movies for that year
        (including the excluded movies)
        """
        year_dict = {}
        for movie in self.movie_list:
            year = movie.get_movie_year()
            if year in year_dict:
                year_dict[year] += 1
            else:
                year_dict[year] = 1

        for movie in self.excluded_movies:
            year = movie.get_movie_year()
            if year in year_dict:
                year_dict[year] += 1
            else:
                year_dict[year] = 1

        return dict(sorted(year_dict.items()))

    def __str__(self):
        return f"A collection of {len(self.movie_list) + len(self.excluded_movies)} movies."
