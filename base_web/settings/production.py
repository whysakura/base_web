from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .localsetting import *
except ImportError:
    pass
