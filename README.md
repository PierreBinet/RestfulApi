# RestfulApi
### Introduction
 Project developed for the Anymind recruitement process\
 _Language_: Python 3\
 _Development OS_: Windows 10\
 This Restful Api is capable of handling two GET requests:
 a search of Tweets by hashtags, and one by users.\
 _IMPORTANT_: Since this project is based on the Twitter API V2, please make that you have developer access to it.
 
#### _EDIT_: my developper access to the twitter API was removed early in the project ("job application" must not be enough to get access), meaning that the project could not be tested...

### Setup
Please be sure to install all the required libraries of the import section:\
pandas, flask, requests, dotenv, ast, os\
Please also make sure to include your Twitter api bearer token in a .env file in the directory where you pulled this repository, with the following syntax:\
`TOKEN=<insert the bearer token here>`


In the same directory, please initiate a virtual environment:\
`pip install virtualenv` (in case it's not installed yet)\
`py -3 -m venv apienv`\
`apienv\Scripts\activate` to enter the virtual environment\
`setx FLASK_APP “main.py”` (please note setting an environment variable requires the command prompt to be restarted for the changes to take effect in Windows)\
`flask run` to launch the app

### How to use
The developed API contains two endpoints:
1. _Hashtag_ allows to search for tweets by keyword\
The request syntax is GET http://localhost:xxxx/hashtags/keyword=yyyyyy?limit=40

2. _User_ allows to search for tweets by (author) username\
The request syntax is GET http://localhost:xxxx/hashtags/user_name=zzzzzz?limit=35 \

With xxxx the port used by Flask for the API (default should be 5000), yyyyyy a keyword and zzzzzz a username.\
The limit argument can also be changed to display the desired number of tweets.

### References
API references for each endpoint:
* https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
* https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username
* https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets
