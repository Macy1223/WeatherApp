def readapi_key(filename):
    with(open(filename)) as file:
        return file.readline()
