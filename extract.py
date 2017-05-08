#!/usr/bin/env python
#coding: utf-8
__author__ = 'stsmith'


"""

# libyaml-cpp-dev libyaml-dev:q

"""
import os, sys, time, warnings, fnmatch, contextlib
import yaml
import pprint
from staticjinja import make_site
try:
    from yaml import CLoader as Loader
    from yaml import CDumper as Dumper
    sys.stderr.write("SWEET: using C yaml\n")
except ImportError:
    from yaml import Loader, Dumper
    sys.stderr.write("WARNING: Could not use C yaml\n")

DATA = './'

class Committee():
    def __init__(self):
        self.database_load()

    def yaml_load(self, y):
        res = yaml.load(y, Loader=Loader)
        if res is None: res = []  # make it an empty iterable
        return res

    def database_access(self, filename):
        fname_fullpath = os.path.join(DATA, filename)
        if os.path.exists(fname_fullpath):
            res = open(fname_fullpath,'r')
        else:
            warnings.warn('File {} doesn\'t exist; clone data from {} and copy it to {} .'.format(filename,self.args.repo,self.data_path))
            res = self.Emptysource()
        return res

    def database_load(self):
        try:
            with self.database_access('legislators-current.yaml') as y:
                self.legislators = self.yaml_load(y)
            with self.database_access('legislators-district-offices.yaml') as y:
                self.offices = self.yaml_load(y)
            with self.database_access('committees-current.yaml') as y:
                self.committees = self.yaml_load(y)
            with self.database_access('committee-membership-current.yaml') as y:
                self.membership = self.yaml_load(y)
        except (BaseException,IOError) as e:
            print(e)


#def data():
#    with open('committees-current.yaml', 'r') as f:
#        doc = yaml.safe_load(f)
#        f.close()
#        #print(doc)
#        pp = pprint.PrettyPrinter(indent=4)
#        pp.pprint(doc)
#
#        for x in doc:
#            print(x['name'])
#            print(x[''])
#

if __name__ == "__main__":

    committee = Committee()


    site = make_site(env_globals={'greeting':'Hello world!'})
    site.render()
