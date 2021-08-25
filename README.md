# RestfulApi
### Introduction
 Project developed for the Anymind recruitement process\
 Language: Python 3\
 Development OS: Windows 10\
 This Restful Api is capable of handling two GET requests:
 a search of Tweets by hashtags, and one by users.\
 IMPORTANT: Since this project is based on the Twitter API V2, please make that you have developer access to it.

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


