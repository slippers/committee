#!/usr/bin/env python
#coding: utf-8
__author__ = 'kirk erickson'


"""

# libyaml-cpp-dev libyaml-dev:q

"""
import os, sys, time, warnings, fnmatch, contextlib
import yaml
import pprint
import markdown
import markupsafe
import pickle
from staticjinja import make_site
try:
    from yaml import CLoader as Loader
    from yaml import CDumper as Dumper
    sys.stderr.write("SWEET: using C yaml\n")
except ImportError:
    from yaml import Loader, Dumper
    sys.stderr.write("WARNING: Could not use C yaml\n")

DATA = './'


def dictsubset(dictionary, subset=()):
    return {k:v for k, v in dictionary.items() if k in subset}


def dictskip(dictionary, subset=()):
    return {k:v for k, v in dictionary.items() if k not in subset}


class Committee():
    def __init__(self):
        self.database_load()

    def database_access(self, filename):
        fname_fullpath = os.path.join(DATA, filename)
        if not os.path.exists(fname_fullpath):
            raise FileNotFoundError(
                'File {} doesn\'t exist;'.format(filename)
            )

        with open(fname_fullpath, 'r') as f:
            doc = yaml.safe_load(f)
            if doc is None: doc = []  # make it an empty iterable
            return doc

    def database_load(self):
        self.legislators = self.database_access('legislators-current.yaml')
        self.offices = self.database_access('legislators-district-offices.yaml')
        self.committees = self.database_access('committees-current.yaml')
        self.membership = self.database_access('committee-membership-current.yaml')

    def lookup_by_member(self, member):
        #print(mem['name'])
        for leg in ( leg for leg in self.legislators if \
                    (leg['name']['official_full'] == member['name']) \
                    or ('bioguide' in leg['id'] \
                        and 'bioguide' in member \
                        and leg['id']['bioguide'] == member['bioguide']) \
                    or ('thomas' in leg['id'] \
                        and 'thomas' in member \
                        and leg['id']['thomas'] == member['thomas']) ):
            return leg
        raise Exception('member not found:{}'.format(member['name']))

    def report(self):
        committees = []
        for com in self.committees:
            #print(com['name'])

            comx = {}
            comx['committee'] = dictskip(com, ('subcommittees'))

            memx = {}

            if not com['thomas_id'] in self.membership:
                print('members not found in:%s', com['thomas_id'])
                continue
            for mem in self.membership[com['thomas_id']]:
                leg = self.lookup_by_member(mem)
                memx[mem['name']] = dictsubset(leg, ('bio', 'id', 'name'))

                # add the office data

            comx['members'] = memx

            committees.append(comx)

        return committees



if __name__ == "__main__":

    report = 'report.txt'

    if not os.path.exists(report):
        committee = Committee()
        comm = committee.report()

        with open(report, 'wb') as fp:
            pickle.dump(comm, fp)

    else:
        comm = pickle.load( open( report, "rb" ) )

    print('committes:%s', len(comm))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(comm[0])

    site = make_site(env_globals={'comm':comm,})
    site.render()

    # https://pythonhosted.org/Markdown/reference.html#the-basics
    markdown.markdownFromFile(input='index.md_', output='index.html')




