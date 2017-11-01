# -*- coding: utf-8 -*-
# ############# version ##################
try:
    from pkg_resources import get_distribution, DistributionNotFound
except BaseException:
    DistributionNotFound = Exception
import os.path
import subprocess
import re
# Import slogging to patch logging as soon as possible
from . import slogging  # noqa


GIT_DESCRIBE_RE = re.compile(
    '^(?P<version>v\d+\.\d+\.\d+)-(?P<git>\d+-g[a-fA-F0-9]+(?:-dirty)?)$')


__version__ = None
try:
    _dist = get_distribution('pyethapp')
    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'pyethapp')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
    __version__ = _dist.version
except DistributionNotFound:
    pass

if not __version__:
    try:
        rev = subprocess.check_output(['git', 'describe', '--tags', '--dirty'],
                                      stderr=subprocess.STDOUT)
        match = GIT_DESCRIBE_RE.match(rev)
        if match:
            __version__ = "{}+git-{}".format(
                match.group("version"), match.group("git"))
    except BaseException:  # FIXME!
        pass

if not __version__:
    __version__ = 'undefined'

# ########### endversion ##################

"""from rctoken import utils
from rctoken import trie
from rctoken import securetrie
from rctoken import blocks
from rctoken import transactions
from rctoken import processblock
from rctoken import tester
from rctoken import abi
from rctoken import keys
from rctoken import ethash"""
