from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os
import requests

from dotenv import load_dotenv, find_dotenv
app = Flask(__name__)
api = Api(app)

#test part
@app.route('/')
def hello_world():
    return 'Hello world!'

load_env(find_dotenv())

#authentification and headers
def auth():
    return os.getenv('TOKEN') #token is the api key

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def create_url(keyword, max_results = 30):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent" #recent search endpoint

                    #'start_time': start_date,
                    #'end_time': end_date,
    query_params = {'query': keyword,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)

    
def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


#test parameters
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "python"
#start_time = "2021-03-01T00:00:00.000Z"
#end_time = "2021-03-31T00:00:00.000Z"
max_results = 15

url = create_url(keyword, max_results)

json_response = connect_to_endpoint(url[0], headers, url[1])

class Hashtags(Resource):
    # methods go here
    pass


class Users(Resource):
    # methods go here
    pass


api.add_resource(Hashtags, '/hashtags')  # and '/locations' is our entry point for Locations
api.add_resource(Users, '/users')  # '/users' is our entry point for Users


if __name__ == '__main__':
    app.run()  # run test