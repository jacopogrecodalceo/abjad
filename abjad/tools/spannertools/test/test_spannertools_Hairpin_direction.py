# -*- coding: utf-8 -*-
import abjad
from abjad import *


def test_spannertools_Hairpin_direction_01():

    staff = abjad.Staff("c'8 d'8 e'8 f'8")
    hairpin = Hairpin(descriptor='p < f', direction=Down)
    attach(hairpin, staff[:])

    assert format(staff) == String.normalize(
        r'''
        \new Staff {
            c'8 _ \< _ \p
            d'8
            e'8
            f'8 _ \f
        }
        '''
        )
