import requests


async def define(word: str):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term": word}
    headers = {
        "X-RapidAPI-Key": "178546401fmsh379ab32fcb4716cp1ac68ajsnbb25e1e0686e",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
