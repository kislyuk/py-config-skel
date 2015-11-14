#!/usr/bin/env python3

from __future__ import print_function, unicode_literals, division, absolute_import

import os, sys, json, errno
from collections import MutableMapping

class Config(MutableMapping):
    config_home = os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    def __init__(self, name=os.path.basename(__file__), parent=None):
        # TODO: scan XDG_CONFIG_DIRS
        self.config_dir = os.path.join(self.config_home, name)
        self.config_file = os.path.join(self.config_dir, "config.json")
        try:
            with open(self.config_file) as fh:
                self._data = json.load(fh)
        except Exception as e:
            self._data = {}

    def save(self):
        try:
            os.makedirs(self.config_dir)
        except OSError as e:
            if not (e.errno == errno.EEXIST and os.path.isdir(self.config_dir)):
                raise
        with open(self.config_file, "w") as fh:
            json.dump(self._data, fh)

    def __getitem__(self, item):
        if item not in self._data:
            raise KeyError(item)
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        for item in self._data:
            yield item

    def __len__(self):
        return len(self._data)

config = Config()
config["test"] = 1
print(config["test"])
config.save()
