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

from index import each

class EachTest(unittest.TestCase):
    def test_basic(self):
        args = []
        def each_iter(args, item):
            fuzz()
            args += [item]
            fuzz()
            return item
        res, err = each([1,3,2], lambda item: each_iter(args, item))
        self.assertEqual(err, None)
        args.sort()
        self.assertEqual(args, [1,2,3]) # ENHANCE: auto-ensure parallelized

if __name__ == '__main__':
    unittest.main()
