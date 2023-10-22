import config.read
import requests
import json

conf = config.read.Config.data

cookie = conf["account-service"]["cookie"]
csrf = conf["account-service"]["X-Hd-Csrf"]
agcteamid = conf["account-service"]["Agcteamid"]

headers = {
    "cookie": "",
    "X-Hd-Csrf": "",
    "Agcteamid": ""
}

print(cookie, csrf, agcteamid, sep="\n")


def create_project(name) -> dict:
    response = requests.post(
        url=r"https://agc-drcn.developer.huawei.com/agc/edge/cpms/project-management-service/v1/projects",
        data={
            "createAllianceProjectFlag": 1,
            "createDevProjectFlag": 0,
            "createTenantProjectFlag": 0,
            "name": name
        },
        headers=headers
    )

    return json.loads(response.text)


if __name__ == "__main__":
    response = create_project(input("name>"))
    print(response)
