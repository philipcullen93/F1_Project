CURRENT_SEASON = None

def set_current_season(season):

    global CURRENT_SEASON

    CURRENT_SEASON = season

def get_data_folder():

    return f"data/{CURRENT_SEASON}"