import pandas as pd


def generate_data():
    d = {
        "id": 1,
        "jinja_template": "Dear user {{ user_full_name }}, new movie for you in our online cinema: {{ movie_title }}",
        "vars": {"movie_title": "default", "movie_title": "default"},
    }
    return d
