from unittest.mock import Mock
import unittest
import time
import random

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
    if FUZZ:
        time.sleep(random.random())

###########################################################################################


from index import each_limit


class EachLimitTest(unittest.TestCase):
    def test_basic(self):
        args = []

        def iter(args, item):
            fuzz()
            args += [item]
            fuzz()
            return item
        res, err = each_limit([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2, lambda item: iter(args, item))
        self.assertEqual(err, None)
        args.sort()
        self.assertEqual(args, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # ENHANCE: auto-ensure parallelized


if __name__ == '__main__':
    unittest.main()
