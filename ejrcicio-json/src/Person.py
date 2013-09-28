class Person(object):
    def __init__(self, name, last_name, birth):
        self.name = name
        self.last_name = last_name
        self.birth = birth

    def to_dict(self):
        return {
            'name': self.name,
            'last_name': self.last_name,
            'birth': self.birth
        }

JSON_FILE = './json_file.json'
