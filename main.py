from flask import Flask, render_template, request

from model_creation.model import recommendation_for_a_movie

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    r = recommendation_for_a_movie(movie)
    movie = movie.upper()
    if type(r) == type('string'):
        return render_template('recommend.html', movie=movie, r=r, t='s')
    else:
        return render_template('recommend.html', movie=movie, r=r, t='l')


if __name__ == '__main__':
    app.run(debug=True, port=5151)
