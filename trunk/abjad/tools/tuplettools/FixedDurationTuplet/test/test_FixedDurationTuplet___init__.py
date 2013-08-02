# -*- encoding: utf-8 -*-
from abjad import *


def test_FixedDurationTuplet___init___01():
    r'''Initialize typical fixed-duration tuplet.
    '''

    t = tuplettools.FixedDurationTuplet(Duration(2, 8), Note(0, (1, 8)) * 3)

    assert repr(t) == "FixedDurationTuplet(1/4, [c'8, c'8, c'8])"
    assert str(t) == "{@ 3:2 c'8, c'8, c'8 @}"
    assert t.lilypond_format == "\\times 2/3 {\n\tc'8\n\tc'8\n\tc'8\n}"
    assert len(t) == 3
    assert t.target_duration == Fraction(1, 4)
    assert t.multiplier == Fraction(2, 3)
    assert t.get_duration() == Fraction(1, 4)


def test_FixedDurationTuplet___init___02():
    r'''Initialize empty fixed-duration tuplet.
    '''

    t = tuplettools.FixedDurationTuplet(Duration(1, 4), [])

    assert repr(t) == 'FixedDurationTuplet(1/4, [])'
    assert str(t) == '{@ 1/4 @}'
    assert len(t) == 0
    assert t.target_duration == Fraction(1, 4)
    assert t.multiplier == None
    assert t.get_duration() == Fraction(1, 4)
