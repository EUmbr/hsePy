import pickle as pk


def load_data(path):
    filename = open(path, 'rb')
    data, reg = pk.load(filename)
    filename.close()
    return data, reg
