from jsend import RSuccess
from jsend import RFail
from jsend import RError

__all__ = (RSuccess, RFail, RError)

__author__ = 'darkdarkfruit'

VERSION = (0, 1, 6)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version

__version__ = get_version()
