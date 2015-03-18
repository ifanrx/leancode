# coding: utf-8

import client
from .acl import ACL
from .client import init
from .errors import LeanCloudError
from .file_ import File
from .geo_point import GeoPoint
from .object_ import Object
from .query import FriendshipQuery
from .query import Query
from .relation import Relation
from .user import User
from .role import Role

__author__ = 'asaka <lan@leancloud.rocks>'
__version__ = '0.0.1'


__all__ = [
    'ACL',
    'File',
    'FriendshipQuery',
    'GeoPoint',
    'LeanCloudError',
    'Object',
    'Query',
    'Relation',
    'User',
    'client',
    'init',
    'Role',
]
