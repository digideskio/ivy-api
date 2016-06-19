try:
    import ujson as json
except:
    import json

from modules.common import Bunch

class Config(object):
    def __init__(self, depth=1):
        importer = FileManager()

        self.raw = {}
        for item in ['db', 'logging', 'server', 'api']:
            data = importer.loadFile('./{}.json'.format(item), is_json=True)
            self.raw[item] = data
            if depth == 2: data = Bunch(data, 'one')
            self.__dict__[item] = data


class FileManager(object):
    def __init__(self):
        pass

    def loadFile(self, filename, location=None, is_json=False):
        file_at = "./config/{}".format(filename)
        if location: file_at = "{}/{}".format(location, filename)
        try:
            with open(file_at) as f:
                data = f.read()
        except:
            with open("." + file_at) as f:
                data = f.read()
        if is_json:
            return json.loads(data)
        return data

    def saveFile(self, filename, data, location=None, append=False):
        mode = "w"
        if append: mode = "a"
        file_at = "./config/{}".format(filename)
        if location: file_at = "{}/{}".format(location, filename)
        try:
            with open(file_at, mode) as f:
                f.write(data)
                f.truncate()
        except:
            with open("." + file_at, mode) as f:
                f.write(data)
                f.truncate()
