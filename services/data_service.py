import json
import os


def save_json(data, filepath):
    """
    Save data to a JSON file.
    """

    directory = os.path.dirname(filepath)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_json(filepath):
    """
    Load data from a JSON file.
    """

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)