#!/usr/bin/env python3

import best_sort
import unittest


class TestBestSort(unittest.TestCase):
    
    # Static value containing the expected results of the sort function
    test_cases = [
        ('abracadabra', 'baaracadabr', 0),
        ('seesaw', 'esswea', 0),
        ('elk', 'lke', 0),
        ('grrrrrr', 'rgrrrrr', 5),
        ('up', 'pu', 0),
        ('a', 'a', 1)
    ]
    
    def _for_each_case(self, cb):
        for st in self.test_cases:
            cb(st)
    
    # best_sort.count with same string passed as both args should return the score as len(s)
    def test_unchanged_count(self):
        def assert_unchanged_count(st):
            s = st[0]
            score = len(s)
            
            self.assertEqual(best_sort.count(s, s), score)
            
        self._for_each_case(assert_unchanged_count)
    
    # best_sort.count with original string and new string as args should return expected score as defined in self.test_cases
    def test_changed_count(self):
        def assert_changed_count(st):
            s = st[0]
            ns = st[1]
            score = st[2]
            
            self.assertEqual(best_sort.count(s, ns), score)
        
        self._for_each_case(assert_changed_count)
    
    # best_sort.best_sort with original string as arg should return expected tuple as defined in self.test_cases
    def test_best_sort(self):
        def assert_best_sort(st):
            s = st[0]
            ns = st[1]
            score = st[2]
            
            res = best_sort.best_sort(s)

            self.assertEqual(res, (s, ns, score))
            
        self._for_each_case(assert_best_sort)


if __name__ == '__main__':
    unittest.main()

