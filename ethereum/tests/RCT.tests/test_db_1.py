# -*- coding: UTF-8 -*-

from colorama import Fore, Back, Style
from termcolor import colored

import redis
import random
import sys
import pytest
from rlp.utils import ascii_chr, decode_hex,encode_hex
from ethereum import utils

print(Fore.BLUE)




def random_string(length):
    rand_str = b''.join([ascii_chr(random.randint(0, 255)) for _ in range(length)])
    return rand_str

def generate_simplified_random_TX(number_of_TX):
    sender = utils.sha3(random_string(100))
    receiver = utils.sha3(random_string(100))
    transaction_id = utils.sha3(random_string(100))
    return (transaction_id,sender,receiver)

def main():
    (transaction_id, sender, receiver)= generate_simplified_random_TX(8)
    # print(utils.encode_hex(sender))
    # print(utils.encode_hex(receiver))
    # print(utils.encode_hex(transaction_id))
    reputation_db = redis.StrictRedis(host='localhost', port=6379, db=0)
    reputation_db.set(transaction_id, sender+receiver)
    my_decode_key = decode_hex('352f81d7e82301723bc56ce1d33e1a608e07f007e19f8e846a062336d64d544f')
    test_get_results = reputation_db.get(my_decode_key)
    print(utils.encode_hex(test_get_results))
    # print(reputation_db.keys())
    for i in reputation_db.keys():
        print(utils.encode_hex(i))
    # print(sys.getsizeof(reputation_db))


if __name__ == '__main__':
    main()





