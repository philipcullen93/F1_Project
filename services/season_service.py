import os

def get_available_seasons():

    seasons = []

    data_folder = "data"

    for folder in os.listdir(data_folder):

        path = os.path.join(data_folder, folder)
        if os.path.isdir(path) and folder.isdigit():
            seasons.append(folder)

    return sorted(seasons)

def create_season_folder(season):

    folder = f"data/{season}"

    if not os.path.exists(folder):
        os.makedirs(folder)
        return True

    return False

def get_current_season_folder(season):

    return f"data/{season}"