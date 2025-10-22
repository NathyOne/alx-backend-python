#!/usr/bin/env python3
import requests


def access_nested_map(nested_map, path):
    """Access nested map with key path."""
    for key in path:
        if not isinstance(nested_map, dict):
            raise KeyError(key)
        if key not in nested_map:
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Get JSON from remote URL."""
    response = requests.get(url)
    return response.json()
