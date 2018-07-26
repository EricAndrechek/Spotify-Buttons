from __future__ import division
from flask import Flask, render_template, request, redirect
import requests
import base64
import json
import math

app = Flask(__name__)

# key declaration:

key = ''


# devices:

def devices():
    url = "https://api.spotify.com/v1/me/player/devices"
    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers)
    return response.text


# volume:

def volume(percent):
    url = "https://api.spotify.com/v1/me/player/volume"

    querystring = {"volume_percent": percent}

    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers, params=querystring)

    return response.text


# play:

def play():
    url = "https://api.spotify.com/v1/me/player/play"

    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers)

    return response.text


# pause:

def pause():
    url = "https://api.spotify.com/v1/me/player/pause"

    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers)

    return response.text


# next:

def next():
    url = "https://api.spotify.com/v1/me/player/next"

    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, headers=headers)

    return response.text


# previous:

def previous():
    url = "https://api.spotify.com/v1/me/player/previous"

    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, headers=headers)

    return response.text


# shuffle:

def shuffle(toggle):
    url = "https://api.spotify.com/v1/me/player/shuffle"

    querystring = {"state": toggle}

    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }
    response = requests.request("PUT", url, headers=headers, params=querystring)

    return response.text


# repeat:

def repeat(toggle):
    url = "https://api.spotify.com/v1/me/player/repeat"

    querystring = {"state": toggle}

    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }

    response = requests.request("PUT", url, headers=headers, params=querystring)

    return response.text


# Currently Playing:

def cp(to_get):
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = {
        'Authorization': "Bearer %s" % key,
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    json_file = response.text
    if json_file[5:14] == "timestamp":
        response_data = json.loads(response.text)
        item = response_data["item"]
        album = item["album"]
        artists = album["artists"]
        artistsub = artists[0]
        name = artistsub["name"]
        images = album["images"]
        imagesub = images[0]
        url = imagesub["url"]
        song = item["name"]
        progress = response_data["progress_ms"]
        duration = item["duration_ms"]
        ppdata = response_data["is_playing"]
        if ppdata is True:
            pp = "pause"
        else:
            pp = "play"
        if to_get == "artist":
            return name
        elif to_get == "song":
            return song
        elif to_get == "img":
            return url
        elif to_get == "time":
            return progress / duration
        elif to_get == "pro":
            prosec = progress / 1000
            prominrem = prosec / 60
            prorem = prosec % 60 / 60
            promin = prominrem - prorem
            prosec = prorem * 60
            profinsec = math.floor(prosec)
            if profinsec < 10:
                profinsecsml1 = "0{}".format(profinsec)
                profinsecsml = profinsecsml1.split(".")[0]
            else:
                profinsecsml = str(math.floor(prosec)).split(".")[0]
            profin = "{}:{}".format(str(math.floor(promin)).split(".")[0], profinsecsml)
            return profin
        elif to_get == "dur":
            dursec = duration / 1000
            durminrem = dursec / 60
            durrem = dursec % 60 / 60
            durmin = durminrem - durrem
            dursec = durrem * 60
            durfinsec = math.floor(dursec)
            if durfinsec < 10:
                durfinsecsml1 = "0{}".format(durfinsec)
                durfinsecsml = durfinsecsml1.split(".")[0]
            else:
                durfinsecsml = str(math.floor(dursec)).split(".")[0]
            durfin = "{}:{}".format(str(math.floor(durmin)).split(".")[0], durfinsecsml)
            return durfin
        elif to_get == "dev":
            return response.text
        elif to_get == "pp":
            return pp
        elif to_get == "shuffle":
            url = "https://api.spotify.com/v1/me/player"
            headers = {
                'Authorization': "Bearer %s" % key,
                'Cache-Control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers)
            json_file = json.loads(response.text)
            shufflestate = json_file["shuffle_state"]
            if shufflestate is True:
                return "false"
            else:
                return "true"
        elif to_get == "repeat":
            url = "https://api.spotify.com/v1/me/player"
            headers = {
                'Authorization': "Bearer %s" % key,
                'Cache-Control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers)
            json_file = json.loads(response.text)
            repeatstate = json_file["repeat_state"]
            if (repeatstate == "track") or (repeatstate == "context"):
                return "off"
            else:
                return "context"
        else:
            return "{} NOTICE: If you are seeing this message and are able to control your content normally, something may be wrong.".format(response.text)
    else:
        return "{} NOTICE: If you are seeing this message and are able to control your content normally, something may be wrong.".format(response.text)


# set redirect URI:

CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 5000
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)


@app.route('/')
def main():
    data = {
        'CPA': cp("artist"),
        'CPS': cp("song"),
        'CPI': cp("img"),
        'CPT': cp("time"),
        'CPTP': cp("pro"),
        'CPTD': cp("dur"),
        'CPST': cp("shuffle"),
        'CPRT': cp("repeat"),
        'CP': cp("dev"),
        'pp': cp("pp"),
        'devices': devices(),
        'status': "You are not logged in. Click the link below to login"
    }
    if cp("dev")[5:14] != "timestamp":
        return redirect("/login", code=302)
    else:
        return render_template("index.html", **data)


@app.route('/login')
def login():
    return redirect('https://accounts.spotify.com/authorize/?client_id=470f615d8cb342e488fe71416ffb504c&scope=user-read-playback-state%20user-read-private%20user-read-currently-playing%20user-modify-playback-state&response_type=code&redirect_uri={}'.format(REDIRECT_URI), code=302)


@app.route('/callback/q')
def callback():
    if request.args.get('error') != 'access_denied':
        global key
        url = "https://accounts.spotify.com/api/token"
        code = request.args.get('code')
        code_payload = {
            'grant_type': "authorization_code",
            'code': str(code),
            'redirect_uri': REDIRECT_URI
        }
        base64encoded = base64.b64encode(
            "{}:{}".format('470f615d8cb342e488fe71416ffb504c', '4c4f12d06d6a4fcb8f6ba2d765e19b53'))
        headers = {"Authorization": "Basic {}".format(base64encoded)}
        response = requests.request("POST", url, headers=headers, data=code_payload)
        response_data = json.loads(response.text)
        key = response_data["access_token"]
        refresh_token = response_data["refresh_token"]
        token_type = response_data["token_type"]
        expires_in = response_data["expires_in"]
        data = {
            'CPA': cp("artist"),
            'CPS': cp("song"),
            'CPI': cp("img"),
            'CPT': cp("time"),
            'CPTP': cp("pro"),
            'CPTD': cp("dur"),
            'CPST': cp("shuffle"),
            'CPRT': cp("repeat"),
            'CP': cp("dev"),
            'pp': cp("pp"),
            'devices': devices(),
            'status': response
        }
        return render_template("index.html", **data)
    else:
        data = {
            'status': 'Error logging in - access denied'
        }
        if cp("dev")[5:14] != "timestamp":
            return redirect("/login", code=302)
        else:
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
        'CPA': cp("artist"),
        'CPS': cp("song"),
        'CPI': cp("img"),
        'CPT': cp("time"),
        'CPTP': cp("pro"),
        'CPTD': cp("dur"),
        'CPST': cp("shuffle"),
        'CPRT': cp("repeat"),
        'CP': cp("dev"),
        'status': status,
        'pp': cp("pp"),
        'devices': devices()
    }
    if cp("dev")[5:14] != "timestamp":
        return redirect("/login", code=302)
    else:
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
        'CPA': cp("artist"),
        'CPS': cp("song"),
        'CPI': cp("img"),
        'CPT': cp("time"),
        'CPTP': cp("pro"),
        'CPTD': cp("dur"),
        'CPST': cp("shuffle"),
        'CPRT': cp("repeat"),
        'CP': cp("dev"),
        'status': status,
        'pp': cp("pp"),
        'devices': devices()
    }
    if cp("dev")[5:14] != "timestamp":
        return redirect("/login", code=302)
    else:
        return render_template("index.html", **data)


@app.errorhandler(404)
def page_not_found(e):
    data = {
        'CPA': cp("artist"),
        'CPS': cp("song"),
        'CPI': cp("img"),
        'CPT': cp("time"),
        'CPTP': cp("pro"),
        'CPTD': cp("dur"),
        'CPST': cp("shuffle"),
        'CPRT': cp("repeat"),
        'CP': cp("dev"),
        'pp': cp("pp"),
        'status': '404: page not found. This may be because you are not logged in. Click the link below to login',
        'devices': devices()
    }
    if cp("dev")[5:14] != "timestamp":
        return redirect("/login", code=302)
    else:
        return render_template("index.html", **data), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

