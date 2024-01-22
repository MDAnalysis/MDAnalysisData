"""
Barebones setup.py for dynamic authors list generation.
"""
import codecs
import os
import warnings

from setuptools import setup


def abspath(file):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), file
    )


def dynamic_author_list():
    """Generate __authors__ from AUTHORS
    This function generates authors.py that contains the list of the
    authors from the AUTHORS file. This avoids having that list maintained in
    several places. Note that AUTHORS is sorted chronologically while we want
    __authors__ in authors.py to be sorted alphabetically.
    The authors are written in AUTHORS as bullet points under the
    "Chronological list of authors" title.
    """

    # The dynamic_author_list() function was taken from MDAnalysis's setup.py
    # file, which is licensed under GPL v2+. All original authors of the
    # function (@jbarnoud, @tylerjereddy, @lilyminium) agreed to re-license the
    # code under the BSD 3-clause license
    # (https://github.com/MDAnalysis/MDAnalysisData/pull/49#discussion_r672489685)
    # so that it can be included here with modifictions necessary for
    # MDAnalysisData.

    authors = []
    with codecs.open(abspath('AUTHORS'), encoding='utf-8') as infile:
        # An author is a bullet point under the title "Chronological list of
        # authors". We first want move the cursor down to the title of
        # interest.
        for line_no, line in enumerate(infile, start=1):
            if line.rstrip() == "Chronological list of authors":
                break
        else:
            # If we did not break, it means we did not find the authors.
            raise IOError('EOF before the list of authors')
        # Skip the next line as it is the title underlining
        line = next(infile)
        line_no += 1
        if line[:4] != '----':
            raise IOError('Unexpected content on line {0}, '
                          'should be a string of "-".'.format(line_no))
        # Add each bullet point as an author
        for line in infile:
            if line.strip()[:2] == '- ':
                # This is a bullet point, so it should be an author name.
                name = line.strip()[2:].strip()
                # Remove any @-handles in "A.U. Thor (@donnergott)"
                name = name.split("(")[0].strip()
                authors.append(name)

    # So far, the list of authors is sorted chronologically. We want it
    # sorted alphabetically of the last name.
    authors.sort(key=lambda name: name.split()[-1])

    # Write the authors.py file.
    out_path = abspath('MDAnalysisData/authors.py')
    with codecs.open(out_path, 'w', encoding='utf-8') as outfile:
        # Write the header
        header = '''\
#-*- coding:utf-8 -*-
# This file is generated from the AUTHORS file during the installation process.
# Do not edit it as your changes will be overwritten.
'''
        print(header, file=outfile)

        # Write the list of authors as a python list
        template = u'__authors__ = [\n{}\n]'
        author_string = u',\n'.join(u'    u"{}"'.format(name)
                                    for name in authors)
        print(template.format(author_string), file=outfile)


if __name__ == '__main__':
    try:
        dynamic_author_list()
    except (OSError, IOError):
        warnings.warn('Cannot write the list of authors')

    setup()
