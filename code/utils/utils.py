import json
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).absolute().parents[2].resolve()


def dict_from_json(json_path):
    try:
        with open(json_path, "r") as f:
            file = json.load(f)
        return file
    except Exception as e:
        print(f"{e} - files missing?")
        raise Exception(e)
