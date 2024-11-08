import pickle


def save_data(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_data(filename, default):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default
