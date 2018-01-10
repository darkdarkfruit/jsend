# import jsend
from .jsend import Message, make_successful_message, make_failed_message, SuccessfulMessage, FailedMessage


__author__ = 'darkdarkfruit'

VERSION = (0, 9, 0)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version

__version__ = get_version()
