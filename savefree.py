import requests
import json
from bs4 import BeautifulSoup

def get_down_link(insta_url):
    url = "https://social-media-video-downloader.p.rapidapi.com/smvd/get/instagram"

    querystring = {"url":insta_url}

    headers = {
	"x-rapidapi-key": "165bcef4c0mshc6f30d0a66f9206p1ba83ejsnfd7ef3bfbda6",
	"x-rapidapi-host": "social-media-video-downloader.p.rapidapi.com"}

    response = requests.get(url, headers=headers, params=querystring)

    resdict = response.json()

    if resdict["success"] == False:
        return "An error occured."
    else:
        links = resdict["links"]

        download_links = []

        for x in range(len(links)):
            if (x % 2) == 0:
                continue
            else:
                download_links.append(links[x]["link"])

        return download_links
