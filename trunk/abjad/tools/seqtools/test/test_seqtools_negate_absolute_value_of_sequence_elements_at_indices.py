from abjad import *
import py.test


def test_seqtools_negate_absolute_value_of_sequence_elements_at_indices_01( ):

   l = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]
   t = seqtools.negate_absolute_value_of_sequence_elements_at_indices(l, [0, 1, 2])
   
   assert t == [-1, -2, -3, 4, 5, -6, -7, -8, -9, -10]


def test_seqtools_negate_absolute_value_of_sequence_elements_at_indices_02( ):

   l = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]
   t = seqtools.negate_absolute_value_of_sequence_elements_at_indices(l, [0, 1, 2], period = 5)
   
   assert t == [-1, -2, -3, 4, 5, -6, -7, -8, -9, -10]


def test_seqtools_negate_absolute_value_of_sequence_elements_at_indices_03( ):

   assert py.test.raises(TypeError,
      "seqtools.negate_absolute_value_of_sequence_elements_at_indices('foo', [0, 1, 2])")
