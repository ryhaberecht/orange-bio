"""
obiKEGG2 configuration 

mostly just caching settings

"""

import os
import ConfigParser
from StringIO import StringIO

default = {"cache.path": "%HOME/.obiKEGG/",
           "cache.store": "sqlite3",
           "cache.kgml_invalidate": "always", #Can be session, always, release, never
           }

default = """
[cache]
path = %(home)s/.obiKEGG/
store = sqlite3
kegg_invalidate = always

"""

#_defaults_env = dict(default)
#_defaults_env.update(dict(os.environ))

parser = ConfigParser.ConfigParser(dict(os.environ))#_defaults_env)
# TODO: global settings

parser.readfp(StringIO(default), "default")

parser.read([os.path.expanduser("~/.obiKEGG/rc.cfg")])

params = {}


for section in parser.sections():
    for option in parser.options(section):
        params[section + "." + option] = parser.get(section, option)