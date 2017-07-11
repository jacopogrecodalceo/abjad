# -*- coding: utf-8 -*-
import abjad
from abjad import *


def test_spannertools_TextSpanner_position_01():

    staff = abjad.Staff("c'8 c'8 c'8 c'8")
    text_spanner = spannertools.TextSpanner()
    attach(text_spanner, staff[:])

    assert format(staff) == String.normalize(
        r'''
        \new Staff {
            c'8 \startTextSpan
            c'8
            c'8
            c'8 \stopTextSpan
        }
        '''
        )


def test_spannertools_TextSpanner_position_02():

    staff = abjad.Staff("c'8 c'8 c'8 c'8")
    text_spanner = spannertools.TextSpanner()
    attach(text_spanner, staff[:])
    command = indicatortools.LilyPondCommand('textSpannerNeutral')
    attach(command, text_spanner[0])

    assert format(staff) == String.normalize(
        r'''
        \new Staff {
            \textSpannerNeutral
            c'8 \startTextSpan
            c'8
            c'8
            c'8 \stopTextSpan
        }
        '''
        )


def test_spannertools_TextSpanner_position_03():

    staff = abjad.Staff("c'8 c'8 c'8 c'8")
    text_spanner = spannertools.TextSpanner()
    attach(text_spanner, staff[:])
    command = indicatortools.LilyPondCommand('textSpannerUp')
    attach(command, text_spanner[0])

    assert format(staff) == String.normalize(
        r'''
        \new Staff {
            \textSpannerUp
            c'8 \startTextSpan
            c'8
            c'8
            c'8 \stopTextSpan
        }
        '''
        )


def test_spannertools_TextSpanner_position_04():

    staff = abjad.Staff("c'8 c'8 c'8 c'8")
    text_spanner = spannertools.TextSpanner()
    attach(text_spanner, staff[:])
    command = indicatortools.LilyPondCommand('textSpannerDown')
    attach(command, text_spanner[0])

    assert format(staff) == String.normalize(
        r'''
        \new Staff {
            \textSpannerDown
            c'8 \startTextSpan
            c'8
            c'8
            c'8 \stopTextSpan
        }
        '''
        )


def test_spannertools_TextSpanner_position_05():
    r'''TextSpanner attaching to container formats correctly.
    '''

    container = Container("c'8 c'8 c'8 c'8")
    text_spanner = spannertools.TextSpanner()
    attach(text_spanner, container[:])

    assert format(container) == String.normalize(
        r'''
        {
            c'8 \startTextSpan
            c'8
            c'8
            c'8 \stopTextSpan
        }
        '''
        )
