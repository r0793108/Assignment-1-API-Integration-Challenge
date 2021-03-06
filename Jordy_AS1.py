#import libraries
from tmdbv3api import TMDb, Movie
import requests
import urllib3

#disable warnings
urllib3.disable_warnings()

#connect and authenticate to the API
url = "https://api.themoviedb.org/4/auth/request_token"
payload = "{\"redirect_to\":\"http://www.themoviedb.org/\"}"
headers = {
    'content-type': "application/json;charset=utf-8",
    'authorization': "Bearer 'Your_API_READ_ACCES_TOKEN'"
    }
response = requests.request("POST", url, data=payload, headers=headers)

#declare variables
tmdb = TMDb()
tmdb.api_key = 'Your_API_KEY'
tmdb.language = 'en'
tmdb.debug = True
movie = Movie()

#check status code and run script
if response.status_code == 200:
    print("Succesful connection with API.")
    print(' ')
    
    #ask for input
    movie_name = input("what movie do you want to search for ? ")
    search = movie.search(movie_name)

    for info in search:
        print('{')
        print('ID:')
        print(info.id)
        print(' ')
        
        print('Title:')
        print(info.title)
        print(' ')
        
        print('Overview:')
        print(info.overview)
        print(' ')
        
        print('Average Vote:')
        print(info.vote_average)
        print('}')
        print(' ')
elif response.status_code == 404:
        print("Unable to reach URL.")
        print(' ')
else:
    print("Unable to connect API")
    print(' ')



