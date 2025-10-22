import requests


def access_nested_map(nested_map, path):
    """
    Access nested map using sequence of keys.

    Args:
        nested_map: A nested dictionary
        path: A tuple representing the path of keys

    Returns:
        The value at the specified path

    Raises:
        KeyError: If the path is invalid
    """
    for key in path:
        if not isinstance(nested_map, dict):
            raise KeyError(key)
        if key not in nested_map:
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str):
    response = requests.get(url)
    return response.json()
