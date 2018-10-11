#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
#
# MDAnalysisData --- https://www.mdanalysis.org
# Copyright (c) 2018 The MDAnalysis Development Team and contributors
# (see the file AUTHORS for the full list of names)
#
# Released under the BSD 3-clause license (see LICENSE)
#
#

"""
The MDAnalysisData package unifies access to test and example
trajectories that can be used for workshops and extended tests.
"""

from __future__ import print_function
from setuptools import setup, find_packages
import versioneer

import codecs

if __name__ == '__main__':
    with codecs.open("README.md", encoding="utf-8") as summary:
        LONG_DESCRIPTION = summary.read()

    CLASSIFIERS = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: C',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

    setup(name='MDAnalysisData',
          version=versioneer.get_version(),
          cmdclass=versioneer.get_cmdclass(),
          description='MDAnalysis example data',
          long_description=LONG_DESCRIPTION,
          long_description_content_type='text/markdown',
          author='Oliver Beckstein',
          author_email='orbeckst@gmail.com',
          maintainer='Richard Gowers',
          maintainer_email='mdnalysis-discussion@googlegroups.com',
          url='https://www.mdanalysis.org',
          download_url='https://github.com/MDAnalysis/MDAnalysisData/releases',
          project_urls={'Documentation': 'https://www.mdanalysis.org/MDAnalysisData',
                        'Developer Group': 'https://groups.google.com/forum/#!forum/mdnalysis-devel',
                        'Issue Tracker': 'https://github.com/mdanalysis/MDAnalysisData/issues',
                        'Source': 'https://github.com/mdanalysis/MDAnalysisData',
                        },
          license='GPL 3',
          classifiers=CLASSIFIERS,
          packages=find_packages(),
          package_dir={'MDAnalysisData': 'MDAnalysisData'},
          package_data={'MDAnalysisData': ['descr/*.rst']},
          install_requires=[],
          zip_safe=True,
    )
