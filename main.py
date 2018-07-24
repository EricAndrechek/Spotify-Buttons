from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

# api key:
KEY = "Bearer BQA8_dOd3BK8KPbaMk8tqhhjXRb-O6isnCpPMPaGHfNbZO4Mj9DShjuS3TiKHe-0LyKuPg2pGDyGQNOp98EW8zrPnmPZKWzNPOrtR8jHXtHicXceSssTG1HIP9vJwD8RCdq4ydSfZmvTIdG-J7M8ePxUCefnscXveAPbx2TB6EcyO1QUFgwFkgFmPcIqrn_pEH4DQ6hOf5IK00FHi3kdR_xxPWU-BE2vQQVTEe_cHbXARpsf7tBFaet5--IxOX64uWYTBof6mqdXOicAYH7lzpyDdPL1D4sTm2HB"


# devices:

def devices():
    url = "https://api.spotify.com/v1/me/player/devices"
    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers)
    return response.text


# volume:

def volume(percent):
    url = "https://api.spotify.com/v1/me/player/volume"

    querystring = {"volume_percent": percent}

    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers, params=querystring)

    return response.text


# play:

def play():
    url = "https://api.spotify.com/v1/me/player/play"

    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers)

    return response.text


# pause:

def pause():
    url = "https://api.spotify.com/v1/me/player/pause"

    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers)

    return response.text


# next:

def next():
    url = "https://api.spotify.com/v1/me/player/next"

    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, headers=headers)

    return response.text


# previous:

def previous():
    url = "https://api.spotify.com/v1/me/player/previous"

    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, headers=headers)

    return response.text


# shuffle:

def shuffle(toggle):
    url = "https://api.spotify.com/v1/me/player/shuffle"

    querystring = {"state": toggle}

    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }
    response = requests.request("PUT", url, headers=headers, params=querystring)

    return response.text


# repeat:

def repeat(toggle):
    url = "https://api.spotify.com/v1/me/player/repeat"

    querystring = {"state": toggle}

    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers, params=querystring)

    return response.text


# Currently Playing:

def cp():
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = {
        'Authorization': KEY,
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


@app.route('/')
def main():
    data = {
        'CP': cp(),
        'devices': devices()
    }
    return render_template("index.html", **data)


@app.route("/<action>")
def action(action):
    if action == "play":
        status = play()
    elif action == "pause":
        status = pause()
    elif action == "next":
        status = next()
    elif action == "previous":
        status = previous()
    else:
        status = "the \'%s\' command didn't match an assigned function" % action
    data = {
        'CP': cp(),
        'status': status,
        'devices': devices()
    }
    return render_template("index.html", **data)


@app.route("/<action>/<toggle>")
def toggle(action, toggle):
    if action == "volume":
        status = volume(toggle)
    elif action == "shuffle":
        status = shuffle(toggle)
    elif action == "repeat":
        status = repeat(toggle)
    else:
        status = "the \'%s\' command didn't match an assigned function with sub-command \'%s\'" % action % toggle
    data = {
        'CP': cp(),
        'status': status,
        'devices': devices()
    }
    return render_template("index.html", **data)


@app.errorhandler(404)
def page_not_found(e):
    data = {
        'CP': cp(),
        'status': '404: page not found',
        'devices': devices()
    }
    return render_template('index.html', **data), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')

