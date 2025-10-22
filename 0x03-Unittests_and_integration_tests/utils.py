import requests


def access_nested_map(nested_map, path):
    """Access nested map with key sequence."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str):
    response = requests.get(url)
    return response.json()


print(get_json("https://savanna.alxafrica.com/projects/101941"))