import json
import os

path = os.path.dirname(os.path.abspath(__file__))


class Config:
    def __init__(self):
        self.metadata = open(file=f"{path}\\config.json", mode="r", encoding="utf-8").read()
        with open(file=f"{path}\\config.json", mode="r", encoding="utf-8") as meta:
            self.data = json.load(meta)

    def getdata(self) -> dict:
        return self.data
