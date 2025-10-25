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


def memoize(func):
    """Memoize decorator for methods."""
    cache = {}

    def wrapper(self, *args, **kwargs):
        key = (id(self), args, frozenset(kwargs.items()) if kwargs else args)
        if key not in cache:
            cache[key] = func(self, *args, **kwargs)
        return cache[key]

    return wrapper


class GithubOrgClient:
    def __init__(self, url):
        self.url = url

    def org(self):
        response = requests.get(self.url)
        return response.json()
