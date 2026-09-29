import os
import pickle

FILENAME = "library.dat"


def load_library():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'rb') as f:
            data = pickle.load(f)
            if isinstance(data, tuple) and len(data) == 2:
                return data
    return [], []


def save_library(books, members):
    with open(FILENAME, 'wb') as f:
        pickle.dump((books, members), f)