from flask import Flask, request
import tmdb_functions
from movie_collection import MovieCollection
import data_functions
from project_cli import save_movie_collection
import json
import tempfile

with open("directory.txt") as file:
    directory = file.readline()

app = Flask(__name__, static_folder=directory)


def html_template(head, body):
    return """
    <html lang="en">
      <head>
        <title>TMdB API</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
        body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
        .w3-bar,h1,button {font-family: "Montserrat", sans-serif}
        .fa-anchor,.fa-coffee {font-size:200px}
        </style>
      </head>
    <body>
    
    <!-- Navbar -->
    <div class="w3-top">
      <div class="w3-bar w3-red w3-card w3-left-align w3-large">""" + \
        head + \
        """</div>
    </div>
    
    <!-- First Grid -->
    <div class="w3-row-padding w3-padding-64 w3-container">
      <div class="w3-content">
        """ + \
        body + \
        """</div>
    </div>
    
    <!-- Second Grid -->
    <div class="w3-row-padding w3-light-grey w3-padding-64 w3-container">
      <div class="w3-content">
        <div class="w3-third w3-center">
    </p>
        </div>
    
    <!-- Footer. This section contains an ad for W3Schools Spaces. You can leave it to support us. -->
    <footer class="w3-container w3-center w3-opacity"> 
        <a class="fa fa-github w3-hover-opacity" href="https://github.com/IC-COMP172-2024-SP/172-project02-oopforanapi-Marzopa"></a>
     </footer>
    </body>
    </html>"""


def html_graph_from_collection(data_options, movie_collection):
    if data_options == "r":
        html_plot = data_functions.html_user_rating_against_tmdb_rating(movie_collection)
    elif data_options == "b":
        html_plot = data_functions.html_rating_against_budget(movie_collection)
    elif data_options == "d":
        html_plot = data_functions.html_director_distribution(movie_collection)
    elif data_options == "a":
        html_plot = data_functions.html_actor_distribution(movie_collection)
    elif data_options == "p":
        html_plot = data_functions.html_rating_against_profit(movie_collection)
    elif data_options == "n":
        html_plot = data_functions.html_order_movies_by_date(movie_collection)
    elif data_options == "t":
        html_plot = data_functions.html_runtime_against_age(movie_collection)
    elif data_options == "y":
        html_plot = data_functions.html_distribution_by_year(movie_collection)
    elif data_options == "m":
        predicted_movie = tmdb_functions.movie_prediction(movie_collection)
        html_plot = f"""<p>You should watch</p><h5>{predicted_movie}</h5><img src='https://image.tmdb.org/t/p/original{predicted_movie.poster_path}' height='30%'>"""
    else:
        html_plot = "<p>There was an error</p>"
    return html_plot


@app.route("/")
def home():
    return """
    <html lang="en">
      <head>
        <title>TMdB API</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
        body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
        .w3-bar,h1,button {font-family: "Montserrat", sans-serif}
        .fa-anchor,.fa-coffee {font-size:200px}
        </style>
      </head>
    <body>
    
    <!-- Navbar -->
    <div class="w3-top">
      <div class="w3-bar w3-red w3-card w3-left-align w3-large">
        <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
        <a href="/" class="w3-bar-item w3-button w3-padding-large w3-white">Home</a>
        <a href="/api" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">API requests</a>
        <a href="/fileupload" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Upload file</a>
      </div>
    </div>
    
    <!-- Header -->
    <header class="w3-container w3-red w3-center" style="padding:128px 16px">
      <h1 class="w3-margin w3-jumbo">The Movie Db</h1>
      <p class="w3-xlarge">Oscar Jimenez</p>
      <a class="w3-button w3-black w3-padding-large w3-large w3-margin-top" href="/api">Get Started </a>
    </header>
    
    <!-- First Grid -->
    <div class="w3-row-padding w3-padding-64 w3-container">
      <div class="w3-content">
        <div class="w3-twothird">
          <h1>How it works</h1>
          <h5 class="w3-padding-32">Description: a program that allows to generate lists of movies from TMdB (or load from a JSON file) and do operations with them.</h5>
    
          <p class="w3-text-grey">
            Capabilities:
            <ul>
              <li>Compare user rating against TMdB rating.</li>
              <li>Compare budget against TMdB rating.</li>
              <li>Get distribution of directors across list of movies.</li>
              <li>Get distribution of actors appearances across list of movies.</li>
              <li>Compare TMdD rating against movie profit.</li>
              <li>Order movies from oldest to newest.</li>
              <li>Compare runtime against age of the movie.</li>
              <li>Get distribution of movies by year.</li>
            </ul>
          </p>
    
          <p class="w3-text-grey">
            Important notes:
            <ul>
              <li>Plot user rating against TMdB rating only works when list is generated with Get rated movies from TMdB account (R), or when a json file generated by this command is opened. And because the way the API works, this only works with the movies I have rated from my own TMdB account.</li>
              <li>Some movies appear as without a budget or box office in the API responses, so they are generally excluded from images and calculations. However, the following data visualization options do include them:
                <ul>
                  <li>Graph distribution of directors.</li>
                  <li>Graph distribution of actors.</li>
                  <li>Order movies from oldest to newest.</li>
                  <li>Plot runtime against age of the movie.</li>
                  <li>Graph distribution of movies by year.</li>
                </ul>
              </li>
            </ul>
          </p>
        </div>
    
      </div>
    </div>
    
    <!-- Second Grid -->
    <div class="w3-row-padding w3-light-grey w3-padding-64 w3-container">
      <div class="w3-content">
        <div class="w3-third w3-center">
    </p>
        </div>
    
    <!-- Footer. This section contains an ad for W3Schools Spaces. You can leave it to support us. -->
    <footer class="w3-container w3-center w3-opacity"> 
        <a class="fa fa-github w3-hover-opacity" href="https://github.com/IC-COMP172-2024-SP/172-project02-oopforanapi-Marzopa"></a>
     </footer>
    </body>
    </html>"""


@app.route("/api")
def api_requests():
    head = """<a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
        <a href="/" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Home</a>
        <a href="/api" class="w3-bar-item w3-button w3-padding-large w3-white">API requests</a>
        <a href="/fileupload" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Upload file</a>"""
    body = """<h1>Select API request</h1>
      <form action="/apidata">
      <label for="actions">Choose an option to request from the API:</label>
      <select name="actions" id="actions">
        <option value="b">Best rated TMdB movies</option>
        <option value="p">Most popular TMdB movies</option>
        <option value="l">Movies from TMdB list</option>
        <option value="r">Rated movies from TMdB account</option>
        <option value="t">Trending movies on TMdB</option>
      </select>
      <br><br>
      <label for="actions">Choose a data visualization option:</label>
      <select name="data_options" id="data_options">
        <option value="r">Plot user rating against TMdB rating</option>
        <option value="b">Plot budget against TMdB rating</option>
        <option value="d">Graph distribution of directors</option>
        <option value="a">Graph distribution of actors</option>
        <option value="p">Plot TMdD rating against profit</option>
        <option value="n">Order movies from oldest to newest</option>
        <option value="t">Plot runtime against age of the movie</option>
        <option value="y">Graph distribution of movies by year</option>
        <option value="m">Movie prediction</option>
      </select>
      <br><br>
      <label for="quantity">Number of movies (between 1 and 250):</label>
      <input type="number" id="quantity" name="quantity" min="1" max="250">
      <br>
      <input type="checkbox" id="save_file" name="save_file" value="true">
      <label for="save_file"> Save collection to a file</label><br>
      <br>
      <input type="submit" value="Submit">
      <br><br>
    
      </form>"""

    return html_template(head, body)


@app.route("/apidata")
def data_visualization_from_api():
    option = request.args.get("actions")
    number = int(request.args.get("quantity"))
    data_options = request.args.get("data_options")
    save_file = request.args.get("save_file")

    if option == "b":
        movies_list = tmdb_functions.best_rated_list(number)
    elif option == "p":
        movies_list = tmdb_functions.popular_list(number)
    elif option == "l":
        movies_list = tmdb_functions.get_movies_from_tmdb_list()
    elif option == "r":
        movies_list = tmdb_functions.user_rated_list()
    elif option == "t":
        movies_list = tmdb_functions.trending_list(number)
    else:
        movies_list = []

    movie_collection = MovieCollection(movies_list)

    if save_file == 'true':
        save_movie_collection(movie_collection)

    html_plot = html_graph_from_collection(data_options, movie_collection)

    fetch_message = (f"<h1>{len(movie_collection.movie_list)} movies fetched correctly</h1>"
                     f"<h4>(excluded {len(movie_collection.excluded_movies)} because they do not have budgets or box offices)</h4>")

    head = """<a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
        <a href="/" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Home</a>
        <a href="/api" class="w3-bar-item w3-button w3-padding-large w3-white">API requests</a>
        <a href="/fileupload" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Upload file</a>"""
    body = fetch_message + "<br><br>" + html_plot

    return html_template(head, body)


@app.route("/fileupload")
def upload_file():
    head = """<a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
        <a href="/" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Home</a>
        <a href="/api" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">API requests</a>
        <a href="/fileupload" class="w3-bar-item w3-button w3-padding-large w3-white">Upload file</a>"""
    body = """<h1>File upload</h1>
      <h4>(must be JSON generated from the TMdB API)</h4>
      <br>
        <form action="/filedata" method="post" enctype="multipart/form-data">
        <input type="file" id="user_file" name="user_file">
        <br><br>
        <label for="actions">Choose a data visualization option:</label>
        <select name="data_options" id="data_options">
            <option value="r">Plot user rating against TMdB rating</option>
            <option value="b">Plot budget against TMdB rating</option>
            <option value="d">Graph distribution of directors</option>
            <option value="a">Graph distribution of actors</option>
            <option value="p">Plot TMdD rating against profit</option>
            <option value="n">Order movies from oldest to newest</option>
            <option value="t">Plot runtime against age of the movie</option>
            <option value="y">Graph distribution of movies by year</option>
            <option value="m">Movie prediction</option>
        </select>
        <input type="submit" value="Upload">
        </form>"""

    return html_template(head, body)


@app.route("/filedata", methods=["POST"])
def filedata():
    if 'user_file' not in request.files:
        return 'No file part'

    user_file = request.files.get('user_file', "")

    if user_file.filename == '':
        return 'No selected file'

    with tempfile.NamedTemporaryFile(delete=False):
        file_contents = user_file.stream.read()
        data_options = request.form.get('data_options', "")

    movie_collection = MovieCollection(json.loads(file_contents))

    html_plot = html_graph_from_collection(data_options, movie_collection)

    fetch_message = (f"<h1>{len(movie_collection.movie_list)} movies fetched correctly</h1>"
                     f"<h4>(excluded {len(movie_collection.excluded_movies)} because they do not have budgets or box offices)</h4>")

    head = """<a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
            <a href="/" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Home</a>
            <a href="/api" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">API requests</a>
            <a href="/fileupload" class="w3-bar-item w3-button w3-padding-large w3-white">Upload file</a>"""

    body = fetch_message + "<br><br>" + html_plot

    return html_template(head, body)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
