import pickle as pk


def load_data(path):
    filename = open(path, 'rb')
    data = pk.load(filename)
    filename.close()
    return data
