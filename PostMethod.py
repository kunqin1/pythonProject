import time

import requests

import sign

if __name__ == '__main__':
    sign = sign.InterfaceSign
    # 测试服
    key = "84b4aea73e331b15cf7c6d1dd0f7ee9c"
    host = "https://api-beta.cdhourong.top/"
    # 拼装Url
    url = host + "game/userHave/page?current=2&&size=1"
    data = {

        "gameId": "1437345809191411714",
        "sort": "4",
        "longitude": "104.10194",
        "latitude": "30.65984",
        # "current": "2",
        # "size": "2",
        # "refundIllustrate": "sadasd",
        "timestamp": int(time.time()),
        "nonceStr": "8c5e2a16-93c7-4937-b2f7-93a9124ac3bc"
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9'
                         '.eyJ1c2VyIjoie1widW5pb25JZFwiOjE1NDc1MDMyMixcIm'
                         'ltVG9rZW5cIjpcIjA4NWQ4NWJiODc0MmM4YWE4NmE4NjE3YTZhM'
                         'TkzYzkzXCIsXCJwZXJmZWN0SW5mb1wiOjEsXCJhY2NJZFwiOlwiZjg'
                         '4Yjk0OTJkNWEwNDJjMTg2ZGNjODMzNWQzZGRjMGZcIixcImlkXCI6MTQz'
                         'MzczNDM4NDM4OTk1MTQ5MH0iLCJqdGkiOiJaR1ZpTW1ZMFpqQXRZbVF5T1'
                         'MwMFpXWmpMVGczWldVdFltRmxPR1U0TjJSaU16SmkiLCJleHAiOjc5NDM4M'
                         'TE5NzZ9.iUrVlRnz4sAR-qZ8ut1dWDrpAlhxVohY04RkdQCgkyyXQqBEXa8U'
                         'IV98UPZNi9NJeawdXDr3lg3q_ECTS_L9Q52gcDn7Z35N_2OjG7-a8eOBUw_tB'
                         'vQRXp8vn0Pp9jwHaj_Idqve5r_M0YoVzr96A-lFtQHL2x5EKIhm8St_WmxYocdn'
                         'UmL0kq3jv1xMeVG8tR9546R57LfpGmlHiaz1hvK3qt8bGh8wLyco972PbgiwgLi6'
                         '1ax0lnU79_HQeFptJznezmiVWvFZ4fUpzI57B1lHcgrx-iiG2Nynd7dFWwKwUG0N'
                         '5K_hMCJ61-XLkB7YnzCz8zI2rQNe6h1QdUxt2w '
    }
    # # POST请求
    params1 = sign.GetStringSignTemp(key, data)
    response = requests.request("post", url, headers=headers, data=params1)
    print(response.text)
