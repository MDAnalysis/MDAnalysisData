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
from os import environ, listdir, makedirs
from os.path import dirname, exists, expanduser, isdir, join, splitext
import hashlib
from pkg_resources import resource_string

from tqdm import tqdm

#: Default value for the cache directory. It can be changed by setting
#: the environment variable :envvar:`MDANALYSIS_DATA`. The current
#: value should be queried with :func:`get_data_home`.
#:
#: .. SeeAlso:: :ref:`managing-data`.
DEFAULT_DATADIR = join('~', 'MDAnalysis_data')

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
                                DEFAULT_DATADIR)
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
    with TqdmUpTo(unit='B', unit_scale=True, miniters=1,
                  desc=remote.filename) as t:
        urlretrieve(remote.url, filename=file_path,
                    reporthook=t.update_to, data=None)
    checksum = _sha256(file_path)
    if remote.checksum != checksum:
        raise IOError("{} has an SHA256 checksum ({}) "
                      "differing from expected ({}), "
                      "file may be corrupted.".format(file_path, checksum,
                                                      remote.checksum))
    return file_path


def _read_description(filename, description_dir='descr'):
    """Read the description from restructured text file.

    Arguments
    ---------
    filename : str
        name of the description file under the ``descr`` directory

    Note
    ----
    All description files are supposed to be stored in the directory
    `description_dir` ``="descr"`` that lives in the same directory as
    the :mod:`MDAnalysisData.base` module file. All descriptions are
    assumed to be in restructured text format and in UTF-8 encoding.

    """
    # The descr directory should be in the same directory as this file base.py.
    # `resource_string` returns bytes, which we need to decode to UTF-8
    DESCR = resource_string(__name__,
                            '{}/{}'.format(description_dir, filename)
                           ).decode("utf-8")
    return DESCR


class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`.

    From https://pypi.org/project/tqdm/#hooks-and-callbacks
    """

    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize
