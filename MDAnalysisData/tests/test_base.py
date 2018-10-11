# -*- coding: utf-8 -*-

from __future__ import absolute_import, division

import os.path

import pytest

from MDAnalysisData import base
from MDAnalysisData import adk_equilibrium

def test_read_description():
    descr = base._read_description("adk_equilibrium.rst")
    assert len(descr) == 1252
    assert descr.startswith(".. -*- coding: utf-8 -*-\n\n.. _`adk-equilibrium-dataset`:")

def test_sha256(tmpdir):
    filename = "address.txt"
    with tmpdir.as_cwd():
        with open(filename, "w") as txt:
            txt.write("Four score and seven years ago \n"
                      "our fathers brought forth on this continent, \n"
                      "a new nation, conceived in Liberty, and dedicated\n"
                      "to the proposition that all men are created equal.")
        checksum = base._sha256(filename)
    assert checksum == "4446bfb2ec5dedfbd981d059d6005f5144b067b392a00e3bcf98f8302ec8f765"

@pytest.mark.parametrize('data_home,location', [
    (None, os.path.expanduser("~/MDAnalysis_data")),
    ("/tmp/MDAnalysisData", "/tmp/MDAnalysisData"),
    ])
def test_get_data_home(data_home, location):
    assert base.get_data_home(data_home=data_home) == location

@pytest.fixture
def remote_topology():
    # small-ish file
    return adk_equilibrium.ARCHIVE['topology']

def test_fetch_remote(remote_topology, tmpdir):
    filename = base._fetch_remote(remote_topology, dirname=str(tmpdir))
    assert os.path.basename(filename) == remote_topology.filename
    assert os.path.dirname(filename) == str(tmpdir)
