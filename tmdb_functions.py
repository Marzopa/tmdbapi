import requests


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


def get_movies_from_tmdb_list(list_id):
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


def user_rated_list(acct_id):
    """
    :param acct_id: id of TMdB account
    :return: a list of lists, each containing [movie_dictionary, user_rating]
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

