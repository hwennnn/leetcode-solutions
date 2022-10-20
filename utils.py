def get(dictionary, key):
    keys = key.split(".")
    for k in keys:
        if k not in dictionary:
            return None
        dictionary = dictionary[k]
    return dictionary
