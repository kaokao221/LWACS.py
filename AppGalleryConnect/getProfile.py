import requests
import json
import os

headers = {
    "cookie": "",
    "X-Hd-Csrf": "",
    "Agcteamid":""
}


def create_profile() -> dict:
    response = requests.post(
        url="https://agc-drcn.developer.huawei.com/agc/edge/cps/harmony-cert-manage/v1/cert",
        data=None,
        headers=headers
    )
    return json.loads(response.text)

