from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os
import requests

from dotenv import load_dotenv, find_dotenv
app = Flask(__name__)
api = Api(app)

#test to see if the api is running
@app.route('/')
def hello_world():
    return 'Hello world!'


#authentification and headers
load_dotenv(find_dotenv())
def auth():
    return os.getenv('TOKEN') #token is the api key

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

#corresponding variables
bearer_token = auth()
headers = create_headers(bearer_token)


# creates the url for the requests
def create_url_hashtag(keyword, max_results = 30):
    search_url = "https://api.twitter.com/2/tweets/search/recent" #recent search endpoint

    query_params = {'query': keyword,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}} #indicates if more results are available or not
    return (search_url, query_params)

# def create_url_user(username, max_results = 30):
#     search_url = "https://api.twitter.com/2/tweets/search/recent" #recent search endpoint

#     query_params = {'query': keyword,
#                     'max_results': max_results,
#                     'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
#                     'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
#                     'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
#                     'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
#                     'next_token': {}} #indicates if more results are available or not
#     return (search_url, query_params)


# connect to the twitter endpoints
def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

class Hashtags(Resource):
    #keyword = "python"
    #max_results = 15

    def get(self):
        parser = reqparse.RequestParser()  # initialize parser
        
        parser.add_argument('hashtag', required=True)  # parse each arg
        parser.add_argument('limit', required=False)
        args = parser.parse_args()

        keyword = args['hashtag']
        max_results = args['limit']

        url = create_url_hashtag(keyword, max_results) # url[0]: endpoint, url[1]: parameters
        json_response = connect_to_endpoint(url[0], headers, url[1])
   
        
        return {'tweets': json_response}, 200  # return data and 200 OK code


class Users(Resource):
    # username = "twitter"
    # max_results = 15

    # url = create_url_user(keyword, max_results) #url[0]: endpoint, url[1]: parameters

    # json_response = connect_to_endpoint(url[0], headers, url[1])
    pass


api.add_resource(Hashtags, '/hashtags')  # and '/locations' is our entry point for Locations
api.add_resource(Users, '/users')  # '/users' is our entry point for Users


if __name__ == '__main__':
    app.run()  # run test