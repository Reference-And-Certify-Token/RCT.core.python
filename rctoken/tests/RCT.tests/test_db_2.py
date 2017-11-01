# -*- coding: UTF-8 -*-

from colorama import Fore, Back, Style
from termcolor import colored

import itertools
import random
import pytest
from rctoken.db import _EphemDB
from rlp.utils import ascii_chr


print(Fore.BLUE)


random.seed(100)




def random_string(length):
    rand_str = b''.join([ascii_chr(random.randint(0, 255)) for _ in range(length)])
    return rand_str



def test_ephem():
    db = _EphemDB()
    print("\nTest EphemDB with checking, put, delete functions")
    for key in content:
        assert key not in db
        with pytest.raises(KeyError):
            db.get(key)
    for key, value in content.items():
        db.put(key, value)
        assert key in db
        assert db.get(key) == value
    for key in content:
        db.put(key, alt_content[key])
        assert key in db
        assert db.get(key) == alt_content[key]
    for key, value in content.items():
        db.delete(key)
        assert key not in db
        with pytest.raises(KeyError):
            db.get(key)




content = {random_string(lk): random_string(lv)
           for lk, lv in itertools.product([1, 32, 255], [0, 1, 32, 255])}
alt_content = {key: random_string(32) for key in content}
test_ephem()







