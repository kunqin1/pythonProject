import time

import sign
import requests

key = " 84b4aea73e331b15cf7c6d1dd0f7ee9c"
url = "https://api-beta.cdhourong.top/game/userHave/userDetailGame"

params = {'userId': "1339067253853945858",
          'gameId': '1',
        "timestamp": int(time.time()),
        "nonceStr": MakeStr()

          }
headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9'
                     '.eyJ1c2VyIjoie1widW5pb25JZFwiOjg4ODg4OCxcImltVG9rZW5cIjpcIjNkZGI3NmY4Y2I2YTZhNjdmNmZjZTY1MWNlN2JkZjExXCIsXCJwZXJmZWN0SW5mb1wiOjEsXCJhY2NJZFwiOlwiY2E0NjgyNzVmN2Q2NDZjY2FiMGI1NzVlMjg1ZjI4MTJcIixcImlkXCI6MTMzOTA4NjIyMjM2MzA5OTEzOH0iLCJqdGkiOiJaVEUzWVRnNVl6TXRPV0poTUMwME4yTmlMV0kzWTJRdE1tUXpZV0psWVRneE5EWXciLCJleHAiOjc5NDA2ODg2NDB9.bThUIF9AFCToK4HUqOTRPurLK44P7W2R7MsBSSYTDN3VG9N8nyPApWqqq1LF9mcJk9d9g7ULbIemosYxUYGhmDM8k_YnasSm-HieDJRpzjbZKz6hFQ2Z2MCiAWBI8RJKtZs8w3S1ZtSWfM1uf4NoiBAY5c45mN6YV_j4gy8m6BBSicf7SD48zXu9vrHbBLVWaZpxIqIJZtwL-5si8GYux1qNZn3n_yz7YdepXZ08Thtqo77JMJ88zWpKSAR_ONuZOHgTySzlIUi_9p4KOl0m14IWPK_-IEsIMrlLx1CmLA6wAbrc44xqp4l0nKM_rC6crZeLcd0Yr69ohU8GwkdBpQ '
}
sign.InterfaceSign.GetStringSignTemp(key,)
response = requests.request("GET", url, headers=headers, data=params)

print(response.text)
