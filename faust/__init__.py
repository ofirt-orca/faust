# -*- coding: utf-8 -*-
"""Stream processing"""
# :copyright: (c) 2017, Robinhood Markets
#             All rights reserved.
# :license:   BSD (3 Clause), see LICENSE for more details.
import re
from typing import NamedTuple

__version__ = '1.0.0'
__author__ = 'Robinhood Markets'
__contact__ = 'opensource@robinhood.com'
__homepage__ = 'https://github.com/robinhoodmarkets/faust'
__docformat__ = 'restructuredtext'

# -eof meta-


class version_info_t(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: str


# bumpversion can only search for {current_version}
# so we have to parse the version here.
_temp = re.match(
    r'(\d+)\.(\d+).(\d+)(.+)?', __version__).groups()
VERSION = version_info = version_info_t(
    int(_temp[0]), int(_temp[1]), int(_temp[2]), _temp[3] or '', '')
del(_temp)
del(re)

from .app import App                                      # noqa: E402
from .models import Record                                # noqa: E402
from .sensors import Monitor, Sensor                      # noqa: E402
from .streams.stream import Stream                        # noqa: E402
from .streams.table import Table                          # noqa: E402
from .topics import topic                                 # noqa: E402
from .types import Event                                  # noqa: E402
from .windows import (                                    # noqa: E402
    HoppingWindow, TumblingWindow, SlidingWindow,
)
from .worker import Worker                                # noqa: E402

__all__ = [
    'App',
    'Event',
    'Record',
    'Monitor',
    'Sensor',
    'Stream',
    'Table',
    'HoppingWindow', 'TumblingWindow', 'SlidingWindow',
    'Worker',
    'topic', 'use_uvloop',
]


def use_uvloop() -> None:
    try:
        import uvloop
    except ImportError:
        pass
    else:
        import asyncio
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
