import py.test
from abjad.tools.treetools import *
from abjad.tools.treetools._make_test_blocks import _make_test_blocks


py.test.skip('Being re-implemented.')

def test_treetools_compute_logical_not_of_intervals_in_interval_01( ):
   a = BoundedInterval(0, 3)
   b = BoundedInterval(6, 12)
   c = BoundedInterval(9, 15)
   tree = IntervalTree([a, b, c])
   d = BoundedInterval(1, 14)
   logic = compute_logical_not_of_intervals_in_interval(tree, d)
   assert [x.signature for x in logic] == [(3, 6)]

def test_treetools_compute_logical_not_of_intervals_in_interval_02( ):
   a = BoundedInterval(0, 3)
   b = BoundedInterval(6, 12)
   c = BoundedInterval(9, 15)
   tree = IntervalTree([a, b, c])
   d = BoundedInterval(-1, 16)
   logic = compute_logical_not_of_intervals_in_interval(tree, d)
   assert [x.signature for x in logic] == [(-1, 0), (3, 6), (15, 16)]

def test_treetools_compute_logical_not_of_intervals_in_interval_03( ):
   a = BoundedInterval(0, 3)
   b = BoundedInterval(6, 12)
   c = BoundedInterval(9, 15)
   tree = IntervalTree([a, b, c])
   d = BoundedInterval(2001, 2010)
   logic = compute_logical_not_of_intervals_in_interval(tree, d)
   assert [x.signature for x in logic] == [(2001, 2010)]
