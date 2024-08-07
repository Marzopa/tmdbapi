import matplotlib.pyplot as plt


def scatter_plot(x_label, values_x, y_label, values_y, title):
    """
    :param x_label: label for the x-axis
    :param values_x: values for the x-axis
    :param y_label: label for the y-axis
    :param values_y: values for the y-axis
    :param title: title for the graph
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(values_x, values_y, marker='o', color='r')
    plt.xlabel(x_label, fontweight='bold')
    plt.ylabel(y_label, fontweight='bold')
    plt.title(title, fontweight='bold', fontsize=24)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def html_scatter_plot(x_label, values_x, y_label, values_y, title):
    """
    :param x_label: label for the x-axis
    :param values_x: values for the x-axis
    :param y_label: label for the y-axis
    :param values_y: values for the y-axis
    :param title: title for the graph
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(values_x, values_y, marker='o', color='r')
    plt.xlabel(x_label, fontweight='bold')
    plt.ylabel(y_label, fontweight='bold')
    plt.title(title, fontweight='bold', fontsize=24)
    plt.grid(True)
    plt.tight_layout()
    # filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # plt.savefig(f"images/{filename}.png")
    plt.savefig(f"images/scatterplot.png")
    # html = f"<img src='images/{filename}.png' width='50%' height='50%'>"
    html = f"<img src='images/scatterplot.png' width='60%' height='50%'>"
    return html


def bar_plot(x_label, values_x, y_label, values_y, title):
    """
    :param x_label: label for the x-axis
    :param values_x: values for the x-axis
    :param y_label: label for the y-axis
    :param values_y: values for the y-axis
    :param title: title for the graph
    """
    plt.figure(figsize=(14, 6))
    plt.bar(values_x, values_y, align='center', color='mediumaquamarine')
    plt.xticks(rotation=90)
    plt.xlabel(x_label, fontweight='bold')
    plt.ylabel(y_label, fontweight='bold')
    plt.title(title, fontweight='bold', fontsize=24)
    plt.tight_layout()
    plt.show()


def html_bar_plot(x_label, values_x, y_label, values_y, title):
    """
    :param x_label: label for the x-axis
    :param values_x: values for the x-axis
    :param y_label: label for the y-axis
    :param values_y: values for the y-axis
    :param title: title for the graph
    """
    plt.figure(figsize=(14, 6))
    plt.bar(values_x, values_y, align='center', color='mediumaquamarine')
    plt.xticks(rotation=90)
    plt.xlabel(x_label, fontweight='bold')
    plt.ylabel(y_label, fontweight='bold')
    plt.title(title, fontweight='bold', fontsize=24)
    plt.tight_layout()
    # filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # plt.savefig(f"images/{filename}.png")
    plt.savefig(f"images/barplot.png")
    # html = f"<img src='images/{filename}.png' width='60%' height='50%'>"
    html = f"<img src='images/barplot.png' width='60%' height='50%'>"
    return html


def user_rating_against_tmdb_rating(collection):
    values_x = collection.tmdb_ratings
    values_y = collection.user_ratings

    # Deletes movies that don't have user rating
    indices_to_delete = []
    for i in range(len(values_y)):
        if values_y[i] <= 0:
            indices_to_delete.append(i)
    indices_to_delete = indices_to_delete[::-1]
    for i in indices_to_delete:
        del values_x[i]
        del values_y[i]

    best_user_movie = collection.best_rated_user_movie()
    print(f"Best rated movie by user is {best_user_movie.title}, rated with {best_user_movie.rating}"
          f" (TMdB average of {best_user_movie.vote_average})")

    worst_user_movie = collection.worst_rated_user_movie()
    print(f"Worst rated movie by user is {worst_user_movie.title}, rated with {worst_user_movie.rating}"
          f" (TMdB average of {worst_user_movie.vote_average})")

    print()

    best_rated_movie = collection.best_rated_movie()
    print(f"Best rated movie is {best_rated_movie.title}, with an average of {best_rated_movie.vote_average}"
          f" (user rating of {best_rated_movie.rating})")

    worst_rated_movie = collection.worst_rated_movie()
    print(f"Worst rated movie is {worst_rated_movie.title}, with an average of {worst_rated_movie.vote_average}"
          f" (user rating of {worst_rated_movie.rating})")

    scatter_plot('TMdB rating', values_x, 'User rating', values_y, 'User rating against TMdB rating')


def html_user_rating_against_tmdb_rating(collection):
    values_x = collection.tmdb_ratings
    values_y = collection.user_ratings

    # Deletes movies that don't have user rating
    indices_to_delete = []
    for i in range(len(values_y)):
        if values_y[i] <= 0:
            indices_to_delete.append(i)
    indices_to_delete = indices_to_delete[::-1]
    for i in indices_to_delete:
        del values_x[i]
        del values_y[i]

    best_user_movie = collection.best_rated_user_movie()
    best_user_movie_poster = best_user_movie.poster_path
    worst_user_movie = collection.worst_rated_user_movie()
    worst_user_movie_poster = worst_user_movie.poster_path

    best_rated_movie = collection.best_rated_movie()
    best_rated_movie_poster = best_rated_movie.poster_path
    worst_rated_movie = collection.worst_rated_movie()
    worst_rated_movie_poster = worst_rated_movie.poster_path

    html_page = html_scatter_plot('TMdB rating', values_x, 'User rating', values_y, 'User rating against TMdB rating')

    html_page += f"<br><br> <h3>User:</h3>"\
                 f"<p><img src='https://image.tmdb.org/t/p/original{best_user_movie_poster}' height='30%'>" \
                 f"  Best rated: {best_user_movie.title}, rated with {best_user_movie.rating}"\
                 f" (TMdB average of {best_user_movie.vote_average})</p>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{worst_user_movie_poster}' height='30%'>" \
                 f"  Worst rated: {worst_user_movie.title}, rated with {worst_user_movie.rating}"\
                 f" (TMdB average of {worst_user_movie.vote_average})</p>"

    html_page += f"<br><br> <h3>TMdB:</h3>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{best_rated_movie_poster}' height='30%'>" \
                 f"  Best rated: {best_rated_movie.title}, with an average of {best_rated_movie.vote_average}" \
                 f" (user rating of {best_rated_movie.rating})</p>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{worst_rated_movie_poster}' height='30%'>" \
                 f"  Worst rated: {worst_rated_movie.title}, with an average of {worst_rated_movie.vote_average}" \
                 f" (user rating of {worst_rated_movie.rating})</p>"

    return html_page


def rating_against_budget(collection):
    values_x = collection.tmdb_ratings
    values_y = collection.get_budgets_in_millions()

    most_expensive_movie = collection.most_expensive_movie()
    print(f"Most expensive movie is {most_expensive_movie.title}, with a budget of {most_expensive_movie.budget}"
          f" (average of {most_expensive_movie.vote_average})")

    least_expensive_movie = collection.least_expensive_movie()
    print(f"Least expensive movie is {least_expensive_movie.title}, with a budget of {least_expensive_movie.budget}"
          f" (average of {least_expensive_movie.vote_average})")

    print()

    best_rated_movie = collection.best_rated_movie()
    print(f"Best rated movie is {best_rated_movie.title}, with a budget of {best_rated_movie.budget}"
          f" (average of {best_rated_movie.vote_average})")

    worst_rated_movie = collection.worst_rated_movie()
    print(f"Worst rated movie is {worst_rated_movie.title}, with a budget of {worst_rated_movie.budget}"
          f" (average of {worst_rated_movie.vote_average})")

    scatter_plot('TMdB rating', values_x, 'Budget (in millions)', values_y, 'Budget against rating')


def html_rating_against_budget(collection):
    values_x = collection.tmdb_ratings
    values_y = collection.get_budgets_in_millions()

    most_expensive_movie = collection.most_expensive_movie()
    most_expensive_movie_poster = most_expensive_movie.poster_path
    least_expensive_movie = collection.least_expensive_movie()
    least_expensive_movie_poster = least_expensive_movie.poster_path

    best_rated_movie = collection.best_rated_movie()
    best_rated_movie_poster = best_rated_movie.poster_path
    worst_rated_movie = collection.worst_rated_movie()
    worst_rated_movie_poster = worst_rated_movie.poster_path

    html_page = html_scatter_plot('TMdB rating', values_x, 'Budget (in millions)', values_y, 'Budget against rating')

    html_page += f"<br><br> <h3>By budget:</h3>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{most_expensive_movie_poster}' height='30%'>" \
                 f"  Most expensive: {most_expensive_movie.title}, with a budget of {most_expensive_movie.budget}" \
                 f" (TMdB average of {most_expensive_movie.vote_average})</p>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{least_expensive_movie_poster}' height='30%'>" \
                 f"  Least expensive: {least_expensive_movie.title}, with a budget of {least_expensive_movie.budget}" \
                 f" (TMdB average of {least_expensive_movie.vote_average})</p>"

    html_page += f"<br><br> <h3>By TMdB rating:</h3>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{best_rated_movie_poster}' height='30%'>" \
                 f"  Best rated: {best_rated_movie.title}, with an average of {best_rated_movie.vote_average}" \
                 f" (budget of {best_rated_movie.budget})</p>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{worst_rated_movie_poster}' height='30%'>" \
                 f"  Worst rated: {worst_rated_movie.title}, with an average of {worst_rated_movie.vote_average}" \
                 f" (budget of {worst_rated_movie.budget})</p>"

    return html_page


def director_distribution(collection):
    while True:
        director_threshold = input("Enter the minimum number of movies for a director to count: ")
        try:
            director_threshold = int(director_threshold)
            if director_threshold > 0:
                break
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Please enter a valid integer")

    director_dict = collection.get_directors(director_threshold)
    keys = list(director_dict.keys())
    values = list(director_dict.values())

    print(f"\nThere were {len(director_dict)} directors with at least {director_threshold} movies")

    bar_plot('Directors', keys, 'Number of movies', values, 'Director distribution')


def html_director_distribution(collection):
    director_threshold = 0
    while True:
        director_threshold += 1
        director_dict = collection.get_directors(director_threshold)
        if len(director_dict) <= 50:
            break

    keys = list(director_dict.keys())
    values = list(director_dict.values())

    html_page = html_bar_plot('Directors', keys, 'Number of movies', values, 'Director distribution')
    html_page += f"<br><br><h4>There were {len(director_dict)} directors with at least {director_threshold} movies</h4>"
    return html_page


def actor_distribution(collection):
    while True:
        actor_threshold = input("Enter the minimum number of movies for an actor to count: ")
        try:
            actor_threshold = int(actor_threshold)
            if actor_threshold >= 0:
                break
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Please enter a valid integer")

    actor_dict = collection.get_actors(actor_threshold)
    keys = list(actor_dict.keys())
    values = list(actor_dict.values())

    print(f"\nThere were {len(actor_dict)} actors with at least {actor_threshold} movies")

    bar_plot('Actors', keys, 'Number of movies', values, 'Actor distribution')


def html_actor_distribution(collection):
    actor_threshold = 0
    while True:
        actor_threshold += 1
        actor_dict = collection.get_actors(actor_threshold)
        if len(actor_dict) <= 50:
            break

    keys = list(actor_dict.keys())
    values = list(actor_dict.values())

    html_page = html_bar_plot('Actors', keys, 'Number of movies', values, 'Actor distribution')
    html_page += f"<br><br><h4>There were {len(actor_dict)} actors with at least {actor_threshold} movies</h4>"
    return html_page


def rating_against_profit(collection):
    values_x = collection.tmdb_ratings
    values_y = collection.profits

    most_profitable_movie = collection.most_profitable_movie()
    print(f"Most profitable movie is {most_profitable_movie.title}, with a profit of "
          f"{most_profitable_movie.get_profit()} millions (average of {most_profitable_movie.vote_average})")

    least_profitable_movie = collection.least_profitable_movie()
    print(f"Least profitable movie is {least_profitable_movie.title}, with a profit of "
          f"{least_profitable_movie.get_profit()} millions (average of {least_profitable_movie.vote_average})")

    print()

    best_rated_movie = collection.best_rated_movie()
    print(f"Best rated movie is {best_rated_movie.title}, with a profit of {best_rated_movie.get_profit()} millions"
          f" (average of {best_rated_movie.vote_average})")

    worst_rated_movie = collection.worst_rated_movie()
    print(f"Worst rated movie is {worst_rated_movie.title}, with a profit of {worst_rated_movie.get_profit()} millions"
          f" (average of {worst_rated_movie.vote_average})")

    scatter_plot('TMdB rating', values_x, 'Profit (in millions)', values_y, 'Profit against rating')


def html_rating_against_profit(collection):
    values_x = collection.tmdb_ratings
    values_y = collection.profits

    most_profitable_movie = collection.most_profitable_movie()
    most_profitable_movie_poster = most_profitable_movie.poster_path
    least_profitable_movie = collection.least_profitable_movie()
    least_profitable_movie_poster = least_profitable_movie.poster_path

    best_rated_movie = collection.best_rated_movie()
    best_rated_movie_poster = best_rated_movie.poster_path
    worst_rated_movie = collection.worst_rated_movie()
    worst_rated_movie_poster = worst_rated_movie.poster_path

    html_page = html_scatter_plot('TMdB rating', values_x, 'Profit', values_y, 'Profit against TMdB rating')

    html_page += f"<br><br> <h3>By profit:</h3>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{most_profitable_movie_poster}' height='30%'>" \
                 f"  Most profitable: {most_profitable_movie.title}, with a profit of {most_profitable_movie.get_profit()} millions" \
                 f" (TMdB average of {most_profitable_movie.vote_average})</p>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{least_profitable_movie_poster}' height='30%'>" \
                 f"  Least profitable: {least_profitable_movie.title}, with a profit of {least_profitable_movie.get_profit()} millions" \
                 f" (TMdB average of {least_profitable_movie.vote_average})</p>"

    html_page += f"<br><br> <h3>By TMdB rating:</h3>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{best_rated_movie_poster}' height='30%'>" \
                 f"  Best rated: {best_rated_movie.title}, with a profit of {best_rated_movie.get_profit()} millions" \
                 f" (TMdB average of {best_rated_movie.vote_average})</p>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{worst_rated_movie_poster}' height='30%'>" \
                 f"  Worst rated: {worst_rated_movie.title}, with a profit of {worst_rated_movie.get_profit()} millions" \
                 f" (TMdB average of {worst_rated_movie.vote_average})</p>"

    return html_page


def order_movies_by_date(collection):
    ordered_movies = collection.order_movies_by_date()
    print("\nOrdered list:")
    for movie_i in range(len(ordered_movies)):
        print(f"{movie_i+1}.- {ordered_movies[movie_i]}")


def html_order_movies_by_date(collection):
    ordered_movies = collection.order_movies_by_date()
    html_page = '<h3>Ordered list:</h3><ol>'
    for movie_i in range(len(ordered_movies)):
        html_page += f"<li>{ordered_movies[movie_i]}</li>"
    return html_page + "</ol>"


def runtime_against_age(collection):
    values_x = collection.get_ages_in_years()
    values_y = collection.get_excluded_runtimes()

    ordered_movies = collection.order_movies_by_date()
    print(f"Oldest movie is {ordered_movies[0].title} which is {ordered_movies[0].days_since_release()} days old today"
          f", and has a runtime of {ordered_movies[0].runtime} minutes"
          f" (TMdB average of {ordered_movies[0].vote_average})")

    print(f"Newest movie is {ordered_movies[-1].title} which is {ordered_movies[-1].days_since_release()} days old "
          f"today, and has a runtime of {ordered_movies[-1].runtime} minutes"
          f" (TMdB average of {ordered_movies[-1].vote_average})")

    print()

    longest_movie = collection.longest_movie()
    print(f"Longest movie is {longest_movie.title}, with a runtime of {longest_movie.runtime} minutes"
          f" ({longest_movie.days_since_release()} days old today)")

    shortest_movie = collection.shortest_movie()
    print(f"Shortest movie is {shortest_movie.title}, with a runtime of {shortest_movie.runtime} minutes"
          f" ({shortest_movie.days_since_release()} days old today)")

    scatter_plot('Movie age (in years)', values_x, 'Runtime (in minutes)', values_y, 'Runtime against age')


def html_runtime_against_age(collection):
    values_x = collection.get_ages_in_years()
    values_y = collection.get_excluded_runtimes()

    ordered_movies = collection.order_movies_by_date()

    longest_movie = collection.longest_movie()
    longest_movie_poster = longest_movie.poster_path
    shortest_movie = collection.shortest_movie()
    shortest_movie_poster = shortest_movie.poster_path

    html_page = html_scatter_plot('Movie age (in years)', values_x, 'Runtime (in minutes)', values_y, 'Runtime against age')

    html_page += f"<br><br> <h3>By movie age:</h3>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{ordered_movies[0].poster_path}' height='30%'>" \
                 f"  Oldest movie: {ordered_movies[0].title}, which is {ordered_movies[0].days_since_release()} days old today, " \
                 f"and has a runtime of {ordered_movies[0].runtime} minutes"\
                 f" (TMdB average of {ordered_movies[0].vote_average})</p>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{ordered_movies[-1].poster_path}' height='30%'>" \
                 f"  Newest movie: {ordered_movies[-1].title}, which is {ordered_movies[-1].days_since_release()} days old today, " \
                 f"and has a runtime of {ordered_movies[-1].runtime} minutes" \
                 f" (TMdB average of {ordered_movies[-1].vote_average})</p>"

    html_page += f"<br><br> <h3>By runtime:</h3>" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{longest_movie_poster}' height='30%'>" \
                 f"  Longest movie: {longest_movie.title}, with a runtime of {longest_movie.runtime} minutes " \
                 f"({longest_movie.days_since_release()} days old today)" \
                 f"<p><img src='https://image.tmdb.org/t/p/original{shortest_movie_poster}' height='30%'>" \
                 f"Shortest movie: {shortest_movie.title}, with a runtime of {shortest_movie.runtime} minutes " \
                 f"({shortest_movie.days_since_release()} days old today)"

    return html_page


def distribution_by_year(collection):
    movie_dict = collection.get_movies_by_year()
    most_movies_year = None
    most_movies = 0
    for key in movie_dict:
        if movie_dict[key] > most_movies:
            most_movies_year = key
            most_movies = movie_dict[key]

    print(f"\nThe year with most movies was {most_movies_year}, with {most_movies} movies")

    keys = list(movie_dict.keys())
    values = list(movie_dict.values())
    bar_plot('Year', keys, 'Number of movies', values, 'Movie distribution by year')


def html_distribution_by_year(collection):
    movie_dict = collection.get_movies_by_year()
    most_movies_year = None
    most_movies = 0
    for key in movie_dict:
        if movie_dict[key] > most_movies:
            most_movies_year = key
            most_movies = movie_dict[key]

    keys = list(movie_dict.keys())
    values = list(movie_dict.values())

    html_page = html_bar_plot('Year', keys, 'Number of movies', values, 'Movie distribution by year')

    html_page += f"<p>The year with most movies was {most_movies_year}, with {most_movies} movies</p>"

    return html_page
