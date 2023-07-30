import requests
import os
import json
from zipfile import ZipFile
import shutil
from renpy import config

USER = ""
REPO = ""
URL = f"https://api.github.com/repos/{USER}/{REPO}/releases/latest"
ZIP_PATH = os.path.join(config.basedir, "temp.zip")
JSON_PATH = os.path.join(config.basedir, "game_update.json")
VER_PATH = os.path.join(config.gamedir, "version.txt")

def parse_ver() -> str:
    with open(JSON_PATH, "r") as g:
        req = json.load(g)
        return req["tag_name"]
        
def check_update() -> bool:
    repo_ver = parse_ver()
    try:
        with open(VER_PATH, "r") as v:
            installed_ver = v.read()
    except IOError:
        installed_ver = config.version
    return repo_ver == installed_ver

def get_json_data() -> None:
    data = requests.get(URL).json()
    with open(JSON_PATH, "w") as g:
        json.dump(data, g)

def download_update() -> None:
    if not check_update():
        with open(JSON_PATH, "r") as g:
            data = json.load(g)

        tag = data["tag_name"]
        download_url = data["assets"][0]["browser_download_url"]

        try:
            update_data = requests.get(download_url)
            with open(VER_PATH, "w") as v:
                v.write(tag)

            with open(ZIP_PATH, "wb") as ud:
                ud.write(update_data.content)

            with ZipFile(ZIP_PATH, "r") as u:
                u.extractall()

            dir = f"{REPO}-{tag[1:]}/"
            for f in os.listdir(dir):
                shutil.move(f"{dir}/{f}", "game/")

            os.removedirs(dir)
            os.remove(ZIP_PATH)
            return True
        except: 
            return False
