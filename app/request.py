from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the movie base url
base_url = app.config["SOURCE_API_BASE_URL"]

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_source_response['results']
            source_results = process_results(source_results_list)


    return movie_results