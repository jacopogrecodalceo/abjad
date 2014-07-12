# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_DistributionFileWrangler_go_to_next_score_01():

    input_ = 'red~example~score d >> q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores depot',
        'Red Example Score (2013)',
        'Red Example Score (2013) - distribution directory',
        'Blue Example Score (2013)',
        ]
    assert ide._transcript.titles == titles


def test_DistributionFileWrangler_go_to_next_score_02():

    input_ = 'D >> q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores depot',
        'Abjad IDE - distribution depot',
        'Blue Example Score (2013)',
        ]
    assert ide._transcript.titles == titles