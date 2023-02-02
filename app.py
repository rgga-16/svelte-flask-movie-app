from flask import Flask, send_from_directory
import random, requests

TMDB_API = "6c5762e26264089fee02b959c6b5343b"

app = Flask(__name__, static_folder="./client/public")

@app.route("/popular_tvs")
def get_popular_tvshows():
    URL=f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API}&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    return data


@app.route("/popular_movies")
def get_popular_movies():
    URL = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API}&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    return data

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('./client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('./client/public', path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True)
