import requests

from movie import Movie


def best_rated_list(number):
    """
    :param number: number of movies to look at from the list
    :return: a list of movie dictionaries
    """
    if number <= 0:
        raise ValueError('Number of movies must be positive!')
    movies = []
    i = 1
    while len(movies) < number:
        response = get_request("https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=" + str(i))
        # print(json.dumps(response, indent=4))
        temp_list = response['results']
        for movie_dict in temp_list:
            movies.append(get_movie_info(movie_dict['id']))
        i += 1
    return movies[:number]


def popular_list(number):
    """
    :param number: number of movies to look at from the list
    :return: a list of movie dictionaries
    """
    if number <= 0:
        raise ValueError('Number of movies must be positive!')
    movies = []
    i = 1
    while len(movies) < number:
        response = get_request("https://api.themoviedb.org/3/movie/popular?language=en-US&page=" + str(i))
        # print(json.dumps(response, indent=4))
        temp_list = response['results']
        for movie_dict in temp_list:
            movies.append(get_movie_info(movie_dict['id']))
        i += 1
    return movies[:number]


def get_movies_from_tmdb_list(list_id=8292727):
    """
    :param list_id: TMdB id of list to fetch from (GUI doesn't have an option to edit, so a sample default parameter was
    set)
    :return: a list of movie dictionaries
    """
    movies = []
    i = 1
    number = 1
    while len(movies) < number:
        response = get_request("https://api.themoviedb.org/3/list/" + str(list_id) + "?language=en-US&page=" + str(i))
        # print(json.dumps(response, indent=4))
        temp_list = response['items']
        number = response['total_results']
        for movie_dict in temp_list:
            movies.append(get_movie_info(movie_dict['id']))
        i += 1
    return movies


def trending_list(number):
    """
    :param number: number of movies to look at from the list
    :return: a list of movie dictionaries
    """
    if number <= 0:
        raise ValueError('Number of movies must be positive!')
    movies = []
    i = 1
    while len(movies) < number:
        response = get_request("https://api.themoviedb.org/3/trending/movie/week?language=en-US")
        # print(json.dumps(response, indent=4))
        temp_list = response['results']
        for movie_dict in temp_list:
            movies.append(get_movie_info(movie_dict['id']))
        i += 1
    return movies[:number]


def user_rated_list(acct_id=21033804):
    """
    :param acct_id: id of TMdB account (has to be mine because the way the API works)
    :return: a list of movie dictionaries
    """
    movies = []
    i = 1
    number = 1
    while len(movies) < number:
        response = get_request("https://api.themoviedb.org/3/account/" + str(acct_id) +
                               "/rated/movies?language=en-US&page=" + str(i) + "&sort_by=created_at.asc")
        # print(json.dumps(response, indent=4))
        temp_list = response['results']
        number = response['total_results']
        for movie_dict in temp_list:
            mini_dict = get_movie_info(movie_dict['id'])
            mini_dict['rating'] = movie_dict['rating']
            movies.append(mini_dict)
        i += 1
    return movies


def get_request(url):
    """
    :param url: the url to search API
    :return: a python object containing the request
    """
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDE0MDY3MWVjYjkwNzlkYTBlNTA0MjBjNjFhMGU3YyIsInN" +
                         "1YiI6IjY1ZGQ1NWFlZGNiNmEzMDE4NTg1YzRlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ" +
                         ".NgU2C0hLdcP3gz_BWDPnx8qzR8wAQiKntxj987SIM7M"
    }

    response = requests.get(url, headers=headers)

    return response.json()


def get_movie_info(movie_id):
    """
    :param movie_id: TMdB id of the movie
    :return: a movie dictionary representing the movie
    """
    if type(movie_id) is not int:
        raise TypeError("movie_id must be an integer")

    movie_dict = {}
    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?language=en-US"
    response = get_request(url)

    movie_dict['title'] = response['title']
    movie_dict['id'] = movie_id
    movie_dict['release_date'] = response['release_date']
    movie_dict['vote_average'] = response['vote_average']
    movie_dict['box_office'] = response['revenue']
    movie_dict['budget'] = response['budget']
    movie_dict['runtime'] = response['runtime']
    movie_dict['poster_path'] = response['poster_path']

    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/credits?language=en-US"
    response = get_request(url)
    for person in response['crew']:
        if person['job'] == "Director":
            movie_dict['director'] = person['name']
            break
    movie_dict['cast'] = []
    for person in response['cast']:
        movie_dict['cast'].append(person['name'])

    return movie_dict


def movie_prediction(movie_collection):
    """
    :param movie_collection: an object of the MovieCollection class
    :return: a Movie object with the recommended movie
    """
    year_dict = movie_collection.get_movies_by_year()
    most_popular_year = max(year_dict, key=year_dict.get)
    median_runtime = movie_collection.get_median_runtime()
    titles = movie_collection.get_movie_titles()
    i = 1
    while True:
        url = ("https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=" +
               str(i) + "&sort_by=vote_count.desc&vote_average.gte=7.5&with_watch_providers=Netflix&with_runtime.gte=" +
               str(median_runtime-30) + "&with_runtime.lte=" + str(median_runtime+30) + "&primary_release_date.lte=" +
               str(most_popular_year+2) + "-01-01&primary_release_date.gte=" + str(most_popular_year-2) + "-12-31")
        response = get_request(url)
        for movie in response['results']:
            if movie['title'] not in titles:
                return Movie(get_movie_info(movie['id']))
        i += 1
