#!/usr/bin/env python
#coding: utf-8
__author__ = 'kirk erickson'


"""

# libyaml-cpp-dev libyaml-dev

"""
import os, sys, time, warnings, fnmatch, contextlib
import pprint
import pdb
import markupsafe
import markdown
import pickle
from staticjinja import make_site
import markdown_replace
from committee import Committee


if __name__ == "__main__":

    # save generated data
    report = 'report.pickle'

    if not os.path.exists(report):
        committee = Committee()
        comm = committee.report()

        with open(report, 'wb') as fp:
            pickle.dump(comm, fp)

    else:
        comm = pickle.load( open( report, "rb" ) )

    #print('committes:%s', len(comm))
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(c)

    # process data into template
    site = make_site(env_globals={'comm':comm}, outpath='./markdown')

    # split each committee into separate file
    for c in comm:
        # _ makes the template not process in site.render

        filepath_md = './markdown/{}.md'.format(c['committee']['thomas_id'])
        site.render_template(site.get_template('_committee.md'),
                             context={'c' : c},
                             filepath=filepath_md
                            )

        filepath_exp = './export/{}.txt'.format(c['committee']['thomas_id'])
        site.render_template(site.get_template('_committee.txt'),
                             context={'c' : c},
                             filepath=filepath_exp
                            )


    site.render()

    # convert template markdown into html
    # https://pythonhosted.org/Markdown/reference.html#the-basics
    for filename in os.listdir('./markdown'):
        if filename.endswith('.md'):
            print('markdown:', filename)
            markdown.markdownFromFile(
                input= os.path.join('./markdown/', filename),
                output= os.path.join('./html', os.path.splitext(filename)[0] + '.html'),
                extensions=['markdown.extensions.tables',
                            'markdown_replace(search=.md, replace=.html)']
            )
