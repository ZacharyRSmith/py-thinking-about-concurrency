from unittest.mock import Mock
import unittest
import time
import random

from index import concat


class ConcatTest(unittest.TestCase):
    def test_basic(self):
        args = []
        call_order = []

        def iter(item):
            nonlocal args, call_order
            time.sleep(.25 * item)
            call_order.append(item)
            return [item, item+1]

        res, err = concat([1, 3, 2], iter)
        self.assertEqual(err, None)
        self.assertEqual(call_order, [1, 2, 3])
        self.assertEqual(res, [
            [1, 2],
            [3, 4],
            [2, 3],
        ])


if __name__ == '__main__':
    unittest.main()
