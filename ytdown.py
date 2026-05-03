import requests
from urllib.parse import urlparse, parse_qs
from contextlib import suppress

# noinspection PyTypeChecker
def get_yt_id(url, ignore_playlist=True):
    # Examples:
    # - http://youtu.be/SA2iWivDJiE
    # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    # - http://www.youtube.com/embed/SA2iWivDJiE
    # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com', 'music.youtube.com'}:
        if not ignore_playlist:
        # use case: get playlist id not current video in playlist
            with suppress(KeyError):
                return parse_qs(query.query)['list'][0]
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]
        if query.path[:8] == '/shorts/': return query.path.split('/')[2]
   # returns None for invalid YouTube url

def get_yt_down_link(yturl, formatid=360):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    videoid = get_yt_id(yturl)
    querystring = {"videoId":videoid}

    headers = {
        "X-RapidAPI-Key": "a0e1ddbe92msh26c57efc2540a18p1d5f5cjsne4d3191f9340",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if formatid == 360:
        videourl = response.json()["videos"]["items"][0]["url"]
    elif formatid == 720:
        videourl = response.json()["videos"]["items"][1]["url"]
        
    return videourl
