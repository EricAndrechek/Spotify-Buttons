import requests

def sendrequest():
    url = "https://api.spotify.com/v1/me/player/shuffle"
    querystring = {"state":var}
    headers = {
        'Authorization': "Bearer BQARTn__0MVGMa8FUI-OsrXRdMAxaV2a62bEKzy5sy7PeRM4mwPPV8e0NMHpBH1lMRIaJxt9Ul9N2FTwl7jwKOJwCD7pVTDSXi_kHHtmoj9U2qQwTtcfiysRViEOk3t5EQ1K65Fd9dl-imYfUZr115p5c1oXYqFAckxInUk8P27qgKXKVO9gpVDXkYnBaaKV765lc2quhFEHxK-OO7DzSInvKFhev5OM9_MsogntT2ebXY_diPm1U0jDMKyaXfZwot2s1hFXw5S9eipbPD4ZsowEO8eFB8AAtStB",
        'Cache-Control': "no-cache"
    }
    response = requests.request("PUT", url, headers=headers, params=querystring)
    print(response.text)


toggle = input("To turn on shuffle, type \'1\', to turn off shuffle type \'2\'\n")

if toggle == 1:
    var = "true"
    print("turning shuffle on...")
    sendrequest()
elif toggle == 2:
    var = "false"
    print("turning shuffle off...")
    sendrequest()
else:
    print("Your input: \'%s\' didn\'t match either option 1 or option 2." % toggle)