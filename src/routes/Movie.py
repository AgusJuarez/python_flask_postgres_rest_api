from flask import Blueprint, jsonify, request
#Models
from models.MovieModel import MovieModel

main=Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/add', methods=['POST'])
def add_movie():
    try:
        print(request.json)
        return jsonify({})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500


