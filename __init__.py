import os
import re

def reglob(pattern):
    '''searches for files matching $pattern'''
    split = pattern.split("/")
    d = "/".join(split[:-1])
    if not d: directory = '.'
    regex = split[-1]
    d = os.path.expanduser(d)
    try:
        return [d + "/" + f for f in os.listdir(d) if re.search(regex, f)]
    except Exception:
        return []
