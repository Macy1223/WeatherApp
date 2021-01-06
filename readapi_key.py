def readapi_key(filename):
    '''
    :param filename
    :return: Return api key
    '''
    with(open(filename)) as file:
        return file.readline().strip()

