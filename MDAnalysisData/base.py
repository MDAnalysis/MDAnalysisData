"""Base I/O code for all datasets.

Based on :mod:`sklearn.datasets.base` (used under BSD 3-clause license).


Developer notes
---------------

Downloading a zip archive from figshare with code like the following
will *not work* because the checksum on the zip files changes between
downloads and the checksum check in :func:`_fetch_remote` will fail:

     logger.info('Downloading "AdK equilibrium" dataset from {} to {}'.format(
         ARCHIVE.url, data_location))

     archive_path = _fetch_remote(ARCHIVE, dirname=data_location)

     with zipfile.ZipFile(archive_path, mode="r") as z:
         z.extractall(path=data_location)
     remove(archive_path)

"""

# Code taken from sklearn/utils/ and sklearn/datasets under the 'New BSD license'
# https://github.com/scikit-learn/scikit-learn/blob/master/COPYING and adapted


from __future__ import print_function

from six.moves.urllib.request import urlretrieve

import shutil
from collections import namedtuple
from os import environ, listdir, makedirs, remove
from os.path import dirname, exists, expanduser, isdir, join, splitext
import hashlib
import codecs




class Bunch(dict):
    """Container object for datasets

    Dictionary-like object that exposes its keys as attributes.

    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6
    """

    def __init__(self, **kwargs):
        super(Bunch, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        # Bunch pickles generated with scikit-learn 0.16.* have an non
        # empty __dict__. This causes a surprising behaviour when
        # loading these pickles scikit-learn 0.17: reading bunch.key
        # uses __dict__ but assigning to bunch.key use __setattr__ and
        # only changes bunch['key']. More details can be found at:
        # https://github.com/scikit-learn/scikit-learn/issues/6196.
        # Overriding __setstate__ to be a noop has the effect of
        # ignoring the pickled __dict__
        pass


#: Each remote resource is described by a :class:`RemoteFileMetadata`,
#: which is a :func:`~collections.namedtuple` with fields
#:
#: - *filename*: name of the file in the local file system
#: - *url*: full URL for downloading
#: - *checksum*: SHA256 (can be generated with :func:`MDAnalysisData.base._sha256`;
#:   often it is just as convenient to run the downloader during testing and note the
#:   required SHA256 then)
#:
RemoteFileMetadata = namedtuple('RemoteFileMetadata',
                                ['filename', 'url', 'checksum'])

DATASET_NAMES = {}

class _DatasetRegister(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        if not cls.NAME is None:
            DATASET_NAMES[cls.NAME] = cls
        return cls


class Dataset(Bunch, metaclass=_DatasetRegister):
    NAME = None
    DESCRIPTION = None
    ARCHIVE = None

    def __init__(self, data_home=None, download_if_missing=True):
        data_location = join(get_data_home(data_home=data_home),
                             self.NAME)

        if not exists(data_location):
            makedirs(data_location)

        contents = {}
        for file_type, meta in self.ARCHIVE.items():
            local_path = join(data_location, meta.filename)
            contents[file_type] = local_path

            if not exists(local_path):
                if not download_if_missing:
                    raise IOError("Data {0}={1} not found and `download_if_missing` is "
                                  "False".format(file_type, local_path))
                logger.info("Downloading {0}: {1} -> {2}...".format(
                    file_type, meta.url, local_path))
                archive_path = _fetch_remote(meta, dirname=data_location)

        module_path = dirname(__file__)
        with codecs.open(join(module_path, 'descr', self.DESCRIPTION),
                         encoding="utf-8") as dfile:
            contents['DESCR'] = dfile.read()


        # finally, init the Bunch object
        super().__init__(**contents)

    def __repr__(self):
        return self.__doc__


def fetch(dataset, data_home=None, download_if_missing=True):
    """Grab a named dataset"""
    try:
        return DATASET_NAMES[dataset](data_home=data_home,
                                      download_if_missing=True)
    except KeyError:
        raise KeyError("unknown dataset: {}".format(dataset))


def get_data_home(data_home=None):
    """Return the path of the MDAnalysisData data dir.

    This folder is used by some large dataset loaders to avoid
    downloading the data several times.  By default the data dir is
    set to a folder named 'MDAnalysis_data' in the user's home directory.

    Alternatively, it can be set by the :envvar:`MDANALYSIS_DATA` environment
    variable or programmatically by giving an explicit folder path. The '~'
    symbol is expanded to the user home folder.

    If the folder does not already exist, it is automatically created.

    Parameters
    ----------
    data_home : str | None
        The path to MDAnalysisData data dir.

    """
    if data_home is None:
        data_home = environ.get('MDANALYSIS_DATA',
                                join('~', 'MDAnalysis_data'))
    data_home = expanduser(data_home)
    if not exists(data_home):
        makedirs(data_home)
    return data_home


def clear_data_home(data_home=None):
    """Delete all the content of the data home cache.

    Parameters
    ----------
    data_home : str | None
        The path to MDAnalysisData data dir.
    """
    data_home = get_data_home(data_home)
    shutil.rmtree(data_home)

def _sha256(path):
    """Calculate the sha256 hash of the file at path."""

    sha256hash = hashlib.sha256()
    chunk_size = 8192
    with open(path, "rb") as f:
        while True:
            buffer = f.read(chunk_size)
            if not buffer:
                break
            sha256hash.update(buffer)
    return sha256hash.hexdigest()


def _fetch_remote(remote, dirname=None):
    """Helper function to download a remote dataset into path

    Fetch a dataset pointed by remote's url, save into path using remote's
    filename and ensure its integrity based on the SHA256 Checksum of the
    downloaded file.

    Parameters
    -----------
    remote : RemoteFileMetadata
        Named tuple containing remote dataset meta information: url, filename
        and checksum
    dirname : string
        Directory to save the file to.

    Returns
    -------
    file_path: string
        Full path of the created file.
    """

    file_path = (remote.filename if dirname is None
                 else join(dirname, remote.filename))
    urlretrieve(remote.url, file_path)
    checksum = _sha256(file_path)
    if remote.checksum != checksum:
        raise IOError("{} has an SHA256 checksum ({}) "
                      "differing from expected ({}), "
                      "file may be corrupted.".format(file_path, checksum,
                                                      remote.checksum))
    return file_path
