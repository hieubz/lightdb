import os
import json


def load(db_path, auto_dump):
    """
    return a lightdb object, db_path is the path to the json file.
    """
    return LightDB(db_path, auto_dump)


class LightDB(object):

    def __init__(self, db_path, auto_dump):
        self.data_path = db_path
        self.auto_dump = auto_dump
        self.db = {}
        self.load(db_path)

    def load(self, db_path):
        """
        loads data from db file
        """
        if os.path.exists(db_path):
            self._load_db()

        return True

    def _load_db(self):
        """
        load the data from the file
        """
        try:
            self.db = json.load(open(self.data_path, 'rt'))
        except ValueError:
            # if file is empty
            if os.stat(self.data_path).st_size == 0:
                self.db = {}
            else:
                # file is not empty, there are some errors
                raise

    def dump(self):
        pass

    def set(self, key, value):
        """set value for the key"""
        self.db[key] = value

    def get(self, key):
        """get the value of the key"""
        try:
            return self.db[key]
        except KeyError:
            return False

    def get_all_items(self):
        """return all items in db"""
        return self.db.items()

    def is_exists(self, key):
        """return True if key exists in db, else return False"""
        return key in self.db

    def get_all_keys(self):
        """return all keys in db"""
        pass

    def get_values(self):
        pass

    def append(self, key, more):
        pass

    def deldb(self):
        """
        delete everything from the database
        """
        self.db = {}
