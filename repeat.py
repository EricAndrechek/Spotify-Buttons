import requests

def sendrequest():
    url = "https://api.spotify.com/v1/me/player/repeat"
    querystring = {"state":var}
    headers = {
        'Authorization': "Bearer BQARTn__0MVGMa8FUI-OsrXRdMAxaV2a62bEKzy5sy7PeRM4mwPPV8e0NMHpBH1lMRIaJxt9Ul9N2FTwl7jwKOJwCD7pVTDSXi_kHHtmoj9U2qQwTtcfiysRViEOk3t5EQ1K65Fd9dl-imYfUZr115p5c1oXYqFAckxInUk8P27qgKXKVO9gpVDXkYnBaaKV765lc2quhFEHxK-OO7DzSInvKFhev5OM9_MsogntT2ebXY_diPm1U0jDMKyaXfZwot2s1hFXw5S9eipbPD4ZsowEO8eFB8AAtStB",
        'Cache-Control': "no-cache"
    }
    response = requests.request("PUT", url, headers=headers, params=querystring)
    print(response.text)


toggle = input("To turn on repeat, type \'1\', to turn off repeat type \'2\'\n")

if toggle == 1:
    var = "context"
    print("turning repeat on...")
    sendrequest()
elif toggle == 2:
    var = "off"
    print("turning repeat off...")
    sendrequest()
else:
    print("Your input: \'%s\' didn\'t match either option 1 or option 2." % toggle)
