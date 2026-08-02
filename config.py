import os

CURRENT_SEASON = None

def set_current_season(season):

    global CURRENT_SEASON

    CURRENT_SEASON = season

def get_data_folder():

    return f"data/{CURRENT_SEASON}"

def season_has_data():

    folder = get_data_folder()

    return os.path.exists(folder) and bool(os.listdir(folder))