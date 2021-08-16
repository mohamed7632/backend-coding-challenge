from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json


@api_view(['GET'])
def get_data(request):

    today = datetime.now()
    two_months_ago = (today - timedelta(days=60)).strftime("%Y-%m-%d")
    # api call to list of 100 trending repositories in GH sorted by stars
    # in descending order
    url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page=100".format(
        two_months_ago)
    response = requests.get(url)
    #if The request has succeeded
    if response.status_code == 200:
        trending_repositories = response.json()['items']
        repos_languages = {}
        no_of_repos = "No of repos"
        repos = "List of repos"
        URL = "url"
        HTML_URL = "html_url"

        for repo in trending_repositories:
            language = repo['language']
            #setdefault method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary
            val = repos_languages.setdefault(language,
                                                  {no_of_repos: 0,
                                                   repos: []})
            #increment no_of_repos then add it again to repos_languages dictionary
            #append two repos urls (URL,HTML_URL)
            repos_languages[language][no_of_repos] = val[no_of_repos] + 1
            val[repos].append({repo[URL], repo[HTML_URL]})

        return Response(repos_languages)
        
    
    return Response(response, status=response.status_code)
    
