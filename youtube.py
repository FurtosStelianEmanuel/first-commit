import urllib.parse
import webbrowser
import re
import random as rand
from urllib.request import urlopen, Request


def search(query_string):
    query_string = urllib.parse.urlencode({"search_query": query_string})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    html=html_content.read().decode()
    results = re.findall(
        r'/watch\?v=(.{11})', html
    )

    webbrowser.open("http://www.youtube.com/watch?v=" + results[0])


def search_results(query_string):
    query_string = urllib.parse.urlencode({"search_query": query_string})
    webbrowser.open("http://www.youtube.com/results?" + query_string)


def show_results():
    html_content = urllib.request.urlopen(
        "https://www.youtube.com/watch?v=yps3qCbo0F0&list=RDMM&start_radio=1"
    )
    results = re.findall(
        r'/watch\?v=(.{11})', html_content.read().decode()
    )
    # webbrowser.open("http://www.youtube.com/watch?v="+search_results[0])
    for result in results:
        print(result)


def play_random():
    html_content = urllib.request.urlopen(
        "https://www.youtube.com/watch?v=yps3qCbo0F0&list=RDMM&start_radio=1"
    )
    search_results = re.findall(
        r'/watch\?v=(.{11})', html_content.read().decode()
    )
    index = rand.randint(0, len(search_results) - 1)
    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[index])

