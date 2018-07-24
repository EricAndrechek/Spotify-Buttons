import requests

url = "https://api.spotify.com/v1/me/player/play"

headers = {
    'Authorization': "Bearer BQAebRKsggHm-1ccdDNo7arccJxPH6Y1jlTiuDLsF8JWRRCMBiPH2o1vKP2ib92S0Q9NgVE07N-XCQGOZaF4qUCye3sAsDsDupbK4gVwp0Pah_kKL6lOsH7hbBKrDuG-ZLkFtMj8IDzUiqjeSd0sDpw88V160KLkI84g4ZKM9VXGrehZyBkbgJnv-IhhRIq1NNqZlcJG6vUUUfcvXYPdp_RIKPKV5cmROwOyswsW7kNYPHmRA2BTX-JabcDTBbBDOSe5PFJXZlVkevIBZrVq4Ptap8yET9b771DF",
    'Cache-Control': "no-cache"
    }

response = requests.request("PUT", url, headers=headers)

print(response.text)