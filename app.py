import markov
from flask import Flask, request, render_template, jsonify, json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def parse_json():
    """ takes in POST data as JSON from Node app and converts values to make
    them accessible to rest of Flask app """
    if request.method == 'GET': # only executed with HTTP GET requests
        return "Please send a POST request to use this application."

    params = request.get_json()

    # get the user's answers and add file extension
    gender = params['gender'] + '.txt'
    cultural = params['cultural'] + '.txt'
    literary = params['literary'] + '.txt'

    return markov.main(gender, cultural, literary, 'corpus.txt')

@app.route('/index')
def index():
    """ Demonstration of api; returns a web template"""
    index_name = markov.main('girl.txt', 'app_names.txt', 'modern.txt', 'corpus.txt')
    return render_template('index.html', index_name=index_name)


@app.route('/api')
def return_json():
    """ Demonstration of api; returns json result """
    json_name = markov.main('girl.txt', 'app_names.txt', 'modern.txt', 'corpus.txt')
    return jsonify(json_name)
