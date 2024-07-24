from flask import Flask, request
app = Flask(__name__)


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
              <li>Some movies appear as without a budget or box office in the API responses, so they are generally excluded from plots and calculations. However, the following data visualization options do include them:
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
    return """Tweaking tf out"""


@app.route("/data")
def data_visualization():
    return """Tweaking tf out"""


if __name__ == "__main__":
    app.run(host="localhost", debug=True)